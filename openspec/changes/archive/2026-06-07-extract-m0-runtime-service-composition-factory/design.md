## Context

`GameplayLifetimeScope` currently performs several responsibilities:

- calls generated NhemDI gameplay scope registration
- registers the logger
- validates authored tuning configs
- converts ScriptableObject configs to runtime settings
- manually registers special-case runtime services that require config/factory construction
- delegates explicit scene component registration/wiring to `M0SceneCompositionRegistrar`

The scene registrar and memory runtime tuning work reduced the class, but the manual service construction block still makes the root scope read like implementation detail instead of composition order.

This change extracts the remaining manual runtime service registration into a focused Bootstrap-owned collaborator while keeping all runtime service ownership and behavior unchanged.

## Goals / Non-Goals

**Goals:**

- Keep `GameplayLifetimeScope` as the high-level gameplay composition root.
- Move manually constructed runtime service registration into a small collaborator.
- Preserve current lifetimes and `.As<T>()` registrations exactly.
- Preserve authored config validation and conversion, either in the collaborator or in small explicit factory methods.
- Keep scene component registration in `M0SceneCompositionRegistrar`.
- Add tests proving the extraction does not introduce broad lookup, direct debug logging, or gameplay truth in Bootstrap.

**Non-Goals:**

- No runtime behavior change for combat, locomotion, memory, VFX, prompt, or runtime log.
- No move from VContainer manual factories to generated NhemDI for these special cases in this slice.
- No service lifetime change.
- No scene/prefab redesign.
- No R3/MessagePipe migration.

## Decisions

### Decision: Add a Bootstrap-owned `M0RuntimeServiceCompositionFactory` or registrar

The new collaborator should receive explicit config references and expose a narrow method such as `Register(IContainerBuilder builder)`.

Rationale: this mirrors the scene registrar slice while keeping construction details out of the root scope.

Alternative considered: split into separate combat, locomotion, and memory registrars immediately. Rejected for now because that adds more files and coupling churn than the current class size justifies.

### Decision: Preserve manual VContainer factory registrations for config-backed services

`M0CombatCore`, `M0PlayerLocomotion`, `M0MemoryState`, and `M0MemoryVFXResponse` currently require authored config/settings or logger resolution during construction. These remain documented manual special cases.

Rationale: forcing NhemDI generated registration here would either hide the factory dependency or require larger constructor/data model changes. That belongs in later, explicit specs if needed.

### Decision: Keep settings conversion explicit and testable

The collaborator may validate configs and call `ToSettings()` methods, but it must not own gameplay truth. Null config failures should stay clear and early.

Rationale: this keeps the runtime services pure and preserves the existing SO tuning direction.

### Decision: `GameplayLifetimeScope` should read as composition order

After the refactor, the root scope should be mostly:

1. generated NhemDI registration
2. logger registration
3. runtime service composition collaborator registration
4. scene composition registrar registration

Rationale: that makes the root useful as an architectural map instead of a construction details bucket.

## Risks / Trade-offs

- [Risk] Registration parity drift.
  - Mitigation: source composition tests assert existing `.As<T>()`, `.AsSelf()`, and singleton lifetimes remain.

- [Risk] New collaborator becomes another catch-all.
  - Mitigation: limit it to pure/runtime service construction from authored configs; scene components stay in `M0SceneCompositionRegistrar`.

- [Risk] Bootstrap starts owning gameplay truth.
  - Mitigation: guardrails assert no calls to combat requests, locomotion input consumption, memory interaction commands, or presentation playback authority.

- [Risk] Missing config errors move or become less clear.
  - Mitigation: preserve explicit `InvalidOperationException` messages and add tests for required config references.

## Migration Plan

1. Capture baseline tests for scene composition and core M0 runtime regressions.
2. Add the runtime service composition collaborator.
3. Move manual runtime service registrations into the collaborator without changing construction parameters.
4. Update `GameplayLifetimeScope` to delegate to the collaborator.
5. Add/update tests and guardrails.
6. Run compile, EditMode regressions, PlayMode/manual smoke, console classification, and OpenSpec validation.

Rollback is straightforward: restore the registration block inside `GameplayLifetimeScope` and remove the collaborator before commit/archive.

## Open Questions

- Should logger registration remain in `GameplayLifetimeScope` or move into the collaborator?
  - Recommendation: keep logger registration in `GameplayLifetimeScope` for now because it is environment/define selection, not runtime service construction.

- Should this collaborator be named `Factory`, `Registrar`, or `Composition`?
  - Recommendation: prefer `M0RuntimeServiceCompositionRegistrar` if it directly registers services with VContainer.
