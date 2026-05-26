## 1. Reset Contract Definition

- [x] 1.1 Confirm reset entry/exit contract and reset order across Combat Core, Player Locomotion, Enemy Intent, and Target Context.
- [x] 1.2 Define/reset trigger path for M0 smoke usage without changing input binding architecture.
- [x] 1.3 Document allowed vs forbidden implementation files in change notes before code edits.

## 2. Combat and Locomotion Reset Wiring

- [x] 2.1 Add/reset Combat Core API path to force post-reset `Neutral` and clear transient combat state.
- [x] 2.2 Add/reset Player Locomotion API path to restore known start transform and clear movement/dodge transient runtime state.
- [x] 2.3 Bridge reset orchestration in GameplayTickHandler/bootstrap without moving gameplay truth ownership.

## 3. Enemy and Target Reset Wiring

- [x] 3.1 Add/reset Enemy Intent model/loop path to initial known duel state.
- [x] 3.2 Add/reset Target Context release path for encounter reset (`Active=false`, target cleared unless configured initial reacquire).
- [x] 3.3 Ensure reset ordering prevents stale overlay snapshot or stale target/combat references.

## 4. Debug and Logging Integrity

- [x] 4.1 Ensure debug overlay reflects post-reset snapshot fields read-only (no reset authority).
- [x] 4.2 Add minimal diagnostics using NhemLogger only; gate noisy traces behind debug/prototype defines.
- [x] 4.3 Keep existing non-blocking animation warnings unchanged.

## 5. Verification and Evidence

- [x] 5.1 Compile/domain reload passes with no new compiler errors.
- [x] 5.2 Run focused EditMode tests for reset behavior (or add targeted tests if coverage missing).
- [x] 5.3 Manual PlayMode capture proves reset lifecycle: active duel -> reset -> clean playable state.
- [x] 5.4 Capture before/after reset evidence: combat state, player transform, enemy intent state, lock-on target.
- [x] 5.5 Confirm no new gameplay console errors; classify known non-blocking warnings separately.
- [x] 5.6 Update evidence doc under `production/qa/evidence` with explicit artifact references and final pass/partial/fail table.

## Closure Snapshot — 2026-05-25

Verdict: COMPLETED WITH NOTES

Evidence:
- `production/qa/evidence/wire-m0-encounter-reset-duel-lifecycle-verification-2026-05-25.md`

Summary:
- Compile/domain reload: PASS
- Focused EditMode reset tests: PASS
- Manual PlayMode reset flow: PASS
- Before/after reset state artifacts: PASS
- Console classification: PASS WITH KNOWN NON-BLOCKING WARNINGS
- Evidence doc update: PASS

Known non-blocking warnings:
- Animation presentation adapter missing.
- Animation presentation not assigned.
- Target SceneAdapter inactive registration warning during bootstrap.

Notes:
- Reset lifecycle is verified for the minimum M0 duel loop.
- Scope stayed limited to reset orchestration and domain-owner reset APIs.
- No save/load, checkpoint, scene transition, full encounter manager, UI restart, camera, animation, VFX, multi-enemy, or progression scope was added.

Archive readiness: YES after scoped commit/push.
