# Debug Overlay

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Combat As Interpretation, Melancholic Elegance

## 1. System Summary

`Debug Overlay` defines the M0 developer-facing visibility layer for tuning the first `Glass Refrain` duel. Its purpose is to collect and display read-only debug snapshots from the core M0 systems so designers and testers can understand state, timing, ownership, accepted/rejected requests, and why the loop `read → evade/parry → counter → reveal` succeeded or failed.

For M0, this system does not build a final HUD, a player-facing interface, a logging framework, a replay debugger, a graph visualizer, or a performance profiler. It only organizes and presents high-signal state from the existing gameplay systems in a simple developer-facing way, such as a text overlay or similarly lightweight debug surface.

`Combat Core`, `Player Locomotion`, `Enemy Intent & Telegraph`, `Health / Damage / Hit Reaction`, `Memory State`, `Lock-On / Target Context`, `Lock-On & Combat Camera`, and `Encounter Framework` remain the owners of their own gameplay truth. `Debug Overlay` owns only display organization, visibility toggles, read-only presentation of debug snapshots, debug labels, and the developer-facing readability of that information.

In short, `Debug Overlay` is the M0 explanation layer. It does not make the duel work. It helps the team understand why the duel works or fails.

## 2. Design Intent

The design intent of `Debug Overlay` is to reduce guesswork during combat feel tuning. `Glass Refrain` M0 is a tightly coupled duel prototype where combat, locomotion, enemy telegraphing, target focus, camera readability, consequence handling, memory response, and encounter flow all interact. If one of those systems is unclear, the team needs a fast way to inspect what actually happened.

For M0, the overlay should remain simple, readable, and high-signal. It does not need to be elegant in a player-facing sense. It needs to let a designer answer practical questions quickly:

- what state are we in?
- what just got accepted or rejected?
- why is control restricted?
- was `CounterWindow` really open?
- was the enemy punishable?
- did reveal get requested, accepted, or rejected?

The overlay should support understanding, not compensation. It should not be used to excuse unclear gameplay. If the duel only makes sense when debug is on, the underlying gameplay is still failing. The overlay exists to help diagnose that failure, not to hide it.

## 3. Player Experience Goals

`Debug Overlay` is not a player-facing system, so its goals are developer-facing rather than fantasy-facing.

### Fast Diagnosis

Designers should be able to identify the current duel state and the last important state transition quickly.

### Ownership Clarity

The overlay should make it easier to see which system owns the current truth instead of obscuring boundaries.

### High-Signal Readability

The overlay should show the most important duel-facing information without collapsing into noise.

### Loop Explainability

The overlay should help explain why `read → evade/parry → counter → reveal` succeeded or failed in a given exchange.

### Repeatable Tuning Support

The overlay should support repeated M0 duel testing without requiring a heavy tools pass or a large debug ecosystem.

## 4. M0 Scope

This section defines exactly what `Debug Overlay` includes for `M0 — Katana Combat Feel Prototype`.

### Included In M0

#### One Developer-Facing Overlay

M0 includes one simple developer-facing overlay. A text overlay is enough.

#### Read-Only Snapshot Presentation

M0 includes read-only display of debug snapshots or current state values from the relevant systems.

#### Channel Grouping

M0 includes grouped visibility for the key duel systems so the team can focus on the relevant source of truth.

#### Simple Visibility Toggles

M0 may include lightweight toggles to show or hide major groups of debug information.

#### Minimal Cross-System Readability

M0 includes enough cross-system visibility to understand the whole duel loop without requiring a separate replay or analysis tool.

### Explicitly Out Of Scope For M0

- final HUD
- player-facing UI
- editor tooling
- analytics system
- logging framework
- replay/timeline debugger
- graph visualization
- performance profiler

## 5. Non-Goals

`Debug Overlay` must stay tightly scoped for M0. It exists to surface truth, not to become a tools platform.

### Not Gameplay UI

This system must not become part of the player-facing combat interface.

### Not Gameplay Authority

It must not own or change combat, movement, camera, memory, health, or encounter results.

### Not A Fix For Bad Readability

The overlay must not be treated as the solution to unclear gameplay. It only helps explain unclear gameplay.

### Not A Logging Or Telemetry Platform

M0 does not require a persistent logging, analytics, or telemetry framework here.

### Not A Replay Or Timeline Tool

M0 does not require recorded timelines, step-through debugging, or event history visualization beyond lightweight last-event/state display.

### Not A Profiling Tool

Performance budgets and profiling belong elsewhere.

## 6. Core Debug Loop

The core M0 debug loop should support:

`observe current state → inspect last accepted/rejected request → relate ownership across systems → identify failure/success cause → retest`

This loop exists to help designers move from confusion to a concrete next tuning decision.

### Observe Current State

The overlay should show the current important duel states across the relevant systems.

### Inspect Last Request / Result

The overlay should expose the last meaningful accepted or rejected request where useful, such as dodge accepted/rejected or reveal accepted/rejected.

### Relate Ownership

The overlay should make it easier to tell which system owns the current truth.

### Identify Cause

The overlay should support diagnosing why the current exchange succeeded or failed.

### Retest

The overlay should support rapid iteration by making the duel understandable enough to try again immediately.

## 7. Debug Display Model

For M0, a small grouped display model is enough.

### Global Duel Header

The overlay should expose a compact top-level summary such as:

- encounter state
- combat state
- locomotion state
- current target state
- enemy state
- memory state

### Channel Groups

The overlay should support grouped channels for:

- `Combat Core`
- `Player Locomotion`
- `Enemy Intent & Telegraph`
- `Health / Damage / Hit Reaction`
- `Memory State`
- `Lock-On / Target Context`
- `Lock-On & Combat Camera`
- `Encounter Framework`

### Last-Reason Surface

Where possible, the overlay should include the latest accepted/rejected result reason rather than forcing designers to infer from state alone.

### Simple Toggle Model

M0 may support:

- all on
- per-channel visibility
- compact vs expanded display if needed

No advanced tooling UI is required.

## 8. Required M0 Debug Channels

The following M0 debug channels are required:

- current combat state/result
- current player locomotion state
- movement restriction source
- dodge requested/accepted/rejected
- dodge phase/result
- parry result
- `CounterWindow` open/closed
- `EnemyPunishWindow` active/inactive
- enemy telegraph/commit/active/recovery
- current target focus state
- current camera state
- health values
- hit reaction active/source
- reveal requested/accepted/rejected
- current memory state
- encounter state
- last accepted/rejected request reason
- `Animator` / FSM mismatch if available

These channels are the minimum needed to tune the first duel honestly.

## 9. Combat Core Debug Contract

`Debug Overlay` should be able to read and display the following from `Combat Core`:

- current combat state
- last combat result
- dodge result
- parry result
- counter result if relevant
- `CounterWindow` open/closed
- reveal request context
- last accepted/rejected combat-facing request reason if surfaced

`Debug Overlay` must not infer missing combat truth. It only displays what `Combat Core` exposes.

## 10. Player Locomotion Debug Contract

`Debug Overlay` should be able to read and display the following from `Player Locomotion`:

- current locomotion state
- movement phase
- movement restriction source
- dodge requested/accepted/rejected
- dodge phase
- dodge result if surfaced from combat context
- facing mode
- recovery active/source
- hit reaction movement suppression if surfaced
- `Animator` / FSM mismatch if available

The overlay must not change locomotion state or movement behavior.

## 11. Enemy Intent & Telegraph Debug Contract

`Debug Overlay` should be able to read and display the following from `Enemy Intent & Telegraph`:

- current enemy state
- telegraph active?
- commitment active?
- attack active?
- recovery active?
- current attack tags
- `EnemyPunishWindow` active/inactive
- last enemy-side transition reason if surfaced

The overlay must not become enemy AI control or an enemy-state authoring tool.

## 12. Health / Damage / Hit Reaction Debug Contract

`Debug Overlay` should be able to read and display the following from `Health / Damage / Hit Reaction`:

- player health
- enemy health
- last damage source/target if surfaced
- hit reaction active/source
- disabled/defeated state
- last consequence-facing reason if surfaced

The overlay must not apply or modify consequence state.

## 13. Memory State Debug Contract

`Debug Overlay` should be able to read and display the following from `Memory State`:

- current memory state
- reveal requested?
- reveal accepted/rejected/ignored?
- reveal request source/context
- rejection reason
- responding active?
- cooldown/reset active?

The overlay must not create or accept reveal requests.

## 14. Lock-On / Target Context Debug Contract

`Debug Overlay` should be able to read and display the following from `Lock-On / Target Context`:

- target focus active
- current target
- target validity
- target direction if surfaced

The overlay must not own target truth or target changes.

## 15. Lock-On & Combat Camera Debug Contract

`Debug Overlay` should be able to read and display the following from `Lock-On & Combat Camera`:

- current camera state
- current framing/readability state if surfaced
- critical feedback source if useful
- relevant camera reason labels if available

The overlay must not adjust framing, feedback, or target focus behavior.

## 16. Encounter Framework Debug Contract

`Debug Overlay` should be able to read and display the following from `Encounter Framework`:

- current encounter state
- previous encounter state
- time in encounter
- registered player
- registered enemy
- encounter start reason
- encounter end reason
- reset reason
- readiness blockers
- missing participant/config errors

The overlay must not start, end, or reset encounters by itself unless a separate manual debug control is explicitly approved elsewhere.

## 17. Debug Readability Rules

The overlay should remain clear, compact, and useful.

### High Signal First

The most important duel-facing state should be easy to find first.

### Labels Match GDD Terms

Debug labels should match GDD state names where possible.

### Reasons Over Mystery

Where a request is accepted or rejected, reason labels should be shown when available.

### Clutter Avoidance

The overlay should not dump every possible value if it hides the important ones.

### Readability Over Fancy Tools

Simple, readable text is better than a dense tool surface for M0.

## 18. Debug Data Ownership Rules

This section defines how the overlay must relate to source systems.

### Read-Only Rule

`Debug Overlay` must be read-only.

### Source-Of-Truth Rule

Every displayed value must belong to an owning gameplay system.

### No Hidden Derivation Rule

The overlay should avoid inventing gameplay truth by combining data into unowned pseudo-state unless explicitly labeled as derived display-only summary.

### Ownership Clarity Rule

If two systems expose related values, the overlay should preserve who owns each one instead of flattening them into ambiguity.

## 19. Presentation Boundaries

`Debug Overlay` is presentation for developers, but it is still not gameplay authority.

### May Own

- debug display organization
- channel grouping
- visibility toggles
- labels
- compact/expanded presentation if used

### Must Not Own

- gameplay state
- gameplay transitions
- gameplay corrections
- request acceptance
- combat, movement, memory, camera, or encounter truth

### Not Player-Facing

The overlay is not part of the shipped M0 player-facing readability contract.

## 20. Technical Boundaries

This system should stay simple and test-supportive.

### Technically Owns

- debug display organization
- read-only snapshot presentation
- channel toggles
- debug label formatting

### May Consume

- read-only state snapshots
- read-only current values
- read-only last-result/last-reason data

### Must Not Depend On As Authority

- `Animator State Machine`
- VFX / Audio timing
- UI input state as gameplay truth
- hidden global state not owned by a gameplay system

### Simplicity Rule

M0 does not require a full debug architecture. A small, reliable read-only overlay is preferred.

## 21. Dependencies

### Upstream Dependencies

- `Combat Core`
- `Player Locomotion`
- `Enemy Intent & Telegraph`
- `Health / Damage / Hit Reaction`
- `Memory State`
- `Lock-On / Target Context`
- `Lock-On & Combat Camera`
- `Encounter Framework`

### Downstream Consumers

- designers
- testers
- later QA/debug workflows if needed

### Dependency Direction Rules

- all gameplay systems remain authoritative
- overlay only observes exposed debug/state context
- no circular ownership
- no gameplay should require the overlay to function

## 22. Risks

### Major M0 Risks

#### Overlay Becomes Gameplay UI

- Why it matters: ownership and readability goals blur
- Early warning signs: players are expected to read debug instead of gameplay
- Mitigation: keep the overlay explicitly developer-facing
- Priority: High

#### Overlay Becomes Too Noisy

- Why it matters: designers stop using it
- Early warning signs: too many values, unclear grouping, important reasons buried
- Mitigation: prioritize high-signal channels and readable grouping
- Priority: High

#### Overlay Starts Owning Derived Truth

- Why it matters: ownership boundaries collapse
- Early warning signs: overlay invents pseudo-state that conflicts with source systems
- Mitigation: keep source ownership explicit and derived summaries clearly labeled
- Priority: High

#### Missing Reason Labels Slow Tuning

- Why it matters: accepted/rejected requests remain mysterious
- Early warning signs: designers still cannot explain why dodge or reveal failed
- Mitigation: expose last accepted/rejected reason where useful
- Priority: High

#### Overlay Is Used To Excuse Bad Gameplay Readability

- Why it matters: the prototype looks diagnosable but still plays unclearly
- Early warning signs: the duel only makes sense with debug on
- Mitigation: treat debug as diagnosis, not as a substitute for readable design
- Priority: High

## 23. Open Questions

### Must Answer Before M0 Implementation

- Is `Debug Overlay` one combined duel overlay or a set of per-system panels under one surface?
- What is the minimum always-visible header for first-pass tuning?
- Are last accepted/rejected reasons available from all required systems, or only some of them for M0?
- Is manual debug-only control input needed to toggle channel groups from day one?

### Can Answer During M0 Tuning

- exact channel grouping order
- compact vs expanded display format
- whether some channels should be hidden by default
- how much `Animator` / FSM mismatch visibility is needed
- whether target direction or camera reason labels need extra prominence

### Defer After M0

- replay/timeline debugger
- persistent logging
- analytics integration
- graph visualization
- editor debug tools
- profiler integration
- player-accessible debug views

## 24. Acceptance Criteria For M0

### Acceptance Purpose

`Debug Overlay` passes M0 if it proves that designers can inspect the first duel’s critical state, timing, ownership, and accepted/rejected request flow clearly enough to understand why the duel loop succeeds or fails.

### Required M0 Scenario

In one duel arena, the overlay should let the team observe:

- current combat state/result
- current locomotion state
- enemy telegraph/commit/active/recovery
- target focus and camera state
- health and hit reaction state
- reveal requested/accepted/rejected
- encounter lifecycle state

while the duel is running, ending, and resetting.

### Pass If

- the overlay is read-only
- the overlay is not player-facing UI
- the overlay exposes all required M0 debug channels
- reason labels are available where they matter for tuning
- GDD state names are reflected clearly enough in labels
- the overlay helps explain why `read → evade/parry → counter → reveal` succeeded or failed
- the duel remains understandable even when the overlay is off

### Fail If

- important state is missing
- accepted/rejected request reasons remain opaque where M0 tuning depends on them
- the overlay becomes too noisy to use
- the overlay changes or owns gameplay state
- the overlay is relied on as a substitute for readable gameplay

### M0 Pass Statement

`Debug Overlay` M0 passes when one player-versus-one-enemy duel can be observed through a simple read-only developer overlay that clearly surfaces the critical combat, locomotion, enemy, health, memory, targeting, camera, and encounter state needed to understand and tune the first `Glass Refrain` duel loop.

### M0 Out Of Scope

The following are not required to pass this system for M0:

- final HUD
- player-facing UI
- editor tooling
- analytics
- logging framework
- replay/timeline debugging
- graph visualization
- profiling features
