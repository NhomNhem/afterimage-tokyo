# Tasks: Improve M0 Enemy Telegraph Readability

## 1. Baseline Health

- [x] 1.1 Keep EditMode compile green after Odin-serialized config dependency changes.
- [x] 1.2 Run focused composition checks:
      - `SceneComposition_test`
      - `VContainerRegistry_test`
- [x] 1.3 Record any pre-existing unrelated worktree changes before apply.

## 2. Readability Model

- [x] 2.1 Inspect existing Enemy Intent snapshot/read model.
- [x] 2.2 Add or refine read-only fields for phase label, phase progress/time remaining, attack tags, and punish availability only if missing.
- [x] 2.3 Ensure readability data is immutable and derived from Enemy Intent truth.

## 3. Presentation/Debug Consumption

- [x] 3.1 Align Debug Overlay enemy channel labels with Telegraph, Commit, Active, Recovery, and punish availability.
- [x] 3.2 Keep presentation cue consumers observer-only.
- [x] 3.3 Avoid camera, lock-on, VFX, or audio ownership changes unless explicitly needed for read-only cue display.

## 4. Tests

- [x] 4.1 Add focused EditMode tests for phase readability snapshot shape.
- [x] 4.2 Add focused tests for attack tag continuity from Commit through Active.
- [x] 4.3 Add focused tests for punish availability exposure.
- [x] 4.4 Add source/architecture guard test if new presentation/debug code is introduced.

## 5. Evidence

- [x] 5.1 Create evidence at `production/qa/evidence/improve-m0-enemy-telegraph-readability-verification-YYYY-MM-DD.md`.
- [x] 5.2 Record focused automated test results and console classification.
- [x] 5.3 Record manual PlayMode checklist for at least three enemy intent loops.
- [x] 5.4 Mark PASS/PARTIAL/FAIL with explicit notes for any remaining readability ambiguity.

## 6. Closure

- [x] 6.1 Run `openspec validate improve-m0-enemy-telegraph-readability --strict`.
- [x] 6.2 Confirm no out-of-scope gameplay systems were added.
- [x] 6.3 Confirm M0 ownership boundaries remain intact.
