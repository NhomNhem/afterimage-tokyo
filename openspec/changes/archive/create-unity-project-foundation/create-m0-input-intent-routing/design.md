## Context

`M0 Input Mapping` already defines the broad boundary: Unity New Input System only, raw intent only, enabled/disabled state, and debug visibility. The current foundation contracts provide `InputIntentSnapshot`, `InputRoutingResult`, and an input action asset, but the change still needs a precise routing contract that keeps input from becoming gameplay authority.

This change sits upstream of locomotion, combat, targeting, camera, and debug presentation. It must preserve the architecture rule that `Input Mapping` emits intent and routing outcomes, while downstream systems own validation and state truth.

## Goals / Non-Goals

**Goals:**
- Represent raw M0 input intent from Unity New Input System actions.
- Preserve input enabled/disabled state.
- Record downstream routing outcomes, including ignored and rejected results with optional reasons.
- Keep the latest input snapshot read-only and consumable by future debug presentation.
- Keep input code under `Assets/_Project/Code/Input` and shared contract types under `Assets/_Project/Code/Core`.
- Avoid direct coupling to concrete combat, locomotion, targeting, or camera implementations.

**Non-Goals:**
- Gameplay validation for attacks, dodges, parries, counters, lock-on, or reveal.
- Movement behavior, combat behavior, target acquisition behavior, or camera behavior.
- Final debug UI or player-facing UI.
- Legacy Unity Input Manager support.
- Service locator or global gameplay orchestration.

## Decisions

### 1. Keep input as a thin router over a read-only intent model

**Decision:** Treat the input layer as a thin adapter that samples Unity New Input System actions and produces immutable intent snapshots plus routing outcomes.

**Why:** This matches the architecture boundary already established in `M0Contracts.cs` and avoids hiding gameplay truth inside input handling.

**Alternatives considered:**
- Let input call gameplay systems directly
  - rejected because it would couple input to concrete combat/locomotion logic
- Make input a stateful gameplay subsystem
  - rejected because input must not own validation or movement truth

### 2. Extend the routing outcome model to distinguish categories explicitly

**Decision:** Use explicit routing outcomes for disabled, ignored, routed, and rejected states, with an optional reason when downstream systems provide one.

**Why:** The proposal requires those distinctions to be visible without making input own validation.

**Alternatives considered:**
- Single accepted/rejected flag only
  - rejected because it loses the difference between disabled input and downstream rejection
- Push rejection reasons into gameplay state
  - rejected because that would move authority out of downstream systems

### 3. Keep debug visibility read-only and snapshot-based

**Decision:** Expose debug-facing input state as a read-only snapshot/event surface, not as a mutable debug model.

**Why:** `Debug Overlay` should explain input state later without becoming part of the input decision path.

**Alternatives considered:**
- Mutate a shared debug singleton
  - rejected because it blurs ownership and creates a hidden authority layer
- Defer all debug visibility until the debug UI exists
  - rejected because the proposal explicitly needs debug-consumable input state

### 4. Preserve New Input System as the only input path

**Decision:** Keep the M0 action contract aligned to Unity New Input System only and reject any legacy Input Manager path.

**Why:** The project architecture already requires this and the current foundation asset is already New Input System-based.

**Alternatives considered:**
- Support both input paths temporarily
  - rejected because it creates ambiguity and violates the M0 input rule

### 5. Keep input routing decoupled from concrete gameplay implementations

**Decision:** Input should emit intent and routing results against abstract contracts, not against concrete combat or locomotion classes.

**Why:** This preserves testability and keeps Input Mapping from owning downstream authority.

**Alternatives considered:**
- Inject concrete gameplay services directly into input
  - rejected because it introduces tight coupling and encourages validation leakage

## Risks / Trade-offs

- **Action-name drift between asset and contract** → Keep the input action list mirrored in one contract/asset review and cover it with tests.
- **Routing categories become vague** → Use explicit outcome states and keep reasons optional but preserved.
- **Debug snapshot becomes a second source of truth** → Make the snapshot read-only and derived from the input router state only.
- **Input layer grows into orchestration** → Keep it as a facade/router only; no gameplay validation or recovery handling.
- **More contract churn before implementation** → Lock the intent vocabulary first, then wire consumers later.

## Migration Plan

1. Review current M0 input foundation, contracts, and action asset.
2. Refine or add input DTOs and routing outcome shapes in `Assets/_Project/Code/Core`.
3. Add the lightweight input router/facade in `Assets/_Project/Code/Input`.
4. Expose the read-only input snapshot/event surface for debug consumption.
5. Add tests for contract shape, no legacy input references, and read-only snapshot access.
6. Import/validate in Unity and confirm no legacy input path appears.

Rollback strategy:

- Revert the input DTO/router additions and keep the foundation asset unchanged if the routing contract proves too broad.

## Open Questions

- Should `Counter` remain a separate raw action or be represented as a contextual follow-up later?
- Should `Pause` remain optional in the gameplay map for M0, or stay out of this change entirely?
- Should debug actions use the current `ResetEncounter` / `ToggleDebugOverlay` names or be normalized later to `Debug*` names?
