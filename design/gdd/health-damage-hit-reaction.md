# Health / Damage / Hit Reaction

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Combat As Interpretation, Melancholic Elegance, Personal Restoration Over Power Fantasy

## 1. System Summary

`Health / Damage / Hit Reaction` defines the provisional M0 rules for what happens after `Combat Core` confirms a valid combat result. Its purpose is to make successful hits, failures, stagger moments, and temporary defeat states readable, fair, and easy to tune during the first `Glass Refrain` duel prototype.

For M0, this system supports one player, one simple enemy, and one Tokyo Street duel space. It owns simple player and enemy health values, damage application after confirmed hit results, basic hit reaction classification, control-suppression context, simple enemy stagger context, defeat or disabled requests, and health-facing debug truth. Its purpose is not to build a full RPG stats framework, a deep poise or armor model, or a production-ready damage architecture. Its purpose is to prove that consequences of combat are understandable and that the duel loop remains emotionally restrained and mechanically trustworthy.

This system does not own combat validity, timing windows, dodge success, parry success, counter validity, `CounterWindow`, or reveal request context. Those remain owned by `Combat Core`. `Player Locomotion` owns the movement expression of hit reaction, movement restriction, and recovery flow. `Enemy Intent & Telegraph` owns telegraph, commitment, attack tags, enemy-side recovery, and `EnemyPunishWindow`. `Memory State` owns whether reveal context is accepted and what memory-side response occurs afterward. Presentation systems may communicate health, damage, and reaction state, but they remain presentation-only unless responding to confirmed gameplay context.

In short, `Health / Damage / Hit Reaction` is the consequence layer for the first duel. It translates confirmed combat outcomes into health change, readable reaction context, defeat state requests, and debug-visible consequence data without stealing ownership from combat, locomotion, enemy behavior, or memory systems.

## 2. Design Intent

The design intent of `Health / Damage / Hit Reaction` is to make combat consequences legible without making them heavy, noisy, or systemically overbuilt. In `Glass Refrain`, a hit should matter, but it should matter in a restrained and readable way. The player should understand when contact was real, why a reaction happened, and when control is returning.

For M0, the system must support the duel rhythm `read → evade/parry → counter → reveal` rather than distract from it. Health values only need to be deep enough to make repeated exchanges possible. Damage only needs to be trustworthy enough that a successful hit or a failed defense changes the situation in an understandable way. Hit reaction only needs to be strong enough to communicate consequence and preserve commitment.

The emotional shape should remain calm, tense, and elegant. Getting hit should feel like a meaningful failure in reading or spacing, not like arbitrary punishment or a long stun-lock. Hitting the enemy should feel like an earned interruption or stagger when appropriate, not just a floating number. Defeat should exist as a provisional disabled state for M0, but it does not need to become a full fail-state loop yet.

This system should also protect adjacent boundaries. It should not become a second combat authority. It should not decide `CounterWindow`. It should not decide reveal validity. It should not let animation clips secretly own reaction truth. It should not ask `Player Locomotion` to infer hit reaction from visuals alone. It should provide explicit, inspectable consequence context that other systems can trust.

## 3. Player Experience Goals

The player experience goals for M0 health, damage, and hit reaction are about trust, clarity, and consequence.

### Readable Consequence

The player should understand when a hit truly connected. If the player is hit, they should feel that the enemy successfully threatened them. If the enemy is hit, they should feel that their answer had weight.

### Fair Failure

When the player takes damage, the failure should feel explainable through timing, spacing, or a wrong answer. The player should not feel that damage happened through hidden rules or unclear overlap.

### Short, Clear Interruption

Player hit reaction should briefly interrupt or restrict control so failure has meaning, but it should not trap the player in a long or chaotic stun-lock during M0.

### Earned Enemy Vulnerability

Enemy hit reaction or stagger should help the player understand when they meaningfully interrupted the enemy. It should support counter and reveal readability where appropriate without becoming an automatic win state.

### Trustworthy Health Change

The player should trust that health changes happen only after confirmed combat outcomes. Damage should not feel visually implied and then mechanically contradicted.

### Understandable Recovery

The player should be able to tell when a hit reaction ends and when readable control is returning. Recovery should feel like consequence resolution, not random input loss.

### Debuggable Consequence

Designers and testers should be able to inspect health, damage source, hit reaction state, defeat requests, and control-suppression context so feel tuning does not rely on guesswork.

## 4. M0 Scope

This section defines exactly what `Health / Damage / Hit Reaction` includes for `M0 — Katana Combat Feel Prototype`.

### Included In M0

#### Simple Player Health

M0 includes one simple player health value. It only needs to support repeated duel exchanges and readable failure.

#### Simple Enemy Health

M0 includes one simple enemy health value. It only needs to support readable enemy damage, basic defeat, and repeated counter or punish testing.

#### Confirmed Damage Application

M0 includes damage application only after `Combat Core` confirms a valid hit result. No speculative or presentation-only damage is allowed.

#### One Basic Player Hit Reaction

M0 includes one basic player hit reaction category that is sufficient to communicate failure and brief control suppression.

#### One Basic Enemy Hit Reaction / Stagger

M0 includes one basic enemy hit reaction or stagger category that is sufficient to communicate meaningful contact and support punish/counter readability.

#### Simple Defeat / Disabled Request

M0 includes a provisional defeated or disabled state request for player and enemy where needed, but not a full respawn, checkpoint, or progression loop.

#### Recovery / Control Suppression Context

M0 includes explicit control-suppression and recovery context that can be consumed by `Player Locomotion` and other downstream readers.

#### Debug Visibility

M0 includes debug-facing visibility for health value, damage events, reaction source, control suppression, and defeat state.

### Explicitly Out Of Scope For M0

- full RPG stat framework
- armor, resistance, elemental types, or mitigation stacks
- poise or balance system
- combo hit-stun system
- complex knockback system unless needed for readability
- ragdoll
- launch or airborne reactions
- full death/respawn loop
- loot or stat scaling
- damage number UI
- final HUD

## 5. Non-Goals

`Health / Damage / Hit Reaction` must stay tightly scoped for M0. It exists to make combat consequence readable, not to solve all future combat math and reaction needs.

### Not A Full Stats Framework

M0 does not require strength, defense, scaling formulas, equipment stats, elemental layers, or progression-driven combat math.

### Not An Armor / Resistance System

This document does not define mitigation categories, armor states, resist tables, or partial damage models.

### Not A Poise / Balance System

M0 does not need poise, posture, balance break, stagger resistance, or layered interrupt thresholds.

### Not A Complex Knockback Framework

M0 should avoid building a large displacement model before the first duel proves grounded readability.

### Not A Ragdoll Or Physics Reaction System

This system should not rely on ragdoll or uncontrolled physics to communicate hits in M0.

### Not A Full Death / Respawn Pipeline

Defeat exists only as a provisional disabled outcome for M0. Checkpoints, restart flow, and fail-state UX are deferred.

### Not Reveal Authority

This system must not decide reveal validity, narrative consequence, or memory acceptance. It may expose consequence context, but `Memory State` owns memory-side response.

### Not Movement Truth

This system provides reaction and suppression context, but it does not own locomotion state or movement expression.

### Not Animation Authority

This system must not let animation clip length or events secretly define reaction or recovery truth.

## 6. Core Health / Damage Loop

The M0 consequence loop should support:

`confirmed combat result → damage application → reaction classification → control suppression / stagger context → recovery handoff → reset or defeat`

This maps onto the core duel rhythm:

- `confirmed combat result` preserves `Combat Core` authority
- `damage application` makes the exchange matter
- `reaction classification` communicates success or failure
- `control suppression / stagger context` preserves consequence and readability
- `recovery handoff` returns control cleanly
- `reset or defeat` closes the exchange without overbuilding scope

The system should never invent its own hit truth. It reacts to confirmed combat outcomes and makes those outcomes understandable.

## 7. Health State Model

For M0, a small explicit health state model is enough.

### Living

The actor is active, damageable, and able to receive confirmed damage and reaction context.

### Damaged

The actor has recently received confirmed damage and is currently in or just entering a basic reaction path. This is not a separate combat authority state. It is a consequence-facing state that helps downstream systems understand that the hit just occurred.

### Recovering

The actor has resolved the immediate impact but is still under temporary control suppression, locomotion recovery, or stagger cleanup. `Player Locomotion` owns movement-side recovery truth for the player, but this system may expose the source and provisional recovery context.

### Disabled / Defeated

The actor has reached the provisional M0 defeat condition or otherwise entered a disabled state. For the player, this may represent temporary defeat/failure. For the enemy, this may represent duel resolution or collapse into a reveal-supportive end state. Exact higher-level aftermath remains outside this system.

### State Notes

- `Combat Core` still owns combat result truth.
- `Health / Damage / Hit Reaction` owns health state truth.
- `Player Locomotion` owns locomotion state truth during the player-facing movement consequences.
- `Animator` may present all of these states visually, but presentation does not become authority.

## 8. Damage Application Rules

Damage application rules for M0 should remain simple and explicit.

### Confirmed Result Requirement

Damage only applies after `Combat Core` confirms a valid hit result. Raw input, animation contact, VFX, or camera feedback must never apply damage by themselves.

### Targeted Health Change

Each valid hit result should identify the damaged side and the consequence type clearly enough that this system can:

- reduce player health
- reduce enemy health
- classify basic reaction context
- evaluate defeat / disabled threshold

### Simple Numeric Model

M0 can use a simple numeric health model for both player and enemy. Exact values are tuning data, not fixed design commitments at this stage.

### No Hidden Mitigation

Damage should not be modified by armor, resistance, or hidden mitigation systems in M0 unless explicitly added later through another design pass.

### Counter And Heavy Consequence Readability

Counter or other stronger results may apply larger damage or stronger reaction context than light hits, but they must still come from confirmed `Combat Core` result categories rather than from presentation emphasis alone.

### Damage Must Not Open `CounterWindow`

Damage application itself must not secretly open `CounterWindow`. That remains a `Combat Core` decision based on combat result context.

## 9. Hit Reaction Rules

Hit reaction in M0 exists to make consequence readable, not to create a large reaction taxonomy.

### Reaction Follows Confirmed Damage

Reaction classification only occurs after confirmed damage or confirmed consequence context from `Combat Core`.

### One Basic Player Reaction Is Enough

M0 only needs one basic player hit reaction that briefly suppresses or reduces control and cleanly hands off to locomotion-side recovery.

### One Basic Enemy Reaction / Stagger Is Enough

M0 only needs one basic enemy hit reaction or stagger that communicates interruption, hit confirmation, or counter payoff.

### Reaction Must Be Short And Explainable

Reaction should remain short enough that the duel loop stays testable and readable. Long stun-lock behavior is out of scope.

### Reaction Must Not Own Combat Outcome

Hit reaction communicates the consequence of a result. It must not decide whether the result happened.

### Reaction Must Not Own Reveal

A strong reaction may support reveal readability, but reaction itself must not decide whether reveal is valid.

## 10. Player Hit Reaction Contract

The purpose of player hit reaction in M0 is to make failure readable and briefly consequential.

### Contract

When `Combat Core` confirms that the player was successfully hit:

- `Health / Damage / Hit Reaction` applies player damage
- evaluates whether the player remains `Living` or becomes `Disabled / Defeated`
- emits player hit reaction context
- emits temporary control-suppression or movement-restriction context as needed
- emits recovery source context for downstream locomotion handoff

### Player Reaction Expectations

- one basic player hit reaction is enough
- control may be briefly suppressed or reduced
- player should not instantly cancel into every action by default
- hit reaction should be short enough for M0 feel testing
- failure should feel like the result of timing or spacing, not random lockout

### What This System Does Not Own

- movement expression during the reaction
- precise locomotion restriction behavior
- camera feedback truth
- animation timing truth

Those belong downstream to `Player Locomotion` and presentation systems.

## 11. Enemy Hit Reaction / Stagger Contract

The purpose of enemy hit reaction in M0 is to make player success readable and to support counter, punish, and reveal readability where appropriate.

### Contract

When `Combat Core` confirms that the enemy was successfully hit:

- `Health / Damage / Hit Reaction` applies enemy damage
- evaluates whether the enemy remains `Living` or becomes `Disabled / Defeated`
- emits simple enemy hit reaction or stagger context
- may expose a stronger reaction category for counter or heavier success if needed later

### Enemy Reaction Expectations

- one basic enemy reaction or stagger is enough
- enemy reaction should communicate interruption or meaningful contact
- enemy reaction should help the player understand that a punish or counter landed
- enemy reaction must not directly open `CounterWindow`
- enemy reaction may support reveal readability where valid reveal context already exists

### Relationship To `EnemyPunishWindow`

Enemy reaction may visually overlap with punishability, but `Enemy Intent & Telegraph` still owns `EnemyPunishWindow`, and `Combat Core` still owns whether the player actually has `CounterWindow`.

## 12. Defeat / Disabled Contract

Defeat or disabled state in M0 is provisional and intentionally small.

### Player Disabled / Defeated

If player health reaches the provisional defeat threshold:

- this system marks the player as `Disabled / Defeated`
- emits disabled context for downstream locomotion, encounter, and presentation readers
- does not define the full fail-state loop, restart flow, or checkpoint behavior

### Enemy Disabled / Defeated

If enemy health reaches the provisional defeat threshold:

- this system marks the enemy as `Disabled / Defeated`
- emits enemy-disabled context for downstream encounter, presentation, and reveal-support readers
- does not by itself decide whether reveal happens

### Reveal Boundary

Enemy defeat may contribute to reveal-supportive context, but `Memory State` still owns reveal acceptance and memory consequence.

## 13. Recovery / Control Suppression Contract

The purpose of this contract is to make consequence handoff explicit.

### Control Suppression

This system may expose:

- control suppressed?
- movement reduced or locked?
- suppression source
- suppression duration if tracked

For M0, this can remain simple and generic.

### Recovery Handoff

After the immediate reaction, this system should expose:

- recovery active?
- recovery source
- whether the actor is returning from hit reaction or stagger

`Player Locomotion` then owns the movement-side recovery expression for the player. Enemy-side recovery rhythm remains primarily owned by `Enemy Intent & Telegraph`.

### No Animation-Owned Recovery

Recovery must not be owned only by animation clip length or events. Presentation may align to the gameplay consequence, but must not become its source of truth.

## 14. Relationship To Combat Core

`Combat Core` is upstream gameplay authority. This system is downstream consequence authority.

### `Combat Core` Owns

- combat action validity
- hit, parry, dodge, and counter result validation
- timing and result resolution
- `CounterWindow`
- reveal request context

### `Health / Damage / Hit Reaction` Owns

- health value changes
- damage application after confirmed hit
- provisional reaction classification
- defeat / disabled state request
- consequence-facing debug truth

### Contract Rule

`Health / Damage / Hit Reaction` must never infer a hit from animation, camera, or VFX alone. It acts only on confirmed `Combat Core` results.

## 15. Relationship To Player Locomotion

`Player Locomotion` owns movement truth. This system owns consequence context.

### This System Provides

- player hit reaction source
- control suppression context
- movement restriction intent if needed
- recovery source
- disabled context

### `Player Locomotion` Owns

- movement response to hit reaction
- movement restriction expression
- recovery movement
- locomotion state truth

### Boundary Rule

This system must not secretly move the player, define locomotion states, or own recovery movement timing through animation-only logic.

## 16. Relationship To Enemy Intent & Telegraph

`Enemy Intent & Telegraph` owns enemy-side attack readability and punish rhythm. This system owns enemy consequence after confirmed result.

### `Enemy Intent & Telegraph` Owns

- enemy telegraph
- commitment
- active / recovery timing
- attack tags
- `EnemyPunishWindow`

### This System Owns

- enemy health changes
- enemy hit reaction / stagger context
- enemy disabled / defeated context

### Boundary Rule

Enemy reaction may support punish readability, but it must not replace enemy-owned telegraph, commitment, recovery, or punish authority.

## 17. Relationship To Memory State

`Memory State` owns whether reveal context is accepted and what memory-side response occurs.

### This System May Provide

- enemy defeat context
- stronger-success or counter-impact consequence context
- debug-visible aftermath context

### This System Must Not Own

- reveal validity
- memory progression
- memory acceptance or rejection
- narrative consequence

### Boundary Rule

Damage, defeat, or stagger may contribute to the meaning of an exchange, but `Memory State` remains the owner of memory consequence.

## 18. Debug / Readability Requirements

Debug exists to explain health, damage, reaction, and consequence behavior, not to become final gameplay UI.

### Required Debug Data

- current player health
- current enemy health
- last confirmed damage event
- damage target
- damage source
- damage amount
- hit reaction active?
- reaction source
- reaction category
- control suppressed?
- suppression source
- recovery active?
- recovery source
- player disabled / defeated?
- enemy disabled / defeated?
- last `Combat Core` result affecting damage
- last reveal-related consequence context if useful
- last Animator visual state if useful for comparison only

### Debug Goals

Designers should be able to answer:

- did damage only happen after confirmed result?
- why did a reaction occur?
- why is control currently suppressed?
- did defeat happen because of actual health loss?
- did enemy reaction support readability without opening windows automatically?

## 19. Data Authoring Needs

This section defines the minimum tunable data needed for M0.

### Minimum Tunable Data

- player max health
- enemy max health
- light-hit damage
- heavy-hit damage
- counter-hit damage if distinct
- player hit reaction duration
- enemy hit reaction / stagger duration
- control suppression duration
- recovery source labels
- disabled / defeat threshold assumptions
- optional small knockback amount if needed later
- debug labels and verbosity flags

### Guidance

- exact values are deferred to tuning
- M0 can start with simple constants
- values likely to change during feel testing should remain easy to tune
- clip length must not secretly become the source of truth for reaction or recovery

## 20. Presentation Boundaries

Presentation systems may communicate confirmed consequence, but they must not own it.

### Animator

May present:

- player hit reaction
- enemy stagger
- disabled poses
- recovery visuals

Must not own:

- damage truth
- reaction truth
- defeat truth
- recovery truth

### VFX / Audio

May present:

- impact cues
- counter impact emphasis
- defeat feedback
- restrained reveal-support cues after valid context

Must not:

- apply damage
- imply success before confirmation
- open `CounterWindow`
- imply reveal validity before acceptance

### Camera / UI

May present:

- readable impact framing
- target focus support
- optional development-facing health/debug cues

Must not:

- decide damage
- decide hit reaction
- become required to understand basic consequence truth

## 21. Technical Boundaries

This system should remain small, explicit, and testable.

### Technically Owns

- health values
- confirmed damage application
- reaction classification context
- defeat / disabled requests
- damage-facing debug snapshot

### May Consume

- confirmed combat result context from `Combat Core`
- enemy-side or player-side identity/context needed to apply damage
- locomotion-facing downstream consumers
- memory-facing downstream consumers

### Must Not Depend On As Authority

- `Animator State Machine`
- VFX / Audio timing
- camera state
- UI state
- hidden global state

### FSM / Authority Direction

Gameplay truth should stay in explicit gameplay-side models. This system may use a simple explicit state model, but it does not need an overbuilt framework for M0.

## 22. Dependencies

### Upstream Dependencies

- `Combat Core`
- `Player Locomotion` contract consumers downstream for player-side movement response
- `Enemy Intent & Telegraph` for enemy-side downstream rhythm understanding
- `Memory State` as downstream reveal acceptance owner
- `Debug Overlay`
- data authoring / tuning constants

### Downstream Consumers

- `Player Locomotion`
- `Enemy Intent & Telegraph`
- `Lock-On & Combat Camera`
- `Memory State`
- `Animator`
- `VFX`
- `Audio`
- `UI / Debug`

### Dependency Direction Rules

- consume confirmed combat outcomes, not speculative presentation
- expose read-only consequence snapshots or explicit context
- avoid circular ownership with locomotion and enemy state
- keep reveal ownership separate

## 23. Risks

### Major M0 Risks

#### Damage Applies Without Confirmed Result

- Why it matters: destroys trust in the combat loop
- Early warning signs: visual contact changes health even when combat result says otherwise
- Mitigation: require explicit confirmed result before application
- Priority: High

#### Hit Reaction Feels Random

- Why it matters: failure stops teaching timing and spacing
- Early warning signs: player cannot tell why control was lost
- Mitigation: keep one simple reaction, expose source in debug
- Priority: High

#### Long Stun-Lock Emerges

- Why it matters: breaks M0 feel and makes failure oppressive
- Early warning signs: player cannot recover cleanly after one mistake
- Mitigation: keep suppression short and readable
- Priority: High

#### Enemy Stagger Auto-Solves Counter

- Why it matters: removes earned counter rhythm
- Early warning signs: every enemy reaction effectively grants free counter
- Mitigation: keep `CounterWindow` in `Combat Core`
- Priority: High

#### Defeat / Reveal Ownership Blurs

- Why it matters: memory consequence and combat consequence become confused
- Early warning signs: enemy death directly triggers reveal with no memory acceptance seam
- Mitigation: keep reveal acceptance in `Memory State`
- Priority: Medium

#### Animation Becomes Reaction Truth

- Why it matters: clip edits silently change gameplay consequence
- Early warning signs: reaction duration changes when clip length changes
- Mitigation: explicit gameplay-side timing and debug comparison
- Priority: High

#### Overbuilding Damage Framework

- Why it matters: scope drifts into RPG math before duel feel is proven
- Early warning signs: armor, resist, poise, and scaling discussions block prototype progress
- Mitigation: hold to simple health and damage only
- Priority: High

## 24. Open Questions

### Must Answer Before M0 Implementation

- Does M0 use numeric HP or a simpler hit-count model?
- Is enemy defeat part of first playable M0 or only prolonged stagger?
- Who emits the final hit reaction context: `Combat Core`, this system, or a small shared contract?
- Is debug overlay required before meaningful damage/reaction tuning starts?
- Does `Memory State` need explicit defeat-related context in the first prototype?

### Can Answer During M0 Tuning

- exact player and enemy health values
- exact light/heavy/counter damage values
- exact reaction and suppression durations
- whether small knockback is needed for readability
- whether counter applies a stronger reaction than heavy hit
- whether defeat should immediately stop all control or allow a short settle state

### Defer After M0

- armor and resistance systems
- poise / balance
- damage scaling and progression
- elemental layers
- full defeat / respawn loop
- complex hit reaction categories
- production HUD damage presentation
- floating damage numbers

## 25. Acceptance Criteria For M0

### Acceptance Purpose

`Health / Damage / Hit Reaction` passes M0 if it proves that combat consequence is readable, fair, and cleanly separated from combat validity, movement truth, enemy telegraph truth, and memory consequence truth.

### Required M0 Scenario

In one duel arena, the player should be able to:

- hit the enemy and see enemy health change only after confirmed result
- be hit by the enemy and see player health change only after confirmed result
- experience simple player hit reaction with brief control consequence
- experience simple enemy hit reaction or stagger with readable consequence
- reach provisional enemy defeat if enough confirmed hits land
- return to readable control after player hit reaction

### Pass If

- damage only applies after confirmed `Combat Core` result
- player health and enemy health are readable in debug
- player hit reaction is short, understandable, and non-random
- enemy reaction clearly communicates success
- enemy reaction does not secretly open `CounterWindow`
- defeat / disabled context is explicit and debug-visible
- recovery handoff to `Player Locomotion` is understandable
- reveal acceptance remains outside this system
- placeholder animation is enough to validate consequence truth

### Fail If

- damage happens from animation, VFX, or camera alone
- reaction source cannot be explained
- player is stun-locked in M0
- enemy stagger automatically guarantees counter
- defeat directly triggers reveal with no `Memory State` seam
- clip length secretly defines reaction or recovery truth
- debug cannot explain health, damage, reaction, or suppression state
- the system expands into full RPG combat math before M0 duel feel is proven

### M0 Pass Statement

`Health / Damage / Hit Reaction` M0 passes when one player and one simple enemy can exchange confirmed hits in a small duel space and the system consistently makes health loss, reaction, suppression, stagger, recovery handoff, and provisional defeat readable without stealing combat, locomotion, enemy, or memory ownership.

### M0 Out Of Scope

The following are not required to pass this system for M0:

- full RPG stats
- armor / resistance
- poise / balance
- complex knockback
- ragdoll
- full death / respawn flow
- loot or scaling
- damage number UI
- final HUD
