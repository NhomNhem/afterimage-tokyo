## Context

M0 duel flow is verified and must not regress. S3-2 Memory Fragment Interaction is active and depends on the Interact intent path remaining stable. The current input implementation has high coupling: Unity InputAction reading, per-action interpretation, and direct gameplay calls are mixed, which weakens SOLID boundaries and raises regression risk when extending input behavior.

The project constraints require:
- Unity New Input System only.
- Input remains raw intent only.
- Gameplay truth stays in existing owners (CombatCore, PlayerLocomotion, TargetContext, MemoryInteractionService, MemoryState).
- Debug/evidence still exposes latest input routing visibility.

## Goals / Non-Goals

**Goals:**
- Introduce a strict two-layer input architecture:
  1. Unity Input Adapter layer (callback binding/state capture only).
  2. Gameplay Input Intent layer (raw intent snapshot/event publication only).
- Preserve current behavior for Move, LightAttack, HeavyAttack (if present), Dodge, Parry, Counter, LockOn, Interact.
- Keep Interact compatible with S3-2 memory fragment flow.
- Preserve smoke-check readability and debug evidence (LastInput or equivalent).

**Non-Goals:**
- No combat/locomotion/target/memory outcome changes.
- No camera/enemy/animation/VFX/UI changes.
- No R3/MessagePipe migration in this change.
- No generated DI migration or DI strategy redesign.
- No input rebinding UX, persistence, or profile/settings work.

## Decisions

### 1) Two-layer split at input boundary
- Decision: isolate Unity callback binding in a dedicated adapter; publish normalized raw intent through gameplay-facing provider/snapshot layer.
- Rationale: reduces class responsibility overlap and preserves clear ownership boundaries.
- Alternative considered: keep current monolith and only tidy methods.
  - Rejected because structural coupling and testability problems remain.

### 2) Preserve action contract and mapping names
- Decision: retain action semantics and mapping names for all current actions.
- Rationale: enables behavior-preserving refactor and regression comparison against current M0/S3-2 evidence.
- Alternative considered: change action shapes (hold vs press) during refactor.
  - Rejected because it risks hidden gameplay feel drift.

### 3) Keep direct architecture, defer R3/MessagePipe
- Decision: use simple snapshot/events in current architecture and defer reactive bus migration.
- Rationale: this change is refactor-only; introducing messaging patterns now increases scope and uncertainty.
- Alternative considered: migrate input publication to MessagePipe immediately.
  - Rejected due to added moving parts and broader verification burden.

### 4) Maintain existing debug evidence contract
- Decision: keep LastInput (or equivalent) visible to existing overlay/debug evidence path.
- Rationale: needed for smoke/regression verification and triage continuity.
- Alternative considered: redesign debug overlay contract in same change.
  - Rejected as out-of-scope.

## Risks / Trade-offs

- [Risk] Pressed/held/released transitions may drift while moving callback logic.
  → Mitigation: preserve per-action edge semantics and validate with focused routing checks.

- [Risk] Duplicate routing (adapter + legacy path) during intermediate refactor stage.
  → Mitigation: use one active publish path per action at each thin slice.

- [Risk] Interact regression may block S3-2 progress.
  → Mitigation: migrate Interact in first thin-slice verification before broader action migration.

- [Risk] DI wiring ambiguity (manual + auto) may reappear while touching bootstrap.
  → Mitigation: keep DI ownership explicit and apply ND005-safe registration policy.

## Migration Plan

1. Introduce/shape Unity Input Adapter contract while preserving current external behavior.
2. Route adapter output into gameplay intent snapshot/events for Interact first.
3. Verify Interact + memory flow and debug evidence before migrating additional actions.
4. Migrate remaining actions incrementally: LockOn, attacks, defensive inputs, Move.
5. Remove redundant legacy routing path once parity is demonstrated.
6. Run focused routing checks + manual smoke checklist; classify PASS/PARTIAL/FAIL.

Rollback:
- Keep changes in thin slices so each slice can be reverted independently if parity fails.
- If regression appears, disable new routing path and restore prior input bridge behavior for impacted action only.

## Open Questions

- Should HeavyAttack be treated as mandatory in checklist when action is absent in specific scene profiles?
- Is current LastInput field name retained as-is or replaced by equivalent mapped label string?
