## Context

The current M0/M1 memory loop is verified through Sprint 3 and Sprint 4 evidence. The most recent refactor slice extracted memory tick orchestration from `M0GameplayTickHandler`, but runtime composition still has a bootstrap hotspot: `GameplayLifetimeScope` discovers memory scene participants with Unity object search calls and wires them during container configuration.

That approach was tolerable during early prototype setup, but it now conflicts with the refactor-wave goals:

- NhemDI should be the default registration path for gameplay runtime services.
- Bootstrap should compose dependencies, not discover arbitrary scene inventory.
- Setup failures should be explicit and testable.
- Scene adapters may bridge Unity objects into runtime services, but should not become service locators.

This change is the first composition-hardening slice. It does not implement SO/R3/MessagePipe migration; those are later slices after DI boundaries are stable.

## Goals / Non-Goals

**Goals:**

- Remove broad Unity scene discovery fallback behavior from owned runtime composition code.
- Keep `GameplayLifetimeScope` focused on NhemDI/VContainer scope composition.
- Define explicit scene participant composition for memory probe/fragments.
- Preserve existing M0/M1 memory loop behavior and evidence quality.
- Make missing scene composition diagnosable with project logger output or validation paths.
- Add focused guardrails preventing reintroduction of service locator/search fallback APIs.

**Non-Goals:**

- No CombatCore refactor.
- No input architecture refactor.
- No M0 contracts split.
- No ScriptableObject migration.
- No R3/MessagePipe migration.
- No broad NhemDI migration outside the composition seams touched by this slice.
- No scene/prefab edits in proposal phase.
- No behavior change to MemoryState, MemoryInteractionService, prompt, reveal feedback, or runtime memory log.

## Decisions

### Decision 1: Treat scene object discovery as an explicit composition concern

Scene-provided memory participants must be represented through an explicit composition boundary rather than broad calls from `GameplayLifetimeScope`. Acceptable implementation options during apply include:

- a serialized scene registry/adapter component registered into the gameplay scope;
- a narrow provider that receives explicit scene references from an existing scene adapter;
- a bootstrap adapter that registers known participants without runtime search fallback.

The selected implementation must avoid Service Locator patterns and must not silently discover arbitrary scene objects.

Rationale:

- Makes runtime wiring reviewable.
- Keeps scene composition failures visible.
- Prevents new gameplay systems from copying `FindObjectsByType` fallback patterns.

### Decision 2: Keep gameplay truth owners unchanged

The composition boundary only supplies dependencies and participants. It must not decide:

- reveal acceptance/rejection;
- fragment collect/reveal state;
- Interact duplicate policy;
- prompt eligibility;
- reveal feedback replay policy;
- combat/memory outcome validity.

Those remain owned by `MemoryState`, `MemoryInteractionService`, and the existing presentation adapters/read models.

Rationale:

- This is a SOLID/DI refactor, not a gameplay behavior slice.
- Ownership drift would invalidate existing Sprint 3/Sprint 4 evidence.

### Decision 3: NhemDI remains preferred for pure/runtime gameplay services

Pure or runtime-scoped services that can be auto-registered should use existing NhemDI attributes and `IGameplayLifetimeScope`. Manual registration is allowed only for scene object instances or explicitly documented special cases that NhemDI cannot construct.

Rationale:

- Aligns with current project direction.
- Avoids reverting to manual registration for normal gameplay services.
- Keeps special cases honest and visible.

### Decision 4: SO/R3/MessagePipe are deferred follow-up slices

This change may document future seams for authored config (ScriptableObject), read-only streams (R3), or event messaging (MessagePipe), but it must not introduce those migrations in this slice.

Rationale:

- DI composition needs to be stable before introducing event/read-model infrastructure.
- Keeping this slice small makes regression evidence meaningful.

## Target Shape

The target runtime composition shape after implementation:

- `GameplayLifetimeScope`
  - owns gameplay scope configuration;
  - invokes generated/NhemDI registration;
  - registers explicitly provided scene adapters/instances only when necessary;
  - does not perform broad Unity scene searches.

- Scene composition adapter/provider
  - owns serialized or explicitly supplied Unity scene references;
  - exposes narrow read/registration methods;
  - validates required references;
  - logs setup issues via project logger;
  - does not own gameplay truth.

- Memory runtime services
  - continue to own interaction/reveal logic as currently defined.

## Risks / Trade-offs

- **Risk:** Existing scene wiring depends on broad discovery and may fail when removed.
  **Mitigation:** First map current discovery behavior, then replace with explicit references/providers and focused PlayMode checklist.

- **Risk:** Scene adapter becomes a hidden service locator.
  **Mitigation:** Require narrow APIs and source guardrail tests against `FindObject*` / `Resources.Load`.

- **Risk:** Manual registration is reintroduced too broadly.
  **Mitigation:** Allow manual registration only for Unity scene instances or documented special cases; keep pure services NhemDI-registered.

- **Trade-off:** Explicit composition may require small scene-facing adapter types.
  **Mitigation:** Accept small adapters to remove ambiguous runtime search behavior.

## Migration Plan

1. Baseline current composition and memory loop behavior.
2. Identify all owned runtime composition search/fallback calls in `Assets/_Project/Code`.
3. Design the smallest explicit scene composition boundary for memory probe/fragments.
4. Replace broad discovery with explicit composition.
5. Add guardrail tests for no owned runtime `FindObject*` / `Resources.Load` usage in the hardened path.
6. Run compile, focused memory tests, M0 defensive regression, and manual PlayMode memory loop.

Rollback strategy:

- Revert only the composition boundary changes.
- Do not modify MemoryState, MemoryInteractionService, CombatCore, Input, or presentation behavior during rollback.

## Verification Strategy

- `dotnet build afterimage-tokyo/afterimage-tokyo.sln --no-restore`.
- Focused EditMode tests for composition guardrails and memory path parity.
- Existing M1 memory prompt/reveal/log tests.
- M0 defensive regression checks.
- Manual PlayMode checklist:
  - eligible fragment prompt visible;
  - Interact accepted;
  - reveal feedback appears once;
  - runtime memory log appends one entry;
  - spam/duplicate Interact does not replay or append incorrectly.
- Console classification with PASS/PARTIAL/FAIL evidence table.

## Open Questions

- Which existing scene object should own explicit memory participant references: a dedicated registry adapter, an existing memory bootstrap adapter, or a small serialized provider?
- Whether implementation should require scene/prefab edits or can be completed through existing scene components and code-only adapters.
- Whether missing optional scene participants should warn or fail readiness in M0 prototype scenes.
