# Tasks — S2-4 Lock-On Camera Readability Pass

## 1. Planning Scope Lock

- [x] 1.1 Confirm plan-only status (no runtime/scene tuning in this change).
- [x] 1.2 Confirm ownership guardrails for camera vs gameplay truth.
- [x] 1.3 Confirm forbidden scope list is explicit.

## 2. Readability Contract

- [x] 2.1 Define what lock-on readability means for M0 duel.
- [x] 2.2 Define safe camera parameter tuning surface.
- [x] 2.3 Define non-change constraints.

## 3. Verification Contract

- [x] 3.1 Define required evidence categories (tests/manual/console).
- [x] 3.2 Define PASS/PARTIAL/FAIL criteria.
- [x] 3.3 Define manual PlayMode checklist minimum loops and observations.
- [x] 3.4 Define camera-truth independence checks (TargetContext/CombatCore/EnemyIntent unchanged ownership).

### Manual PlayMode Checklist (Concrete)

- [x] Launch M0 combat prototype scene.
- [x] Acquire lock-on target.
- [x] Verify lock-on acquire/release (or on/off) transition readability.
- [x] Observe at least 3 enemy intent loops:
      `Idle -> Telegraph -> Commit -> Active -> Recovery`.
- [x] During observed loops, perform:
      `LightAttack`, `Dodge`, and at least one `Parry` attempt.
- [x] Verify player and enemy remain visible/readable during lock-on framing.
- [x] Verify telegraph/commit/active/recovery cues are not hidden by framing.
- [x] Verify attack/dodge/parry beats are not obscured by camera behavior.
- [x] Verify camera does not cause severe occlusion or loss of target.
- [x] Verify Debug Overlay still displays camera-independent gameplay truth.
- [x] Read console and classify errors/warnings.
- [x] Confirm scene dirty files are intentional if any scene/prefab changes occur.

## 4. Risk & Rollback

- [x] 4.1 Define readability regression risks.
- [x] 4.2 Define rollback plan and recovery workflow.

## 5. Ready-for-Apply Gate

- [x] 5.1 Proposal/design/spec are complete for implementation kickoff.
- [x] 5.2 Scope remains S2-4 camera readability only.
- [x] 5.3 Change is ready for `/opsx:apply tune-m0-lockon-camera-readability`.
