# Memory State

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Combat As Interpretation, Distorted Memory Spaces, Personal Restoration Over Power Fantasy

## 1. System Summary

`Memory State` defines the provisional M0 contract for how `Glass Refrain` responds to meaningful combat success with a restrained memory or reveal response. For the first katana duel prototype, this system does not implement the full narrative memory framework, district reinterpretation, contradiction tracking, or long-term restoration logic. It only decides whether a reveal request from `Combat Core` is accepted, rejected, or ignored, and exposes a small, debug-visible memory response state for downstream presentation support.

For M0, `Memory State` exists to complete the loop `read → evade/parry → counter → reveal` without overbuilding a full mystery system. It gives the first duel a visible meaning beyond damage by allowing certain validated combat outcomes to trigger a brief, emotionally restrained reveal response. Its job is not to decide whether the player succeeded in combat. Its job is to decide whether that already-confirmed success is meaningful enough to produce the first memory-facing response.

`Combat Core` owns combat action validity, hit/parry/dodge/counter result validation, `CounterWindow`, and reveal request context. `Memory State` owns reveal request acceptance or rejection, provisional memory state value, reveal cooldown or guard if needed, and memory-facing debug truth. `Health / Damage / Hit Reaction` owns health and reaction consequence. `Enemy Intent & Telegraph` owns enemy-side telegraph, commitment, tags, and `EnemyPunishWindow`. `Player Locomotion` owns movement truth. `Lock-On & Combat Camera` owns framing and readability after valid memory context. Presentation systems may communicate reveal response, but they remain presentation-only unless responding to confirmed gameplay state.

In short, `Memory State` is the first small meaning layer for the duel. It does not prove the whole narrative. It proves that a successful combat interpretation can produce a readable, restrained memory response without breaking combat ownership or overwhelming M0 scope.

## 2. Design Intent

The design intent of `Memory State` in M0 is to give combat a small but meaningful emotional consequence. `Glass Refrain` is not only about winning exchanges. It is about cutting through distorted truth. The first duel prototype therefore needs a minimal memory-facing system that can answer a simple question: when the player succeeds meaningfully, does the world acknowledge that success as a fracture in false memory?

For M0, the answer should remain small, explicit, and controlled. The reveal response should feel noticeable but restrained. It should not become a cutscene, a branching narrative graph, or a heavy interruption to combat flow. The player should understand that something memory-related just happened, but the duel should remain readable and mechanically trustworthy.

This system therefore prioritizes acceptance rules, rejection rules, cooldown or guard behavior if needed, and debug visibility over narrative complexity. It must be easy to inspect why a reveal request was accepted, rejected, or ignored. It must also be difficult for presentation systems to fake reveal meaning. If a reveal happens, it should be because gameplay requested it through an explicit, valid context.

The emotional goal is not spectacle. The emotional goal is a brief sense of fracture, recognition, and unstable truth after a meaningful defensive or counter-based success. M0 only needs to prove that this connection exists and is readable.

## 3. Player Experience Goals

The player experience goals for M0 `Memory State` are about meaning, restraint, and clarity.

### Reveal Feels Earned

The player should feel that reveal happens because they achieved a meaningful combat success, not because the game arbitrarily fired a visual effect.

### Reveal Is Readable

The player should understand that a reveal response occurred, even if they do not yet understand its full narrative meaning.

### Reveal Is Short And Restrained

The reveal should be brief enough that it does not hijack the duel or turn the prototype into a cinematic interruption.

### Reveal Does Not Replace Combat Truth

The player should not confuse reveal with hit confirmation, counter validation, or defeat validation. Reveal follows meaningfully confirmed gameplay context; it does not create it.

### Rejection Is Understandable In Debug

If a reveal request does not fire, designers and testers should be able to understand why. The system should not feel mystical or hidden during tuning.

### Combat Readability Is Preserved

Reveal should not hide enemy recovery, player recovery, punish windows, or the next telegraph. The player should still be able to follow the duel rhythm.

## 4. M0 Scope

This section defines exactly what `Memory State` includes for `M0 — Katana Combat Feel Prototype`.

### Included In M0

#### One Simple Memory State

M0 includes one simple memory-state flow that can represent dormant, requested, accepted/rejected, responding, and cooldown/reset behavior.

#### One Basic Reveal Response

M0 includes one restrained reveal response only. It exists to show that a meaningful combat success can produce a memory-facing reaction.

#### Reveal Request Handling

M0 includes explicit rules for:

- accepted requests
- rejected requests
- ignored requests if needed
- cooldown or guard behavior if reveal is already responding

#### Debug Visibility

M0 includes debug-facing visibility for reveal request source, accepted/rejected state, reason, and current memory response state.

### Explicitly Out Of Scope For M0

- full narrative memory graph
- clue database
- branching memory progression
- district reinterpretation
- save or persistence
- full cutscene system
- final VFX/audio requirement
- cinematic reveal sequence
- long-term progression consequences
- contradiction-resolution framework

## 5. Non-Goals

`Memory State` must stay tightly scoped for M0. It exists to prove a minimal reveal consequence, not to solve the full narrative architecture of `Glass Refrain`.

### Not A Full Narrative System

M0 does not need branching memory logic, incident history, or story-state progression here.

### Not District Reinterpretation

This system does not yet own altered routes, changed spaces, or restored-world logic.

### Not Clue Or Contradiction Tracking

M0 does not require clue collection, contradiction resolution, or investigation-state ownership.

### Not Save / Persistence

M0 does not require memory-state persistence across sessions or levels.

### Not A Cutscene Driver

Reveal is not a cinematic sequence framework in M0. It should remain brief and readable.

### Not Combat Authority

This system must not validate hit, dodge, parry, counter, or `CounterWindow`.

### Not Health / Damage Authority

This system must not apply damage, decide stagger, or own defeat logic.

### Not Presentation Authority

This system may trigger presentation support through confirmed memory context, but `Animator`, `VFX`, `Audio`, `Camera`, and `UI` must not become the source of reveal truth.

## 6. Core Memory Reveal Loop

The M0 memory reveal loop should support:

`dormant → reveal request received → accept/reject/ignore decision → responding → cooldown/reset → dormant`

This maps onto the combat rhythm:

- `dormant` preserves calm baseline
- `reveal request received` follows meaningful validated combat context
- `accept/reject/ignore` protects gameplay truth and scope
- `responding` communicates a restrained memory fracture
- `cooldown/reset` returns the duel to readable control

This system should not invent requests on its own. It only handles them once they are explicitly provided through valid gameplay context.

## 7. Memory State Model

For M0, the following state model is enough.

### MemoryDormant

No reveal request is currently active. This is the default state for most of the duel.

### RevealRequested

A reveal request has been received from a valid gameplay source and is awaiting acceptance or rejection evaluation.

### RevealAccepted

The request has been validated as meaningful for M0 memory response and is allowed to transition into responding.

### RevealRejected

The request was explicitly evaluated and denied. Rejection reason should be debug-visible.

### RevealResponding

The system is currently exposing the short M0 memory response state for downstream presentation or readability support.

### RevealCooldown / Reset

The system is leaving the active response and preventing immediate repeated reveal spam if a cooldown or guard is needed.

### State Notes

- `RevealRequested`, `RevealAccepted`, and `RevealRejected` may be short-lived state transitions.
- exact timing remains tunable
- `Memory State` owns these memory-facing truth values
- presentation may observe them, but not replace them

## 8. Reveal Request Rules

Reveal requests for M0 should be explicit, meaningfully sourced, and small in number.

### Valid Request Source

Reveal request must come from `Combat Core` or another explicitly valid gameplay context approved later. Presentation-only systems must not create reveal requests.

### Recommended Accepted M0 Contexts

- successful parry-counter
- successful dodge-punish-counter
- meaningful counter stagger
- enemy defeat if approved
- manual debug trigger for testing only

### Recommended Rejected M0 Contexts

- generic hit
- failed dodge
- failed parry
- invalid counter
- no valid target
- reveal already active or cooling down
- request from presentation-only system

### Rule Of Meaningful Success

M0 reveal should only be triggered by meaningful validated combat context, not by ordinary contact or passive time progression.

## 9. Reveal Acceptance / Rejection Rules

The acceptance layer is the core job of this system in M0.

### Accept If

- the request source is valid
- the request context is marked meaningful for M0
- reveal is not already responding or blocked by cooldown/reset
- target and encounter context are valid enough for the response

### Reject If

- the source is not valid
- the combat success was generic rather than meaningful
- reveal is already active or guarded
- no valid target or duel context exists
- the request is otherwise out of scope for M0

### Ignore If

M0 may optionally ignore redundant or obviously invalid requests without full rejection handling if that simplifies prototype behavior, but ignored behavior should still be debug-visible if used.

### Rejection Must Be Explainable

If reveal does not happen, debug must explain whether the request was never made, rejected, or ignored, and why.

## 10. Memory Response Rules

M0 memory response should remain short, readable, and non-authoritative.

### Response Purpose

The response exists to acknowledge meaningful combat interpretation, not to replace combat feedback or start a full narrative event.

### Response Expectations

- short and restrained
- clearly downstream of accepted reveal context
- should not hide enemy punish, recovery, or next telegraph
- should not take control of movement or combat truth
- should return cleanly to dormant or cooldown/reset

### Cooldown / Guard

M0 may use a small cooldown or simple guard to prevent repeated reveal spam from back-to-back qualifying results if needed for readability.

### No Memory Progression Ownership

The response may expose a provisional memory state value, but it does not yet become long-term narrative progression.

## 11. Relationship To Combat Core

`Combat Core` is the upstream reveal-request authority. `Memory State` is the acceptance and response authority.

### `Combat Core` Owns

- combat action validity
- hit/parry/dodge/counter result validation
- `CounterWindow`
- reveal request context

### `Memory State` Owns

- reveal request acceptance/rejection
- provisional memory state value
- reveal cooldown/guard if needed
- memory response state
- memory debug truth

### Boundary Rule

`Memory State` must not infer combat success by itself. If reveal happens, it must be because valid reveal context was explicitly requested upstream.

## 12. Relationship To Health / Damage / Hit Reaction

`Health / Damage / Hit Reaction` owns physical consequence. `Memory State` owns memory consequence.

### `Health / Damage / Hit Reaction` Owns

- health changes
- damage application
- hit reaction classification
- defeat/disabled request
- post-hit consequence context

### `Memory State` May Observe

- enemy defeat context if reveal rules allow it
- stronger consequence context if surfaced by gameplay systems

### Boundary Rule

`Memory State` must not apply damage, decide hit reaction, or own defeat truth. It may respond to valid consequence context, but physical consequence remains outside this system.

## 13. Relationship To Enemy Intent & Telegraph

`Enemy Intent & Telegraph` owns enemy-side readability and punish state. `Memory State` must not replace those systems with reveal theatrics.

### `Enemy Intent & Telegraph` Owns

- enemy telegraph
- enemy commitment
- attack tags
- `EnemyPunishWindow`
- enemy-side readability

### `Memory State` Must Respect

- reveal must not hide the next telegraph
- reveal must not make enemy punish state unreadable
- reveal must not redefine enemy-side commitment or vulnerability

### Boundary Rule

The reveal layer can add meaning after valid context, but it must not override enemy readability.

## 14. Relationship To Player Locomotion

`Player Locomotion` owns movement truth. `Memory State` does not own player control, dodge, or recovery.

### `Player Locomotion` Owns

- movement state truth
- dodge movement
- recovery movement
- hit reaction movement response

### `Memory State` Must Not Do

- change locomotion truth
- interrupt recovery invisibly
- decide movement restrictions
- drive dodge/parry/counter outcome through reveal

### Boundary Rule

If reveal response needs movement-facing support later, it must remain explicitly coordinated and subordinate to locomotion truth.

## 15. Relationship To Lock-On / Combat Camera

`Lock-On & Combat Camera` owns framing and readability after valid memory context.

### `Lock-On / Target Context` Owns

- target focus active
- current target
- target validity
- target direction

### `Lock-On & Combat Camera` Owns

- framing/readability
- reveal framing support after valid memory context

### `Memory State` Provides

- accepted or rejected reveal context
- current memory response state
- cooldown/reset state if needed

### Boundary Rule

Camera may support reveal after valid memory context, but it must not become reveal authority or hide the next enemy read.

## 16. Debug / Readability Requirements

Debug exists to explain reveal request handling and current memory response state.

### Required Debug Data

- current memory state
- reveal request received?
- reveal request source
- reveal request context label
- request accepted, rejected, or ignored?
- rejection/ignore reason
- reveal responding active?
- reveal cooldown/reset active?
- current target if relevant
- last accepted reveal timestamp/state transition if useful
- manual debug trigger used?
- last downstream presentation request if useful for comparison

### Debug Goals

Designers should be able to answer:

- did `Combat Core` actually request reveal?
- was the request accepted, rejected, or ignored?
- why did reveal happen or not happen?
- is reveal being blocked by cooldown/reset?
- is current memory response still active?

## 17. Data Authoring Needs

This section defines the minimum tunable data needed for M0.

### Minimum Tunable Data

- allowed reveal request categories
- rejected request categories
- reveal response duration
- reveal cooldown/reset duration if used
- debug labels for request reasons
- provisional memory state labels
- optional manual debug trigger enable flag

### Guidance

- exact values are deferred to tuning
- M0 can start with simple constants or lightweight config
- the system should remain easy to tune
- no large authored narrative data set is needed for M0

## 18. Presentation Boundaries

Presentation systems may communicate accepted memory response, but they must not own it.

### VFX / Audio

May present:

- restrained reveal pulse
- subtle distortion cue
- short memory-response accent

Must not:

- create reveal requests
- decide reveal validity
- imply reveal acceptance before memory truth exists

### Camera

May present:

- restrained reveal framing support after valid context

Must not:

- accept reveal on its own
- hide punish/recovery/next telegraph
- turn reveal into a cutscene in M0

### Animator / UI

May present:

- optional development-facing state visibility
- optional subtle response alignment

Must not:

- own memory response truth
- become required to understand base reveal state

## 19. Technical Boundaries

This system should remain explicit, small, and testable.

### Technically Owns

- memory state model
- reveal request evaluation
- accepted/rejected/ignored truth
- reveal cooldown/reset guard if used
- memory debug snapshot

### May Consume

- reveal request context from `Combat Core`
- valid target/readability context if explicitly needed
- manual debug request for testing only

### Must Not Depend On As Authority

- `Animator State Machine`
- VFX / Audio timing
- camera state
- UI state
- passive timers unrelated to valid request context

### Simplicity Rule

M0 does not require a full narrative state framework here. A small explicit state model is preferred over a broad future-proof system.

## 20. Dependencies

### Upstream Dependencies

- `Combat Core`
- optional `Health / Damage / Hit Reaction` consequence context
- `Lock-On / Target Context` if target validity is required for acceptance rules
- `Debug Overlay`

### Downstream Consumers

- `Lock-On & Combat Camera`
- `VFX`
- `Audio`
- `UI / Debug`
- later memory/presentation systems

### Dependency Direction Rules

- consume explicit gameplay request context
- expose read-only memory state and reveal result snapshots
- avoid circular ownership with combat or camera
- keep narrative expansion deferred until after M0

## 21. Risks

### Major M0 Risks

#### Reveal Fires Too Often

- Why it matters: the response loses meaning and overwhelms duel readability
- Early warning signs: generic hits repeatedly trigger reveal
- Mitigation: keep accepted contexts narrow and use cooldown/reset if needed
- Priority: High

#### Reveal Never Fires

- Why it matters: the core loop loses its memory-facing payoff
- Early warning signs: meaningful counter success produces no visible memory response
- Mitigation: make request/acceptance debug explicit and keep one simple accepted path
- Priority: High

#### Memory State Infers Combat Success

- Why it matters: ownership boundaries collapse
- Early warning signs: reveal appears without explicit `Combat Core` request
- Mitigation: require explicit request source and reject presentation-only triggers
- Priority: High

#### Reveal Hides Combat Readability

- Why it matters: the memory response harms the duel rather than supporting it
- Early warning signs: reveal obscures punish, recovery, or the next telegraph
- Mitigation: keep response short and restrained, coordinate with camera boundaries
- Priority: High

#### Cooldown Logic Becomes Overbuilt

- Why it matters: M0 scope drifts into a full gating framework
- Early warning signs: multiple timers and state exceptions accumulate
- Mitigation: use only the minimum guard needed to prevent reveal spam
- Priority: Medium

#### Presentation Becomes Reveal Truth

- Why it matters: VFX/audio/camera start driving state instead of observing it
- Early warning signs: reveal appears because an effect fired, not because memory accepted it
- Mitigation: keep memory truth debug-visible and presentation downstream only
- Priority: High

## 22. Open Questions

### Must Answer Before M0 Implementation

- Is enemy defeat an accepted reveal context in the first playable prototype?
- Does M0 need a reveal cooldown/reset guard from day one?
- Does `Lock-On / Target Context` need to be part of reveal acceptance rules for valid target checks?
- Is manual debug reveal trigger required before tuning starts?
- Is one accepted combat success path enough, or must M0 prove both parry-counter and dodge-punish-counter reveal paths?

### Can Answer During M0 Tuning

- exact reveal response duration
- exact cooldown/reset duration if used
- whether accepted reveal should slightly differ by context label
- whether rejected requests should linger briefly in debug
- how much presentation support is needed before reveal becomes readable

### Defer After M0

- branching memory progression
- clue and contradiction tracking
- district reinterpretation
- save/persistence
- full narrative graph
- cinematic reveal sequencing
- long-term memory progression systems

## 23. Acceptance Criteria For M0

### Acceptance Purpose

`Memory State` passes M0 if it proves that a meaningful validated combat success can produce a short, readable, debug-visible reveal response without stealing combat, damage, enemy, locomotion, or camera ownership.

### Required M0 Scenario

In one duel arena, the prototype should be able to:

- receive a reveal request from `Combat Core`
- accept, reject, or ignore that request explicitly
- enter a short responding state after valid accepted context
- return to dormant or cooldown/reset cleanly
- expose the full decision path in debug

### Pass If

- reveal only triggers from meaningful validated combat context
- generic hits and failed responses do not trigger reveal
- accepted/rejected/ignored state is debug-visible
- reveal response is short and restrained
- reveal does not hide recovery, punish, or next telegraph
- `Memory State` does not infer combat success by itself
- `Memory State` does not open `CounterWindow`
- `Memory State` does not apply damage or own enemy stagger
- placeholder presentation is enough to validate reveal truth

### Fail If

- reveal fires from generic light hits or presentation-only events
- reveal request source cannot be explained
- reveal happens without explicit valid gameplay context
- reveal response becomes cutscene-like or obscures duel readability
- cooldown/reset logic becomes more complex than the duel prototype needs
- debug cannot explain why reveal happened or did not happen
- the system expands into full narrative memory design before M0 duel feel is proven

### M0 Pass Statement

`Memory State` M0 passes when one player and one simple enemy can repeatedly reach a meaningful combat success that produces a short, readable memory response only after explicit accepted reveal context, with clear debug visibility for request source, acceptance/rejection, and current memory response state.

### M0 Out Of Scope

The following are not required to pass this system for M0:

- full narrative graph
- clue database
- branching memory progression
- district reinterpretation
- save/persistence
- cutscene system
- final VFX/audio
- cinematic reveal sequence
