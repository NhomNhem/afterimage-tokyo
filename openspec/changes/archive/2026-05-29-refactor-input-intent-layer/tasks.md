## 1. Baseline and parity guardrails

- [x] 1.1 Capture current input routing baseline for Move, LightAttack, Dodge, Parry, Counter (if available), LockOn, and Interact.
- [x] 1.2 Confirm and document current LastInput (or equivalent) debug evidence output used by smoke validation.
- [x] 1.3 Define explicit behavior parity checklist for M0 loop and S3-2 Interact flow.

## 2. Two-layer input architecture refactor

- [x] 2.1 Introduce Unity Input Adapter responsibility boundary: InputAction callback binding and raw state capture only.
- [x] 2.2 Introduce Gameplay Input Intent responsibility boundary: raw intent snapshot/event publication only.
- [x] 2.3 Ensure Input layer does not perform combat validity, locomotion validity, target truth, or memory truth decisions.
- [x] 2.4 Preserve existing action support and semantics for Move, LightAttack, HeavyAttack (if present), Dodge, Parry, Counter, LockOn, Interact.

## 3. Interact-first compatibility slice (S3-2 critical)

- [x] 3.1 Route Interact through the new two-layer path while preserving current MemoryInteractionService orchestration.
- [x] 3.2 Verify Interact remains compatible with Memory Fragment interaction and MemoryState-owned reveal/collect truth.
- [x] 3.3 Confirm no ownership drift into Input for memory acceptance/rejection decisions.

## 4. Remaining action migration and debug continuity

- [x] 4.1 Migrate LockOn routing through the new two-layer path with behavior parity.
- [x] 4.2 Migrate attack and defensive intents (LightAttack/HeavyAttack, Dodge, Parry, Counter) with behavior parity.
- [x] 4.3 Migrate Move intent publication with behavior parity and no locomotion truth ownership changes.
- [x] 4.4 Preserve LastInput or equivalent debug/evidence visibility after migration.

## 5. Verification and evidence

- [x] 5.1 Add focused input routing tests where feasible for key intents and edge transitions.
- [x] 5.2 Execute manual smoke checklist: Move, LightAttack, Dodge, Parry, Counter (if available), LockOn acquire/release, Interact.
- [x] 5.3 Run regression check against M0 duel loop and S3-2 Interact flow.
- [x] 5.4 Produce evidence table with PASS/PARTIAL/FAIL and console classification summary.
