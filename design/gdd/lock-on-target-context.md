# Lock-On / Target Context

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Combat As Interpretation, Melancholic Elegance

## 1. System Summary

`Lock-On / Target Context` defines the authoritative M0 target-truth contract for `Glass Refrain`'s first katana duel prototype. It owns whether target focus is active, which target is current, whether that target is valid, and the direction or context exposed to adjacent systems during the core rhythm:

`read → evade/parry → counter → reveal`

For M0, this system supports one player, one simple enemy, and one active target at most inside the Tokyo Street duel space. Its purpose is not to build a full targeting framework, a multi-target lock-on system, a ranged aiming model, or a boss-part targeting solution. Its purpose is to provide a small, trustworthy source of target truth that supports readable orientation, stable duel framing, and clean debug visibility.

`Lock-On / Target Context` owns target truth only. It does not own camera framing, movement interpretation, combat validity, enemy behavior, or presentation feedback.

## 2. Design Intent

The purpose of `Lock-On / Target Context` in M0 is to stabilize a single duel relationship without making the duel play itself. The player should be able to intentionally focus the current enemy, understand where that enemy is relative to the protagonist, and benefit from clearer orientation support during a close-range katana exchange.

At M0, target focus is a readability aid, not a combat solver. It should help the player stay mentally connected to the duel, but it must not remove spacing discipline, make attacks connect automatically, or turn dodge, parry, and counter into target-truth shortcuts. The player should still need to read telegraphs, control spacing, and commit deliberately.

This system exists to make one duel easier to understand, not to create a broad targeting feature set. It should remain explicit, debug-visible, and conservative. If target focus becomes unclear, hidden, or overly helpful, it will undermine the emotional restraint and precision the prototype is trying to prove.

## 3. Player Experience Goals

For M0, target focus should support the following player-facing outcomes:

- The player can intentionally focus the one current duel enemy.
- The player can understand when target focus is active or inactive.
- The player can understand the general direction of the enemy when focus is active.
- Target focus makes orientation easier without making combat success automatic.
- Releasing target focus feels understandable rather than random.
- Losing target validity feels explainable through distance, state, defeat, or explicit release.

When the system is working, the player should feel more oriented, not more automated.

## 4. M0 Scope

Included in M0:

- one player
- one simple enemy
- one active target max
- simple target focus input intent
- simple target acquisition from the current duel enemy
- simple validation of the current duel target
- simple release when target becomes invalid or player requests release
- target direction/context exposed to locomotion, camera, combat, and debug
- debug-visible acquire, validate, and release reasons

## 5. Non-Goals

Out of scope for M0:

- multi-target cycling
- boss body-part targeting
- ranged targeting
- aim assist framework
- production lock-on HUD
- target priority scoring framework
- multiplayer targeting
- open-world target discovery
- off-screen target arbitration
- large encounter target management

## 6. Core Target Focus Loop

The recommended M0 loop is:

`request focus → acquire duel target → validate target → expose target context → release/reset if invalid or requested`

This loop should remain small and readable.

For M0:

- focus begins from explicit input intent or encounter-seeded startup context if used
- acquisition chooses the current duel enemy only
- validity is checked using simple duel assumptions
- current target context is exposed read-only to adjacent systems
- release occurs when requested or when the current target is no longer valid

## 7. Target Context State Model

Recommended M0 target states:

- `TargetFocusInactive`
- `TargetAcquireRequested`
- `TargetFocused`
- `TargetInvalid`
- `TargetReleaseRequested`
- `TargetReleased`

State intent:

- `TargetFocusInactive`: no active focus and no valid current target
- `TargetAcquireRequested`: input or encounter context requested focus
- `TargetFocused`: a valid current target is active
- `TargetInvalid`: the previous target no longer satisfies validity assumptions
- `TargetReleaseRequested`: player or runtime requested release
- `TargetReleased`: target context has been cleared and can return to inactive

M0 does not require a more abstract or generic targeting state machine than this.

## 8. Target Acquisition Rules

For M0, target acquisition should be conservative and explicit.

Recommended rules:

- acquisition may begin from raw lock-on or target-focus input intent
- acquisition may also begin from explicit encounter setup if that is approved for first-duel usability
- acquisition should consider the one current duel enemy only
- acquisition should succeed only when the candidate target is valid for the current duel
- acquisition should fail with a debug-visible reason when no valid target exists

Recommended acceptance conditions:

- player is in an active duel or equivalent valid encounter state
- a current duel enemy exists
- the candidate enemy is not defeated or otherwise invalid
- the candidate enemy is available to target in the current duel space

Recommended rejection conditions:

- no registered enemy
- encounter not ready or not active if gating is used
- candidate target already invalid
- target focus already active on the same valid target if re-requested

## 9. Target Validity Rules

For M0, target validity should stay simple and readable.

A target may remain valid when:

- the enemy exists in the encounter
- the enemy is not defeated or disabled beyond targetability
- the enemy remains the current duel opponent
- the enemy remains usable for orientation support in the duel space

A target may become invalid when:

- the enemy is defeated
- the enemy is removed from the encounter
- encounter state no longer supports active target focus
- the target is explicitly released

M0 does not require a broad priority or visibility scoring framework. Validity should be understandable from duel truth, not from hidden heuristics.

## 10. Target Release Rules

Release should be explicit and explainable.

Recommended M0 release sources:

- player requested release
- target became invalid
- encounter ended, failed, aborted, or reset
- current target was removed or defeated

Release should:

- clear active target truth
- clear or reset target direction context appropriately
- expose a release reason to debug
- return to an inactive or released state cleanly

Target release should not secretly change movement or combat outcomes by itself.

## 11. Target Direction / Context Rules

`Lock-On / Target Context` should expose enough read-only information for adjacent systems to orient around the duel without becoming a hidden authority.

Minimum M0 context may include:

- target focus active?
- current target
- target validity
- target direction relative to player if available
- target world position or equivalent directional basis if needed later
- last acquire reason
- last release reason
- last invalidation reason

This context supports:

- `Player Locomotion` facing and orientation support
- `Lock-On & Combat Camera` framing and readability
- `Combat Core` read-only contextual checks if needed
- `Debug Overlay` readability

It must not decide whether attacks, dodge, parry, or counter are valid.

## 12. Lock-On Input Intent Rules

`Lock-On / Target Context` does not own raw input mapping.

For M0:

- raw lock-on or target-focus intent comes from `Input Mapping`
- this system interprets that intent only in the narrow sense of focus acquire/release requests
- M0 uses toggle acquire/release behavior for second-press policy
- first press requests focus acquisition when no valid target is focused
- second press requests explicit release when the same valid target is focused
- third press may reacquire the valid duel target

Rejected input requests should be debug-visible when useful.

### M0 Second-Press Policy Decision

Decision date: 2026-06-12

M0 chooses **toggle acquire/release** for LockOn second-press behavior.

Policy:

- Pressing LockOn with no focused valid target requests acquisition of the current duel target.
- Pressing LockOn while a valid target is focused requests explicit release.
- Pressing LockOn again after release may reacquire the same valid duel target.

Rationale:

- Toggle release keeps target focus intentional instead of sticky.
- Explicit release is easier to explain in debug because the player-requested release has a clear reason.
- The policy supports one readable duel by giving the player a simple way to opt out of focus without adding hold timing, multi-target cycling, or camera-owned target truth.
- It matches the latest LockOn evidence from `production/qa/evidence/lockon-toggle-release-2026-05-24.md`, where the observed transition was `None -> Enemy -> None -> Enemy`.
- Earlier acquire/focus evidence in `production/qa/evidence/complete-m0-playable-combat-prototype-verification-evidence.md` remains valid for first-press acquisition; the later toggle-release evidence resolves the second-press ambiguity.

Implementation note:

- This decision documents current M0 policy only.
- No runtime behavior change is required as long as the active runtime continues to match the `None -> Enemy -> None -> Enemy` transition.
- Any future divergence between runtime and this policy should be handled by a separate implementation story.

## 13. Relationship To Input Mapping

`Input Mapping` owns:

- Unity New Input System action maps
- raw lock-on or target-focus input intent
- raw movement and action input intent

`Lock-On / Target Context` owns:

- interpreting lock-on intent into target acquire or release requests
- target-truth state after that request is evaluated

This keeps raw input ownership separate from target-truth ownership.

## 14. Relationship To Player Locomotion

`Player Locomotion` may read target context for:

- facing support
- target-relative orientation assumptions if used
- dodge-direction interpretation support if chosen by locomotion design

`Player Locomotion` still owns:

- movement interpretation
- movement truth
- dodge movement expression
- movement restrictions
- recovery movement

Target focus must not auto-solve spacing or force locomotion outcomes.

## 15. Relationship To Lock-On & Combat Camera

`Lock-On & Combat Camera` reads this system for:

- framing
- readability
- target-focus visual support
- camera feedback after confirmed context

`Lock-On / Target Context` owns target truth.
`Lock-On & Combat Camera` owns how framing responds to that truth.

Camera may expose read-only framing or camera-relative basis context elsewhere, but it must not own or override target truth here.

## 16. Relationship To Combat Core

`Combat Core` may read target context if needed for:

- contextual duel checks
- reveal request context enrichment
- combat debug visibility

However:

- target focus does not decide hit validity
- target focus does not decide dodge validity
- target focus does not decide parry validity
- target focus does not decide counter validity
- target focus does not open `CounterWindow`

`Combat Core` remains the authority for combat validity and results.

## 17. Relationship To Enemy Intent & Telegraph

`Enemy Intent & Telegraph` owns:

- enemy telegraph
- commitment
- active/recovery timing
- attack tags
- `EnemyPunishWindow`

`Lock-On / Target Context` does not own enemy behavior or punish state.

It may only observe whether a current duel enemy exists and is target-valid for M0 purposes.

## 18. Relationship To Encounter Framework

`Encounter Framework` may:

- register the current player and duel enemy
- seed the initial duel enemy as the first focus candidate if approved
- clear or reset encounter context at encounter end/reset

`Lock-On / Target Context` owns runtime target truth after encounter setup completes.

This prevents encounter lifecycle from becoming the hidden owner of targeting behavior.

## 19. Debug / Readability Requirements

Debug must explain:

- current target-focus state
- previous target-focus state if tracked
- target focus active?
- current target
- target validity
- target direction if available
- acquire requested?
- acquire accepted/rejected?
- acquire reason
- acquire rejection reason
- release requested?
- release reason
- invalidation reason
- encounter-seeded target context if used
- last raw lock-on intent if useful

Debug should remain read-only and high-signal.

## 20. Data Authoring Needs

M0 data needs should stay minimal.

Possible tunables:

- focus input behavior: toggle or hold
- simple acquisition allowance rules
- simple release assumptions
- debug labels matching GDD state names

M0 does not need:

- a large target scoring matrix
- many target filters
- broad per-enemy targeting profiles

## 21. Presentation Boundaries

Presentation systems may communicate target focus through:

- camera framing
- optional visual focus support
- debug labels

Presentation must not own:

- target truth
- target validity
- acquire/release rules
- combat outcome

`Animator`, `VFX`, `Audio`, and `UI` remain downstream and non-authoritative unless reacting to confirmed gameplay context.

## 22. Technical Boundaries

Technically, this system should remain a small, inspectable target-truth model.

Recommended technical rules:

- target truth should remain explicit and debug-visible
- mutable target ownership should not be spread across camera, locomotion, and encounter logic
- camera and locomotion should read target context through clear contracts
- avoid hidden service-locator ownership of current target truth
- M0 does not require a full generic targeting framework

This system should stay small enough to reason about during first-duel tuning.

## 23. Dependencies

Upstream dependencies:

- `Input Mapping`
- `Encounter Framework`
- simple duel target existence

Downstream consumers:

- `Player Locomotion`
- `Lock-On & Combat Camera`
- `Combat Core` if needed
- `Debug Overlay`

Read-only coordination only:

- `Enemy Intent & Telegraph`
- `Health / Damage / Hit Reaction`

## 24. Risks

Main M0 risks:

- target focus becomes hidden camera ownership
- target focus becomes hidden locomotion ownership
- target focus auto-solves spacing
- invalidation feels random
- acquire/release rules are unclear in debug
- encounter seeding becomes long-term target ownership by mistake
- target focus starts deciding combat validity

Mitigation direction:

- keep one authoritative owner
- keep rules simple
- keep acquire/release reasons debug-visible
- do not let target focus decide combat results

## 25. Open Questions

- should M0 use toggle or hold focus behavior?
- should encounter startup seed focus automatically or only provide a candidate target?
- does target validity need simple range assumptions for first-duel comfort, or only encounter/existence truth?
- should target direction be exposed only as a direction vector, or also as a richer contextual snapshot?
- should target context remain active through brief enemy disabled states, or always release on invalidation?

## 26. Acceptance Criteria For M0

`Lock-On / Target Context` passes M0 if:

- the player can focus the one current duel enemy intentionally
- focus active/inactive state is understandable
- current target truth is stable and debug-visible
- target validity and release reasons are explainable
- `Player Locomotion` can use target context for orientation support without taking ownership
- `Lock-On & Combat Camera` can frame the duel without taking ownership
- `Combat Core` remains authoritative for combat validity/results
- target focus does not auto-solve spacing
- target focus does not force attacks to hit
- target focus does not make dodge, parry, or counter automatically valid

`Lock-On / Target Context` fails M0 if:

- no clear owner of current target truth exists
- camera behaves like the owner of target focus
- locomotion behaves like the owner of target focus
- acquire/release state cannot be explained in debug
- target focus changes combat outcomes invisibly
- target focus makes the duel easier by removing positioning responsibility instead of improving readability
