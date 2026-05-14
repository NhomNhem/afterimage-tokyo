# Encounter Framework

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Combat As Interpretation, Melancholic Elegance

## 1. System Summary

`Encounter Framework` defines the provisional M0 structure for starting, running, observing, resetting, and ending the first simple combat encounter in `Glass Refrain`. For the first katana duel prototype, it does not build a full mission system, wave system, boss framework, narrative encounter graph, or RPG progression layer. It only owns the encounter lifecycle, participant registration, simple readiness checks, minimal win/fail/reset conditions, and encounter-facing debug truth.

For M0, this system exists to make one duel arena behave like a coherent playable encounter rather than a loose collection of combat systems. It provides a small lifecycle around the core loop `read → evade/parry → counter → reveal` so the player, enemy, target context, memory response, and reset behavior all have a clear beginning, active state, and end.

`Encounter Framework` does not own combat result validation, enemy behavior truth, health logic, memory reveal acceptance, player movement, target truth, or camera state. Those remain owned by their respective systems. `Encounter Framework` may observe them to determine whether the duel has started, completed, failed, aborted, or needs reset.

In short, `Encounter Framework` is the smallest possible M0 encounter shell. It exists to prove that the first duel can be prepared, started, observed, completed, failed, and reset in a clean and debuggable way without becoming a god system.

## 2. Design Intent

The design intent of `Encounter Framework` is to provide just enough structure that the first duel prototype can be run repeatedly and observed clearly. The player should not feel like they are entering a full mission pipeline or a heavily scripted sequence. They should feel that the duel begins cleanly, runs in a readable state, ends for understandable reasons, and can be returned to a ready state for another test.

For M0, the system should stay deliberately narrow. It should not try to solve campaign progression, encounter authoring pipelines, spawn orchestration for many enemies, or narrative branching. It should only make one duel repeatable, stable, and easy to tune. This matters because many M0 validation questions are encounter-level questions:

- did the duel actually begin with all required systems ready?
- did it end because of enemy defeat, player defeat, or manual abort?
- did reveal happen during the encounter?
- can the duel be reset quickly for another tuning pass?

The tone should remain restrained and functional. Encounter state should support the emotional and mechanical rhythm of the duel without becoming a production-heavy wrapper around it. The framework should make repetition easy and readable, not theatrical.

## 3. Player Experience Goals

The player experience goals for M0 `Encounter Framework` are mostly about clarity and repeatability at the duel level.

### Clear Start

The duel should begin in an understandable way. The player should not feel dropped into an ambiguous half-active state.

### Stable Active State

Once the encounter is active, the duel should remain stable and readable rather than feeling like loosely connected systems fighting for control.

### Understandable End

The player and designer should be able to understand whether the encounter ended because the enemy was defeated, the player failed, or the encounter was manually aborted or reset.

### Fast Iteration

The encounter should reset cleanly enough that repeated M0 tuning passes are practical.

### Debuggable Lifecycle

Designers and testers should be able to inspect encounter state, readiness blockers, registered participants, end reasons, and reset reasons without guesswork.

## 4. M0 Scope

This section defines exactly what `Encounter Framework` includes for `M0 — Katana Combat Feel Prototype`.

### Included In M0

#### One Encounter Only

M0 includes one simple duel encounter only.

#### One Player, One Enemy, One Arena

M0 encounter scope is limited to one player, one simple enemy, and one Tokyo Street duel space.

#### Simple Start Condition

M0 includes one simple start condition that moves the encounter from ready to active once the required participants and minimal context are valid.

#### Simple Runtime Observation

M0 includes runtime observation of encounter-relevant state such as participant presence, defeat state, and reveal acceptance if surfaced.

#### Simple Complete / Fail / Abort / Reset Flow

M0 includes minimal end and reset logic sufficient to repeat the duel prototype safely.

#### Debug Visibility

M0 includes encounter-facing debug visibility for lifecycle state, readiness, participants, and end/reset reasons.

### Explicitly Out Of Scope For M0

- wave spawning
- boss phase framework
- multi-enemy roster
- quest system
- narrative branching
- save/persistence
- loot/reward system
- level streaming ownership
- production encounter editor

## 5. Non-Goals

`Encounter Framework` must stay tightly scoped for M0. It exists to structure one duel, not to own the whole game flow.

### Not A Mission System

M0 does not require mission objectives, branching goals, checkpoints, or long-form progression logic here.

### Not A Spawn Wave System

M0 does not need repeated spawning, enemy groups, reinforcements, or wave escalation.

### Not A Boss Framework

This system does not design boss phases, phase transitions, cinematic intros, or special confrontation structures.

### Not A Narrative Or Quest Graph

M0 does not require encounter-driven story branching, dialogue sequencing, or quest-state integration.

### Not Reward / Economy Ownership

This framework does not own loot, score, XP, progression rewards, or post-fight payout.

### Not Combat Authority

It must not decide hit/parry/dodge/counter results, `CounterWindow`, or reveal request validity.

### Not Target Truth

It may help seed initial target registration at encounter start, but `Lock-On / Target Context` owns runtime target truth.

### Not Camera Or Movement Authority

It must not control locomotion truth or camera framing truth.

### Not A God System

If a responsibility clearly belongs to combat, enemy behavior, health, memory, locomotion, targeting, or camera, it should remain there.

## 6. Core Encounter Loop

The recommended M0 encounter loop is:

`prepare → spawn/register participants → start duel → observe combat/memory/health state → complete/fail/reset → return to ready state`

This loop exists to make the first duel repeatable and inspectable.

### Prepare

The encounter validates that its minimal dependencies and participant references exist.

### Spawn / Register Participants

The encounter ensures the player and the one simple enemy are registered as duel participants for M0.

### Start Duel

The encounter transitions into active state once readiness is satisfied.

### Observe Runtime

While active, the framework observes relevant external state:

- participant validity
- player defeat
- enemy defeat
- reveal acceptance if exposed
- manual abort/reset requests

### Complete / Fail / Reset

The encounter ends for explicit reasons and transitions to completion, fail, abort, or reset states without inventing new gameplay truth.

### Return To Ready

After reset, the encounter returns to a state where the duel can be run again.

## 7. Encounter State Model

The following encounter states are enough for M0.

### EncounterUninitialized

The encounter has not yet prepared its participant/config references.

### EncounterPreparing

The encounter is validating its minimal setup and participant availability.

### EncounterReady

All required M0 encounter conditions are satisfied and the duel is ready to start.

### EncounterStarting

The encounter is transitioning from ready to active and may perform minimal registration handoff such as initial target seeding if needed.

### EncounterActive

The duel is live and the framework is observing external systems for end/fail/reveal-relevant encounter state.

### EncounterCompleting

The encounter is resolving a successful completion path, usually because the enemy has been defeated or the duel’s success condition has been met.

### EncounterCompleted

The encounter finished successfully and is awaiting reset or further prototype handling.

### EncounterFailed / EncounterAborted

The encounter ended unsuccessfully or was manually stopped. M0 may keep these close together if a simpler implementation is preferred, but the reason should remain debug-visible.

### EncounterResetting

The encounter is returning its local lifecycle to a reusable ready state.

## 8. Encounter Start Rules

M0 encounter start rules should remain simple and explicit.

### Start Preconditions

The encounter may enter `EncounterStarting` only if:

- the player is registered
- the enemy is registered
- required minimal config is present
- no blocking reset or abort state is active

### Start Reason

The encounter should expose why it started, for example:

- automatic prototype start
- manual debug start
- reset-to-ready restart

### No Combat Authority At Start

Encounter start does not decide combat results, enemy intent, or reveal validity. It only transitions lifecycle state and ensures the duel is ready to begin.

## 9. Participant / Target Registration Rules

For M0, participant registration should remain minimal.

### Participant Registration

The framework owns simple registration of:

- the current player participant
- the current enemy participant

### Target Context Seeding

The framework may provide enough initial encounter context to help seed the current enemy as the initial target for M0. After runtime begins, `Lock-On / Target Context` owns target truth.

### Registration Errors

Missing participant references, duplicate registration, or invalid configuration should be surfaced as readiness blockers in debug.

### No Runtime Target Ownership

Once the encounter is active, `Encounter Framework` must not own target switching, target validity truth, or ongoing target direction.

## 10. Encounter Runtime Rules

During `EncounterActive`, the framework should observe and coordinate at the encounter level without becoming gameplay authority.

### Observe External State

The framework may observe:

- player defeated?
- enemy defeated?
- reveal accepted during encounter?
- manual reset/abort requested?
- required participant still valid?

### Runtime Context

The framework may expose:

- current encounter state
- elapsed encounter time
- currently registered participants
- last major encounter-relevant observed event

### Runtime Non-Ownership

The framework does not own:

- combat result validation
- enemy behavior
- health changes
- player movement
- camera framing
- reveal acceptance

It only observes those systems for encounter lifecycle purposes.

## 11. Encounter End / Reset Rules

M0 end and reset rules should prioritize clarity and fast iteration.

### Complete

The encounter may transition toward completion when the enemy reaches a valid defeated/disabled state and the duel’s success path has been satisfied.

### Fail

The encounter may transition toward failed state when the player reaches a valid defeated/disabled state if M0 needs a fail path.

### Abort

The encounter may be manually aborted for debugging or prototype control.

### Reset

Reset should:

- clear encounter-local lifecycle state
- return the framework to a reusable ready/preparing path
- not silently overwrite combat, health, or memory truth ownership

### Reset Reason

Reset reason should be debug-visible, such as:

- manual reset
- retry after fail
- cleanup after completion
- invalid runtime state recovery

## 12. Win / Fail / Abort Conditions

For M0, these conditions should remain minimal and explicit.

### Win / Complete

Recommended M0 complete condition:

- enemy defeated/disabled in a valid encounter-active state

### Fail

Recommended M0 fail condition if used:

- player defeated/disabled in a valid encounter-active state

### Abort

Recommended M0 abort conditions:

- manual debug abort
- missing participant during runtime
- invalid encounter state that requires teardown

### Reveal Is Not Completion By Itself

Reveal acceptance alone should not automatically complete the encounter unless the approved M0 rule explicitly ties it to success.

## 13. Relationship To Combat Core

`Combat Core` owns the duel’s combat truth. `Encounter Framework` owns the duel’s lifecycle truth.

### `Combat Core` Owns

- combat action validity
- hit/parry/dodge/counter result validation
- `CounterWindow`
- reveal request context

### `Encounter Framework` Owns

- encounter lifecycle state
- encounter start/end/reset flow
- participant registration for M0
- readiness checks
- encounter debug state

### Boundary Rule

The encounter layer may observe major combat results if useful for debug, but it must never decide them.

## 14. Relationship To Enemy Intent & Telegraph

`Enemy Intent & Telegraph` owns enemy behavior and readability. `Encounter Framework` owns only whether the duel is in a lifecycle state where that behavior should be considered active.

### `Enemy Intent & Telegraph` Owns

- enemy behavior/readability loop
- telegraph
- commitment
- active/recovery timing
- attack tags
- `EnemyPunishWindow`

### Boundary Rule

The encounter may start or stop the duel context, but it does not own enemy-side combat rhythm.

## 15. Relationship To Health / Damage / Hit Reaction

`Health / Damage / Hit Reaction` owns physical consequence. `Encounter Framework` may observe consequence outcomes to decide encounter completion, failure, or reset.

### `Health / Damage / Hit Reaction` Owns

- health values
- damage application
- hit reaction classification
- defeated/disabled consequence

### `Encounter Framework` May Observe

- player defeated?
- enemy defeated?
- disabled state relevant to encounter end/fail

### Boundary Rule

Encounter state transitions should respond to valid consequence state, not redefine it.

## 16. Relationship To Memory State

`Memory State` owns reveal acceptance and memory response truth.

### `Memory State` Owns

- reveal request acceptance/rejection
- memory response state

### `Encounter Framework` May Observe

- reveal accepted during encounter?
- current memory response state if useful for encounter debug

### Boundary Rule

The encounter must not decide reveal validity. It may only observe whether reveal happened as part of the duel.

## 17. Relationship To Player Locomotion

`Player Locomotion` owns player movement truth at all times.

### `Player Locomotion` Owns

- movement state truth
- dodge movement
- recovery movement
- hit reaction movement expression

### Boundary Rule

The encounter may start or end the duel lifecycle, but it must not own or override locomotion truth.

## 18. Relationship To Lock-On / Target Context

`Lock-On / Target Context` owns runtime target truth.

### `Lock-On / Target Context` Owns

- target focus active
- current target
- target validity
- target direction

### `Encounter Framework` May Do

- help identify the intended first enemy participant for initial duel setup

### Boundary Rule

After runtime begins, `Encounter Framework` must not own active target truth.

## 19. Relationship To Lock-On & Combat Camera

`Lock-On & Combat Camera` owns framing and readability. `Encounter Framework` owns lifecycle state that camera may observe if needed.

### `Lock-On & Combat Camera` Owns

- framing/readability
- camera state and feedback after confirmed context

### `Encounter Framework` May Provide

- encounter active?
- encounter start/end/reset state
- current participant references for debug context

### Boundary Rule

The encounter must not decide camera framing, and camera must not decide encounter truth.

## 20. Debug / Readability Requirements

Debug exists to explain encounter lifecycle and readiness, not to become gameplay UI.

### Required Debug Data

- current encounter state
- previous encounter state
- time in encounter
- encounter elapsed time
- registered player
- registered enemy
- active target context if relevant
- encounter start reason
- encounter end reason
- reset reason
- player defeated?
- enemy defeated?
- reveal accepted during encounter?
- last major combat result if observed
- readiness blockers
- missing participant/config errors

### Debug Goals

Designers should be able to answer:

- did the encounter actually start cleanly?
- why is it not ready yet?
- why did it end?
- why did it reset?
- was the duel active when the observed event happened?

## 21. Data Authoring Needs

M0 data authoring should remain minimal.

### Minimum Tunable / Authored Data

- participant references
- simple encounter start mode
- simple reset mode
- optional fail enabled/disabled flag if needed
- debug labels for encounter reasons
- optional encounter identifier for debug

### Guidance

- simple constants or lightweight config are acceptable for M0
- avoid building a production encounter editor
- keep the encounter easy to reset and retest

## 22. Presentation Boundaries

Presentation systems may communicate encounter lifecycle, but they must not own it.

### Animator / VFX / Audio

May present:

- duel start emphasis
- completion/fail emphasis
- reset feedback

Must not:

- decide encounter start/end truth
- force encounter reset
- imply completion without valid observed state

### UI

May present:

- optional debug-only encounter state
- optional development-facing retry/start controls

Must not:

- become required to understand the base encounter lifecycle

### Camera

May react to valid encounter state, but must not become the owner of the duel lifecycle.

## 23. Technical Boundaries

This system should remain explicit, small, and testable.

### Technically Owns

- encounter lifecycle state
- participant registration references
- readiness and error state
- encounter-level debug snapshot

### May Consume

- player/enemy participant references
- health/defeat observation
- reveal-state observation
- manual debug start/reset/abort input

### Must Not Depend On As Authority

- `Animator State Machine`
- VFX / Audio timing
- camera state
- hidden global combat truth

### Simplicity Rule

M0 does not require a full encounter orchestration architecture. A small explicit state model is preferred.

## 24. Dependencies

### Upstream Dependencies

- `Combat Core`
- `Enemy Intent & Telegraph`
- `Health / Damage / Hit Reaction`
- `Memory State`
- `Player Locomotion`
- `Lock-On / Target Context`
- `Lock-On & Combat Camera`
- `Debug Overlay`

### Downstream Consumers

- debug overlay
- optional development UI
- presentation systems observing encounter state

### Dependency Direction Rules

- observe authoritative systems rather than replacing them
- expose encounter lifecycle context as read-only state
- avoid circular ownership with combat, target context, and camera

## 25. Risks

### Major M0 Risks

#### Encounter Becomes A God System

- Why it matters: ownership boundaries collapse and architecture churn increases
- Early warning signs: encounter starts deciding combat, reveal, targeting, or movement truth
- Mitigation: keep strict observation-only boundaries for non-encounter systems
- Priority: High

#### Start Conditions Are Ambiguous

- Why it matters: the duel begins in inconsistent states and tuning becomes unreliable
- Early warning signs: encounter sometimes starts before participants/target context are ready
- Mitigation: explicit readiness checks and debug blockers
- Priority: High

#### Reset Is Slow Or Unclear

- Why it matters: repeated M0 iteration becomes painful
- Early warning signs: designers cannot quickly retry after fail/completion
- Mitigation: keep reset simple and expose reason/state clearly
- Priority: High

#### Encounter End Reason Is Opaque

- Why it matters: testers cannot tell whether combat, health, or memory ended the duel
- Early warning signs: completed/failed states appear without clear cause
- Mitigation: explicit end reason debug data
- Priority: High

#### Runtime Target Ownership Blurs

- Why it matters: encounter, target context, and camera start conflicting
- Early warning signs: encounter tries to keep owning target truth after start
- Mitigation: only allow initial seeding, then hand runtime truth to `Lock-On / Target Context`
- Priority: High

## 26. Open Questions

### Must Answer Before M0 Implementation

- Is encounter start automatic on prototype load, proximity-based, or manual debug start?
- Is player fail state required for first playable M0 or only enemy completion/reset?
- Should enemy defeat alone complete the encounter, or does reveal acceptance also need to be observed?
- Does the encounter need explicit abort state separate from fail state in first prototype?
- Is initial target seeding required from the encounter layer, or can target context handle it independently?

### Can Answer During M0 Tuning

- exact reset flow timing
- whether completed encounters briefly linger before reset
- whether fail and abort should remain separate states or merge for M0
- how much runtime encounter debug is visible by default

### Defer After M0

- waves
- boss encounters
- multi-enemy registration
- encounter editor tooling
- quest and narrative branching
- persistence and rewards
- streaming or level-transition ownership

## 27. Acceptance Criteria For M0

### Acceptance Purpose

`Encounter Framework` passes M0 if it proves that the first duel can be prepared, started, observed, completed, failed or aborted, and reset in a clean and debuggable way without stealing ownership from combat, enemy behavior, health, memory, locomotion, targeting, or camera systems.

### Required M0 Scenario

In one Tokyo Street duel arena, the prototype should be able to:

- register one player and one simple enemy
- validate readiness cleanly
- start the duel
- remain in active state while combat systems operate
- observe enemy defeat or player defeat if used
- observe whether reveal was accepted during the duel
- complete, fail, abort, or reset for explicit reasons
- return to a ready state for another run

### Pass If

- the encounter lifecycle states are explicit and debug-visible
- the duel only starts when required participants are ready
- the active encounter remains stable while external gameplay systems own their truth
- completion/fail/abort reasons are explicit
- reset is simple and repeatable
- the framework does not decide combat validity, enemy intent, reveal acceptance, player movement, target truth, or camera truth
- target registration ownership stays clean
- placeholder presentation is enough to validate encounter flow

### Fail If

- encounter state is unclear
- readiness blockers are hidden
- the duel starts without valid participants
- the encounter layer starts deciding combat, reveal, target, or movement truth
- end reason cannot be explained
- reset is inconsistent or slow enough to block M0 iteration
- the system grows into mission/wave/boss/progression scope before the first duel is proven

### M0 Pass Statement

`Encounter Framework` M0 passes when one player and one simple enemy can be registered into a single duel encounter that starts cleanly, runs stably, ends for explicit reasons, and resets predictably, with full debug visibility for lifecycle state and readiness, while all adjacent gameplay systems remain authoritative in their own domains.

### M0 Out Of Scope

The following are not required to pass this system for M0:

- waves
- boss phases
- multi-enemy encounters
- quest logic
- branching narrative
- rewards/loot
- persistence
- encounter editor tooling
