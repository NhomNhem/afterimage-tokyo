## Context

M0 already has the raw input contract, locomotion contracts, and combat contracts in place, but target truth still needs a minimal dedicated owner so the duel can remain legible. `Lock-On / Target Context` must stay narrower than full targeting and avoid becoming a camera, locomotion, or combat authority layer.

This change is a skeleton only: target state, focus state, request shapes, validity, direction/context snapshots, and read-only debug exposure. It must remain compatible with the existing M0 contract style and keep camera-relative or locomotion-facing behavior deferred to downstream consumers.

## Goals / Non-Goals

**Goals:**
- Establish Lock-On / Target Context as the authority for target truth.
- Consume raw `LockOn` intent as a request source without giving Input ownership of target validity.
- Represent target focus, current target, validity, and direction/context in pure C#.
- Expose read-only target snapshots for locomotion, camera, combat, and debug.
- Keep target release/acquire reasons visible and explainable.

**Non-Goals:**
- Production lock-on UI or reticle behavior.
- Camera behavior, locomotion behavior, or combat validation.
- Target cycling, boss-part targeting, aim assist, or enemy AI.
- Final scene/prefab wiring.
- Legacy Input Manager support or generated DI APIs.

## Decisions

### 1. Keep target truth as a pure C# state owner

**Decision:** Model target context as a small FSM/service with explicit state and snapshot output rather than as camera or combat logic.

**Why:** The architecture says target truth belongs in `Lock-On / Target Context`, and the target layer needs to be independently inspectable by locomotion, camera, and combat.

**Alternatives considered:**
- Fold target truth into camera logic
  - rejected because camera should only read target truth
- Fold target truth into combat logic
  - rejected because combat should observe target context, not own it

### 2. Treat raw LockOn input as a request source only

**Decision:** `Input Mapping` supplies raw `LockOn` intent; target context converts that into acquire/release requests and validity state.

**Why:** Input must remain a raw intent source. Target truth and validity are downstream responsibilities.

**Alternatives considered:**
- Let Input decide target validity
  - rejected because it would move gameplay authority into input
- Let locomotion or camera drive lock-on truth directly
  - rejected because target ownership would become ambiguous

### 3. Expose target direction/context as read-only data

**Decision:** Represent the current target reference, validity, and target direction/context as read-only snapshot data.

**Why:** Locomotion and camera need orientation support, but they must not be able to mutate the target authority.

**Alternatives considered:**
- Expose a mutable shared target singleton
  - rejected because it would create hidden authority coupling
- Delay direction/context until later
  - rejected because M0 already needs a skeleton for downstream readability

### 4. Keep release/acquire reasons explicit

**Decision:** Include simple acquire/release/invalid reason shapes in the target skeleton.

**Why:** M0 debug visibility depends on knowing why target focus changed without pushing validity rules into input or presentation layers.

**Alternatives considered:**
- Only expose a yes/no focus flag
  - rejected because it loses debuggability
- Store reasons only in debug UI
  - rejected because the ownership of truth would become unclear

## Risks / Trade-offs

- [Target scope creeps toward full lock-on system] → Keep the state model limited to one target and the M0 duel loop.
- [Camera or locomotion starts owning target truth] → Keep their inputs read-only and expose only snapshots/context.
- [Acquire/release reasons become validation logic] → Keep the skeleton descriptive; downstream systems own actual validation decisions.
- [Debug snapshot becomes a second authority] → Derive it from target context state only and keep it read-only.

## Migration Plan

1. Inspect the current M0 contracts and input router boundaries.
2. Define or refine target context state, focus state, and snapshot contracts if needed.
3. Add the pure C# target context FSM/service skeleton.
4. Consume raw lock-on intent as request data only.
5. Add read-only debug snapshot exposure.
6. Add edit mode tests for acquire, focus, release, and invalid target behavior.
7. Validate that no legacy input or generated DI references were introduced.

Rollback strategy:

- Remove the target context skeleton and restore the prior contract surface if the state model proves too broad for M0.

## Open Questions

- Should the skeleton expose a transition history, or is the latest read-only snapshot enough for M0?
- Should encounter-seeded target acquisition be represented now or deferred to the later gameplay wiring change?
- Should direction/context include a camera-facing basis placeholder, or only target-relative directional data?
