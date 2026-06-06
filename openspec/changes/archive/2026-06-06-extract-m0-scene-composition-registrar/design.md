## Context

`GameplayLifetimeScope` is the M0 gameplay composition root. It now composes generated NhemDI registrations, authored ScriptableObject tuning, manual pure-service special cases, scene component registrations, post-build wiring, and memory scene participant injection.

The class still has too many bootstrap responsibilities. The next safe extraction is not gameplay logic; it is the scene composition wiring that bridges explicit Unity scene references into VContainer. The extraction must keep `GameplayLifetimeScope` as the top-level composition root and must not change runtime ownership or M0/S4 behavior.

## Goals / Non-Goals

**Goals:**

- Reduce `GameplayLifetimeScope` responsibility to high-level composition order.
- Extract scene component registration and post-build scene wiring into a small Bootstrap-owned registrar.
- Preserve explicit serialized scene references and the custom inspector's ability to display/bind them.
- Preserve NhemDI generated gameplay-scope registration for pure/runtime services.
- Preserve combat and locomotion ScriptableObject tuning composition.
- Preserve memory probe/fragment injection, animation service registration, tick handler adapter wiring, and enemy loop debug harness wiring.
- Add guardrail tests/evidence proving behavior-preserving extraction.

**Non-Goals:**

- No gameplay truth migration.
- No scene/prefab hierarchy redesign.
- No CombatCore, PlayerLocomotion, EnemyIntent, TargetContext, MemoryState, MemoryInteractionService, UI, VFX, Animancer, or DebugOverlay behavior changes.
- No R3 or MessagePipe migration.
- No broad NhemDI migration.
- No broad scene discovery or resource fallback.

## Decisions

### Decision: Keep GameplayLifetimeScope as the root, move details to a registrar

`GameplayLifetimeScope` should still override `Configure`, call generated gameplay-scope registration, register authored tuning/manual special cases, and delegate scene component wiring to a registrar/collaborator.

Rationale:

- Unity/VContainer still expects `LifetimeScope` to be the composition entry point.
- A registrar reduces file size without creating a second composition root.
- The change remains behavior-preserving and easy to roll back.

Alternative considered: create another `LifetimeScope` for scene components.

- Rejected because it would change scope boundaries and increase runtime risk.

### Decision: Use explicit scene references, not discovery

The registrar should receive explicit references supplied by `GameplayLifetimeScope` or a serialized scene-reference container. It must not find scene objects through broad Unity APIs.

Rationale:

- This preserves current scene composition evidence.
- Missing references remain visible in Inspector/tests.
- It respects the existing no `FindObject*` / `Resources.Load` guardrails.

Alternative considered: registrar discovers components by type from the scene.

- Rejected because it weakens composition traceability and can hide scene drift.

### Decision: Registrar owns composition wiring only

The registrar may register scene components with `IContainerBuilder`, inject scene participants after build, and call existing adapter wiring methods. It must not decide gameplay outcomes, prompt eligibility, memory acceptance, combat validity, or movement state.

Rationale:

- Bootstrap is allowed to wire Unity scene instances into runtime services.
- Gameplay truth remains in the existing owners.

### Decision: Preserve editor readability as part of closure

The UI Toolkit inspector for `GameplayLifetimeScope` can remain, but closure evidence must prove serialized fields still render/bind correctly enough for scene assignment.

Rationale:

- A readable composition root is only useful if required references can still be assigned.
- The previous binding regression showed this is a real risk.

## Risks / Trade-offs

- [Risk] Registrar becomes a renamed god class -> Mitigation: restrict it to scene component registration and build-time wiring only.
- [Risk] Scene references disappear from Inspector -> Mitigation: keep serialized fields on a Unity object and include editor binding/manual assignment checks.
- [Risk] Wiring order changes M0 behavior -> Mitigation: preserve registration/build callback order and run focused M0/S4 smoke checks.
- [Risk] NhemDI generated registration is skipped -> Mitigation: keep explicit guardrail coverage for `RegisterGeneratedFor<IGameplayLifetimeScope>()`.
- [Risk] Missing scene refs are hidden by fallbacks -> Mitigation: prohibit broad discovery and require diagnosable setup failures.

## Migration Plan

1. Capture baseline `GameplayLifetimeScope` responsibilities and current focused test pass.
2. Add a Bootstrap-owned scene composition registrar/collaborator.
3. Move scene component registration into the registrar.
4. Move post-build scene wiring into the registrar while preserving order and existing logger behavior.
5. Keep authored config conversion and generated NhemDI registration in `GameplayLifetimeScope`.
6. Add/update tests for guardrails, no broad discovery, inspector binding, and scene config references.
7. Run compile, focused EditMode tests, M0/S4 smoke checks, console classification, and OpenSpec validation.

Rollback strategy:

- Move the registrar code back into `GameplayLifetimeScope` if extraction causes composition instability.

## Open Questions

- Whether the explicit scene references should stay directly on `GameplayLifetimeScope` for this slice or move into a serialized `M0GameplaySceneCompositionReferences` container. Default implementation should prefer the smaller move unless a clean container is needed to keep Inspector UX clear.
