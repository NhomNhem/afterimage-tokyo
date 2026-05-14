## Context

M0 needs a locomotion owner before combat, camera, and animation layers accumulate around it. The existing input work already emits raw movement intent, and the architecture says movement truth belongs to Player Locomotion, not to Input, Camera, Target Context, or Animator.

This change is only a skeleton: a pure C# locomotion state model, read-only snapshot surface, movement restriction/recovery seam, and debug visibility. It must stay compatible with the current M0 contract layer and keep root motion, CharacterController polish, and camera-relative movement implementation deferred.

## Goals / Non-Goals

**Goals:**
- Establish Player Locomotion as the owner of movement truth.
- Consume raw movement intent as data from the input routing layer.
- Represent locomotion state transitions in pure C#.
- Expose read-only locomotion snapshots and debug-readable state.
- Represent movement restriction and recovery/action-lock seams for Combat Core.
- Keep camera-relative movement basis read-only and deferred.

**Non-Goals:**
- Full CharacterController movement or tuning.
- Combat movement, dodge feel tuning, parry/counter logic, or hit reaction behavior.
- Final animation graph, root-motion authority, or Animator-driven gameplay truth.
- Target-lock movement behavior.
- Final prefab, scene, or player wiring.
- Legacy Input Manager support or generated DI APIs.

## Decisions

### 1. Keep locomotion as a pure C# state owner

**Decision:** Model Player Locomotion as a small FSM/service with explicit state and snapshot output, rather than binding movement truth to Animator state or scene presentation.

**Why:** The architecture already treats gameplay truth as C#-owned, and locomotion must remain inspectable for the duel prototype. A small state owner is easier to test and easier for Combat Core to restrict or recover against.

**Alternatives considered:**
- Drive locomotion from Animator state
  - rejected because animation must remain presentation-only
- Fold locomotion truth into Combat Core
  - rejected because movement ownership would blur and combat would inherit too much authority

### 2. Consume input as raw intent data only

**Decision:** The locomotion layer should read raw movement intent from the input snapshot and interpret it locally without asking Input to validate movement.

**Why:** Input Mapping already owns raw intent emission. Locomotion can decide how to apply movement state, while Input stays a thin contract layer.

**Alternatives considered:**
- Let Input decide movement validity
  - rejected because it would move gameplay authority into input
- Have locomotion pull from concrete input components directly
  - rejected because it would create unnecessary coupling and weaken testability

### 3. Represent restriction and recovery as explicit contexts

**Decision:** Define movement restriction and recovery/action-lock context shapes that Combat Core can set or clear, while Locomotion interprets them as state restrictions.

**Why:** The player needs readable commitment and recovery seams, but locomotion should not invent combat rules. Explicit contexts keep ownership clear and make debug output explainable.

**Alternatives considered:**
- Encode restrictions as hidden booleans inside movement code
  - rejected because it would obscure ownership and debug traceability
- Let Combat Core directly mutate movement state
  - rejected because locomotion must remain the movement authority

### 4. Keep debug output read-only and derived

**Decision:** Expose locomotion debug state as a read-only snapshot derived from locomotion state and restriction contexts.

**Why:** Debug Overlay needs stable visibility later, but debug consumers must not mutate gameplay truth.

**Alternatives considered:**
- Expose mutable debug state objects
  - rejected because it would create a second source of truth
- Delay debug support until the overlay exists
  - rejected because this skeleton explicitly needs inspectable state now

### 5. Keep camera-relative basis deferred and read-only

**Decision:** If the locomotion skeleton references camera-relative movement at all, it should do so via a read-only basis context, not by owning camera truth.

**Why:** Camera should not become the movement authority, and the locomotion skeleton does not need final camera-relative behavior yet.

**Alternatives considered:**
- Implement full camera-relative movement now
  - rejected because it exceeds skeleton scope
- Let the camera mutate locomotion direction directly
  - rejected because it inverts ownership

## Risks / Trade-offs

- [State model grows too fast] → Keep the FSM small and only add states that are needed to explain current M0 movement ownership.
- [Recovery seam becomes combat logic] → Keep the seam descriptive and data-driven; Combat Core owns validation, not locomotion.
- [Debug snapshot turns into a second authority] → Derive snapshots from locomotion state only and keep them read-only.
- [Camera-relative handling expands early] → Treat it as a read-only placeholder until a later change explicitly owns that behavior.

## Migration Plan

1. Inspect current M0 contracts, input router, and existing locomotion assembly boundaries.
2. Add or refine locomotion state and context contracts in shared core types if needed.
3. Add the pure C# locomotion FSM/service skeleton.
4. Connect raw movement intent consumption as data only.
5. Add a read-only debug snapshot surface.
6. Add edit mode tests for idle, moving, restricted, and recovering behavior.
7. Validate that no legacy input or generated DI references were introduced.

Rollback strategy:

- Remove the locomotion skeleton and restore the prior contract surface if the state model proves too broad for M0.

## Open Questions

- Should dodge become a placeholder locomotion state in the skeleton, or remain entirely deferred until a later locomotion/combat integration change?
- Should camera-relative basis be represented in the locomotion snapshot now or only as a future placeholder contract?
- Should locomotion expose a separate transition history for debug, or is the latest snapshot enough for M0?
