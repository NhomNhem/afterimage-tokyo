# Design — M0 Lock-On Camera Readability (S2-4)

## 1. Readability Definition (M0)

Lock-on camera readability means:

- Player silhouette and enemy silhouette are simultaneously visible most of the duel loop.
- Telegraph/commit/active/recovery phase reads are not hidden by framing.
- Attack/dodge/parry feedback can be observed without camera-induced ambiguity.
- Camera behavior does not become a hidden gameplay rule source.

## 2. Safe Tuning Surface (Plan for later implementation)

Allowed (parameter-level) tuning candidates:

- Camera follow offset (x/y/z bounds)
- Camera distance / shoulder spacing
- Dead zone / soft zone sizing
- Damping and recenter smoothing
- Lock-on framing bias between player and target
- Max yaw/pitch constraints for duel readability

Constraints:

- Tune only readability/framing parameters.
- Keep lock-on source target from `TargetContext`; camera may consume, never author.

## 3. Explicit Non-Changes

- No combat result logic in camera.
- No lock-on truth in camera.
- No enemy lifecycle truth in camera.
- No input intent truth in camera.
- No memory reveal truth in camera.
- No camera system rewrite/new architecture.
- No targeting refactor.
- No combat timing changes.
- No combat result changes.
- No EnemyIntent lifecycle changes.
- No enemy AI behavior tree/GOAP/boss/roster expansion.
- No input architecture changes.
- No TargetContext ownership changes.
- No camera-driven combat, target, input, enemy intent, memory, or debug overlay state.
- No cinematic camera system.
- No multi-enemy camera.
- No root motion authority.

## 4. Ownership Boundaries

- `TargetContext`: lock-on target truth.
- `CombatCore`: combat timing/results.
- `EnemyIntent`: phase lifecycle.
- `PlayerLocomotion`: movement/facing/recovery.
- Camera: presentation/framing only.
- Debug Overlay: read-only verification surface.

## 5. Evidence Plan

Required evidence bundle for S2-4 implementation pass:

- Focused test results (if runtime parameter plumbing/guards are changed).
- Manual PlayMode checklist results (at least 3 duel loops).
- PASS/PARTIAL/FAIL matrix for:
  - Player+enemy simultaneous readability
  - Attack/dodge/parry readability under lock-on
  - Enemy phase readability
  - Camera independence from gameplay truth
  - Console/domain classification

Concrete rubric:

- Player + enemy framing
  - PASS: player and locked enemy remain readable through at least 3 observed enemy intent loops.
  - PARTIAL: occasional framing/occlusion issue occurs, but duel remains understandable and playable.
  - FAIL: player or enemy is repeatedly lost/off-screen/obscured during core duel beats.

- Enemy telegraph visibility
  - PASS: Telegraph/Commit/Active/Recovery cues remain visible during lock-on framing checks.
  - PARTIAL: at least one cue is hard to read but recoverable.
  - FAIL: enemy cue visibility is frequently blocked or unreadable.

- Attack/Dodge/Parry visibility
  - PASS: LightAttack, Dodge, and Parry attempts remain readable and are not obscured by camera framing.
  - PARTIAL: one beat is unclear but gameplay still continues.
  - FAIL: camera framing prevents reliable reading of one or more core defensive/offensive beats.

- Ownership boundary
  - PASS: no changes to TargetContext ownership, CombatCore timing/results, EnemyIntent lifecycle, Input, Debug Overlay truth, or PlayerLocomotion truth.
  - FAIL: any gameplay truth is moved into camera logic or camera drives gameplay state.

- Console/domain
  - PASS: no S2-4 scope errors/exceptions.
  - PASS WITH NOTES: only known external/non-S2-4 warnings/errors are present and classified.
  - FAIL: new S2-4-related error/exception appears.

## 6. Rollback / Migration

If readability worsens:

1. Revert tuned parameter set to previous known-good baseline.
2. Keep evidence diff showing before/after readability impact.
3. Retry with smaller deltas and one-parameter-at-a-time changes.
4. Mark status `PARTIAL` with disclosed limitation rather than forcing PASS.
5. Revert camera tuning values/parameters only.
6. Do not revert or alter `TargetContext`, `CombatCore`, `EnemyIntent`, `Input`, or `PlayerLocomotion` to fix camera readability.
