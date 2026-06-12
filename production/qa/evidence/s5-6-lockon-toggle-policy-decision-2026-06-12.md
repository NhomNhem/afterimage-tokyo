# S5-6 LockOn Toggle Policy Decision

Date: 2026-06-12

Story: `production/sprints/sprint-5-stories/story-s5-6-lockon-toggle-policy.md`

## Verdict

PASS — M0 LockOn second-press policy is **toggle acquire/release**.

## Decision

M0 chooses **Option B: toggle acquire/release**.

Policy:

- First LockOn press with no focused valid target requests acquisition of the current duel target.
- Second LockOn press while a valid target is focused requests explicit release.
- Third LockOn press after release may reacquire the same valid duel target.

## Rationale

Toggle acquire/release best supports M0 duel readability because it keeps target focus intentional and makes release explainable. The player can opt out of focus without needing hold timing, multi-target cycling, or camera-owned target truth.

This is still a small one-duel policy:

- one player
- one simple enemy
- one active target max
- explicit acquire/release reasons
- no multi-target scope
- no camera or combat authority changes

## Evidence Cited

- `production/qa/evidence/complete-m0-playable-combat-prototype-verification-evidence.md`
  - Validates first-press acquire/focus behavior.
  - Records second-press ambiguity as follow-up in the 2026-05-21 capture.
- `production/qa/evidence/lockon-toggle-release-2026-05-24.md`
  - Later focused evidence validates the full transition: `None -> Enemy -> None -> Enemy`.
  - Confirms first press acquire, second press release, and third press reacquire through debug overlay/log observation.

## Design Update

Updated:

- `design/gdd/lock-on-target-context.md`

Added:

- M0 second-press policy decision.
- Toggle acquire/release rules.
- Rationale for why toggle-release better supports one readable M0 duel.

## Follow-Up Implementation

No follow-up implementation story is required right now because the latest focused evidence already matches the selected policy.

If a future runtime pass diverges from this policy, create a separate implementation story/change. Do not modify runtime behavior as part of S5-6.

## Scope Confirmation

No runtime code, scene, prefab, gameplay, camera, UI, or input-binding behavior was changed by this story.
