# Player Locomotion

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Combat As Interpretation, Melancholic Elegance

## 1. System Summary

`Player Locomotion` defines how the player moves, turns, repositions, and recovers in moment-to-moment play so the first duel prototype in `Glass Refrain` feels readable, precise, and emotionally controlled. Its purpose is not to build a full traversal stack, an acrobatic action-mobility system, or a broad movement framework for every future gameplay mode. Its purpose is to make one katana duel feel grounded, fair, and legible.

For M0, this system exists to support the loop `read → evade/parry → counter → reveal` by ensuring the player can hold spacing, reposition intentionally, dodge with readable displacement, and return to a neutral rhythm after each exchange. Movement should help the player interpret enemy intent rather than drown the duel in speed, drift, or spectacle.

This system does not own combat truth. It does not decide hit results, parry success, dodge validity, counter validity, `CounterWindow`, or reveal validity. Those remain owned by `Combat Core` and supporting enemy- and memory-facing systems. `Player Locomotion` owns movement implementation, orientation support, committed movement restrictions, and readable displacement under gameplay rules defined elsewhere.

### Animation / FSM Boundary Note

For M0, gameplay truth should remain owned by a pure C# finite state machine layer rather than by the Animator State Machine. The pure C# FSM should own gameplay state, locomotion state, combat action state, cancel rules, action validity, and debug truth. The Animator State Machine is presentation only.

Animation layers and `Avatar Masks` may be used later for visual blending, but they must not own gameplay truth. For M0, simple full-body combat actions are preferred first: `light attack`, `heavy attack`, `dodge`, `parry`, `counter`, and `hit reaction`. `Avatar Mask` support is optional for M0 and should not be required to prove combat feel. It may be introduced later for upper-body guard, parry overlay, lock-on strafe polish, or more advanced attack blending.

Root motion remains an open decision and must be coordinated with `Player Locomotion` and `Combat Core`. Animation events may request sync points later, but `Combat Core` and `Player Locomotion` must validate gameplay timing.

In short, `Player Locomotion` is the movement truth layer for the first duel. If movement feels floaty, sticky, unreadable, or animation-driven in the wrong way, the combat prototype will fail even if the combat rules themselves are strong.

## 2. Design Intent

The design intent of `Player Locomotion` is to make the player feel deliberate, grounded, and capable of small but meaningful movement decisions. In `Glass Refrain`, movement should not feel like skating, twitching, or endlessly circling for advantage. It should feel like measured footwork under emotional tension.

For M0, locomotion should support a restrained katana duel. The player should be able to:

- approach or hold spacing with intent
- make short positional corrections
- dodge with understandable displacement
- feel committed during heavier actions
- return to readable neutral after each exchange

Movement should serve readability before expressiveness. The player should not feel hyper-mobile or animation-locked in a way that hides control. The goal is controlled elegance: enough responsiveness to feel precise, enough commitment to make choices meaningful, and enough stability that the player always understands where they are, where the enemy is, and why an exchange succeeded or failed.

Tonally, locomotion should support the melancholic and elegant identity of `Glass Refrain`. The player should feel like they are navigating tension through careful posture and footwork rather than through frantic action-game noise. Even defensive movement should feel intentional instead of panic-driven.

This system should also align cleanly with the camera and combat layers. `Lock-On & Combat Camera` should be able to read and frame locomotion clearly. `Combat Core` should be able to restrict or permit movement explicitly. Animation should communicate locomotion, but not secretly control gameplay truth.

## 3. Player Experience Goals

The player experience goals for M0 locomotion are about trust, clarity, and controlled movement under pressure.

### Grounded Control

The player should feel that movement is stable and grounded. Movement should not feel slippery, floaty, or detached from the duel space. Small directional inputs should produce understandable results.

### Readable Spacing

The player should be able to judge their distance to the enemy clearly enough to understand whether they are safe, threatened, or in position to punish. Locomotion should support spacing as a real gameplay skill.

### Intentional Repositioning

The player should be able to reposition around the enemy with purpose. Movement should support reading, circling, approach, retreat, and dodge follow-through without becoming chaotic.

### Clear Dodge Displacement

The player should understand where dodge moved them and why that mattered. A successful dodge should feel spatially meaningful, not like a visual trick.

### Controlled Commitment

The player should feel that heavier actions and defensive commitments matter. Locomotion should not erase the consequences of attack commitment or recovery by allowing unrestricted cancellation through movement.

### Orientation Clarity

The player should understand which way they are facing, especially during focused duel states. Movement, facing, and target relationship should remain readable even under pressure.

### Fair Failure

If the player is hit, fails a dodge, or misjudges range, they should be able to tell whether they were too early, too late, too close, too far, or committed in the wrong direction. Movement should help failure feel explainable rather than random.

### Debuggable Feel

Designers and testers should be able to inspect locomotion state, movement restrictions, facing mode, dodge displacement, and any combat-imposed movement limits while tuning. If movement feel is wrong, the team should be able to identify whether the problem comes from locomotion, combat restrictions, camera framing, or presentation.

## 4. M0 Scope

This section defines exactly what `Player Locomotion` includes for `M0 — Katana Combat Feel Prototype`. The purpose is to support one player, one simple enemy, one duel space, and the first readable combat loop.

### Included In M0

#### Basic Ground Movement

M0 includes basic grounded movement sufficient for duel spacing and controlled repositioning. The player should be able to move, slow, stop, and change direction in a readable way.

#### Orientation / Facing Support

M0 includes enough orientation support to keep the player’s facing understandable during free movement, focused movement, and committed combat actions. Final movement-relative mode choices may remain provisional during tuning.

#### Dodge Movement

M0 includes one readable dodge action with clear displacement. Dodge only needs to be strong enough to test spacing, avoidance, and post-dodge punish visibility.

#### Combat Movement Restrictions

M0 includes movement restrictions during committed actions where needed so `Combat Core` can preserve fair action commitment, recovery, and cancel rules.

#### Hit Reaction / Recovery Movement Response

M0 includes the minimum locomotion response needed when the player is hit, recovers, or returns to neutral after an exchange.

#### Target Focus / Camera Coordination Contract

M0 includes a provisional contract with `Lock-On & Combat Camera` so locomotion remains readable under target focus or lock-on, without making camera truth the owner of movement.

#### Debug Visibility

M0 includes debug-facing visibility for locomotion state, movement mode, facing mode, movement restrictions, and dodge displacement so the feel of movement can be tuned intentionally.

### M0 Completion Target For This System

`Player Locomotion` is in scope for M0 when the player can move, hold spacing, dodge, recover, and reorient in a way that makes one duel readable and fair without relying on advanced animation layering, traversal systems, or broad movement feature sets.

## 5. Non-Goals

`Player Locomotion` must stay tightly scoped for M0. It exists to make one duel feel good, not to solve every movement problem for the full game.

### Not A Full Traversal System

M0 does not need climbing, vaulting, ledge logic, sprint parkour, platforming movement, exploration traversal, or broad world-navigation support.

### Not A Stylish Mobility System

M0 does not need air dashes, cancels-heavy mobility, acrobatic launch movement, chained evasions, or spectacle-first action locomotion.

### Not A Boss Arena Movement Framework

This system does not need special boss duel locomotion rules, giant-arena chase logic, or large-scale positioning tools.

### Not A Full Strafe / Guard Blend System

M0 does not require advanced lock-on strafe polish, upper-body guard overlays, or production-grade `Avatar Mask` blending. Those may come later if needed, but they are not required to prove combat feel.

### Not Animation-Driven Gameplay Truth

M0 locomotion should not hand gameplay authority to the Animator State Machine. Animation may support movement readability, but it must not own locomotion state truth, cancel rules, or action validity.

### Not A Root-Motion Commitment

M0 does not need to decide full root-motion policy up front. Root motion remains open and must be validated against locomotion and combat readability before it is allowed to own anything important.

### Not A Full Hit-Reaction Framework

This system only needs enough movement-side response to support being hit, staggered, and returned to readable neutral. It does not need a large stagger-physics or cinematic knockback framework.

### Not A Camera Authority Layer

`Player Locomotion` should coordinate with the duel camera, but it must not be reshaped around camera spectacle or allow camera state to silently change movement truth.

### Not A Multiplayer / Network Movement Model

M0 does not need rollback-ready, replicated, predicted, or online-safe locomotion behavior.

### Not Over-Architected

M0 should not build a broad locomotion framework for every future mode before one duel feels correct. If a movement feature does not improve one readable katana duel, it should be deferred.

## 6. Core Movement Loop

The purpose of the M0 locomotion loop is to define the player’s movement rhythm inside the duel. This loop is not about broad traversal, flashy movement expression, or large-space navigation. It exists to make one katana duel readable, grounded, and emotionally controlled.

### 6.1 Core Movement Loop Overview

The M0 movement loop should support:

`orient → approach/reposition → read → evade/hold ground → recover → counter-position → reset`

This maps directly onto the combat loop:

- `orient` supports target awareness
- `approach/reposition` supports spacing
- `read` supports enemy telegraph interpretation
- `evade/hold ground` supports the dodge or parry decision
- `recover` supports action commitment and fairness
- `counter-position` supports punish and counter readability
- `reset` returns the player to readable duel control

The key principle is that locomotion should help the player interpret the duel. The player should feel that movement is part of reading and answering the enemy, not separate from it.

### 6.2 Orient Phase

The orient phase is where the player establishes readable facing and target relationship before or between committed exchanges.

In this phase:

- the player should understand current facing
- target direction should remain understandable when target focus is active
- camera-relative versus target-relative movement remains an open implementation decision
- facing support should not auto-solve combat positioning
- the player should feel grounded and deliberate

This phase should make the duel legible before threat arrives. If the player does not understand where they are facing, the rest of the loop becomes harder to trust.

### 6.3 Approach / Reposition Phase

The approach and reposition phase is where the player manages distance and angle relative to the enemy.

In this phase:

- the player can move toward, away from, or around the enemy
- movement should preserve spacing readability
- movement should not feel floaty or overly fast
- movement should support the controlled tone of a katana duel
- no advanced traversal is required

This phase is about measured footwork. The player should feel like they are choosing distance rather than skating through it.

### 6.4 Read Phase

The read phase is where movement slows into observation and controlled readiness. The player is not necessarily idle, but they should have enough locomotion control to watch the enemy and decide what to do next.

In this phase:

- movement should allow the player to observe enemy telegraph
- the player should be able to slow, hold position, or make small spacing corrections
- locomotion should not fight the camera during `EnemyTelegraph`
- player movement should not obscure enemy readability
- the phase should support decision-making before commitment

This phase matters because movement that is too slippery, too fast, or too restless will corrupt the player’s ability to read intent.

### 6.5 Evade / Hold Ground Phase

The evade or hold-ground phase is the player’s immediate physical answer to danger.

For M0:

- dodge is the main movement-based defensive response
- parry is a hold-ground and timing response rather than a movement escape
- dodge should have readable displacement
- parry should preserve facing and readability if target focus supports it
- dodge and parry success remain owned by `Combat Core`

This phase should feel clear and intentional. Dodge should look like meaningful repositioning. Parry should look like a deliberate stand rather than accidental movement noise.

### 6.6 Recover Phase

The recover phase is where movement commitment remains visible after dodge, attack, parry, counter, or hit reaction. Recovery matters because locomotion must help preserve the consequences of action.

For M0:

- after dodge, attack, parry, counter, or hit reaction, the player may enter readable recovery
- recovery creates commitment and prevents action spam
- recovery should stay short enough for M0 feel testing
- recovery state should be debug-visible
- animation recovery must not secretly own gameplay recovery

This phase is especially important for fairness. If the player can ignore every commitment through immediate movement freedom, the duel loses weight.

### 6.7 Counter-Position Phase

The counter-position phase is where the player turns a valid opening into a readable response opportunity.

For M0:

- after a valid punish or counter opportunity, player position and facing should support counter readability
- limited alignment support may be allowed later
- counter should not teleport or auto-solve spacing unless explicitly approved
- counter validity remains owned by `Combat Core`
- locomotion should make counter feel intentional and grounded

The player should feel that they reached the counter through readable spacing and timing, not through invisible auto-correction.

### 6.8 Reset Phase

The reset phase returns the player to readable locomotion control after the exchange resolves.

In this phase:

- the player should be able to reorient and prepare for the next enemy read
- movement state should reset cleanly
- camera and target-focus coordination may help preserve orientation
- reset should support the rhythm `calm → threat → answer → punish/reveal → calm`

This is where locomotion helps the duel breathe again.

### 6.9 Loop Variants

The locomotion loop should support a few simple M0 exchange variants:

- `reposition → enemy telegraph → parry hold-ground → counter → reset`
- `reposition → enemy telegraph → dodge displacement → enemy whiff → counter-position → reset`
- `approach too late → failed parry/dodge → hit reaction → recover → reset`
- `no lock-on / soft target focus → player still retains readable movement and orientation`

These variants help prove that locomotion supports both success and failure without losing clarity.

### 6.10 Relationship To Combat Core

`Player Locomotion` exposes movement-side truth. `Combat Core` owns combat validity.

The relationship should remain:

- `Player Locomotion` exposes movement state, dodge state, recovery state, and facing or alignment context if needed
- `Combat Core` validates dodge, parry, and counter success
- `Player Locomotion` does not decide hit, parry, or counter outcome
- `Player Locomotion` should respect combat action locks and recovery constraints
- `Combat Core` should not require Animator state as gameplay truth

This boundary keeps locomotion readable without allowing it to become accidental combat authority.

### 6.11 Relationship To Camera / Lock-On

`Lock-On & Combat Camera` supports orientation and readability, but it does not own movement truth.

The relationship should remain:

- camera and lock-on support orientation and readability
- locomotion may later need camera-relative or target-relative movement context
- the camera must not secretly own movement rules
- target focus may support facing but should not auto-solve positioning
- movement should remain understandable under camera framing

Locomotion and camera should cooperate without one silently replacing the other.

### 6.12 Relationship To Animator

The animator expresses locomotion visually, but does not own locomotion truth.

For M0:

- the Animator expresses locomotion and action movement visually
- the Animator State Machine does not own movement truth
- `Avatar Mask` is optional for M0
- simple full-body combat actions are preferred first
- animation events may request sync points later, but gameplay systems validate timing

This keeps the pure C# FSM and gameplay-side locomotion state authoritative from the start.

### 6.13 Debug Requirements

For M0, debug should expose:

- current locomotion state
- current movement phase
- movement input
- movement speed
- facing mode
- `target focus active?`
- `dodge active?`
- `recovery active?`
- `movement locked/restricted?`
- action causing restriction
- `player grounded?`
- last movement transition reason
- camera-relative or target-relative mode if used

This should let the team explain whether an unclear exchange came from locomotion, combat restriction, or camera readability.

### 6.14 Anti-patterns

The following should be treated as failures for M0:

- movement feeling floaty or disconnected from combat
- dodge becoming an auto-escape
- parry moving the player unintentionally
- recovery owned only by animation
- camera secretly deciding movement direction
- target focus auto-solving spacing
- counter teleporting without design approval
- Animator State Machine owning gameplay state
- `Avatar Mask` being required before M0 feel is proven
- adding advanced traversal before duel movement works

### 6.15 Open Questions

The following questions remain unresolved:

- whether M0 movement is camera-relative or target-relative during focus
- whether the player always faces the target during lock-on
- whether dodge direction is input-relative, camera-relative, or target-relative
- whether attacks allow movement during startup or recovery
- whether parry allows micro-movement or full stop
- whether counter has limited auto-alignment
- whether root motion is used for any M0 actions
- whether the locomotion state machine is pure C# only or partly `MonoBehaviour`-driven

## 7. Locomotion State Model

The purpose of the M0 locomotion state model is to make movement truth explicit for the first duel prototype. This is a gameplay-side design state model, not an animation graph and not implementation code. The pure C# FSM owns locomotion truth. The Animator State Machine only presents that truth visually.

### 7.1 LocomotionIdle

`LocomotionIdle` is the default grounded state when the player has no movement input and is not under a stronger locomotion override.

Its purpose is to:

- provide a readable grounded baseline
- support calm duel pacing
- allow the player to read enemy intent before acting

Rules for this state:

- it may transition to `LocomotionMove` when movement input exists
- it may transition to `TargetFocusMove / DuelMove` when target focus is active and movement input exists
- it may transition to `Dodge`, `CombatActionLocked`, `ParryHold / GuardMoment`, `HitReaction`, or `Disabled / ControlSuppressed` based on validated requests
- it must remain debug-visible

This is the lowest-intensity locomotion state, but it still needs clear ownership and visibility.

### 7.2 LocomotionMove

`LocomotionMove` is the basic grounded movement state when the player is moving without strict target-focus locomotion behavior.

Its purpose is to:

- support approach, retreat, and repositioning
- preserve grounded duel movement
- keep spacing readable during ordinary movement

Rules for this state:

- movement direction may be camera-relative or input-relative; the final choice remains open
- movement should preserve spacing readability
- movement should not feel floaty
- it may transition back to `LocomotionIdle` when input stops
- it may transition to `TargetFocusMove / DuelMove` when focus activates

This is the player’s general movement state outside stronger duel-orientation handling.

### 7.3 TargetFocusMove / DuelMove

`TargetFocusMove / DuelMove` is the movement state used when the player is moving with explicit duel-target awareness.

Its purpose is to:

- support spacing while oriented around the current duel target
- preserve facing readability
- help the player observe enemy telegraph while moving
- support controlled lock-on or target-focus movement

Rules for this state:

- it may be camera-relative, target-relative, or hybrid; the final decision remains open
- it should help keep enemy direction understandable
- it should not auto-solve spacing
- it should not make lock-on required for all combat actions
- it should coordinate with `Lock-On & Combat Camera`

This state exists to support readable dueling, not to impose rigid automated movement.

### 7.4 Dodge

`Dodge` is the main movement-based defensive response state.

Its purpose is to:

- create readable displacement
- express committed evasive movement
- support spacing-based defensive play

Rules for this state:

- dodge direction must remain understandable
- dodge is not an auto-escape
- `Combat Core` validates dodge success or failure
- dodge may contain startup, active, and recovery concepts if needed
- dodge may temporarily restrict normal movement
- dodge recovery must not be owned only by animation

This state should feel intentional and spatially meaningful.

### 7.5 ParryHold / GuardMoment

`ParryHold / GuardMoment` is the hold-ground defensive response state for timing-based defense.

Its purpose is to:

- support katana duel precision
- preserve readable facing during a committed timing response
- differentiate parry from movement-based escape

Rules for this state:

- parry should preserve facing and readability
- parry may restrict movement or allow very small micro-adjustment; this remains open
- `Combat Core` validates parry timing and eligibility
- locomotion does not decide parry success
- animation may present parry, but cannot own gameplay timing

This state should feel like a deliberate stand rather than a mobility action.

### 7.6 CombatActionLocked

`CombatActionLocked` is the movement-restricted state used during committed combat actions such as `light attack`, `heavy attack`, `counter`, or possibly attack recovery.

Its purpose is to:

- preserve action commitment
- enforce readable movement restrictions during combat actions
- prevent unrestricted sliding during committed attacks

Rules for this state:

- action movement restrictions should support commitment
- the player should not freely slide during committed attacks unless explicitly designed
- `Combat Core` owns action validity and combat action state
- `Player Locomotion` enforces movement restrictions requested by valid combat action context
- the Animator must not be the only source of movement lock

This state is one of the key places where locomotion and combat must cooperate without blurring authority.

### 7.7 CounterMovement / CounterPositioning

`CounterMovement / CounterPositioning` is an optional or limited locomotion state used if counter movement expression needs to be separated from more general combat action locking.

Its purpose is to:

- support readable counter alignment and movement expression
- make counter feel intentional and grounded
- preserve clear spacing expectations during the counter moment

Rules for this state:

- counter may need facing support or small alignment help
- counter must not teleport or auto-solve spacing unless explicitly approved
- `Combat Core` owns counter validity
- `Player Locomotion` owns movement expression
- whether this is a true separate state or part of `CombatActionLocked` remains open

This state is intentionally provisional because M0 may not need a distinct counter-movement layer.

### 7.8 Recovery

`Recovery` is the readable post-action locomotion state after dodge, attack, parry, counter, or other movement-interrupting responses.

Its purpose is to:

- preserve commitment after actions
- prevent immediate spam
- return the player cleanly toward baseline movement control

Rules for this state:

- recovery should prevent immediate spam and preserve commitment
- recovery should remain short enough for M0 feel testing
- recovery source should be debug-visible
- recovery may transition back to `LocomotionIdle`, `LocomotionMove`, or `TargetFocusMove / DuelMove`
- animation recovery must not secretly override gameplay recovery

This state is where movement consequences stay honest after the action itself has finished.

### 7.9 HitReaction

`HitReaction` is the locomotion response state when the player is hit, staggered, or otherwise interrupted by valid gameplay outcome.

Its purpose is to:

- make failure readable
- temporarily restrict or alter player control after a hit
- support transition back into readable recovery

Rules for this state:

- player control may be temporarily restricted
- the reaction should make failure understandable
- `Health / Damage / Hit Reaction` may later own the full reaction model
- `Player Locomotion` only needs provisional movement restriction behavior for M0
- it should transition to `Recovery` or to an appropriate baseline locomotion state afterward

This state exists to preserve readable consequence without demanding a full reaction framework yet.

### 7.10 Disabled / Dead / ControlSuppressed

`Disabled / Dead / ControlSuppressed` is the explicit state where the player cannot move because control is suppressed by defeat, debug reset, pause, or another external reason.

Its purpose is to:

- make non-playable control states explicit
- prevent hidden or ambiguous locomotion suppression
- keep M0 locomotion truth inspectable

Rules for this state:

- it is not a full death system for M0
- it exists to keep the locomotion model explicit
- it should be debug-visible
- it should not grow into a full player lifecycle framework here

This state is small but important because invisible suppression is hard to debug.

### 7.11 State Transition Overview

The normal locomotion paths for M0 should remain simple:

- `LocomotionIdle → LocomotionMove → LocomotionIdle`
- `LocomotionIdle / LocomotionMove → TargetFocusMove / DuelMove → LocomotionIdle / LocomotionMove`
- `LocomotionIdle / LocomotionMove / TargetFocusMove → Dodge → Recovery → LocomotionIdle / LocomotionMove / TargetFocusMove`
- `LocomotionIdle / LocomotionMove / TargetFocusMove → ParryHold / GuardMoment → Recovery or LocomotionIdle`
- `LocomotionIdle / LocomotionMove / TargetFocusMove → CombatActionLocked → Recovery → LocomotionIdle / LocomotionMove / TargetFocusMove`
- `any valid state → HitReaction → Recovery → LocomotionIdle`
- `any valid state → Disabled / ControlSuppressed` if control is suppressed

Important branch behavior includes:

- dodge succeeds or fails according to `Combat Core` result
- parry succeeds or fails according to `Combat Core` result
- counter request enters `CombatActionLocked` or `CounterMovement / CounterPositioning` if valid
- hit interrupts movement into `HitReaction`
- target focus activates or deactivates between `LocomotionMove` and `TargetFocusMove / DuelMove`

These transitions should be readable, explicit, and easy to inspect in debug.

### 7.12 State Authority Notes

State ownership must remain explicit:

- the pure C# FSM owns locomotion state truth
- the Animator State Machine observes locomotion and combat state and plays visuals
- `Avatar Masks` and animation layers may support visual blending, but do not define locomotion truth
- `Combat Core` owns combat action validity and result
- `Lock-On & Combat Camera` owns framing and target readability, not movement state
- `Player Locomotion` owns movement restrictions, but should respect valid `Combat Core` action locks

This authority split is one of the most important architectural constraints for the system.

### 7.13 State Priority Philosophy

The M0 priority order should remain simple and explicit:

- `Disabled / ControlSuppressed` overrides all
- `HitReaction` overrides normal movement
- `CombatActionLocked` overrides free movement
- `Dodge` and `ParryHold / GuardMoment` are explicit requested action states
- `Recovery` prevents immediate spam
- `TargetFocusMove / DuelMove` modifies movement framing and orientation, but does not override higher action locks
- `LocomotionIdle` and `LocomotionMove` are the lowest-priority baseline states

This priority order helps ensure that duel readability and commitment are not lost inside ambiguous overlapping states.

### 7.14 Debug Requirements

For M0, debug should expose:

- current locomotion state
- previous locomotion state
- time in state
- requested state
- accepted or rejected transition reason
- current movement input
- current movement speed
- facing mode
- `target focus active?`
- `movement locked/restricted?`
- restriction source
- `dodge active?`
- `parry hold active?`
- `combat action lock active?`
- `recovery active?`
- `hit reaction active?`
- grounded state
- last `Combat Core` request or result affecting locomotion
- last camera or target-focus context affecting orientation

This should allow the team to diagnose whether an unclear exchange came from locomotion truth, combat truth, or camera framing.

### 7.15 Locomotion State Table

| State | Purpose | Trigger Source | Player Control Allowed | Can Transition To | M0 Notes |
| --- | --- | --- | --- | --- | --- |
| `LocomotionIdle` | Default grounded baseline | No movement input and no stronger override | Minimal stance control, no directional movement | `LocomotionMove`, `TargetFocusMove`, `Dodge`, `ParryHold`, `CombatActionLocked`, `HitReaction`, `Disabled` | Calm duel baseline |
| `LocomotionMove` | Basic grounded movement | Movement input without stronger duel focus behavior | Normal grounded movement | `LocomotionIdle`, `TargetFocusMove`, `Dodge`, `ParryHold`, `CombatActionLocked`, `HitReaction`, `Disabled` | Supports approach/reposition |
| `TargetFocusMove / DuelMove` | Focused duel movement | Target focus active with movement input | Controlled duel movement | `LocomotionIdle`, `LocomotionMove`, `Dodge`, `ParryHold`, `CombatActionLocked`, `HitReaction`, `Disabled` | Supports readable target-oriented movement |
| `Dodge` | Main evasive displacement | Valid dodge request | Limited to dodge expression | `Recovery`, `HitReaction`, `Disabled` | Combat result still external |
| `ParryHold / GuardMoment` | Hold-ground timing response | Valid parry request | Restricted or micro-adjusted control | `Recovery`, `LocomotionIdle`, `HitReaction`, `Disabled` | Parry truth remains in `Combat Core` |
| `CombatActionLocked` | Movement-restricted combat action state | Valid combat action request | Restricted according to action | `Recovery`, `HitReaction`, `Disabled` | Supports commitment |
| `CounterMovement / CounterPositioning` | Optional counter movement expression | Valid counter request if separated | Limited, counter-specific control | `Recovery`, `HitReaction`, `Disabled` | May collapse into `CombatActionLocked` for M0 |
| `Recovery` | Post-action readable recovery | Dodge, attack, parry, counter, or hit aftermath | Limited or gradually returning control | `LocomotionIdle`, `LocomotionMove`, `TargetFocusMove`, `Disabled` | Must stay debug-visible |
| `HitReaction` | Movement-side failure response | Valid hit or interruption result | Temporarily restricted control | `Recovery`, `LocomotionIdle`, `Disabled` | Provisional M0 reaction handling |
| `Disabled / ControlSuppressed` | Explicit no-control state | Defeat, pause, debug reset, external suppression | No locomotion control | prior baseline state or external exit path | Small but important explicit state |

### 7.16 Anti-patterns

The following should be treated as failures for M0:

- the Animator State Machine owning locomotion truth
- dodge implemented only as animation with no gameplay state
- attack movement lock hidden inside animation clips
- camera state directly forcing locomotion state
- target focus overriding all player movement
- hit reaction skipping clear recovery
- counter movement teleporting without design approval
- recovery duration existing only in animation
- too many locomotion states before M0 needs them
- full traversal state machine logic leaking into the duel prototype

### 7.17 Open Questions

The following questions remain unresolved:

- whether `TargetFocusMove / DuelMove` is a separate state or a modifier over `LocomotionMove`
- whether `CounterMovement / CounterPositioning` is a separate state or part of `CombatActionLocked`
- whether `ParryHold / GuardMoment` allows micro-movement
- whether `Dodge` has startup, active, and recovery sub-states or a single state with timing data
- whether `Recovery` is generic or action-specific
- whether `HitReaction` remains here or moves under a fuller `Health / Damage / Hit Reaction` design later
- whether the movement state machine is pure C# only or coordinated with a `MonoBehaviour` adapter
- whether root motion affects any M0 locomotion state

## 8. Movement Input / Facing Rules

The purpose of this section is to define how player movement input, facing, orientation, target focus, and dodge direction should work for the M0 duel prototype. `Player Locomotion` owns movement input interpretation and facing support. `Combat Core` owns action validity and combat result. `Lock-On & Combat Camera` owns framing and target readability. The Animator remains presentation only.

### 8.1 Movement Input Purpose

Movement input should allow the player to:

- approach the enemy
- retreat from danger
- reposition around the enemy
- maintain readable spacing
- prepare dodge, parry, and counter responses
- feel grounded and deliberate

Movement input should not:

- auto-solve spacing
- override combat commitment
- bypass recovery
- make dodge, parry, or counter automatically valid
- depend on the Animator State Machine as truth

The player should feel that movement is a readable tool for positioning and response, not an invisible assist system.

### 8.2 M0 Input Interpretation Options

For M0, three conceptual input-interpretation options are acceptable:

#### Camera-Relative Movement

In `Camera-Relative Movement`:

- movement input maps relative to camera direction
- general third-person movement often feels more natural
- the main risk is that, during target focus, enemy orientation may become less consistent

#### Target-Relative Movement

In `Target-Relative Movement`:

- movement input maps relative to the current target
- duel strafing and spacing may become easier to read
- the main risk is that the movement can feel rigid or over-locked too early

#### Hybrid Movement

In `Hybrid Movement`:

- general movement is camera-relative
- focused duel movement may bias toward target-relative behavior
- the main risk is additional complexity before the first duel is proven

#### Recommended M0 Direction

For M0:

- the final decision should remain open until camera and locomotion feel are tested together
- the implementation should start simple
- readability and player comfort should matter more than system purity

### 8.3 Facing Rules

Facing should remain understandable at all times.

For M0:

- in free movement, facing may follow movement or input direction
- in target focus, facing may bias toward the enemy
- during combat actions, facing may be constrained or lightly corrected
- any facing correction must remain small, readable, and debug-visible
- facing support must not make attacks auto-hit or parries auto-succeed

The player should understand where they are facing and why, even when combat and target focus are influencing movement.

### 8.4 Target Focus Facing

When target focus or lock-on is active:

- the player should understand enemy direction clearly
- movement should still allow circling, retreating, or approaching
- facing may remain biased toward the target
- target focus should not remove spacing discipline
- target focus should not prevent intentional retreat or repositioning
- target focus should coordinate with `Lock-On & Combat Camera`

Target focus should support duel orientation, not trap the player into automated positioning.

### 8.5 Attack Facing Support

For `light attack` and `heavy attack`:

- attacks may use current facing at action start
- small facing correction may be allowed if it improves readability
- attack movement and facing should support commitment
- `Combat Core` owns attack validity and hit result
- attack-facing support must not force all attacks to connect
- attack-facing behavior should be debug-visible if adjusted

Attack-facing support should improve clarity, not secretly erase spacing mistakes.

### 8.6 Parry Facing Support

For parry:

- parry should preserve readable facing toward the threat when possible
- parry may require facing the attack direction or target; the final rule remains open
- target focus may help parry orientation
- `Combat Core` validates parry timing, eligibility, and result
- locomotion and camera must not make parry succeed automatically

Parry should feel like a deliberate hold-ground answer, not a camera-assisted auto-correct.

### 8.7 Dodge Direction Rules

Several dodge-direction interpretations are acceptable conceptually:

- input-relative dodge
- camera-relative dodge
- target-relative dodge
- backward or side-step focused dodge during lock-on
- neutral or backstep dodge if no input exists

For M0:

- dodge direction must remain readable
- dodge must not become an auto-evade
- dodge should preserve player agency
- dodge should expose clear displacement for camera and gameplay readability
- the final direction model should remain open until feel testing

The player should be able to tell where they dodged and why that mattered.

### 8.8 Counter Facing / Alignment

For counter:

- counter may require target or facing support to look intentional
- counter should not teleport unless explicitly approved later
- limited alignment may be allowed if it remains small and readable
- counter validity remains owned by `Combat Core`
- whether target focus is required for counter readability remains open

The counter should feel intentional and earned, not auto-corrected into success.

### 8.9 Movement Restrictions During Combat

During combat:

- committed combat actions may restrict movement
- recovery may restrict or reduce movement
- dodge temporarily overrides normal movement
- hit reaction suppresses movement temporarily
- parry may stop or reduce movement
- movement restrictions should come from explicit locomotion or combat state, not from animation alone

This keeps movement commitment readable and debuggable instead of burying it inside clips or blend trees.

### 8.10 Relationship To Camera / Lock-On

The camera and lock-on layer may support orientation, but it does not own movement truth.

The relationship should remain:

- camera framing and target focus may provide orientation context
- the camera must not secretly decide movement rules
- camera-relative movement requires stable camera readability
- target-relative movement requires clear target-focus readability
- `Player Locomotion` and `Lock-On & Combat Camera` must agree on movement mode during focus

Movement and camera should feel coordinated without the camera silently driving locomotion.

### 8.11 Relationship To Combat Core

The relationship to `Combat Core` should remain explicit:

- `Player Locomotion` exposes facing, movement, dodge, and restriction context if needed
- `Combat Core` validates action success or failure
- `Player Locomotion` must respect action locks and recovery constraints
- `Combat Core` should not depend on Animator State Machine truth for movement decisions
- movement and facing support must not override `Combat Core` results

Locomotion helps express action context, but combat truth stays upstream.

### 8.12 Debug Requirements

For M0, debug should expose:

- movement input vector
- interpreted movement direction
- current movement mode
- current facing mode
- player facing direction
- target direction
- `target focus active?`
- `facing correction active?`
- facing correction amount or reason if useful
- dodge direction mode
- last dodge direction
- `movement restricted?`
- restriction source
- `combat action lock active?`
- `recovery active?`
- camera-relative or target-relative mode

This should let the team explain whether a movement or facing problem came from locomotion interpretation, combat restrictions, or camera coordination.

### 8.13 Movement / Facing Table

| Area | M0 Rule | Allowed Support | Must Not Do | Open Decision |
| --- | --- | --- | --- | --- |
| `Free movement` | Support approach, retreat, and repositioning with grounded control | Camera-relative or input-relative interpretation | Must not feel floaty or ambiguous | Final free-move interpretation |
| `Target focus movement` | Preserve duel orientation while allowing spacing control | Target bias, circling, retreat, approach | Must not auto-solve spacing | Camera-relative vs target-relative vs hybrid |
| `Facing` | Keep facing understandable and readable | Small visible facing support | Must not secretly determine combat success | Bias strength and mode |
| `Light / Heavy attack` | Preserve commitment and readable attack facing | Small facing correction if needed | Must not force all hits to connect | Whether attack correction is allowed |
| `Parry` | Preserve readable hold-ground orientation | Target-focus-assisted facing if needed | Must not auto-succeed because of facing support | Whether directional facing is required |
| `Dodge` | Provide readable displacement and agency | Input-, camera-, or target-relative dodge | Must not become auto-evade | Final dodge direction model |
| `Counter` | Keep counter alignment readable and intentional | Small alignment support if approved | Must not teleport or auto-solve range | Whether limited auto-alignment exists |
| `Recovery` | Preserve commitment after action | Reduced movement or locked movement by explicit state | Must not be bypassed by input spam | Generic vs action-specific recovery |
| `Hit Reaction` | Temporarily suppress movement after failure | Explicit control suppression | Must not be hidden only in animation | Exact restriction depth |
| `Camera coordination` | Keep movement understandable under camera framing | Shared orientation context with camera | Must not let camera secretly decide movement | Final coordination mode during focus |

### 8.14 Anti-patterns

The following should be treated as failures for M0:

- movement mode changing invisibly
- the camera secretly deciding dodge direction
- target focus auto-solving spacing
- attack-facing correction forcing hits
- parry success depending on camera angle rather than `Combat Core` rules
- dodge direction feeling random
- counter snapping or teleporting without approval
- movement restriction hidden only in animation
- recovery bypassed through movement input
- lock-on being required for all combat actions without explicit decision

### 8.15 Open Questions

The following questions remain unresolved:

- whether M0 movement is camera-relative, target-relative, or hybrid
- whether target focus biases facing or fully locks facing
- whether attacks allow facing correction
- whether parry requires directional facing
- whether dodge direction is input-relative, camera-relative, target-relative, or backstep/side-step focused
- whether counter has limited auto-alignment
- whether movement restrictions are generic or per-action authored
- whether facing-support values should be data-authored later

## 9. Dodge / Evade Rules

The purpose of this section is to define the single readable dodge or evade action used in the M0 duel prototype. `Player Locomotion` owns dodge movement expression, displacement, movement restriction, recovery, and locomotion debug truth. `Combat Core` owns dodge success or failure validation, hit result, `CounterWindow`, and reveal request context. `Enemy Intent & Telegraph` owns attack timing, active windows, recovery, and punish truth. `Lock-On & Combat Camera` owns dodge readability and framing.

### 9.1 Dodge Purpose

Dodge should:

- be the main movement-based defensive answer
- help the player evade enemy active threat through timing and spacing
- create readable displacement
- support whiff and punish readability
- feel grounded, deliberate, and elegant
- support the loop `read → evade/parry → counter → reveal`

Dodge should not:

- be an automatic escape
- ignore enemy timing
- ignore spacing
- bypass all commitment or recovery
- replace parry
- become a spam movement tool

The player should feel that dodge is an intentional evasive answer rather than a universal panic button.

### 9.2 M0 Dodge Scope

For M0, dodge remains intentionally small:

- one basic dodge or evade action
- no advanced dodge chain
- no air dodge
- no perfect dodge system unless explicitly added later
- no slow-motion dodge reward yet
- no stamina or resource cost unless added later
- no invincible dash fantasy
- no animation-heavy evasive combo system

The first prototype only needs one readable defensive movement answer.

### 9.3 Dodge Input Rules

For M0:

- dodge is triggered by explicit player input
- dodge direction may depend on movement input, camera direction, or target-focus mode
- neutral dodge or backstep remains an open option
- dodge input should be ignored or rejected during invalid states
- rejected dodge should be debug-visible with a reason
- dodge input should not cancel every committed action unless explicitly allowed

This keeps dodge as a clear player choice rather than a silent always-available escape.

### 9.4 Dodge Direction Rules

Several conceptual direction models are acceptable for M0:

- input-relative dodge
- camera-relative dodge
- target-relative side-step or backstep dodge
- neutral or backstep dodge when no input exists

For M0:

- direction must remain readable
- direction should preserve player agency
- direction should coordinate with camera and target focus
- direction should not feel random
- the final model remains open until locomotion and camera playtesting

The player should be able to explain where they dodged and why that was the right or wrong answer.

### 9.5 Dodge Timing / Window Concepts

For M0, dodge should have three conceptual movement phases:

- dodge startup
- dodge movement or evade phase
- dodge recovery

The ownership split should remain explicit:

- `Player Locomotion` owns the movement phases
- `Combat Core` validates whether the dodge actually avoids an enemy attack
- dodge avoidability may depend on timing, spacing, and enemy attack data
- exact timing values are deferred to tuning
- timing should be debug-visible

This helps keep dodge expressive without making locomotion the owner of combat success.

### 9.6 Dodge Vulnerability / Avoidance Rules

For M0:

- dodge may contain an avoidance or evade phase if `Combat Core` supports it
- dodge should not be fully safe for its entire duration unless that is explicitly approved
- failed dodge should remain explainable
- late dodge, wrong direction, or bad spacing may fail
- dodge success should feel earned by reading the enemy

The important rule is that dodge should feel like a deliberate answer to a readable threat, not an invincible movement trick.

### 9.7 Dodge Recovery Rules

After dodge:

- dodge should have readable recovery
- recovery should prevent dodge spam
- recovery should stay short enough for M0 feel testing
- recovery may transition to `LocomotionIdle`, `LocomotionMove`, `TargetFocusMove / DuelMove`, or valid combat action if allowed
- recovery must not be hidden only in animation
- recovery duration and source should be debug-visible

Dodge recovery is one of the main tools that keeps dodge meaningful without letting it dominate the duel.

### 9.8 Dodge And Punish / Counter Relationship

The relationship between dodge and counter should remain explicit:

- successful dodge may cause enemy whiff if `Enemy Intent & Telegraph` supports it
- enemy whiff or recovery may expose `EnemyPunishWindow`
- `Combat Core` decides whether `CounterWindow` opens
- dodge alone should not automatically guarantee counter
- counter opportunity should depend on enemy state, spacing, timing, and `Combat Core` validation
- the camera should preserve whiff and recovery visibility

This keeps dodge connected to the reward loop without turning it into automatic counter generation.

### 9.9 Dodge And Parry Relationship

Dodge and parry must remain different defensive answers.

For M0:

- dodge is the movement and spacing answer
- parry is the timing and hold-ground answer
- both should remain meaningful
- dodge should not make parry obsolete
- parry should not replace all dodge use cases

If both answers feel the same in practice, the duel loses important expressive clarity.

### 9.10 Dodge And Combat Actions

For M0:

- dodge may be available from `LocomotionIdle`, `LocomotionMove`, and `TargetFocusMove / DuelMove`
- dodge may be restricted during committed attack, counter, hit reaction, or recovery states
- dodge cancel rules should remain conservative
- if dodge cancel is allowed later, it must be explicit and debug-visible
- dodge must not bypass `Combat Core` action commitment rules

This preserves the weight of committed actions while still allowing dodge to be a meaningful defensive tool.

### 9.11 Dodge And Camera / Target Focus

The relationship to the camera should remain:

- the camera should keep dodge displacement readable
- target focus may help preserve enemy orientation
- the camera should not rotate so much that dodge direction becomes unclear
- the camera does not decide dodge success
- target focus does not make dodge automatically safe

Dodge should remain a movement answer validated by gameplay truth, not a camera-assisted auto-avoid.

### 9.12 Dodge And Animator

The relationship to animation should remain explicit:

- the Animator plays the dodge visual
- the Animator State Machine does not own dodge truth
- dodge movement may be code-driven, root-motion-driven, or hybrid; the final choice remains open
- if root motion is used, `Player Locomotion` and `Combat Core` timing still validate gameplay rules
- animation events may request sync later, but cannot decide avoid success

This keeps dodge gameplay readable even if animation implementation changes later.

### 9.13 Debug Requirements

For M0, debug should expose:

- `dodge requested?`
- `dodge accepted/rejected?`
- rejection reason
- dodge direction
- dodge direction mode
- dodge phase: `startup / evade / recovery`
- dodge elapsed time
- `dodge movement locked?`
- `avoidance/evade active?`
- last enemy attack checked against dodge
- `Combat Core` dodge result
- `recovery active?`
- transition-out-of-dodge reason

This should make it possible to explain whether a failed or successful dodge came from movement expression, combat timing, or enemy timing.

### 9.14 Dodge Rules Table

| Dodge Area | M0 Rule | Owner | Must Not Do | Open Decision |
| --- | --- | --- | --- | --- |
| `Input` | Dodge comes from explicit player input and may be rejected in invalid states | `Player Locomotion` + `Combat Core` context | Must not silently override every other action | Exact valid-state set |
| `Direction` | Dodge direction must remain readable and player-driven | `Player Locomotion` | Must not feel random or auto-corrected by camera | Input/camera/target-relative model |
| `Startup` | Dodge has a readable start before full evade motion | `Player Locomotion` movement phase | Must not hide timing in animation only | Phase separation detail |
| `Evade Phase` | Dodge movement or avoidance is the main evasive expression | `Player Locomotion` movement phase, `Combat Core` validates success | Must not be universally safe | Whether avoidance exists and how |
| `Recovery` | Dodge ends in readable short recovery | `Player Locomotion` | Must not allow spam or be animation-only | Fixed vs authored recovery |
| `Vulnerability` | Dodge may fail on bad timing or spacing | `Combat Core` result, locomotion expresses phases | Must not become full invulnerability by default | Vulnerability model |
| `Punish / Counter` | Dodge may lead to enemy whiff and possible punish | `Enemy Intent & Telegraph` + `Combat Core` | Must not guarantee counter automatically | Counter opening source |
| `Camera Support` | Camera preserves displacement and enemy relation | `Lock-On & Combat Camera` | Must not decide success or direction | Framing behavior during dodge |
| `Animator Support` | Animator presents dodge visually | Animator presentation only | Must not own dodge truth or success | Root motion usage |
| `Debug` | Dodge phases, direction, result, and rejection must be visible | `Player Locomotion` debug truth | Must not leave dodge failures unexplained | Exact debug verbosity |

### 9.15 Anti-patterns

The following should be treated as failures for M0:

- dodge becoming full invincibility with no timing
- dodge canceling every action
- dodge direction changing invisibly
- the camera deciding dodge direction
- target focus making dodge automatically safe
- recovery existing only in animation
- root motion deciding dodge success
- `Combat Core` relying on Animator state to validate dodge
- dodge guaranteeing counter automatically
- adding perfect dodge or slow motion before the basic dodge works

### 9.16 Open Questions

The following questions remain unresolved:

- whether dodge is input-relative, camera-relative, target-relative, or backstep/side-step focused
- whether dodge has invulnerability, avoidance, or only displacement
- whether dodge has startup, evade, and recovery sub-states or simple phase data
- whether dodge can cancel `light attack` or `heavy attack` recovery in M0
- whether successful dodge can open `CounterWindow` directly or only through enemy whiff or punish state
- whether root motion is used for dodge
- whether perfect dodge is deferred completely
- whether dodge recovery duration is fixed or authored data

## 10. Grounding / Movement Restriction Rules

The purpose of this section is to define the grounding assumptions and movement-restriction rules that keep the M0 duel readable, grounded, and fair. `Player Locomotion` owns grounded movement state, movement restrictions, action movement locks, dodge movement restrictions, recovery movement restrictions, and locomotion debug truth. `Combat Core` owns combat action validity and result. The Animator remains presentation only.

### 10.1 Grounding Purpose

Grounding rules should ensure:

- the player feels physically grounded
- movement supports precise duel readability
- dodge, parry, attack, counter, and recovery have understandable commitment
- movement does not feel floaty
- M0 avoids unnecessary traversal complexity

Grounding should not:

- become a full traversal system
- depend on final animation quality
- be controlled only by the Animator
- allow movement to bypass combat commitment
- hide spacing mistakes

The player should feel anchored to the duel space, not detached from it.

### 10.2 M0 Grounding Assumptions

For M0:

- the player is primarily grounded
- no jump is required
- no air control is required
- no climbing, vaulting, or swimming is required
- no parkour is required
- no ledge traversal is required
- one flat or mostly flat duel space is acceptable
- verticality is deferred unless the prototype space specifically requires it

Grounding should also remain:

- explicit and debug-visible
- simple enough for M0
- free to defer complex ground detection unless it becomes a real blocker to prototype feel

This keeps locomotion focused on duel readability rather than environmental traversal.

### 10.3 Basic Movement Restrictions

The baseline rule for M0 is:

- normal movement is allowed in `LocomotionIdle`, `LocomotionMove`, and `TargetFocusMove / DuelMove`
- movement may be reduced or locked during `Dodge`, `ParryHold / GuardMoment`, `CombatActionLocked`, `Recovery`, `HitReaction`, and `Disabled / ControlSuppressed`
- movement restrictions should always have a clear source and reason
- movement restrictions should be temporary and readable
- movement restrictions should not feel like unexplained input loss

The player should be able to tell that control changed because of a readable gameplay state, not because the system stopped listening.

### 10.4 Combat Action Movement Restrictions

During `light attack`, `heavy attack`, `counter`, or other committed combat actions:

- movement may be limited or fully locked
- facing may be constrained
- action commitment should remain readable
- movement restriction should support fairness and prevent spam
- restriction must come from explicit locomotion or combat state, not from animation clip length alone
- `Combat Core` owns whether the action is valid
- `Player Locomotion` owns the movement response to valid action context

These restrictions are part of how the duel preserves meaningful choice instead of letting movement erase every commitment.

### 10.5 Dodge Movement Restrictions

During `Dodge`:

- normal movement is temporarily overridden
- dodge direction should stay readable
- the player should not freely steer dodge unless that is explicitly approved later
- dodge recovery may restrict movement briefly
- dodge should not cancel every other restriction by default
- dodge restriction should be debug-visible

Dodge should feel like a committed evasive action, not an unrestricted steering mode.

### 10.6 Parry Movement Restrictions

During `ParryHold / GuardMoment`:

- the player may hold ground completely or be allowed a very small micro-adjustment; the final decision remains open
- parry should preserve readable facing toward the threat
- parry should not slide the player unintentionally
- parry movement restriction must not determine parry success
- `Combat Core` validates timing and eligibility

Parry should read as a timing answer, not as accidental locomotion drift.

### 10.7 Recovery Movement Restrictions

During `Recovery`:

- movement may be locked, reduced, or delayed depending on recovery source
- recovery prevents immediate action and movement spam
- recovery should remain readable and short enough for M0 feel testing
- recovery source should be debug-visible
- animation recovery must not secretly extend or shorten gameplay recovery

This is one of the most important anti-slop rules in the whole locomotion system.

### 10.8 Hit Reaction Movement Restrictions

During `HitReaction`:

- player control may be suppressed briefly
- knockback, stagger, or pause behavior remains provisional
- failure should remain readable
- a full hit-reaction framework is deferred
- movement should return through `Recovery` or directly to `LocomotionIdle / LocomotionMove` depending on M0 tuning

This keeps failure visible and meaningful without overbuilding the reaction system.

### 10.9 Disabled / Control Suppression

`Disabled / ControlSuppressed` should:

- prevent normal movement
- be used for defeat, pause, debug reset, or explicit external testing control
- remain a small explicit state rather than a full death or lifecycle framework
- remain debug-visible
- never become a hidden catch-all for unclear state bugs

If this state is overused, the locomotion model has likely become unclear elsewhere.

### 10.10 Movement Restriction Priority

For M0, the priority direction should be:

1. `Disabled / ControlSuppressed` overrides all movement
2. `HitReaction` overrides normal movement and most actions
3. `CombatActionLocked` controls committed action movement
4. `Dodge` temporarily overrides normal movement
5. `ParryHold / GuardMoment` restricts or stabilizes movement
6. `Recovery` restricts return to full control
7. `TargetFocusMove / DuelMove` modifies movement orientation only
8. `LocomotionIdle / LocomotionMove` are baseline states

This priority may later be refined in architecture, but M0 needs explicit rules so movement never feels random or contradictory.

### 10.11 Relationship To Combat Core

The relationship to `Combat Core` should remain:

- `Combat Core` may request or expose action-lock and recovery context
- `Player Locomotion` applies movement restrictions from valid combat context
- `Player Locomotion` does not decide combat result
- movement restriction does not make attacks hit or parries succeed
- `Combat Core` should not use Animator state as movement truth

This keeps movement restrictions expressive without making them authoritative over combat outcome.

### 10.12 Relationship To Animator / Root Motion

The relationship to animation should remain explicit:

- the Animator expresses movement restrictions visually
- the Animator State Machine does not own restriction truth
- root motion remains an open decision
- if root motion is used, it must be coordinated with `Player Locomotion` and `Combat Core`
- root motion must not secretly decide hit, dodge, parry, counter, or recovery validity
- `Avatar Mask` is optional for M0 and not required to pass movement restriction criteria

The core rule is simple: gameplay-side movement restriction must exist even if animation presentation changes later.

### 10.13 Debug Requirements

For M0, debug should expose:

- `grounded?`
- current locomotion state
- `movement allowed?`
- `movement restricted?`
- restriction source
- restriction priority
- `movement input received?`
- `movement input applied?`
- movement speed multiplier if used
- `action lock active?`
- `dodge override active?`
- `parry restriction active?`
- `recovery active?`
- `hit reaction control suppression active?`
- `disabled/control suppressed?`
- last restriction start or end reason

This should make movement restriction behavior explainable during both success and failure cases.

### 10.14 Movement Restriction Table

| State / Context | Movement Allowed? | Facing Allowed? | Restriction Source | Why It Matters | M0 Notes |
| --- | --- | --- | --- | --- | --- |
| `Idle` | Yes | Yes | Baseline locomotion state | Supports calm duel readability | Default grounded baseline |
| `Move` | Yes | Yes | Baseline locomotion state | Supports approach and repositioning | Must preserve spacing readability |
| `TargetFocusMove / DuelMove` | Yes | Biased or supported | Target-focus locomotion mode | Supports readable orientation | Must not auto-solve spacing |
| `Dodge Startup` | Limited or committed | Limited | Explicit dodge state | Preserves readable dodge commitment | Direction must remain understandable |
| `Dodge Movement / Evade Phase` | Overridden by dodge path | Limited | Explicit dodge state | Keeps evasive displacement readable | Not freely steerable by default |
| `Dodge Recovery` | Reduced or delayed | Limited or returning | Dodge recovery state | Prevents instant spam after dodge | Must be gameplay-visible |
| `ParryHold / GuardMoment` | Reduced or stopped | Preserved toward threat | Explicit parry state | Supports hold-ground timing response | Micro-movement remains open |
| `Light Attack` | Reduced or locked | Constrained if needed | Valid combat action lock | Preserves action commitment | Must not be animation-only |
| `Heavy Attack` | Reduced or locked | Constrained if needed | Valid combat action lock | Makes heavier action more committed | Should feel punishable |
| `Counter` | Reduced or locked, possibly aligned | Constrained if needed | Valid combat action lock or counter state | Preserves readable reward action | Must not teleport by default |
| `Recovery` | Reduced, delayed, or locked | Limited or returning | Recovery state | Preserves commitment and fairness | Source must be debug-visible |
| `HitReaction` | Temporarily suppressed | Limited | Valid hit-reaction context | Makes failure readable | Full system deferred |
| `Disabled / ControlSuppressed` | No | No or irrelevant | Explicit suppression state | Makes no-control states unambiguous | Must not become catch-all bug state |

### 10.15 Failure Conditions

Grounding and movement restriction fail if:

- the player feels floaty or disconnected from the duel space
- movement bypasses attack, dodge, or parry recovery
- the player slides during committed actions without design reason
- movement locks feel random or unexplained
- Animator clip length secretly defines gameplay recovery
- dodge cancels every restriction by accident
- camera or lock-on silently changes movement restriction
- root motion changes gameplay outcome invisibly
- debug cannot explain why movement was blocked or allowed

These are not just polish issues. They directly affect combat fairness and readability.

### 10.16 Anti-patterns

The following should be treated as failures for M0:

- full traversal complexity before grounded duel movement works
- movement restriction hidden only in animation
- root motion owning gameplay truth
- recovery bypassed by movement input
- dodge overriding all restrictions without explicit rule
- parry sliding the player unintentionally
- hit reaction skipping recovery without reason
- `Disabled / ControlSuppressed` used as a catch-all bug state
- camera state directly locking player movement
- movement locks not visible in debug

### 10.17 Open Questions

The following questions remain unresolved:

- whether M0 needs real grounded detection or a simple grounded assumption
- whether attacks fully lock movement or allow reduced movement
- whether parry fully stops movement or allows micro-adjustment
- whether dodge can be steered after start
- whether recovery restriction is generic or per-action
- whether hit reaction includes knockback in M0
- whether root motion is used for dodge, attacks, or counter
- whether movement speed modifiers become authored data later

## 11. Combat Action Movement Support

The purpose of this section is to define how `Player Locomotion` supports combat actions through movement, facing, restriction, recovery, and readability. `Combat Core` owns light, heavy, parry, dodge, and counter validity, along with hit result, `CounterWindow`, and reveal request context. `Player Locomotion` owns movement expression and movement restrictions caused by valid combat action context.

### 11.1 Combat Movement Support Purpose

Combat action movement support should:

- make attacks feel grounded and committed
- keep dodge, parry, and counter readable
- preserve spacing discipline
- make successful counter feel intentional
- prevent action spam through readable movement and recovery limits
- support the loop `read → evade/parry → counter → reveal`

It should not:

- decide whether actions are valid
- make attacks auto-hit
- make parry auto-succeed
- make dodge auto-evade
- open `CounterWindow`
- validate reveal
- depend on the Animator as truth

The goal is to make valid combat actions physically readable without turning locomotion into combat authority.

### 11.2 Light Attack Movement Support

For `light attack`:

- the action should feel quick, but not weightless
- player movement may be limited during startup, active, or recovery
- small facing support may be allowed if it remains readable
- light attack should not slide freely through the enemy unless explicitly designed
- `Combat Core` owns hit result
- movement support should not make light-attack spam dominant

Light attack should feel responsive while still carrying enough commitment to matter.

### 11.3 Heavy Attack Movement Support

For `heavy attack`:

- the action should feel more committed than `light attack`
- movement should be more restricted than `light attack`
- facing correction, if any, should be limited and readable
- heavy attack should expose risk through commitment and recovery
- heavy attack must not become a homing attack
- `Combat Core` owns hit result

Heavy attack locomotion support should communicate risk, weight, and intention.

### 11.4 Parry Movement Support

For `parry`:

- parry is primarily a hold-ground and timing action
- movement may be stopped or heavily reduced during parry
- target-facing support may help readability
- parry should not slide the player into success
- `Combat Core` validates timing and attack eligibility
- parry movement support should make success and failure visually explainable

Parry should look like a deliberate stand, not like accidental locomotion drift.

### 11.5 Dodge Movement Support

For `dodge`:

- dodge temporarily overrides normal movement
- dodge displacement should remain readable
- dodge direction should follow the selected M0 direction model
- dodge recovery should prevent spam
- dodge should not cancel all combat restrictions unless explicitly allowed
- `Combat Core` validates whether dodge avoids an attack

Dodge remains the primary movement-based defense, but its success still depends on gameplay truth rather than locomotion alone.

### 11.6 Counter Movement Support

For `counter`:

- counter may need limited facing or alignment support
- counter movement should look intentional and grounded
- counter must not teleport or snap unfairly unless explicitly approved later
- counter may restrict movement during execution
- `Combat Core` owns counter validity and result
- the camera should preserve counter alignment and impact readability

Counter should feel earned through readable positioning rather than through invisible correction.

### 11.7 Hit Reaction Movement Support

For `hit reaction`:

- movement may be suppressed or reduced temporarily
- the reaction should make failure readable
- knockback or stagger remains provisional
- a full hit-reaction system is deferred
- locomotion should expose the movement restriction reason
- the recovery path should remain readable

This gives failure a visible physical consequence without expanding into a full reaction framework.

### 11.8 Combat Recovery Movement Support

For recovery after attack, dodge, parry, counter, or hit reaction:

- recovery may restrict movement
- recovery should be explicit and debug-visible
- recovery should prevent spam and preserve commitment
- recovery should be tuned for feel rather than final balance
- recovery must not be defined only by animation clip length

Recovery is one of the main tools that keeps the duel honest and readable.

### 11.9 Facing / Alignment Support During Combat

During combat actions:

- actions may use current facing at action start
- target focus may provide orientation context
- limited facing correction may be allowed for readability
- correction must remain small, explainable, and debug-visible
- facing support must not override `Combat Core` hit, parry, or counter validation
- counter alignment remains an open decision

Facing support should make the action legible, not make it successful by itself.

### 11.10 Combat Action Movement Priority

For M0, the movement-support priority direction should be:

1. `HitReaction / Disabled` overrides combat movement
2. valid `counter` execution overrides normal movement if active
3. `dodge` overrides normal movement during the dodge phase
4. `ParryHold / GuardMoment` stabilizes or restricts movement
5. `heavy attack` restricts movement more strongly
6. `light attack` restricts movement moderately
7. `Recovery` restricts return to full movement
8. `TargetFocusMove / DuelMove` only modifies orientation or movement style

The exact priority can be refined later, but M0 needs clear source and reason for every restriction so movement never feels random.

### 11.11 Relationship To Combat Core

The relationship to `Combat Core` should remain:

- `Combat Core` sends or exposes valid combat action context
- `Player Locomotion` applies movement restrictions and facing support based on that context
- `Player Locomotion` does not decide hit, parry, dodge, or counter success
- movement support must not create combat results
- `Combat Core` should not rely on Animator state as gameplay truth

This keeps locomotion as the movement-expression layer for combat rather than a second combat brain.

### 11.12 Relationship To Camera / Lock-On

The relationship to `Lock-On & Combat Camera` should remain:

- camera and lock-on support visibility and orientation
- target focus may influence facing support, but not validity
- camera state must not directly force combat movement states
- the camera must preserve readability of movement restrictions, dodge displacement, counter alignment, and recovery
- movement should remain understandable under focus mode

The camera helps the player read combat movement, but it does not own it.

### 11.13 Relationship To Animator / Avatar Mask / Root Motion

The relationship to presentation should remain explicit:

- the Animator presents action movement visually
- `Avatar Mask` and animation layers are optional presentation tools
- M0 should prefer full-body combat actions first unless readability later demands more blending
- root motion remains open
- if root motion is used, gameplay timing and movement restrictions still come from `Player Locomotion` and `Combat Core` contracts
- animation events may request sync later, but cannot own movement locks or combat results

This keeps gameplay truth stable even if the visual presentation evolves later.

### 11.14 Debug Requirements

For M0, debug should expose:

- current combat-related locomotion state
- current combat action context
- `movement restricted?`
- restriction source
- restriction priority
- `facing support active?`
- facing correction amount or reason if useful
- `dodge movement override active?`
- `parry movement restriction active?`
- `attack movement restriction active?`
- `counter alignment active?`
- `recovery active?`
- `hit reaction suppression active?`
- last `Combat Core` action or result affecting movement
- last Animator or requested visual state if useful for comparison

This should make combat-related movement behavior explainable during playtests and tuning.

### 11.15 Combat Movement Support Table

| Combat Action | Movement Support | Facing / Alignment Support | Restriction Level | Owner Of Validity | M0 Notes |
| --- | --- | --- | --- | --- | --- |
| `Light Attack` | Quick committed movement with moderate restriction | Small readable support if needed | `Reduced` | `Combat Core` | Must not slide freely while hitting |
| `Heavy Attack` | Stronger commitment with clearer movement lock or reduction | Limited readable correction only | `Locked` | `Combat Core` | Must not become homing |
| `Parry` | Hold-ground or near-stationary response | Threat-facing support if needed | `Locked` | `Combat Core` | Must not drift into success |
| `Dodge` | Temporary movement override with readable displacement | Direction follows selected dodge model | `Override` | `Combat Core` | Main movement-based defense |
| `Counter` | Committed response with optional limited alignment | Small readable support if approved | `Locked` | `Combat Core` | Must not teleport by default |
| `Hit Reaction` | Movement suppressed or reduced after valid failure | Limited or none | `Provisional` | upstream reaction/result context | Full reaction system deferred |
| `Recovery` | Restricted return to full control | Returning or constrained facing | `Reduced` | context from valid action/result | Must remain debug-visible |
| `Target Focus Movement` | Orientation-aware duel movement | Bias toward readable target relationship | `None` | not a validity owner | Only affects movement style/orientation |
| `Reveal Support / Post-Counter Reset` | Return to readable control after reveal-capable success | May preserve orientation through reset | `Provisional` | reveal context owned elsewhere | Must not become cutscene locomotion |

### 11.16 Failure Conditions

Combat action movement support fails if:

- attacks feel weightless or slide unnaturally
- `heavy attack` has no commitment
- parry moves the player into success unintentionally
- dodge becomes auto-escape
- counter teleports or snaps without approval
- recovery can be bypassed by movement input
- animation clip length secretly controls gameplay recovery
- camera or target focus decides action validity
- debug cannot explain why movement was restricted
- movement support makes `Combat Core` outcomes feel false

These failures damage both feel and trust.

### 11.17 Anti-patterns

The following should be treated as failures for M0:

- combat movement implemented only through the Animator
- root motion deciding hit, dodge, parry, or counter success
- `light attack` sliding freely while hitting
- `heavy attack` homing to the enemy
- parry drifting into valid range
- dodge canceling every action by default
- counter teleporting to the target without explicit design decision
- recovery hidden inside animation
- camera state forcing movement restrictions
- `Avatar Mask` being required before M0 combat feel is proven

### 11.18 Open Questions

The following questions remain unresolved:

- whether `light attack` and `heavy attack` fully lock movement or only reduce it
- whether attacks allow a small forward step or lunge
- whether parry allows micro-movement
- whether counter uses limited auto-alignment
- whether dodge can cancel attack recovery
- whether root motion is used for attacks, dodge, or counter
- whether recovery duration is generic or per-action
- whether `Avatar Mask` is needed for parry or guard while moving after M0

## 12. Hit Reaction / Recovery Movement Contract

The purpose of this section is to define the provisional M0 contract for how `Player Locomotion` responds to hit reaction and recovery movement states. This is not a full `Health / Damage / Hit Reaction` design. `Player Locomotion` only defines movement restriction, control suppression, recovery flow, and locomotion debug visibility. `Combat Core` owns hit result and combat outcome validation. The Animator remains presentation only.

### 12.1 Contract Purpose

The hit-reaction and recovery movement contract should clarify:

- what happens to player movement after being hit
- how control is temporarily restricted
- how the player returns to readable control
- how recovery preserves combat commitment
- how failure remains understandable
- what `Player Locomotion` owns versus `Health / Damage / Hit Reaction` and `Combat Core`

This contract exists so movement consequence remains explicit and debuggable during the first duel.

### 12.2 Hit Reaction Purpose

Hit reaction should:

- make player failure readable
- briefly interrupt or restrict control
- show that the enemy attack connected
- prevent immediate action spam after being hit
- return player to a clear recovery or control state
- support fair learning of timing and spacing

Hit reaction should not:

- become a full damage system
- depend only on animation clip length
- create long stun-lock in M0
- hide why the player was hit
- override `Combat Core` hit result
- become a ragdoll or physics system

The player should feel consequence, not chaos.

### 12.3 M0 Hit Reaction Scope

For M0:

- one basic player hit reaction is enough
- one basic stagger or control-suppression response is enough
- no complex reaction categories are required yet
- no directional knockback is required unless needed for readability
- no ragdoll is required
- no launch or airborne reactions are required
- no combo hit-stun system is required
- no full death or defeat flow is required unless needed as `Disabled / ControlSuppressed`

This keeps the system lean enough to support one duel without absorbing the whole damage architecture.

### 12.4 Hit Reaction Trigger Contract

The expected contract flow is:

- `Combat Core` confirms that an enemy hit result occurred
- `Health / Damage / Hit Reaction` may later classify reaction severity
- `Player Locomotion` receives or observes valid hit-reaction context
- locomotion enters `HitReaction` or a related movement-restricted state
- the Animator presents the reaction visually
- the camera may support readability after confirmed result

`Player Locomotion` must not:

- decide whether the enemy hit was valid
- decide damage amount
- decide final health outcome
- infer hit result only from animation, `VFX`, or `Audio`

This keeps locomotion reactive rather than authoritative.

### 12.5 Hit Reaction Movement Rules

During hit reaction:

- normal movement may be locked or heavily reduced
- player control may be suppressed briefly
- facing may be constrained or allowed to settle
- the reaction should stay short and readable for M0
- the player should not immediately cancel into dodge or attack unless explicitly allowed
- movement restriction source should be debug-visible

The player should understand that control was interrupted because the enemy’s attack actually connected.

### 12.6 Knockback / Displacement Rules

Several conceptual options are acceptable provisionally:

- no knockback, only brief control suppression
- small authored displacement
- direction-based knockback
- root-motion visual displacement only

For M0:

- knockback should remain minimal unless clearly needed for readability
- displacement must not break camera readability
- knockback must not create unclear spacing results
- physics should not create chaotic player position
- the final knockback model remains open

The first duel should prefer readable consequence over dramatic force.

### 12.7 Recovery Purpose

Recovery should:

- return the player from hit reaction, dodge, parry, attack, or counter back to readable control
- preserve commitment
- prevent spam
- make state transitions understandable
- support duel rhythm

Recovery should not:

- be hidden only in animation
- last so long that M0 testing feels sluggish
- be bypassed by movement input accidentally
- replace explicit action states
- become a full stamina or balance system

Recovery is part of how the duel breathes after both success and failure.

### 12.8 Recovery Sources

Recovery may come from:

- dodge recovery
- `light attack` recovery
- `heavy attack` recovery
- parry recovery
- counter recovery
- hit-reaction recovery
- debug reset or control restoration

For each source:

- the source should be debug-visible
- duration may remain provisional
- recovery can be generic for M0 or become source-specific later

This makes post-action control loss explainable rather than vague.

### 12.9 Recovery Movement Rules

During recovery:

- movement may be locked, reduced, or delayed depending on source
- the player should understand when control returns
- facing support may be preserved if target focus is active
- recovery should transition back to `LocomotionIdle`, `LocomotionMove`, or `TargetFocusMove / DuelMove`
- recovery should not hide enemy punish or readability context
- animation recovery must not secretly define gameplay recovery

Recovery should feel like a clear tail on the action, not a hidden timer buried in animation.

### 12.10 Recovery Priority / Interruption Rules

For M0:

- hit-reaction recovery should prevent immediate spam after being hit
- dodge recovery should prevent dodge spam
- attack recovery should preserve commitment
- counter recovery should preserve impact readability
- interruption rules should remain conservative
- any cancel or interrupt exception must be explicit and debug-visible

This keeps the duel readable and stops movement behavior from quietly becoming too permissive.

### 12.11 Relationship To Combat Core

The relationship to `Combat Core` should remain:

- `Combat Core` validates hit, dodge, parry, counter, and action outcomes
- `Combat Core` may expose recovery or action-lock context
- `Player Locomotion` applies movement restriction and recovery flow
- `Player Locomotion` does not validate combat result
- recovery should not contradict `Combat Core` result

Locomotion responds to outcome truth, but does not create it.

### 12.12 Relationship To Health / Damage / Hit Reaction

The relationship to a fuller hit-reaction system should remain provisional:

- `Health / Damage / Hit Reaction` may later own reaction categories, damage, stagger severity, defeat, i-frames, and hit-stop policy
- `Player Locomotion` only needs provisional movement response for M0
- full hit-reaction design can be split later if needed
- M0 should avoid making locomotion responsible for all damage consequences

This keeps the M0 movement layer small and avoids prematurely turning it into a damage architecture.

### 12.13 Relationship To Animator / Root Motion

The relationship to animation should remain explicit:

- the Animator presents hit and recovery visually
- the Animator State Machine does not own recovery truth
- root motion remains open
- if root motion is used for hit reaction or recovery, gameplay state still controls timing and movement authority
- animation events may request sync later, but cannot end recovery by themselves without validation

The player should never be left in a gameplay restriction only because an animation clip kept playing.

### 12.14 Relationship To Camera

The relationship to the camera should remain:

- the camera should keep hit reaction and recovery readable
- the camera may provide restrained feedback after confirmed hit
- the camera should not hide recovery or the next enemy read
- the camera does not decide hit or recovery validity
- reveal and counter camera support should not interrupt recovery clarity

This helps preserve fair failure without letting presentation blur control return.

### 12.15 Debug Requirements

For M0, debug should expose:

- `hit reaction active?`
- hit-reaction source
- hit-reaction elapsed time
- `control suppressed?`
- `movement restricted?`
- restriction source
- `knockback/displacement active?`
- `recovery active?`
- recovery source
- recovery elapsed or remaining time if tracked
- `recovery can be interrupted?`
- transition-out-of-recovery reason
- last `Combat Core` result affecting hit or recovery
- last `Health / Hit Reaction` context if available
- Animator visual state if useful for comparison

This should make movement-side consequence readable during both tuning and playtest diagnosis.

### 12.16 Hit Reaction / Recovery Table

| Context | Movement Response | Control Response | Owner Of Truth | M0 Requirement | Open Decision |
| --- | --- | --- | --- | --- | --- |
| `Enemy hit confirmed` | Enter explicit movement consequence path | Control may be reduced or suppressed | `Combat Core` confirms result | Required | Exact downstream reaction routing |
| `Player hit reaction` | Lock or heavily reduce movement briefly | Brief suppression | `Player Locomotion` movement response | Required | Exact duration and severity |
| `Knockback / displacement` | Minimal or no displacement by default | Movement shift only if readable | provisional shared contract | Optional | None vs small authored displacement |
| `Dodge recovery` | Restricted return to movement | Prevent immediate repeat input spam | `Player Locomotion` | Required | Duration tuning |
| `Light attack recovery` | Moderate restriction before full control return | Reduced control | `Player Locomotion` from valid action context | Required | Generic vs authored duration |
| `Heavy attack recovery` | Stronger restriction than light | Reduced or locked control briefly | `Player Locomotion` from valid action context | Required | Commitment strength |
| `Parry recovery` | Brief controlled return after hold-ground action | Reduced or restored control | `Player Locomotion` from valid action context | Required | Micro-movement rules |
| `Counter recovery` | Preserve readable follow-through after counter | Reduced control briefly | `Player Locomotion` from valid action context | Required | Duration and alignment carryover |
| `Hit reaction recovery` | Return from failure to readable control | Control restored through recovery path | `Player Locomotion` | Required | Generic vs source-specific |
| `Disabled / defeated` | No normal movement | Full suppression | explicit suppression state | Provisional | Whether full defeat is needed in M0 |

### 12.17 Failure Conditions

Hit reaction and recovery movement contract fails if:

- the player is hit but movement response is unclear
- the player can instantly spam after hit with no explicit rule
- recovery is hidden only in animation
- hit reaction lasts too long for M0 feel testing
- knockback makes spacing unreadable
- recovery can be bypassed accidentally
- `Combat Core` result and locomotion response contradict each other
- the camera hides recovery or the next read
- debug cannot explain why control was suppressed or restored

These failures damage both fairness and the team’s ability to tune the duel.

### 12.18 Anti-patterns

The following should be treated as failures for M0:

- treating hit reaction as a full damage system inside locomotion
- animation clip length secretly defining recovery
- ragdoll or physics knockback before grounded duel feel works
- long stun-lock in M0
- immediate cancel from hit reaction without explicit rule
- recovery hidden from debug
- root motion deciding recovery end
- camera feedback hiding player control return
- `Health / Damage` and `Player Locomotion` both owning reaction truth
- adding complex poise or balance systems before M0

### 12.19 Open Questions

The following questions remain unresolved:

- whether M0 player hit reaction includes knockback
- whether hit-reaction recovery is generic or source-specific
- whether recovery durations are fixed or authored per action
- whether recovery can be canceled by dodge or parry in M0
- whether root motion is used for hit reaction
- whether `Health / Damage / Hit Reaction` needs its own GDD before implementation
- whether hit-stop belongs to `Combat Core`, hit reaction, camera, or presentation
- whether player defeat or disabled state is needed for M0

## 13. Camera / Target Focus Coordination Contract

The purpose of this section is to define the provisional M0 coordination contract between `Player Locomotion`, `Lock-On & Combat Camera`, and target focus. `Player Locomotion` owns movement input interpretation, facing support, dodge displacement, movement restrictions, recovery, and locomotion debug truth. `Lock-On & Combat Camera` owns camera state, framing, target-focus readability, target-focus state, and camera debug truth. `Combat Core` owns action validity and combat result. Neither locomotion nor camera should secretly own the other system’s truth.

### 13.1 Coordination Purpose

This contract should ensure:

- movement and camera support the same duel readability goal
- target focus helps orientation without auto-solving spacing
- dodge, parry, counter, and recovery remain readable
- camera-relative versus target-relative movement is handled explicitly
- neither camera nor locomotion owns the other system’s truth

The contract exists to make the duel feel coordinated, not entangled.

### 13.2 Shared M0 Readability Goals

`Player Locomotion` and `Lock-On & Combat Camera` should together support:

- the player knows where the enemy is
- the player knows where they are facing
- the player can judge spacing
- enemy telegraph remains visible
- dodge displacement remains readable
- parry and counter alignment remain understandable
- recovery, punish, and reveal moments do not disorient the player
- reset returns the duel to stable readable control

These goals are shared, but ownership of how they are achieved remains distinct.

### 13.3 Movement Mode Coordination

Several focused-movement interpretations remain open for M0:

#### Camera-Relative During Focus

- movement input remains relative to the camera
- this can support familiar third-person control
- the risk is that duel orientation may feel less intentional

#### Target-Relative During Focus

- movement input maps around the target
- this can support strafing and duel readability
- the risk is that movement may feel rigid

#### Hybrid During Focus

- movement remains camera-relative while facing or framing biases toward the target
- this may feel natural while preserving readability
- the risk is additional complexity

For M0:

- the final choice remains open for tuning
- whichever mode is chosen must be debug-visible
- `Player Locomotion` owns movement interpretation
- the camera provides framing and orientation context only

This keeps locomotion in charge of movement truth even when focus mode exists.

### 13.4 Target Focus And Facing Coordination

The target-focus contract should remain modest and readable:

- target focus may provide target direction or context
- locomotion may use target direction for facing support
- any facing support should be small, readable, and debug-visible
- facing support must not make attacks auto-hit, parries auto-succeed, or counters auto-valid
- target focus should not remove spacing discipline

Target focus should help the player understand the duel, not silently correct it for them.

### 13.5 Dodge Coordination

During dodge:

- `Player Locomotion` owns dodge direction and displacement
- the camera should preserve displacement readability
- target focus may help keep the enemy in view
- the camera should not rotate so much that dodge direction becomes unclear
- dodge success or failure remains owned by `Combat Core`
- target focus must not make dodge automatically safe

The player should feel that dodge moved them clearly, and the camera should help that movement make sense.

### 13.6 Parry Coordination

During parry:

- locomotion may restrict or stabilize movement
- target focus may help facing and readability
- the camera should preserve enemy timing and parry result visibility
- parry success remains owned by `Combat Core`
- camera and target focus must not make parry succeed automatically

Parry should remain a timing truth with readable orientation support, not a focus-driven auto-correction.

### 13.7 Attack / Counter Coordination

For attacks:

- locomotion owns movement restriction and facing expression
- the camera preserves player-enemy relationship and spacing
- target focus may help orientation
- `Combat Core` owns hit result

For counter:

- locomotion may provide limited alignment if explicitly approved
- the camera preserves counter impact and enemy reaction visibility
- target focus may help counter look intentional
- counter validity remains owned by `CombatCore`
- no teleport or snap alignment should occur unless explicitly approved later

This keeps movement expression, camera readability, and combat truth aligned without collapsing them together.

### 13.8 Recovery / Reset Coordination

During recovery and reset:

- locomotion returns the player toward readable control
- the camera returns toward readable duel framing
- target focus may remain active if the target is still valid
- reset should not hide enemy recovery, punish, or player recovery
- the return of movement control should be understandable
- reveal support should not disorient the next movement read

Both systems should help the duel breathe again after an exchange.

### 13.9 Information Exchange

`Player Locomotion` may need from `Lock-On & Combat Camera` or target focus:

- `target focus active?`
- current target context
- target direction if exposed
- camera-relative basis if camera-relative movement is used
- camera state or framing mode only as read-only context if truly needed

`Lock-On & Combat Camera` may need from `Player Locomotion`:

- player position
- player facing
- movement state
- `dodge active?`
- dodge direction or displacement context
- `recovery active?`
- `movement restricted?`
- `hit reaction active?`
- counter or attack movement context if exposed

The boundary rules are:

- all cross-system data should be read-only across the seam
- circular ownership should be avoided
- service-locator style access should be avoided

This contract should stay narrow enough that each system remains independently understandable.

### 13.10 Relationship To Combat Core

The relationship to `Combat Core` should remain explicit:

- `Combat Core` is the final authority for action validity and results
- locomotion and camera coordination must not bypass `Combat Core`
- dodge, parry, and counter success must always trace back to `Combat Core`
- camera and movement feedback should follow confirmed context
- any alignment or facing support must not override `Combat Core` outcomes

This is the core rule that prevents coordination from becoming hidden gameplay authority.

### 13.11 Relationship To Enemy Intent & Telegraph

The relationship to `Enemy Intent & Telegraph` should remain:

- `Enemy Intent & Telegraph` exposes telegraph, commitment, active, recovery, and punish states
- the camera uses enemy state for framing and readability
- locomotion may indirectly respond through player decisions, not by owning enemy truth
- enemy telegraph visibility should be preserved without forcing player movement
- enemy punish visibility should not be lost during player recovery or reset

This keeps enemy readability external to locomotion while still allowing locomotion to support readable player response.

### 13.12 Relationship To Animator

The relationship to presentation should remain explicit:

- the Animator presents movement, facing, dodge, parry, counter, and recovery
- the Animator State Machine does not own coordination truth
- `Avatar Mask` may later support upper- and lower-body visual blending
- root motion remains open and must coordinate with both locomotion and camera readability
- animation events may request sync later, but cannot decide movement or camera state authority

This prevents presentation from quietly becoming the glue that controls gameplay behavior.

### 13.13 Debug Requirements

For M0, debug should expose:

- current movement mode
- current camera state
- `target focus active?`
- current target
- target direction
- player facing direction
- camera-relative basis if used
- target-relative basis if used
- dodge direction
- `camera moved during dodge/parry/counter?`
- `movement restricted?`
- `camera reset active?`
- `locomotion recovery active?`
- current coordination reason
- last cross-system context used
- rejected coordination request if any

This should allow the team to explain whether an orientation or readability issue came from locomotion, camera, target focus, or bad coordination assumptions.

### 13.14 Coordination Table

| Coordination Area | Locomotion Owns | Camera / Target Focus Owns | Shared Context | Must Not Do | M0 Notes |
| --- | --- | --- | --- | --- | --- |
| `Movement Mode` | Input interpretation and actual movement direction | Framing support and target readability | Camera-relative or target-relative basis if exposed | Camera must not secretly choose movement mode | Final mode remains open |
| `Facing` | Facing expression and support rules | Orientation readability and target direction clarity | Target direction and facing context | Facing support must not create action success | Keep correction small and visible |
| `Target Focus` | Read locomotion implications only | Target-focus state and readability support | Target active/valid context | Locomotion must not own focus truth | One target only in M0 |
| `Dodge` | Direction, displacement, movement override, recovery | Enemy visibility and dodge readability | Dodge state, target direction, camera framing | Camera must not decide dodge success | Main movement-defense seam |
| `Parry` | Movement restriction or stabilization | Readable threat framing | Facing context, target direction | Focus must not auto-succeed parry | Hold-ground timing answer |
| `Attack` | Restriction and movement expression | Spacing and player-enemy relationship readability | Action context, facing context | Camera must not force action movement | Covers light/heavy |
| `Counter` | Optional small alignment and movement expression | Impact readability and enemy reaction visibility | Counter context and orientation cues | No teleport or snap because focus exists | Limited alignment remains open |
| `Recovery` | Return of movement control | Return of duel framing | Recovery active, target valid, camera reset state | Systems must not hide each other’s readable recovery | Important for loop reset |
| `Reveal / Reset` | Maintain readable player control return | Maintain readable duel framing and next-read visibility | Reveal context, reset context | Reveal must not disorient movement control return | Keep reveal restrained |
| `Debug` | Locomotion truth and restriction truth | Camera truth and focus/framing truth | Context reasons and shared state traces | Debug must not become hidden authority | Use clear source labeling |

### 13.15 Failure Conditions

Coordination fails if:

- the camera changes movement direction invisibly
- locomotion assumes lock-on validity as combat validity
- target focus auto-solves spacing
- dodge direction becomes unclear because of camera movement
- parry or counter appears valid visually but `Combat Core` rejects it without explainable reason
- camera reset hides locomotion recovery
- locomotion recovery hides enemy punish readability
- target-relative movement feels rigid without explicit decision
- camera-relative movement loses enemy orientation
- debug cannot explain which system caused orientation or movement behavior

These failures are usually coordination failures rather than single-system failures.

### 13.16 Anti-patterns

The following should be treated as failures for M0:

- camera secretly deciding movement rules
- locomotion secretly forcing camera state
- target focus treated as hit validity
- dodge direction derived from camera in a way players cannot predict
- counter alignment snapping because lock-on exists
- movement mode switching without debug visibility
- camera reset interrupting player control readability
- the Animator used as coordination source of truth
- circular dependencies between camera and locomotion
- overbuilding a full targeting or movement framework before M0

### 13.17 Open Questions

The following questions remain unresolved:

- whether focused movement is camera-relative, target-relative, or hybrid
- whether target focus fully locks facing or only biases it
- whether dodge direction changes when target focus is active
- whether counter alignment requires target focus
- whether camera state is allowed to influence movement mode
- whether locomotion state is allowed to influence camera state priority
- whether root motion needs special camera coordination
- whether coordination data should be events, snapshots, or read-only state

## 14. Animation / FSM Boundary

The purpose of this section is to define the boundary between `Player Locomotion` gameplay truth, the pure C# FSM, the Animator State Machine, animation layers, `Avatar Masks`, root motion, and animation events. For M0, gameplay truth must remain explicit, inspectable, and testable even if animation is still rough or incomplete.

### 14.1 Boundary Purpose

This boundary should clarify:

- what the pure C# FSM owns
- what the Animator owns
- what animation layers and `Avatar Masks` may support
- what root motion may or may not control
- what animation events may request
- why gameplay truth must remain inspectable and testable without final animation

The goal is not to devalue animation. The goal is to prevent presentation from quietly becoming the hidden owner of movement and combat behavior.

### 14.2 Pure C# FSM Owns

The pure C# FSM owns:

- locomotion state truth
- movement phase
- movement restrictions
- dodge state and phase
- parry movement state
- combat-action movement lock
- recovery state
- hit-reaction movement suppression
- disabled or control-suppressed state
- transition acceptance or rejection
- debug-visible state reasons

The pure C# FSM may coordinate with `Combat Core` for:

- valid action context
- action-lock requests
- dodge, parry, and counter outcome context
- hit-reaction context
- recovery context

The pure C# FSM must remain testable without the Animator.

### 14.3 Animator State Machine Owns

The Animator State Machine owns:

- visual playback
- locomotion blend presentation
- attack animation presentation
- dodge animation presentation
- parry and counter animation presentation
- hit-reaction animation presentation
- transition visuals
- pose readability

The Animator State Machine must not own:

- gameplay movement state
- dodge success or failure
- parry timing or result
- counter validity
- action locks
- recovery truth
- hit-reaction truth
- `CounterWindow`
- reveal validity

The Animator expresses accepted gameplay truth. It does not define it.

### 14.4 Animation Layers / Avatar Mask Boundary

Animation layers and `Avatar Masks` are presentation tools.

They may later support:

- upper/lower body blending
- lock-on guard pose
- parry overlay
- attack overlay
- strafing polish

For M0:

- they are optional
- the system should prefer simpler full-body combat actions first when that better preserves weight and commitment

Animation layers and `Avatar Masks` must not:

- decide which actions are valid
- bypass movement restrictions
- override gameplay recovery
- make attacks connect
- make parries succeed
- hide state bugs behind blending
- become required before M0 feel is proven

This keeps blending as polish rather than hidden logic.

### 14.5 Full-Body Action Direction For M0

The recommended M0 direction is:

- `light attack` may be full-body first
- `heavy attack` should likely be full-body because commitment and weight matter
- `dodge` should have clear full-body displacement and readability
- `parry` may become upper-body or mixed later, but M0 can keep it simple
- `counter` should likely be full-body for impact and emotional weight
- `hit reaction` should be full-body or otherwise unmistakably readable

This direction fits the tone of `Glass Refrain`:

- combat is deliberate and emotional
- actions should feel committed rather than layered into weightless overlays
- full-body commitment supports `read → evade/parry → counter → reveal`
- `Avatar Mask` can be introduced later for polish once base feel is proven

### 14.6 Root Motion Boundary

Root motion remains an open decision.

For M0:

- root motion may later be useful for attacks, dodge, counter, or hit reaction
- root motion may improve weight if carefully coordinated
- root motion must not own gameplay truth by itself
- if root motion is used, `Player Locomotion` and `Combat Core` still validate timing, movement restrictions, collision, hit result, dodge result, parry result, counter result, and recovery

Root motion must not:

- secretly move the player into valid hit range
- secretly avoid attacks
- decide dodge success
- decide counter success
- override movement locks
- make debug movement state inaccurate

Root motion may support feel, but it must not replace gameplay-side authority.

### 14.7 Animation Event Boundary

Animation events may request sync points later, but they are not authoritative truth for M0.

Animation events may:

- request sync points
- support presentation timing
- request hitbox timing or `VFX`/`Audio` timing only if validated by gameplay systems

Animation events should not be authoritative for combat truth in M0.

Animation events must not directly:

- apply damage
- validate hit
- validate parry
- validate dodge
- open `CounterWindow`
- end recovery without validation
- trigger reveal validity
- change locomotion state without accepted request

This protects the FSM from being silently driven by clip events.

### 14.8 Combat Core Relationship

The relationship to `Combat Core` should remain:

- `Combat Core` owns combat action validity and results
- the `Player Locomotion` FSM owns movement response and restrictions
- the Animator follows accepted gameplay state
- `Combat Core` should not read the Animator State Machine as combat truth
- animation playback mismatch should be treated as a presentation issue, not a gameplay truth issue

This is the core anti-drift rule between gameplay logic and presentation.

### 14.9 Camera / Target Focus Relationship

The relationship to `Lock-On & Combat Camera` should remain:

- the camera reads gameplay and camera state, not Animator truth
- target focus may influence facing or orientation context
- the Animator may later present target-facing pose or guard pose
- `Avatar Mask` may later help lock-on pose polish
- camera and target focus must not rely on Animator layers to decide movement or combat validity

This keeps camera readability tied to explicit state rather than visual guesswork.

### 14.10 Debug Requirements

For M0, debug should expose:

- current pure C# locomotion state
- current combat-related movement state
- current Animator visual state if available
- mismatch between gameplay state and animation state if useful
- `animation layer active?`
- `Avatar Mask active?`
- `root motion active?`
- `root motion displacement applied?`
- `animation event request received?`
- `animation event accepted/rejected?`
- movement-lock source
- recovery source
- transition reason

This should help the team distinguish gameplay truth bugs from presentation mismatch.

### 14.11 Boundary Table

| Area | Owns | May Request / Support | Must Not Own | M0 Decision |
| --- | --- | --- | --- | --- |
| `Pure C# FSM` | Locomotion truth, restrictions, recovery, transitions, debug reasons | Coordinate with valid `Combat Core` context | Presentation playback, animation truth | Primary gameplay authority |
| `Animator State Machine` | Visual playback, blends, pose readability, transition visuals | Present accepted gameplay state | Movement truth, combat validity, recovery truth | Presentation only |
| `Animation Layers` | Visual layering and polish | Support blending later if useful | Action validity, restriction truth, recovery truth | Optional, not required |
| `Avatar Mask` | Visual upper/lower body separation later | Support polish such as guard or strafe overlay | Combat/movement truth | Optional and deferred unless needed later |
| `Root Motion` | Visual displacement support if chosen | Support weight and commitment if coordinated | Hit/dodge/parry/counter success, movement truth | Open decision |
| `Animation Events` | Sync requests and presentation timing requests | Request validated sync points later | Damage, `CounterWindow`, recovery end, locomotion authority | Non-authoritative |
| `Combat Core` | Action validity, result truth, `CounterWindow`, reveal request context | Drive valid locomotion consequences | Animator authority | Gameplay authority for combat |
| `Player Locomotion` | Movement response, restrictions, recovery flow, facing support | Coordinate with camera and combat context | Combat validity, animation truth | Gameplay movement authority |
| `Lock-On / Camera` | Framing, readability, target focus state | Support orientation and readability | Movement/combat validity, animation truth | Readability authority |

### 14.12 Failure Conditions

The animation/FSM boundary fails if:

- the Animator State Machine becomes gameplay truth
- animation clip length secretly defines recovery
- root motion changes combat outcomes invisibly
- animation events apply damage or open `CounterWindow` directly
- `Avatar Mask` becomes required before M0 feel is proven
- animation blending hides movement restriction bugs
- `Combat Core` reads Animator state as authority
- debug cannot explain mismatch between movement state and animation state
- final animation polish is required to validate basic movement feel

These failures make the system hard to test, hard to trust, and hard to tune.

### 14.13 Anti-patterns

The following should be treated as failures for M0:

- using the Animator as the real FSM
- hiding action locks in animation clips
- ending recovery through animation event only
- root motion deciding dodge success
- `Avatar Mask` used to fake combat while gameplay state is unclear
- upper-body attack overlay making katana attacks feel weightless
- animation event directly applying hit result
- debugging by watching animation only
- building a full animation-layer architecture before one duel works
- treating presentation mismatch as gameplay truth

### 14.14 Open Questions

The following questions remain unresolved:

- whether M0 uses root motion for dodge, attacks, counter, or hit reaction
- whether `light attack` remains full-body or becomes upper-body overlay later
- whether `parry` should become upper-body overlay after M0
- whether lock-on guard pose needs `Avatar Mask` in M0 or only later
- whether animation events are allowed as validated timing requests in the first prototype
- whether Animator visual state should be displayed in debug
- whether animation/state mismatch should fail M0 acceptance
- whether full-body actions remain preferred through vertical slice

## 15. Debug / Readability Requirements

The purpose of locomotion debug and readability tooling in M0 is to make movement feel inspectable instead of mysterious. `Player Locomotion` cannot be tuned responsibly if the team cannot see what movement state the player is in, how input was interpreted, why movement was restricted, how dodge phases are progressing, and whether animation presentation still matches gameplay truth closely enough.

### 15.1 Debug Purpose

Debug and readability tooling should help designers answer:

- what locomotion state is the player currently in
- why did the locomotion state change
- what input was received
- how was that input interpreted
- is movement allowed, reduced, locked, or overridden
- what is the current facing mode
- is target focus affecting movement or facing
- is dodge active, and which phase is active
- why was dodge accepted or rejected
- is recovery active, and what caused it
- is hit reaction suppressing control
- does Animator presentation match pure C# FSM truth

Debug should not:

- become required for player understanding
- change gameplay state
- force locomotion states
- decide combat validity
- replace real movement feel testing

Debug exists to explain locomotion behavior, not to excuse unclear locomotion behavior.

### 15.2 Required Locomotion State Debug

For M0, locomotion-state debug should expose:

- current locomotion state
- previous locomotion state
- time in state
- requested state
- accepted or rejected transition
- transition reason
- current movement phase
- current movement input
- interpreted movement direction
- movement speed
- grounded state
- `movement allowed?`
- `movement restricted?`
- restriction source
- restriction priority

This should make it possible to explain why the player could or could not move at a given moment.

### 15.3 Required Facing / Orientation Debug

Facing and orientation debug should expose:

- current facing mode
- player facing direction
- target direction
- `target focus active?`
- current target
- camera-relative basis if used
- target-relative basis if used
- `facing correction active?`
- facing correction amount or reason if useful
- `action-constrained facing active?`
- last facing change reason

This helps determine whether orientation confusion came from locomotion rules, target focus, or camera coordination.

### 15.4 Required Dodge Debug

Dodge debug should expose:

- `dodge requested?`
- `dodge accepted/rejected?`
- rejection reason
- dodge direction
- dodge direction mode
- dodge phase: `startup / evade / recovery`
- dodge elapsed time
- `dodge movement override active?`
- `avoidance/evade active?` if supported by `Combat Core`
- last enemy attack checked against dodge
- `Combat Core` dodge result
- transition-out-of-dodge reason

This is one of the highest-value debug groups because dodge is the main movement-based defense in M0.

### 15.5 Required Combat Movement Restriction Debug

Combat movement restriction debug should expose:

- combat action context
- `action movement lock active?`
- `attack movement restriction active?`
- `parry movement restriction active?`
- `counter movement/alignment active?`
- `recovery active?`
- recovery source
- recovery elapsed or remaining time if tracked
- movement speed multiplier if used
- `can movement be interrupted?`
- last `Combat Core` action or result affecting movement

This should make action commitment and restriction visible rather than hidden inside feel.

### 15.6 Required Hit Reaction / Recovery Debug

Hit-reaction and recovery debug should expose:

- `hit reaction active?`
- hit-reaction source
- `control suppressed?`
- `movement suppressed/reduced?`
- `knockback/displacement active?`
- `recovery active?`
- recovery source
- transition-out-of-recovery reason
- last `Health / Damage / Hit Reaction` context if available
- last confirmed hit result from `Combat Core`

This ensures failure consequence remains explainable and recovery return can be tuned intentionally.

### 15.7 Required Camera / Target Focus Coordination Debug

Cross-system locomotion/camera debug should expose:

- current camera state if available
- `target focus active?`
- current target
- target direction
- movement mode during focus
- camera-relative or target-relative mode
- `camera moved during dodge/parry/counter?` if available
- current coordination reason
- last cross-system context used
- rejected coordination request if any

This helps identify whether a locomotion readability issue is truly locomotion-owned or is coming from coordination with the duel camera.

### 15.8 Required Animation / FSM Boundary Debug

Animation/FSM boundary debug should expose:

- current pure C# locomotion state
- current Animator visual state if available
- current combat-related movement state
- `Animator layer active?`
- `Avatar Mask active?`
- `root motion active?`
- `root motion displacement applied?`
- `animation event request received?`
- `animation event accepted/rejected?`
- gameplay-state vs animation-state mismatch if useful
- movement-lock source as gameplay truth rather than animation truth

This allows the team to distinguish real movement bugs from presentation mismatch.

### 15.9 Debug Readability Checklist

A designer should be able to answer:

- Did movement input produce the expected direction?
- Did facing support help or hurt duel readability?
- Did dodge direction match player expectation?
- Did dodge feel earned rather than automatic?
- Did movement restriction come from a clear state or action?
- Did recovery prevent spam without feeling sluggish?
- Did hit reaction make failure readable?
- Did target focus help orientation without auto-solving spacing?
- Did Animator presentation match gameplay state closely enough?
- Can unclear movement moments be explained by debug state?

If these questions cannot be answered, locomotion tuning is still too opaque.

### 15.10 Debug Output Format Guidance

For M0:

- debug can remain simple overlay text, labels, or gizmos
- no final HUD polish is required
- debug should be human-readable
- debug names should match GDD state names where possible
- debug should prioritize high-signal data over clutter
- designers should be able to toggle locomotion debug independently if possible
- debug should remain usable while testing `Basic Attack A` repeatedly

The goal is fast diagnosis, not instrumentation spectacle.

### 15.11 Debug Table

| Debug Area | Required Data | Why It Matters | M0 Priority | Notes |
| --- | --- | --- | --- | --- |
| `Locomotion State` | Current/previous state, time in state, requested/accepted state, transition reason | Explains core movement truth | `Must Have` | Use GDD state names |
| `Movement Input` | Input vector, interpreted direction, movement speed | Explains how player input became movement | `Must Have` | Essential for feel tuning |
| `Facing / Orientation` | Facing mode, facing direction, target direction, facing correction | Explains duel orientation readability | `Must Have` | Important under target focus |
| `Target Focus Coordination` | Focus active, target, movement mode during focus, coordination reason | Explains cross-system orientation behavior | `Should Have` | Useful once focus is active |
| `Dodge` | Request/result, phase, direction, dodge result, phase timing | Explains M0 primary movement defense | `Must Have` | High-value tuning area |
| `Combat Movement Restrictions` | Action locks, recovery flags, restriction source/priority | Explains commitment and anti-spam behavior | `Must Have` | Important for fair action feel |
| `Recovery` | Recovery active, source, timing, transition-out reason | Explains return to control | `Must Have` | Crucial for flow tuning |
| `Hit Reaction` | Hit-reaction active, source, suppression, knockback/displacement if any | Explains readable failure consequence | `Should Have` | M0 still needs clear failure |
| `Animator / FSM Boundary` | Gameplay state, visual state, mismatch, layer/mask status | Explains whether bugs are gameplay or presentation | `Should Have` | Important once animation arrives |
| `Root Motion / Animation Events` | Root motion active, displacement applied, event request/acceptance | Prevents presentation from hiding truth | `Nice To Have` | May matter only if those features are used |
| `Camera Coordination` | Camera state during movement, cross-system context, camera motion during critical windows | Explains locomotion/camera seam | `Should Have` | Important for focused duel feel |

### 15.12 Debug Failure Conditions

`Player Locomotion` debug is insufficient if:

- the current locomotion state cannot be identified
- movement input interpretation cannot be inspected
- dodge acceptance or rejection reason is unknown
- movement restriction source is unclear
- recovery source is unknown
- hit-reaction control suppression cannot be explained
- facing correction happens without debug reason
- target focus changes movement behavior invisibly
- Animator/FSM mismatch cannot be diagnosed when it affects feel
- debug data is stale or disagrees with actual behavior
- debug is so noisy that designers stop using it

If any of these are true, locomotion tuning is likely being done too much by intuition alone.

### 15.13 Anti-patterns

The following should be treated as failures for M0:

- debug overlay becoming gameplay UI
- debug changing locomotion behavior
- using vague state names
- hiding transition rejection reasons
- movement locks without source labels
- recovery hidden from debug
- dodge phase hidden from debug
- target focus changing movement with no visible mode
- Animator visual state treated as gameplay truth
- root-motion movement not visible in debug
- too much visual clutter during playtest

### 15.14 Open Questions

The following questions remain unresolved:

- whether locomotion debug is part of a shared M0 combat overlay or a separate locomotion overlay
- whether Animator visual state should be shown in M0 debug
- whether root-motion displacement needs explicit debug if root motion is deferred
- whether dodge phase should be displayed as state or timing data
- whether movement-restriction priority should be displayed
- whether camera-relative / target-relative basis needs gizmo visualization
- whether debug should be available in development builds
- whether rejected input or action requests should be logged or only shown live

## 16. Data Authoring Needs

The purpose of locomotion data authoring in M0 is to expose only the minimum tuning surfaces needed to make one duel feel grounded, readable, and fair. This is not an implementation spec and not a full locomotion framework. It is a design-level definition of which movement-facing values should be easy to inspect and adjust while tuning the first katana duel.

### 16.1 Data Authoring Purpose

Locomotion data should allow designers to tune:

- grounded movement speed and responsiveness
- acceleration and deceleration feel
- facing behavior
- target-focus movement behavior
- dodge direction, distance, timing, and recovery
- combat action movement restrictions
- recovery behavior
- hit-reaction movement response
- camera and target-focus coordination assumptions
- debug display configuration

Locomotion data should not:

- decide combat action validity
- decide hit, parry, dodge, or counter result
- open `CounterWindow`
- validate reveal
- replace `Combat Core` contracts
- replace playtesting

The purpose of authoring data is to make locomotion feel tunable, not to move gameplay authority out of explicit systems.

### 16.2 M0 Movement Data

Minimum tunable movement data may include:

- walk, run, or basic move speed
- acceleration
- deceleration
- rotation speed or facing responsiveness
- grounded movement smoothing
- target-focus movement speed modifier if used
- movement deadzone or input sensitivity if needed

Exact values are deferred to prototype tuning, but the target feel is clear: movement should feel grounded and deliberate rather than floaty.

### 16.3 Facing / Orientation Data

Minimum tunable facing and orientation data may include:

- free-facing responsiveness
- target-facing bias strength
- action-facing correction allowance
- maximum facing-correction angle if used
- facing-correction speed
- facing-mode labels for debug

This data must not make attacks auto-hit or parries auto-succeed. Facing correction should remain small and readable for M0.

### 16.4 Target Focus Movement Data

Minimum tunable target-focus movement data may include:

- camera-relative versus target-relative mode flag
- target-focus movement speed modifier
- strafe, retreat, or approach tuning if used
- target-facing bias
- target-focus release or transition assumptions if needed
- movement-mode debug label

This data must not decide target validity or combat validity. It only supports how focused movement feels and reads.

### 16.5 Dodge Data

Minimum tunable dodge data may include:

- dodge direction mode
- dodge distance
- dodge speed or duration
- dodge startup duration
- dodge evade or avoidance phase duration if supported by `Combat Core`
- dodge recovery duration
- dodge steering allowance if any
- dodge cooldown or spam-prevention rule if needed
- neutral or backstep behavior if used

This data supports dodge movement expression only. `Combat Core` still validates dodge success or failure.

### 16.6 Combat Action Movement Restriction Data

Minimum tunable combat-action movement restriction data may include profiles for:

- `light attack`
- `heavy attack`
- `parry`
- `counter`
- `hit reaction`
- `recovery`

Each restriction profile may define:

- movement allowed, reduced, or locked
- speed multiplier
- facing allowed or constrained
- correction allowance
- recovery movement restriction
- debug label

These restrictions must come from explicit gameplay state or context, not from animation alone.

### 16.7 Recovery Data

Minimum tunable recovery data may include:

- dodge recovery duration
- `light attack` recovery duration
- `heavy attack` recovery duration
- parry recovery duration
- counter recovery duration
- hit-reaction recovery duration
- recovery movement speed modifier
- recovery interrupt or cancel permissions if any

For M0:

- recovery may start simple or generic
- recovery should remain easy to tune
- animation clip length must not secretly define recovery truth

### 16.8 Hit Reaction Movement Data

Minimum tunable hit-reaction movement data may include:

- hit-reaction control-suppression duration
- hit-reaction movement lock or reduction
- small displacement or knockback amount if used
- knockback direction rule if used
- transition into recovery
- `Disabled / ControlSuppressed` behavior if needed

Full `Health / Damage / Hit Reaction` data is deferred. `Player Locomotion` only needs provisional movement-response data for M0.

### 16.9 Root Motion / Animation Sync Data

Root motion remains an open decision.

If root motion is used later, data may need to define:

- when root motion is allowed
- when root motion is scaled
- when root motion is ignored
- how root motion requests are validated
- any animation-sync request labels later

For M0:

- locomotion should not require root-motion data to pass basic feel testing
- root motion and animation sync data must not become authoritative gameplay truth

### 16.10 Debug Display Data

Minimum tunable debug-display configuration may include:

- locomotion debug enabled
- movement-input debug enabled
- facing debug enabled
- dodge debug enabled
- recovery debug enabled
- combat movement restriction debug enabled
- hit-reaction debug enabled
- camera or target-focus coordination debug enabled
- Animator/FSM mismatch debug enabled
- debug verbosity level
- debug labels matching GDD state names

This debug configuration exists to speed up diagnosis and tuning, not to become a permanent player-facing layer.

### 16.11 Hardcoded vs Authored Guidance

For M0, it is acceptable to hardcode temporarily:

- one basic grounded movement setup
- one dodge action
- one simple target-focus movement mode
- simple movement restriction profiles
- simple recovery behavior
- simple hit-reaction response
- debug labels

The following should remain easy to tune even if the first implementation is simple:

- movement speed
- acceleration and deceleration
- rotation or facing responsiveness
- dodge distance, timing, and recovery
- action movement restrictions
- recovery durations
- hit-reaction control suppression
- target-focus movement modifiers

The following should not be deeply hardcoded because they are likely to change during feel tuning:

- dodge phase timing
- movement restriction priority
- action-lock behavior
- recovery or cancel permissions
- root-motion authority behavior
- facing-correction rules
- values likely to change during movement feel testing

### 16.12 Data Table

| Data Area | Tunable Values | Why It Matters | M0 Requirement | Can Be Deferred? |
| --- | --- | --- | --- | --- |
| `Grounded Movement` | Speed, acceleration, deceleration, smoothing | Defines baseline grounded duel feel | Required | No |
| `Facing / Orientation` | Facing responsiveness, target bias, correction allowance, correction speed | Preserves readable orientation | Required | No |
| `Target Focus Movement` | Focus mode, movement modifier, strafe/approach/retreat tuning | Shapes duel-focused movement feel | Recommended | No |
| `Dodge` | Direction mode, distance, startup, evade phase, recovery, steering allowance | Defines the main movement-based defense | Required | No |
| `Combat Action Restrictions` | Allowed/reduced/locked movement, speed multiplier, facing constraints | Preserves commitment and fairness | Required | No |
| `Recovery` | Per-source or generic recovery durations, movement modifier, cancel rules | Controls return to readable control | Required | No |
| `Hit Reaction Movement` | Suppression duration, movement reduction, displacement if any | Makes failure readable | Recommended | No |
| `Root Motion / Animation Sync` | Root-motion use flags, allow/ignore/scale assumptions, sync labels later | Prevents presentation from owning movement truth | Optional | Yes |
| `Camera Coordination` | Focus-mode assumptions, basis mode, coordination labels | Keeps movement/camera contract tunable | Recommended | No |
| `Debug Display` | Toggles, verbosity, debug labels | Enables intentional tuning and diagnosis | Required | No |

### 16.13 Anti-patterns

The following should be treated as failures for M0:

- building a full locomotion data framework before one duel works
- hiding all movement values in code
- data deciding combat validity
- dodge data guaranteeing success
- target-focus data auto-solving spacing
- animation clip length defining recovery
- root-motion data overriding gameplay truth
- too many movement profiles for M0
- data split across too many places
- debug labels not matching GDD state names
- tuning stylish mobility before grounded duel feel

### 16.14 Open Questions

The following questions remain unresolved:

- whether M0 locomotion data starts as simple constants or authored assets
- whether movement, facing, and dodge data should be separate or grouped
- whether recovery durations are generic or per-action
- whether dodge timing is authored from day one
- whether root-motion data is needed at all for M0
- whether target-focus movement mode is data-authored or fixed
- whether movement restriction profiles should exist before implementation
- whether debug configuration is shared with the M0 combat/camera overlay

## 17. Presentation Boundaries

The purpose of this section is to define what presentation systems may communicate for `Player Locomotion`, and what they must not own. `Player Locomotion` owns movement state truth, movement input interpretation, facing support, dodge displacement, action movement restrictions, recovery movement, hit-reaction movement response, and locomotion debug truth. `Combat Core` owns combat action validity and results. `Lock-On & Combat Camera` owns framing and target-focus readability. Presentation systems communicate locomotion state, but must not secretly define it.

### 17.1 Presentation Boundary Purpose

This boundary should clarify:

- how locomotion is communicated visually and audio-wise
- which systems may react to locomotion state
- which systems must remain presentation-only
- how to avoid presentation hiding gameplay truth
- how to keep M0 testable without final assets

The goal is not to reduce presentation value. The goal is to stop presentation from becoming a hidden source of movement truth.

### 17.2 Animation Presentation Boundary

The Animator may present:

- idle stance
- grounded movement
- target-focus or duel movement
- dodge
- parry pose
- `light attack` and `heavy attack` movement visuals
- counter movement visuals
- hit reaction
- recovery
- `Disabled / ControlSuppressed` pose if needed

The Animator must not own:

- locomotion state truth
- movement input interpretation
- dodge success or failure
- parry result
- hit result
- `CounterWindow`
- movement restriction truth
- recovery truth
- reveal validity

Animation expresses locomotion. It does not define locomotion.

### 17.3 VFX Presentation Boundary

`VFX` may communicate:

- dodge trail or subtle displacement cue
- parry readiness or impact feedback after confirmed result
- counter impact after confirmed result
- hit-reaction feedback
- restrained memory distortion response after valid reveal context
- ground-contact or movement polish if useful

`VFX` must not:

- decide whether dodge succeeded
- decide whether parry succeeded
- decide whether counter is valid
- imply `CounterWindow` when it is not open
- imply reveal validity before `Memory` / `Combat` context allows it
- obscure enemy telegraph, player recovery, or spacing readability

If VFX become clearer than gameplay truth, the duel has already drifted too far into presentation authority.

### 17.4 SFX / Audio Boundary

`Audio` may communicate:

- footstep weight
- dodge movement sound
- parry input or impact feedback
- attack effort or impact after confirmed hit
- counter impact
- hit reaction
- recovery/control-return cue if useful
- subtle memory cue after valid reveal context

`Audio` must not:

- imply success before `Combat Core` confirms result
- hide timing readability
- replace debug or visual clarity
- create feedback that contradicts gameplay state

Audio should reinforce locomotion and combat readability, not rewrite it.

### 17.5 Camera Feedback Boundary

`Lock-On & Combat Camera` may communicate:

- grounded movement readability
- target-focus orientation
- dodge displacement
- parry or counter impact after confirmed result
- hit-reaction feedback
- recovery and reset readability
- restrained reveal support after valid context

The camera must not:

- decide movement mode
- decide dodge direction
- decide parry or counter success
- force locomotion state
- hide recovery
- hide enemy punish window
- turn reveal into a cutscene in M0

The camera helps the player understand locomotion. It must not secretly own it.

### 17.6 UI / HUD Boundary

`UI` may communicate:

- optional target-focus indicator
- optional debug-only locomotion state
- optional movement or recovery state for development
- optional player-state visibility during testing

`UI` must not:

- become required to understand basic movement
- replace readable animation, camera, or spacing
- promise a final HUD for M0
- decide gameplay state

The duel should still read without production HUD support.

### 17.7 Debug Presentation Boundary

`Debug` may communicate:

- locomotion state truth
- transition reasons
- input interpretation
- facing mode
- dodge phase
- restriction source
- recovery source
- hit-reaction state
- camera or target-focus coordination
- Animator/FSM mismatch

`Debug` must not:

- alter gameplay state
- force accepted transitions
- become player-facing UI
- mask unclear player-facing feedback

Debug explains locomotion truth. It does not replace readable locomotion presentation.

### 17.8 Memory / Reveal Presentation Boundary

Memory-related presentation may communicate:

- brief visual or audio response after valid reveal context
- restrained distortion tied to meaningful combat success
- post-counter emotional feedback

Memory presentation must not:

- trigger reveal validity by itself
- imply memory progression without `Memory State` acceptance
- hide locomotion recovery
- hide enemy reset or next telegraph
- turn every dodge or hit into reveal feedback

Reveal must remain meaningful and rare enough to support the duel instead of overwhelming it.

### 17.9 Presentation Timing Rules

For M0, the timing rules should remain explicit:

- presentation should follow accepted gameplay state
- success feedback should happen after confirmed result
- anticipation feedback may support readability, but must not imply success
- recovery visuals should align with gameplay recovery
- `VFX`, `Audio`, and camera shake should not fire from raw input alone unless clearly input-feedback only
- animation timing mismatch should be treated as a presentation issue, not as gameplay truth

This keeps timing authority in gameplay systems even when presentation becomes richer later.

### 17.10 M0 Placeholder Guidance

For M0, the following placeholders are acceptable:

- simple animation clips
- primitive debug visualizers
- basic movement or dodge `VFX`
- simple audio placeholders
- minimal camera feedback
- text debug overlay

The following are not required for M0:

- final katana animation set
- polished animation layers
- `Avatar Mask` polish
- final `VFX`
- final `Audio`
- final `HUD`
- cinematic reveal sequence

The duel should be testable before any of these are finished.

### 17.11 Cross-System Boundary Table

| Presentation System | May Communicate | Must Not Own | Timing Rule | M0 Requirement |
| --- | --- | --- | --- | --- |
| `Animator` | Movement pose, attack/dodge/parry/counter/recovery visuals, hit reaction | Locomotion truth, combat result truth, recovery truth | Follow accepted gameplay state | Required |
| `Animation Layers / Avatar Mask` | Optional visual blending and polish | Gameplay truth, movement restrictions, combat validity | Only after accepted gameplay state | Optional |
| `Root Motion` | Visual displacement support if used | Dodge/parry/counter success, movement truth, recovery truth | Must be validated by gameplay state | Optional / open |
| `VFX` | Dodge trail, impact accents, hit feedback, restrained reveal distortion | Combat validity, `CounterWindow`, reveal validity | Fire after confirmed context | Optional |
| `Audio` | Footsteps, dodge/parry/counter/hit cues, subtle reveal cue | Combat validity, contradictory result truth | Follow confirmed or clearly input-only feedback | Optional |
| `Camera Feedback` | Orientation readability, dodge/counter/recovery readability, restrained reveal support | Movement mode truth, movement state truth, combat validity | Follow valid locomotion/combat/memory context | Required |
| `UI / HUD` | Optional focus indicator, development-only locomotion info | Gameplay truth, readability ownership | Supplemental only | Optional |
| `Debug Overlay` | State truth, reasons, mismatch, coordination traces | Gameplay authority, player-facing truth | Reflect current authoritative state | Required |
| `Memory Reveal Presentation` | Brief post-counter emotional response | Reveal validity, memory progression truth | Only after valid reveal context | Optional |

### 17.12 Failure Conditions

Presentation boundaries fail if:

- animation becomes the real locomotion FSM
- `VFX` imply dodge, parry, or counter success before confirmation
- `Audio` contradicts `Combat Core` result
- camera hides movement restriction or enemy punish state
- `UI` is required to understand movement
- debug is the only way to understand player-facing movement
- reveal presentation triggers without valid context
- root motion changes gameplay result invisibly
- final assets are required to validate M0 movement feel

These failures make it impossible to tell whether locomotion itself is working.

### 17.13 Anti-patterns

The following should be treated as failures for M0:

- presentation-first combat where visuals decide truth
- hiding movement locks inside animation clips
- firing impact `VFX` from input instead of confirmed hit
- camera shake before result confirmation
- dodge trail implying invulnerability for the entire dodge
- parry glow implying success before timing validation
- recovery visible only in animation but not gameplay state
- `UI` compensating for unreadable movement
- reveal `VFX` spam after every hit
- polishing animation layers before basic movement feel works

### 17.14 Open Questions

The following questions remain unresolved:

- whether M0 needs any player-facing `UI` for movement state
- whether dodge gets a subtle `VFX` trail or stays animation-only
- whether parry has anticipation `VFX` or only result `VFX`
- whether counter uses camera or audio feedback in M0
- whether reveal presentation is included in locomotion tests or only in Combat/Memory tests
- whether root motion is allowed in placeholder animations
- whether Animator/FSM mismatch should be shown through the debug overlay
- whether final presentation boundaries should become an ADR later

## 18. Technical Boundaries

The purpose of this section is to define the technical ownership boundaries for `Player Locomotion` in M0. These boundaries should keep locomotion small, testable, inspectable, and focused on one readable duel rather than allowing it to grow into a full character-controller, RPG-movement, or presentation-owned system.

### 18.1 Technical Boundary Purpose

This boundary should clarify:

- what `Player Locomotion` owns technically
- what it exposes to other systems
- what it consumes from other systems
- what it must not depend on directly
- what must remain presentation-only
- how to keep locomotion testable, inspectable, and M0-scaled

The core goal is to keep movement truth explicit and separate from combat truth, camera truth, and animation truth.

### 18.2 Player Locomotion Owns

`Player Locomotion` technically owns:

- locomotion state model
- movement input interpretation
- grounded movement response
- facing and orientation support
- dodge movement expression
- movement restrictions
- recovery movement flow
- hit-reaction movement suppression
- disabled or control-suppressed movement state
- locomotion debug data
- movement-facing context exposed to other systems if needed

This ownership means:

- it owns movement truth, not combat truth
- it owns movement response, not animation truth
- it owns player movement state, not camera state

### 18.3 Player Locomotion May Consume

`Player Locomotion` may consume read-only or validated context from:

- `Input Mapping`: movement input, dodge input, action input intent
- `Combat Core`: valid action-lock or recovery context, dodge/parry/counter result context if needed
- `Lock-On / Target Context`: target focus active, current target, target direction
- `Camera Context`: camera-relative movement basis if using camera-relative movement
- `Health / Damage / Hit Reaction`: valid hit-reaction context if available
- `Ground / Physics Query`: grounded state, collision, or movement constraints if needed
- `Debug Overlay`: output channel for locomotion debug

Consumed context should not create circular ownership, and `Player Locomotion` should not pull hidden global state through service-locator patterns.

### 18.4 Player Locomotion May Expose

`Player Locomotion` may expose:

- current locomotion state
- movement phase
- current movement input
- interpreted movement direction
- current speed
- facing mode
- player facing direction
- `dodge active / dodge phase`
- `recovery active / recovery source`
- `movement restricted / restriction source`
- `hit reaction movement suppression active`
- grounded state
- target-facing support context if needed
- debug snapshot

This exposed state should be for observation and coordination. Mutable internals should stay internal. Later architecture should prefer clear read-only snapshots, events, or contracts.

### 18.5 Must Not Own

`Player Locomotion` must not own:

- combat action validity
- hit detection
- damage calculation
- parry timing success
- dodge success/failure validation
- counter validity
- `CounterWindow`
- enemy intent or telegraph truth
- memory reveal validity
- target selection truth
- camera framing state
- Animator State Machine truth
- `VFX`/`Audio` result truth
- save/load progression
- RPG stats or stamina economy unless explicitly added later

This prevents locomotion from quietly absorbing responsibilities that belong to combat, enemy, memory, camera, or progression systems.

### 18.6 Dependency Direction

The technical dependency direction should remain explicit.

Allowed direction:

- core contracts may be shared upward
- `Player Locomotion` may depend on core contracts
- `Combat Core` may observe locomotion context through contracts
- camera may observe locomotion context through contracts
- debug may observe locomotion debug snapshot
- presentation may observe locomotion state

Avoid:

- `Player Locomotion` directly depending on `UI` implementation
- `Player Locomotion` directly depending on `VFX` or `Audio` implementation
- `Combat Core` depending on Animator state
- camera forcing locomotion state
- Animator driving locomotion truth
- circular references between camera and locomotion
- global service-locator access for movement state

This keeps movement readable in architecture as well as in play.

### 18.7 Pure C# FSM Technical Rule

For M0, locomotion gameplay state should be represented by a pure C# FSM or equivalent explicit state model.

The rule should remain:

- `MonoBehaviour` may act as Unity adapter or driver
- the Animator observes accepted state
- the FSM should be inspectable and debug-visible
- state transitions should have accepted or rejected reasons where useful

M0 does not require an over-engineered generic FSM framework. A simple explicit state model is preferred over abstract complexity.

### 18.8 Unity Character Controller / Rigidbody / Transform Boundary

Movement implementation remains an open technical decision.

Possible approaches include:

- `CharacterController`
- `Rigidbody`
- custom controller
- `Transform`-based prototype movement

For M0:

- the final choice should be based on feel, collision needs, and simplicity
- one flat duel arena allows simpler assumptions
- whichever approach is used must preserve debug truth and movement restriction rules

Physics may assist movement and collision, but it should not secretly decide combat truth. Physics chaos should be avoided in M0. Root motion, physics, and transform movement must not contradict FSM state.

### 18.9 Root Motion Technical Boundary

Root motion remains open.

If root motion is used:

- root motion is movement-expression data, not combat authority
- `Player Locomotion` must still expose movement state and restriction truth
- `Combat Core` still validates hit, dodge, parry, and counter results
- root-motion displacement should be debug-visible if it affects feel

Root motion must not:

- secretly decide dodge success
- bypass movement restrictions
- create hidden counter alignment
- let animation clip length define gameplay recovery

This keeps root motion subordinate to the gameplay state model.

### 18.10 VContainer / Lifetime Scope Boundary

`Player Locomotion` should live in gameplay or combat scene scope, not `ProjectRoot`.

For M0:

- locomotion truth belongs in gameplay/combat scene scope
- root scope must not own current player locomotion truth
- locomotion services and components should be scene/session scoped
- player movement should not become a global singleton
- dependency injection should support explicit composition and testing

If generated DI tooling is used later, it should register pure C# services where appropriate, while scene objects and Unity components remain explicitly composed.

### 18.11 R3 / Reactive Observation Boundary

`R3` may be used for observation, debug, or event streams if useful, but it must not hide movement truth.

For M0:

- `R3` may expose read-only locomotion/debug observation
- `R3` should not hide timing truth for dodge, recovery, or combat locks
- hot movement decisions should remain explicit and inspectable
- over-reactive architecture should be avoided before M0 feel is proven

This keeps movement behavior debuggable and local instead of spreading it across hidden reactive chains.

### 18.12 Input System Boundary

The input ownership split should remain:

- `Input Mapping` owns raw input and action mapping
- `Player Locomotion` interprets movement input into movement direction or state requests
- `Combat Core` validates combat action requests
- input buffering and cancel rules should remain conservative for M0
- rejected movement or action requests should be debug-visible if useful

This keeps input interpretation explicit without blurring movement and combat ownership.

### 18.13 Testing Boundary

M0 locomotion should remain testable before final content exists.

For M0:

- locomotion state transitions should be testable without final Animator
- movement restriction rules should be testable without final `VFX` or `Audio`
- dodge acceptance/rejection and phase flow should be inspectable
- recovery source and transition should be testable
- camera and target-focus coordination should be testable with simple context stubs if needed

This ensures locomotion feel can be validated early rather than waiting on full presentation completeness.

### 18.14 Technical Boundary Table

| Area | Player Locomotion Role | Allowed Dependency / Context | Must Not Depend On | M0 Technical Note |
| --- | --- | --- | --- | --- |
| `Input Mapping` | Interpret movement and locomotion requests | Raw movement input and intent | Direct UI button logic or hidden globals | Input owner remains separate |
| `Combat Core` | Apply movement response to valid combat context | Action lock, recovery, dodge/parry/counter outcome context | Combat validity logic inside locomotion | Combat truth stays external |
| `Enemy Intent` | Indirect coordination only | None directly required beyond combat-readability interplay | Enemy telegraph truth or attack validity | Enemy truth stays external |
| `Lock-On / Target Context` | Use target context for orientation support | Focus active, target, target direction | Target validity truth | Supports readable facing only |
| `Camera` | Coordinate read-only orientation/readability seam | Camera-relative basis if needed, camera context if exposed | Camera state authority over movement | Avoid circular ownership |
| `Animator` | Present accepted movement state | Visual playback only | Gameplay locomotion truth | Presentation-only |
| `Root Motion` | Optional movement expression support | Validated root-motion displacement if used | Root-motion-owned gameplay truth | Open decision |
| `Health / Hit Reaction` | Consume provisional hit-reaction context | Valid hit-reaction context | Full damage/severity ownership inside locomotion | Full reaction system deferred |
| `Physics / Grounding` | Assist movement and grounded checks | Grounded queries, collision constraints | Physics-chaos-owned combat truth | Keep simple for one duel |
| `VContainer Scope` | Keep locomotion local and testable | Scene/session-scoped composition | `ProjectRoot` movement singleton | Scene-owned truth |
| `R3 Observation` | Optional observation/debug stream | Read-only state/event observation | Hidden reactive state truth | Use only if it stays inspectable |
| `Debug Overlay` | Expose locomotion debug snapshots | Output path for debug | Owning locomotion truth | Debug is observer only |
| `UI / VFX / Audio` | Presentation observers only | Read-only locomotion-facing context if needed | Gameplay truth or movement authority | Optional for M0 |

### 18.15 Failure Conditions

Technical boundaries fail if:

- `Player Locomotion` validates combat outcomes
- `Combat Core` reads Animator state as truth
- camera directly forces locomotion state
- target focus auto-solves movement or spacing
- root motion bypasses gameplay restrictions
- movement truth is stored in `ProjectRoot` or a global singleton
- movement state is not debug-visible
- recovery exists only in animation clip length
- `UI`, `VFX`, or `Audio` become required to determine movement truth
- circular dependencies make movement behavior hard to reason about
- technical design becomes too generic before M0 feel is proven

These are architecture failures as much as feel failures.

### 18.16 Anti-patterns

The following should be treated as failures for M0:

- building a full character-controller framework before one duel works
- building a generic movement ability system for M0
- service-locator access to player movement everywhere
- Animator-driven gameplay state
- physics-driven combat truth
- root-motion-only dodge validation
- camera-owned movement mode changes
- global singleton player locomotion
- hidden reactive chains controlling dodge or recovery
- over-abstracting the state machine before tuning feel

### 18.17 Open Questions

The following questions remain unresolved:

- whether M0 uses `CharacterController`, `Rigidbody`, custom controller, or `Transform`-based movement
- whether locomotion FSM is a pure C# service plus `MonoBehaviour` adapter
- whether target-focus context comes from `Lock-On` system or shared `Target Context`
- whether movement mode is stored in locomotion or in target-focus context
- whether dodge timing is locomotion-owned phase data or `Combat Core`-shared timing
- whether root motion is allowed in the first playable M0
- whether `R3` is used for debug observation or avoided initially
- whether locomotion data starts as constants or authored assets
- whether movement-state snapshots should later be events, properties, or debug DTOs

## 19. Dependencies

### 19.1. Dependency Purpose

This section defines the upstream and downstream dependencies for `Player Locomotion` M0 so the team can see exactly what locomotion needs, what other systems may observe from it, and where the ownership boundaries must remain protected.

For M0, the dependency map should clarify:
- what `Player Locomotion` needs from other systems
- what other systems may need from `Player Locomotion`
- which dependencies are required to prove the first duel
- which dependencies are provisional and may stay lightweight
- which dependencies should be deferred until after M0
- how to avoid circular ownership between movement, combat, camera, and presentation

The goal is to keep locomotion small, testable, and explicit while still supporting one readable duel.

### 19.2. Upstream Dependencies

`Player Locomotion` may consume the following upstream context.

`Input Mapping`
- movement input
- dodge input
- parry / attack / counter intent if routed through shared action input
- input enabled / disabled context if needed

`Input Mapping` owns raw input collection and mapping. `Player Locomotion` owns how movement input is interpreted into movement direction, facing support, and locomotion state requests.

`Combat Core`
- valid combat action context
- action lock requests
- recovery context
- dodge / parry / counter result context if needed
- hit confirmation context if routed through `Combat Core`

`Combat Core` owns combat action validity and results. `Player Locomotion` should only react to validated or read-only combat context and must not infer combat truth on its own.

`Lock-On / Target Context`
- target focus active?
- current target if valid
- target direction
- target validity if exposed
- focus mode if needed

For M0, `Lock-On / Target Context` is the provisional owner of target focus truth, including `target focus active`, `current target`, `target validity`, and `target direction`. `Lock-On & Combat Camera` may read this context for framing and readability. `Player Locomotion` may read this context for orientation and facing support. Neither camera nor locomotion should independently own target focus truth.

This dependency may be a dedicated `Lock-On` system or a smaller shared target context. In either case, locomotion only needs enough target information to support orientation and movement interpretation.

`Lock-On & Combat Camera`
- camera-relative movement basis if camera-relative movement is used
- camera / framing context if needed for movement mode coordination

Camera context should remain read-only. Camera owns framing and readability. `Player Locomotion` owns movement interpretation and facing support. `Combat Core` owns combat validity and results. `Player Locomotion` must not depend on camera-owned truth for its own gameplay state.

`Enemy Intent & Telegraph`
- enemy telegraph / active / recovery / punish state indirectly through `Combat Core` or a read-only context if needed

Direct dependency on `Enemy Intent & Telegraph` is not required for basic movement truth in M0. Locomotion should not own or mirror enemy state.

`Health / Damage / Hit Reaction`
- valid hit reaction context
- reaction severity if available later
- control suppression / knockback request if available later

This remains provisional for M0. Locomotion only needs enough confirmed context to enter movement suppression or recovery states cleanly.

`Grounding / Physics / Collision`
- grounded state
- collision checks
- movement obstruction
- simple ground assumptions for M0

This dependency may stay minimal as long as locomotion can remain grounded, readable, and non-chaotic in one duel space.

`Data Authoring`
- movement tuning values
- facing tuning values
- dodge timing / distance values
- restriction / recovery tuning values
- debug config

`Data Authoring` provides tuning inputs only. It must not become a hidden owner of gameplay truth.

`Debug Overlay`
- output channel for locomotion debug snapshot

`Debug Overlay` is a consumer-facing surface for state inspection, not an authority over locomotion behavior.

### 19.3. Downstream Dependencies

The following systems may observe or consume locomotion output.

`Combat Core` may need:
- current locomotion state
- dodge phase / context
- movement / facing context
- action lock / recovery state if coordinated
- player position / facing context
- whether player is control-suppressed

`Combat Core` should observe locomotion through explicit context rather than by reading animation or camera state.

`Lock-On & Combat Camera` may need:
- player position
- player facing
- movement state
- dodge active / direction
- recovery active
- hit reaction active
- movement restricted
- counter / attack movement context if exposed

Camera should use this context to preserve readability, not to take ownership of movement.

`Enemy Intent & Telegraph` may need:
- usually no direct dependency
- player position / spacing through shared player or target context if needed

`Enemy Intent & Telegraph` should not depend on locomotion internals for its own truth.

`Health / Damage / Hit Reaction` may need:
- whether player is already in hit reaction or recovery
- whether control is suppressed
- movement response status if coordinated

This should remain a narrow coordination seam rather than a shared ownership layer.

`Animator / Presentation` may need:
- locomotion state
- movement speed
- facing mode
- dodge / parry / attack / counter movement state
- recovery / hit reaction state
- debug mismatch context if needed

Presentation should observe accepted gameplay state and not drive it.

`VFX / Audio` may need:
- confirmed locomotion or combat presentation events
- dodge started / ended
- recovery started / ended
- hit reaction started

These are presentation consumers only.

`UI / Debug` may need:
- locomotion debug snapshot
- state labels
- transition reasons
- movement restriction source
- camera / target-focus coordination state

This is especially important for M0 tuning because unreadable movement moments should be explainable.

### 19.4. Required M0 Dependencies

The following dependencies are required for M0:
- `Input Mapping`
- `Combat Core`
- `Lock-On / Target Context`, or an equivalent simple target context
- `Lock-On & Combat Camera` coordination
- `Debug Overlay`
- grounding / simple movement collision
- `Animator` presentation adapter, or simple placeholder animation
- `Data Authoring`, or temporary tuning constants

These may all start in minimal form. M0 does not require production-ready implementations, but it does require enough coordination to test movement feel, facing clarity, dodge readability, and duel spacing.

### 19.5. Provisional M0 Dependencies

The following dependencies are provisional for M0:
- `Health / Damage / Hit Reaction`
- direct `Enemy Intent` context
- `Root Motion`
- `R3` observation
- `VFX / Audio` feedback
- `UI / HUD` target indicators
- advanced data assets

These may become useful during iteration, but they should not block the first playable locomotion pass unless a real readability problem proves they are needed.

### 19.6. Deferred Dependencies

The following dependencies should be deferred until after M0:
- full traversal system
- boss movement / camera framework
- multi-enemy target cycling
- RPG stats / stamina economy
- progression upgrades
- parkour / climbing / swimming / jump systems
- advanced animation layer framework
- full hit reaction framework
- final HUD
- cinematic reveal / cutscene systems
- save / load movement persistence
- multiplayer / network movement

None of these should be allowed to expand the M0 locomotion scope before one readable duel works.

### 19.7. Dependency Direction Rules

The dependency direction for `Player Locomotion` should remain simple and explicit:
- `Player Locomotion` may consume read-only or validated context
- other systems may observe locomotion through explicit contracts, snapshots, or events
- mutable shared state should be avoided
- service locator access should be avoided
- camera and locomotion must not become circular authorities
- `Animator` must not become a gameplay dependency
- presentation must not become a locomotion truth dependency
- `Combat Core` and `Player Locomotion` should coordinate through explicit contracts, not hidden assumptions

The practical rule for M0 is that locomotion should be understandable even if camera, animation, and effects are reduced to minimal placeholders.

### 19.8. Contract / Interface Expectations

The following conceptual contracts are expected later:
- movement input context
- locomotion state snapshot
- facing / orientation context
- dodge context
- recovery context
- movement restriction context
- hit reaction movement context
- target focus context
- camera movement basis context
- debug snapshot

These names can remain conceptual for now. Exact interfaces should be decided later during architecture and `OpenSpec` work. The important M0 requirement is that the seams are explicit and that ownership does not blur across them.

### 19.9. Dependency Table

| System | Direction | What Player Locomotion Needs / Provides | Required For M0? | Boundary Note |
| --- | --- | --- | --- | --- |
| Input Mapping | Upstream | Needs movement, dodge, and action intent input | Yes | Raw input only; locomotion interprets movement meaning |
| Combat Core | Both | Needs valid action, recovery, and result context; may provide locomotion state and dodge/recovery context | Yes | `Combat Core` owns validity and result truth |
| Enemy Intent & Telegraph | Mostly upstream, preferably indirect | May need indirect telegraph or punish context; usually provides none directly to locomotion | No, provisional | Locomotion must not own enemy truth |
| Lock-On / Target Context | Both | Needs target focus active, current target, target direction; may provide facing and movement context | Yes | Provisional owner of target focus truth for M0; supports orientation, not combat validity |
| Lock-On & Combat Camera | Both | May need camera-relative basis; may provide movement state, dodge state, facing, and recovery context | Yes | Camera owns framing/readability only and must not force movement truth |
| Health / Damage / Hit Reaction | Both | May need valid hit reaction context; may provide suppression/recovery status if coordinated | No, provisional | Keep seam narrow and result-driven |
| Grounding / Physics / Collision | Upstream | Needs grounded state, obstruction, and collision constraints | Yes | Physics supports movement, not combat truth |
| Animator | Downstream | Provides locomotion state, speed, facing mode, dodge/recovery state | Yes, minimal | Presentation only; not gameplay authority |
| VFX | Downstream | Provides presentation events such as dodge start/end or hit reaction start | No, provisional | Must not define locomotion truth |
| Audio | Downstream | Provides presentation events for movement and recovery beats | No, provisional | Must not contradict gameplay state |
| UI / HUD | Downstream | May provide debug or optional player-facing state visibility | No, provisional | Must not become required for basic movement readability |
| Debug Overlay | Both | Needs debug output channel; provides locomotion debug snapshot | Yes | Debug explains behavior but does not change it |
| Data Authoring | Upstream | Needs tuning values, debug config, and restriction/recovery tuning | Yes | Tuning source only, not combat authority |
| VContainer / Lifetime Scope | Structural | Scene-scoped composition and lifetime | Yes, minimal | Locomotion truth must not live in `ProjectRoot` |
| R3 Observation | Structural / optional | May observe locomotion state and debug streams | No, provisional | Must not hide timing-critical truth |
| Root Motion | Structural / optional | May support movement expression if used | No, provisional | Must not override gameplay state or restrictions |

### 19.10. Failure Conditions

Dependency design fails if:
- `Player Locomotion` requires full `Combat Core` implementation before basic movement can be tested
- `Combat Core` reads `Animator` state as movement truth
- camera directly forces locomotion state
- `Animator` owns movement locks or recovery
- `VFX` / `Audio` / `UI` become required for movement truth
- `Enemy Intent` must be fully implemented before basic movement works
- target focus auto-solves movement or spacing
- dependencies create circular ownership
- movement cannot be tested with simple stubs or placeholders
- M0 depends on full traversal or production animation systems

### 19.11. Anti-patterns

Avoid the following:
- making `Player Locomotion` a global singleton
- letting every system directly mutate player movement
- using service locator access to read movement state everywhere
- overbuilding a generic dependency graph before M0 feel is proven
- requiring boss camera or multi-target systems for one duel
- coupling locomotion to final `UI / HUD`
- coupling locomotion to the final animation graph
- coupling locomotion directly to `VFX` or `Audio` implementation
- hiding dependency through animation events
- treating target focus as combat validity

### 19.12. Open Questions

The following dependency questions remain open:
- whether target context is owned by `Lock-On` or a shared `Target Context` system
- whether camera-relative basis comes from the camera system or a simpler Unity transform context
- whether `Combat Core` sends action locks to locomotion, or locomotion queries combat state
- whether hit reaction context comes from `Combat Core` or `Health / Damage / Hit Reaction`
- whether data is authored as constants or assets for M0
- whether `R3` is used for observation from day one
- whether `Debug Overlay` is shared across combat, camera, and locomotion or kept separate
- whether root motion requires its own coordination contract before implementation
- whether these dependencies are formalized now or during `/create-architecture`

## 20. Risks

### 20.1. Risk Purpose

This section identifies the main M0 risks that could cause `Player Locomotion` to fail as the movement layer for the first duel prototype.

For M0, risk analysis should clarify:
- what can make `Player Locomotion` fail M0
- what risks most directly affect combat feel
- what risks most directly affect duel readability
- what risks threaten technical ownership boundaries
- what risks should be tested earliest
- what risks should be deferred instead of over-solved now

The intent is to keep the team focused on proving one grounded duel rather than prematurely solving broader movement scope.

### 20.2. Major M0 Risks

#### A. Movement Feels Floaty

Risk description:
- player movement lacks weight, friction, or groundedness

Why it matters:
- `Glass Refrain` combat should feel deliberate and elegant
- floaty movement weakens the katana duel tone immediately

Early warning signs:
- player slides after input stops
- attacks feel disconnected from movement
- dodge feels like skating
- spacing mistakes feel unclear

Mitigation direction:
- tune acceleration and deceleration early
- restrict movement during committed actions
- test movement with a simple enemy telegraph as soon as possible
- prioritize grounded feel over raw speed

M0 priority:
- `High`

#### B. Dodge Becomes Auto-Escape

Risk description:
- dodge avoids too much danger regardless of timing, direction, or spacing

Why it matters:
- this weakens the `read → evade/parry → counter` loop
- it makes enemy telegraph and parry less meaningful

Early warning signs:
- player spams dodge safely
- dodge succeeds even when late or badly aimed
- counter becomes guaranteed after every dodge

Mitigation direction:
- keep dodge recovery readable
- keep dodge success `Combat Core`-owned
- tune avoidance and spacing carefully
- defer perfect dodge reward until the base dodge works

M0 priority:
- `High`

#### C. Facing / Target Focus Auto-Solves Combat

Risk description:
- target focus or facing correction makes positioning too easy

Why it matters:
- this removes spacing discipline
- it makes attacks, parries, and counters feel false rather than earned

Early warning signs:
- attacks snap into target
- counter always aligns perfectly
- player does not need to manage facing or spacing
- lock-on feels required for everything

Mitigation direction:
- keep facing correction small and debug-visible
- do not let target focus decide validity
- test no-lock-on and soft-focus cases
- keep `Combat Core` authoritative

M0 priority:
- `High`

#### D. Movement Restrictions Feel Like Input Loss

Risk description:
- player feels like controls are ignored without understanding why

Why it matters:
- commitment is good, but unclear lockouts feel bad
- recovery and action locks must feel fair rather than arbitrary

Early warning signs:
- dodge or attack input is ignored with no feedback
- player cannot tell when control returns
- restrictions feel inconsistent
- debug cannot explain blocked movement

Mitigation direction:
- expose restriction source in debug
- keep recovery short for M0
- make transition reasons explicit
- align animation with gameplay state

M0 priority:
- `High`

#### E. Animator Becomes Gameplay Truth

Risk description:
- movement locks, recovery, dodge, hit reaction, or action transitions are secretly controlled by `Animator`

Why it matters:
- this breaks testability
- it creates hidden timing bugs
- it conflicts with `Combat Core` authority

Early warning signs:
- changing clip length changes gameplay recovery
- `Animator` state is checked to validate dodge, parry, or counter
- animation events directly change gameplay state
- debug disagrees with actual movement

Mitigation direction:
- pure C# FSM owns state truth
- `Animator` observes accepted state
- animation events request only and never decide
- show `Animator` / FSM mismatch in debug if useful

M0 priority:
- `High`

#### F. Camera / Locomotion Fight Each Other

Risk description:
- camera framing and movement interpretation produce confusing direction or facing

Why it matters:
- dodge direction, spacing, and enemy telegraph readability depend on camera and locomotion agreeing

Early warning signs:
- input direction feels different during focus
- dodge direction changes unpredictably
- camera rotates during dodge or parry and confuses the player
- target-relative movement feels rigid or camera-relative movement loses enemy orientation

Mitigation direction:
- explicitly choose and test movement mode
- expose movement mode in debug
- keep camera movement restrained during timing-critical windows
- coordinate through read-only context rather than shared authority

M0 priority:
- `High`

#### G. Recovery Is Too Long Or Too Short

Risk description:
- recovery either makes combat sluggish or allows spam

Why it matters:
- recovery defines commitment and rhythm
- wrong recovery breaks duel feel before balance exists

Early warning signs:
- player can dodge or attack spam
- player feels stuck after every action
- counter timing feels unfair
- recovery differs between animation and gameplay state

Mitigation direction:
- start with short, readable recovery
- tune per action only if needed
- debug recovery source and duration
- do not use animation clip length as authority

M0 priority:
- `High`

#### H. Hit Reaction Feels Unfair Or Unclear

Risk description:
- player is hit but does not understand why, or control suppression feels random

Why it matters:
- failure must teach enemy timing and spacing
- unclear hit reaction makes combat feel unfair

Early warning signs:
- player cannot tell why the hit connected
- hit reaction interrupts without visible cause
- knockback makes spacing unreadable
- control returns unpredictably

Mitigation direction:
- keep hit reaction simple
- avoid complex knockback early
- use confirmed `Combat Core` result
- expose hit reaction and recovery in debug

M0 priority:
- `Medium / High`

#### I. Root Motion Creates Hidden Truth

Risk description:
- root motion moves the player, changes spacing, or affects dodge and counter outcomes without explicit gameplay authority

Why it matters:
- root motion can improve weight, but it can also hide state bugs and break trust in movement

Early warning signs:
- animation moves player into hit range or out of danger unexpectedly
- root motion bypasses movement locks
- counter alignment happens invisibly
- debug position or state does not explain movement

Mitigation direction:
- defer root motion if it is not needed
- if used, expose displacement in debug
- keep FSM and `Combat Core` authoritative
- treat root motion as expression, not truth

M0 priority:
- `Medium`

#### J. Overbuilding Locomotion Before M0 Feel Is Proven

Risk description:
- the team builds a full traversal, generic controller, or ability movement framework too early

Why it matters:
- this wastes time and hides the one real M0 question: does the duel movement feel good?

Early warning signs:
- jump, climb, or parkour appears before dodge feels good
- many movement profiles are created for one prototype
- a generic ability system appears before basic combat works
- implementation focuses on extensibility over feel

Mitigation direction:
- keep one grounded duel controller
- use the minimal state model
- defer traversal and advanced mobility
- validate with one enemy and one arena first

M0 priority:
- `High`

#### K. Debug Is Insufficient

Risk description:
- designers cannot explain movement, facing, dodge, restriction, or recovery behavior

Why it matters:
- M0 tuning depends on quick diagnosis
- hidden movement causes destroy trust in combat feel

Early warning signs:
- rejected dodge or action has no reason
- movement mode is unknown
- restriction source is unknown
- `Animator` / FSM mismatch is not visible when relevant

Mitigation direction:
- implement the required debug snapshot early
- keep labels matching GDD state names
- expose accepted and rejected transition reasons
- avoid noisy but low-signal debug

M0 priority:
- `High`

### 20.3. Highest Priority Risks

The following risks are the highest priority for M0:
- `Movement Feels Floaty`
- `Dodge Becomes Auto-Escape`
- `Facing / Target Focus Auto-Solves Combat`
- `Movement Restrictions Feel Like Input Loss`
- `Animator Becomes Gameplay Truth`
- `Camera / Locomotion Fight Each Other`
- `Recovery Is Too Long Or Too Short`
- `Debug Is Insufficient`

These should be tested before adding advanced movement, final animation polish, or extra enemy patterns. If these risks are not reduced first, later polish may hide the real locomotion problems instead of solving them.

### 20.4. Risk Mitigation Order

Recommended M0 testing order:

1. Test grounded movement feel alone.
2. Add facing and target-focus context.
3. Add dodge movement without an enemy.
4. Add enemy `Basic Attack A` telegraph.
5. Test dodge versus telegraph.
6. Add parry hold movement restriction.
7. Add light and heavy movement restrictions.
8. Add counter movement support.
9. Add hit reaction and recovery.
10. Add camera coordination pass.
11. Add `Animator` presentation pass.
12. Add `VFX` / `Audio` polish only after state truth is clear.

This order keeps the core locomotion risks visible instead of letting presentation or scope growth hide them.

### 20.5. Risk Table

| Risk | Priority | Early Warning Sign | Mitigation | Test Before M0 Pass? |
| --- | --- | --- | --- | --- |
| Movement Feels Floaty | High | Player slides and spacing feels unclear | Tune acceleration/deceleration and prioritize grounded feel | Yes |
| Dodge Becomes Auto-Escape | High | Dodge succeeds too safely and too often | Keep recovery readable and let `Combat Core` own success | Yes |
| Facing / Target Focus Auto-Solves Combat | High | Facing snaps and spacing stops mattering | Keep correction small and keep validity outside locomotion/camera | Yes |
| Movement Restrictions Feel Like Input Loss | High | Inputs seem ignored with no explanation | Expose restriction sources and transition reasons in debug | Yes |
| Animator Becomes Gameplay Truth | High | Clip length or animation events change gameplay timing | Keep pure C# FSM authoritative and `Animator` observational | Yes |
| Camera / Locomotion Fight Each Other | High | Direction feels inconsistent during focus or dodge | Explicitly test movement mode and keep camera restrained | Yes |
| Recovery Too Long / Too Short | High | Combat becomes spammy or sluggish | Start short, readable, and tune from debug-visible recovery | Yes |
| Hit Reaction Unclear | Medium / High | Player cannot explain why a hit connected | Keep hit reaction simple and tied to confirmed context | Yes |
| Root Motion Creates Hidden Truth | Medium | Animation displacement changes outcomes invisibly | Defer or tightly debug root motion | No, unless root motion is used |
| Overbuilding Locomotion | High | Framework scope grows before feel is proven | Keep one grounded duel controller and defer extras | Yes |
| Debug Insufficient | High | Tuning problems cannot be explained | Implement high-signal locomotion debug early | Yes |

### 20.6. Deferred Risks

The following risks are real but should be deferred until after M0:
- advanced traversal feel
- jump, climb, and parkour quality
- boss arena locomotion
- multi-enemy movement pressure
- stamina or resource economy
- animation layer polish
- `Avatar Mask` blending complexity
- root motion production pipeline
- long-term controller scalability
- accessibility movement options
- controller / gamepad tuning
- final hit reaction categories

These should not block M0 unless they directly affect the first duel prototype.

### 20.7. Failure Conditions

`Player Locomotion` risk management fails if:
- the team polishes animation before movement truth works
- dodge is tuned without enemy telegraph readability
- target focus hides spacing problems
- movement lockouts are not debug-visible
- `Animator` controls gameplay timing
- root motion changes outcomes invisibly
- recovery is tuned only by clip length
- basic movement cannot be tested without full `Combat Core`
- the team adds traversal before grounded duel movement is satisfying

### 20.8. Anti-patterns

Avoid the following:
- solving future traversal before the current duel movement works
- adding perfect dodge before the basic dodge works
- using lock-on to hide poor facing rules
- using animation polish to hide bad movement
- treating floaty movement as "fix later"
- tuning recovery by animation clip length
- letting camera compensate for unclear dodge direction
- adding many data profiles before one profile feels good
- using debug only after bugs appear
- accepting hidden state because "it looks okay"

### 20.9. Open Questions

The following locomotion risk questions remain open:
- which movement implementation approach carries the least risk for M0?
- should root motion be deferred completely until base movement works?
- how much facing correction is acceptable before it feels like auto-aim?
- how short can recovery be before spam appears?
- how much dodge safety is acceptable without making parry obsolete?
- should movement feel be tested before full camera lock-on?
- how much debug must exist before tuning starts?
- should no-lock-on movement remain viable in M0?
- what is the minimum animation quality needed to judge locomotion feel?

## 21. Open Questions

### 21.1. Open Questions Purpose

This section consolidates the unresolved `Player Locomotion` questions that still matter before M0 implementation planning begins.

It exists to:
- prevent hidden assumptions
- identify decisions that materially affect implementation
- separate M0 blockers from tuning questions
- avoid over-solving future traversal or combat problems too early
- keep `Player Locomotion` aligned with `Combat Core`, `Lock-On & Combat Camera`, `Animator`, and `Debug`

The goal is not to answer every question immediately. The goal is to make sure the team knows which questions must be resolved now, which can be explored during tuning, and which should wait until after M0.

### 21.2. Must Answer Before M0 Implementation

The following questions should be answered before M0 implementation planning starts.

`A. Movement Implementation Approach`
- Will M0 use `CharacterController`, `Rigidbody`, a custom kinematic controller, or a `Transform`-based prototype movement approach?
- Why it matters:
  - this affects collision, grounding, tuning, testing, and animation or root motion coordination

`B. Movement Mode During Target Focus`
- Is focused movement camera-relative, target-relative, or hybrid?
- Why it matters:
  - this affects dodge direction, facing, camera coordination, and player comfort

`C. Facing Rule During Target Focus`
- Does target focus fully lock player facing to the enemy, bias facing, or only provide target direction context?
- Why it matters:
  - this affects spacing discipline and whether lock-on feels like an auto-solve

`D. Dodge Direction Model`
- Is dodge input-relative, camera-relative, target-relative, or side-step/backstep focused during lock-on?
- Why it matters:
  - this affects readability, player agency, and camera coordination

`E. Dodge Safety Model`
- Does dodge use displacement only, an avoidance window, i-frames, or `Combat Core` dodge validation based on timing and spacing?
- Why it matters:
  - this determines whether dodge feels earned or becomes auto-escape

`F. Dodge Phase Model`
- Is `Dodge` a single state with timing data, or does it use startup / evade / recovery sub-phases?
- Why it matters:
  - this affects debug, tuning, `Combat Core` validation, and recovery clarity

`G. Combat Action Movement Locks`
- Do light attack, heavy attack, parry, and counter fully lock movement, reduce movement, or use per-action restriction profiles?
- Why it matters:
  - this defines commitment and prevents spam or floatiness

`H. Recovery Model`
- Is recovery generic, source-specific, or per-action authored?
- Why it matters:
  - this affects combat rhythm, tuning speed, and action commitment

`I. Hit Reaction Ownership`
- Does M0 hit reaction context come from `Combat Core`, `Health / Damage / Hit Reaction`, or a provisional contract?
- Why it matters:
  - this prevents duplicate ownership and unclear control suppression

`J. Root Motion Policy For M0`
- Is root motion completely deferred, allowed only visually, or allowed for specific actions under locomotion authority?
- Why it matters:
  - this affects movement truth, animation sync, and debug reliability

`K. Pure C# FSM Shape`
- Is locomotion a pure C# service with `MonoBehaviour` adapter, or a simpler `MonoBehaviour`-driven prototype with an explicit state model?
- Why it matters:
  - this affects testability, `VContainer` composition, and implementation speed

`L. Debug Minimum Before Tuning`
- What locomotion debug data must exist before movement tuning starts?
- Why it matters:
  - tuning without debug risks hidden state bugs and false feel conclusions

`M. Target Context Ownership`
- Is target context owned by `Lock-On`, a shared `Target Context` system, or a camera/lock-on coordination contract?
- Why it matters:
  - this affects dependency direction and prevents camera/locomotion circular ownership

`N. Movement Data Format`
- Are movement, facing, dodge, and recovery values hardcoded temporarily, stored as constants or config, or authored as data assets?
- Why it matters:
  - this affects iteration speed and future tuning

### 21.3. Can Answer During M0 Tuning

The following questions should be answered through tuning and playtest iteration rather than blocking initial implementation.

`A. Exact Movement Speed / Acceleration / Deceleration`
- tune by feel once the controller exists

`B. Exact Rotation / Facing Responsiveness`
- tune after camera and target focus behavior are testable

`C. Amount Of Facing Correction`
- adjust once attacks and counters are readable

`D. Dodge Distance / Duration / Recovery`
- tune against `Basic Attack A`

`E. Whether Dodge Can Be Steered After Start`
- tune only if dodge feels too rigid or too floaty

`F. Parry Micro-Movement`
- decide after parry timing and readability exist

`G. Light Attack Movement Allowance`
- tune after first light attack implementation

`H. Heavy Attack Movement Commitment`
- tune after heavy attack has readable risk

`I. Counter Alignment Amount`
- tune after valid `CounterWindow` flow exists

`J. Hit Reaction Duration`
- tune after the first enemy hit is readable

`K. Knockback Need`
- add only if failure readability needs it

`L. Recovery Durations Per Source`
- start simple, split only if feel requires it

`M. Camera-Relative / Target-Relative Comfort`
- test with actual camera framing

`N. Animator / FSM Mismatch Visibility`
- decide once placeholder animations exist

`O. Debug Verbosity`
- tune to avoid clutter while keeping important state visible

### 21.4. Defer After M0

The following questions are intentionally deferred until after M0.

`A. Full Traversal`
- jump, climb, vault, swim, parkour, and ledges

`B. Boss-Specific Locomotion`
- boss arenas, cinematic duels, and large-enemy framing

`C. Multi-Enemy Movement Pressure`
- target cycling, crowd spacing, and off-screen threats

`D. Perfect Dodge / Slow Motion Reward`
- only after the basic dodge, parry, and counter loop works

`E. Stamina / Resource Economy`
- only after base movement and combat commitment feel right

`F. Advanced Animation Layers / Avatar Mask System`
- optional polish after full-body M0 feel is proven

`G. Production Root Motion Pipeline`
- only after root motion policy and the base controller are stable

`H. Complex Hit Reaction Categories`
- light or heavy stagger, launch, knockdown, poise, and balance

`I. Accessibility Movement Options`
- camera assist, input assist, lock-on assist, and deeper remapping support

`J. Long-Term Controller Scalability`
- data-heavy movement profiles, upgrades, and advanced abilities

`K. Multiplayer / Network Movement`
- out of scope for single-player M0

`L. Open-World / Exploration Locomotion`
- `Glass Refrain` is semi-linear, so exploration movement can come later

### 21.5. Decision Priority Order

Recommended practical decision order before implementation:

1. Choose the movement implementation approach.
2. Choose the focused movement mode.
3. Choose the target-focus facing rule.
4. Choose the dodge direction model.
5. Choose the dodge safety and phase model.
6. Choose the combat action movement lock policy.
7. Choose the recovery model.
8. Choose hit reaction ownership for M0.
9. Choose the root motion policy.
10. Choose the locomotion FSM shape.
11. Choose the minimum debug requirements.
12. Choose the temporary data format.

This order reduces rework because later decisions depend on earlier movement and control assumptions.

### 21.6. Cross-System Questions

The following questions should be coordinated across system boundaries.

`Combat Core`
- What locomotion context does `Combat Core` need to validate dodge, parry, or counter?
- Does `Combat Core` request recovery or action locks, or does locomotion derive them from accepted action context?
- Does successful dodge open `CounterWindow` directly, or only through enemy whiff or punish?

`Lock-On & Camera`
- Who owns target focus state?
- May camera expose read-only context that `Player Locomotion` uses when selecting its own movement mode?
- Can camera request stabilization during dodge, parry, or counter without controlling movement?
- How is camera-relative movement basis exposed?

Camera may expose framing or camera-relative basis context, but `Player Locomotion` remains the owner of movement mode interpretation. Camera must not choose or force locomotion movement mode.

`Enemy Intent`
- Does locomotion need enemy state directly, or only through `Combat Core` or target context?
- How does `Basic Attack A` expose enough timing for dodge testing?

`Health / Hit Reaction`
- Who confirms hit reaction context?
- Is knockback part of M0?
- Does `Disabled / ControlSuppressed` belong here or in locomotion?

`Animator / Presentation`
- Are animation events allowed as validated timing requests?
- Is root motion allowed in M0?
- Is `Animator` visual state displayed in debug?

`Debug`
- Is locomotion debug separate or part of the shared M0 combat overlay?
- Are rejected inputs logged or only shown live?
- What debug data is mandatory before tuning starts?

### 21.7. Open Questions Table

| Question | Category | Decision Timing | Owner / Collaborating System | Why It Matters |
| --- | --- | --- | --- | --- |
| Which movement implementation approach should M0 use? | Movement | Must Answer Before M0 Implementation | Player Locomotion / Physics | It determines grounding, collision, and tuning workflow |
| Is focused movement camera-relative, target-relative, or hybrid? | Camera / Target Focus | Must Answer Before M0 Implementation | Player Locomotion / Lock-On & Camera | It shapes movement feel, dodge direction, and orientation |
| Does target focus bias facing or fully lock it? | Facing | Must Answer Before M0 Implementation | Player Locomotion / Lock-On | It affects spacing discipline and player control |
| What dodge direction model does M0 use? | Dodge | Must Answer Before M0 Implementation | Player Locomotion / Camera | It defines readability and agency |
| What is the dodge safety model? | Dodge | Must Answer Before M0 Implementation | Player Locomotion / Combat Core | It determines whether dodge feels earned or automatic |
| Does dodge use one state or explicit sub-phases? | Dodge | Must Answer Before M0 Implementation | Player Locomotion / Combat Core | It affects debug, timing, and validation seams |
| How are combat action movement locks modeled? | Combat Support | Must Answer Before M0 Implementation | Player Locomotion / Combat Core | It defines commitment and anti-spam behavior |
| Is recovery generic or source-specific? | Recovery | Must Answer Before M0 Implementation | Player Locomotion / Combat Core | It affects rhythm and tuning speed |
| Who owns hit reaction context in M0? | Hit Reaction | Must Answer Before M0 Implementation | Combat Core / Health / Player Locomotion | It prevents duplicate ownership |
| What is the root motion policy for M0? | Animation / Root Motion | Must Answer Before M0 Implementation | Player Locomotion / Animator | It protects gameplay truth and debug reliability |
| What shape does the locomotion FSM take? | Movement | Must Answer Before M0 Implementation | Player Locomotion / VContainer | It affects testability and implementation speed |
| What debug data must exist before tuning starts? | Debug | Must Answer Before M0 Implementation | Player Locomotion / Debug Overlay | It prevents hidden-state feel tuning |
| Who owns target context? | Camera / Target Focus | Must Answer Before M0 Implementation | Lock-On / Camera / Player Locomotion | It prevents circular ownership |
| Are movement values constants, config, or assets? | Data Authoring | Must Answer Before M0 Implementation | Player Locomotion / Data Authoring | It affects iteration speed |
| What exact movement speed feels right? | Movement | Can Answer During M0 Tuning | Player Locomotion | This is a feel-tuning question, not a blocker |
| How much facing correction is acceptable? | Facing | Can Answer During M0 Tuning | Player Locomotion / Lock-On | It depends on real duel readability |
| What dodge distance and recovery feel right? | Dodge | Can Answer During M0 Tuning | Player Locomotion / Combat Core | It should be tuned against `Basic Attack A` |
| Does parry allow micro-movement? | Combat Support | Can Answer During M0 Tuning | Player Locomotion / Combat Core | It depends on hold-ground readability |
| Does counter need alignment support? | Combat Support | Can Answer During M0 Tuning | Player Locomotion / Combat Core / Camera | It depends on actual counter feel |
| Is knockback needed for hit readability? | Hit Reaction | Can Answer During M0 Tuning | Player Locomotion / Health / Combat Core | It should only be added if failure readability needs it |
| How verbose should locomotion debug be? | Debug | Can Answer During M0 Tuning | Player Locomotion / Debug Overlay | It must stay high-signal without clutter |
| How should full traversal work? | Deferred Scope | Defer After M0 | Future locomotion / traversal systems | It does not help prove the first duel |
| How should boss locomotion differ? | Deferred Scope | Defer After M0 | Future boss/combat/camera systems | It is outside one-enemy M0 scope |
| Does M0 need perfect dodge or slow motion reward? | Deferred Scope | Defer After M0 | Future combat tuning | It should not precede basic dodge feel |
| How should advanced animation layers or Avatar Masks work? | Animation / Root Motion | Defer After M0 | Animator / Presentation | They are polish questions after full-body M0 feel works |
| How should long-term controller scalability be handled? | Deferred Scope | Defer After M0 | Architecture / future locomotion work | It should not block one grounded duel |

### 21.8. Failure Conditions

Open question management fails if:
- implementation begins with hidden assumptions
- camera-relative versus target-relative movement is left implicit
- dodge safety model is unclear
- root motion is allowed without authority rules
- recovery is implemented only by animation clip length
- `Combat Core` and `Player Locomotion` both own action locks
- target focus ownership is unclear
- debug is deferred until after tuning
- future traversal questions block M0
- the team treats all open questions as equally urgent

### 21.9. Anti-patterns

Avoid the following:
- answering deferred questions before M0 blockers
- implementing movement before choosing the dodge direction model
- tuning dodge before choosing the dodge safety model
- adding an `Avatar Mask` system to avoid deciding action locks
- using camera behavior to hide an unclear movement mode
- treating root motion as "just animation" when it changes gameplay position
- delaying debug until after combat feels wrong
- overbuilding data assets before one controller feels good
- turning open questions into full architecture prematurely

### 21.10. Recommended Next Step

The recommended next step is:
- answer the `Must Answer Before M0 Implementation` questions during `/review-all-gdds`, `/gate-check`, and `/create-architecture`
- do not answer deferred traversal, boss, or animation polish questions yet
- after completing this GDD, run a cleanup and readiness pass, then prepare the document for `/review-all-gdds`, `/gate-check`, and `/create-architecture`
- do not expand `Player Locomotion` scope before cross-GDD review

`Player Locomotion` is ready for M0 implementation planning once the must-answer questions are reviewed and either decided or explicitly accepted as prototype assumptions.

## 22. Acceptance Criteria For M0

### 22.1. Acceptance Purpose

The `Player Locomotion` system passes M0 when it proves the following:
- player movement feels grounded and deliberate
- movement supports the combat loop: `read → evade/parry → counter → reveal`
- dodge is readable and not an auto-escape
- facing and target focus help orientation without auto-solving combat
- movement restrictions support commitment without feeling random
- recovery and hit reaction are understandable
- `Animator` remains presentation-only
- debug can explain locomotion behavior

### 22.2. Required M0 Gameplay Scenario

The minimum playable locomotion scenario for M0 is one player versus one enemy in a simple duel arena.

The player should be able to:
- stand idle in a simple duel arena
- move toward, away from, and around one enemy
- understand current facing and enemy direction
- use target focus or equivalent orientation support
- observe `Basic Attack A` telegraph
- dodge with readable displacement
- parry or hold ground with readable facing support
- perform light and heavy actions with movement commitment
- counter after valid context if `Combat Core` opens the opportunity
- experience simple hit reaction when hit
- recover back to readable control
- reset to stable duel movement after each exchange

This scenario should demonstrate:
- `orient → reposition → read → evade/hold ground → recover → counter-position → reset`

### 22.3. Grounded Movement Criteria

Pass if:
- player movement feels grounded enough for a katana duel
- acceleration and deceleration do not feel overly floaty
- player can intentionally approach, retreat, and reposition
- spacing is readable
- movement can be tested without final animations
- movement state is debug-visible

Fail if:
- player slides or skates unintentionally
- movement feels disconnected from duel spacing
- player cannot judge position relative to the enemy
- final animation polish is required to understand basic movement

### 22.4. Facing / Orientation Criteria

Pass if:
- player facing is understandable
- target direction is understandable when target focus is active
- facing support helps readability
- facing correction, if used, is small and debug-visible
- facing support does not make attacks auto-hit or parries auto-succeed

Fail if:
- player frequently loses sense of facing
- target focus auto-solves combat positioning
- facing correction snaps invisibly
- lock-on becomes mandatory for every action without explicit decision

### 22.5. Dodge / Evade Criteria

Pass if:
- dodge has clear input, direction, displacement, and recovery
- dodge direction feels predictable
- dodge does not automatically avoid every attack
- failed dodge can be explained by timing, spacing, direction, or `Combat Core` result
- successful dodge can support enemy whiff or punish readability when appropriate
- dodge phase and result are debug-visible

Fail if:
- dodge becomes an all-purpose invincible escape
- dodge direction feels random
- dodge recovery can be bypassed accidentally
- dodge guarantees counter automatically
- dodge success is decided by animation or camera instead of `Combat Core`

### 22.6. Parry / Hold-Ground Criteria

Pass if:
- parry movement support preserves readable facing
- player can understand parry as a timing or hold-ground answer
- parry does not slide the player into success
- `Combat Core` remains responsible for parry timing and result
- parry movement restriction is debug-visible

Fail if:
- parry success depends on animation or camera movement
- parry movement auto-corrects positioning too much
- parry feels identical to dodge
- parry restriction feels random or unexplained

### 22.7. Combat Action Movement Criteria

Pass if:
- light attack feels quick but not weightless
- heavy attack feels more committed than light attack
- attack movement restrictions are readable
- counter movement or alignment, if used, feels intentional and grounded
- movement support does not decide hit or counter validity
- action locks and restrictions are debug-visible

Fail if:
- attacks freely slide through the enemy
- heavy attack has no commitment
- counter teleports or snaps without approval
- movement support makes `Combat Core` outcomes feel false
- animation clips secretly define action locks

### 22.8. Recovery Criteria

Pass if:
- recovery exists after dodge, attacks, parry or counter, or hit reaction where needed
- recovery prevents spam without making M0 feel sluggish
- player can tell when control returns
- recovery source is debug-visible
- recovery is not defined only by animation clip length

Fail if:
- recovery can be bypassed accidentally
- recovery feels random
- recovery is too long to test flow
- recovery is controlled only by `Animator`
- debug cannot explain recovery source

### 22.9. Hit Reaction Criteria

Pass if:
- player hit reaction is simple but readable
- being hit temporarily affects movement or control in an understandable way
- failure teaches timing or spacing
- hit reaction transitions cleanly into recovery or control
- hit reaction source is debug-visible

Fail if:
- player is hit with no understandable movement response
- hit reaction stun-locks the player in M0
- knockback makes spacing unreadable
- hit reaction contradicts `Combat Core` result
- hit reaction becomes a full damage framework inside locomotion

### 22.10. Camera / Target Focus Coordination Criteria

Pass if:
- movement and camera agree on orientation assumptions
- target focus helps the player read enemy direction
- camera does not make dodge direction unclear
- camera does not hide recovery, enemy punish, or the next telegraph
- camera and target focus do not own movement or combat validity
- coordination state is debug-visible

Fail if:
- camera secretly changes movement rules
- target focus auto-solves spacing
- dodge, parry, or counter readability is harmed by camera movement
- camera reset hides recovery or punish windows
- debug cannot explain movement mode during focus

### 22.11. Animation / FSM Boundary Criteria

Pass if:
- pure C# FSM or an explicit gameplay state model owns locomotion truth
- `Animator` is presentation-only
- animation can be placeholder quality for M0
- `Animator` / FSM mismatch can be diagnosed if it affects feel
- root motion, if used, does not secretly own gameplay truth

Fail if:
- `Animator State Machine` is the real gameplay FSM
- animation clip length defines recovery
- animation events apply gameplay results directly
- root motion decides dodge, parry, or counter outcomes
- final animation polish is required to validate locomotion behavior

### 22.12. Debug Criteria

Pass if debug can show:
- current locomotion state
- previous state and transition reason
- movement input and interpreted direction
- facing mode
- target focus active?
- dodge requested, accepted, or rejected
- dodge phase
- movement restricted?
- restriction source
- recovery active and recovery source
- hit reaction active and hit reaction source
- camera or target focus coordination mode
- `Animator` / FSM mismatch if useful

Fail if:
- movement cannot be diagnosed
- dodge rejection reason is unknown
- movement restriction source is unknown
- recovery source is unknown
- target focus changes movement invisibly
- debug data disagrees with actual behavior
- debug is required as player-facing UI

### 22.13. M0 Out Of Scope

The following are explicitly not required to pass `Player Locomotion` M0:
- final animation set
- final katana animation polish
- polished `Avatar Mask` or animation layer system
- full root motion pipeline
- jump, climb, parkour, swim, or broader traversal
- boss movement rules
- multi-enemy movement pressure
- perfect dodge or slow motion reward
- stamina or resource economy
- full hit reaction, poise, or knockback framework
- final HUD
- cinematic reveal camera
- open-world movement
- multiplayer or network movement

### 22.14. Acceptance Test Checklist

- [ ] Player can idle, move, and reposition in the duel arena.
- [ ] Player can understand facing and enemy direction.
- [ ] Target focus or equivalent orientation support works without auto-solving spacing.
- [ ] Basic movement feels grounded enough for M0.
- [ ] Dodge has readable direction, displacement, and recovery.
- [ ] Dodge does not automatically solve every enemy attack.
- [ ] Parry or hold-ground movement support is readable.
- [ ] Light attack movement feels quick but not weightless.
- [ ] Heavy attack movement feels committed.
- [ ] Counter movement or alignment, if used, is readable and not teleporting.
- [ ] Hit reaction temporarily affects movement or control and remains understandable.
- [ ] Recovery prevents spam and returns player to readable control.
- [ ] Camera or target focus does not hide dodge, recovery, punish, or telegraph readability.
- [ ] Animator is not gameplay truth.
- [ ] Movement restrictions are explicit and debug-visible.
- [ ] Debug can explain locomotion state, input, dodge, recovery, and restrictions.
- [ ] The loop `orient → reposition → read → evade/hold ground → recover → counter-position → reset` can be demonstrated repeatedly.

### 22.15. M0 Pass Statement

`Player Locomotion` M0 passes when the player can repeatedly fight one simple enemy in a small duel arena and movement consistently supports the `Glass Refrain` combat rhythm:

`calm orientation → readable threat → deliberate answer → committed recovery → intentional counter-position → stable reset`

The system does not need final animation, traversal, boss support, or advanced mobility. It only needs to prove that the player can move, dodge, hold ground, recover, and reorient in a way that makes the first katana duel feel readable, grounded, and emotionally restrained.

### 22.16. M0 Fail Statement

`Player Locomotion` M0 fails if movement feels floaty, dodge becomes an auto-escape, target focus auto-solves combat, recovery is hidden in animation, camera and locomotion fight each other, or debug cannot explain player movement behavior.
