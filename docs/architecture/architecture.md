# Glass Refrain M0 Architecture

> **Status**: Draft Architecture
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Scope**: `M0 — Katana Combat Feel Prototype`
> **Engine**: Unity 6000.3.x + URP
> **Language**: C#
> **Review Mode**: lean

## 1. Architecture Overview

### M0 Architecture Summary

`Glass Refrain` M0 is a tightly scoped, additive-scene Unity prototype built to prove one duel loop:

`read → evade/parry → counter → reveal`

The architecture is intentionally small and contract-first. It avoids a giant RPG framework, avoids DOTS/ECS, avoids global gameplay singletons, and keeps gameplay truth in explicit Pure C# state models with Unity components acting as adapters, composition roots, or presentation surfaces.

The M0 architecture is organized around these rules:

- `Combat Core` owns combat validation and result truth.
- `Player Locomotion` owns movement truth.
- `Input Mapping` owns raw input truth.
- `Lock-On / Target Context` owns target truth.
- `Lock-On & Combat Camera` owns framing and readability only.
- `Enemy Intent & Telegraph` owns enemy-side readability and punish truth.
- `Health / Damage / Hit Reaction` owns consequence truth.
- `Memory State` owns reveal acceptance and memory-side consequence truth.
- `Memory VFX Response` is downstream presentation only.
- `Encounter Framework` owns encounter lifecycle only.
- `Debug Overlay` is read-only presentation only.

### Design-To-Technical Translation

The GDD package translates into a small layered architecture:

- **Foundation Layer**
  - bootstrap
  - scene loading
  - DI composition
  - configuration
  - engine adapters
- **Core Gameplay Layer**
  - input intent
  - locomotion truth
  - combat truth
  - target truth
  - health/consequence truth
  - encounter truth
  - memory truth
- **Presentation Layer**
  - camera framing
  - animator adapters
  - memory VFX
  - debug overlay

### System Boundaries

Authoritative systems expose read-only snapshots, request/result contracts, or narrow event streams. Presentation systems observe those contracts but do not become hidden authorities.

### Dependency Direction

Preferred direction:

`Foundation`  
↑  
`Core gameplay systems`  
↑  
`Presentation / debug systems`

Forbidden direction:

- presentation owns gameplay truth
- camera owns movement or target truth
- animator owns combat, movement, or recovery truth
- debug owns gameplay state
- gameplay truth stored in project-root singleton state

## 2. Unity Project Structure

All authored project work lives under `Assets/_Project`.

### Code Folders

Recommended M0 code roots:

- `Assets/_Project/Code/Core`
- `Assets/_Project/Code/Infrastructure`
- `Assets/_Project/Code/Bootstrap`
- `Assets/_Project/Code/Input`
- `Assets/_Project/Code/Locomotion`
- `Assets/_Project/Code/Combat`
- `Assets/_Project/Code/Enemy`
- `Assets/_Project/Code/Targeting`
- `Assets/_Project/Code/Camera`
- `Assets/_Project/Code/Health`
- `Assets/_Project/Code/Memory`
- `Assets/_Project/Code/Encounter`
- `Assets/_Project/Code/VFX`
- `Assets/_Project/Code/UI`

### Content Folders

- `Assets/_Project/Content/Scenes`
- `Assets/_Project/Content/Prefabs`
- `Assets/_Project/Content/Data`
- `Assets/_Project/Content/Animation`
- `Assets/_Project/Content/Materials`
- `Assets/_Project/Content/VFX`
- `Assets/_Project/Content/Audio`
- `Assets/_Project/Content/UI`
- `Assets/_Project/Content/Art`

### Scene Folders

- `Assets/_Project/Content/Scenes/Bootstrap`
- `Assets/_Project/Content/Scenes/Systems`
- `Assets/_Project/Content/Scenes/Gameplay`
- `Assets/_Project/Content/Scenes/Camera`
- `Assets/_Project/Content/Scenes/UI`
- `Assets/_Project/Content/Scenes/Levels/TokyoAct1`
- `Assets/_Project/Content/Scenes/Prototypes/M0_KatanaCombat`

### Data Folders

- `Assets/_Project/Content/Data/Input`
- `Assets/_Project/Content/Data/Combat`
- `Assets/_Project/Content/Data/Locomotion`
- `Assets/_Project/Content/Data/Enemy`
- `Assets/_Project/Content/Data/Targeting`
- `Assets/_Project/Content/Data/Camera`
- `Assets/_Project/Content/Data/Health`
- `Assets/_Project/Content/Data/Memory`
- `Assets/_Project/Content/Data/Encounter`
- `Assets/_Project/Content/Data/Debug`

### Tests Folders

- `Assets/_Project/Tests/EditMode`
- `Assets/_Project/Tests/PlayMode`

### Third-Party Boundary

- `Assets/ThirdParty` is read-only unless explicitly approved.
- `Cinemachine`, `Input System`, `VContainer`, `R3`, `DOTween`, and other packages remain isolated behind assembly or adapter boundaries where practical.

## 3. Assembly Definition Plan

M0 should use a minimal assembly split with strict dependency direction.

### Minimal M0 Asmdef List

- `GlassRefrain.Core`
- `GlassRefrain.Infrastructure`
- `GlassRefrain.Bootstrap`
- `GlassRefrain.Input`
- `GlassRefrain.Locomotion`
- `GlassRefrain.Combat`
- `GlassRefrain.Enemy`
- `GlassRefrain.Targeting`
- `GlassRefrain.Camera`
- `GlassRefrain.Health`
- `GlassRefrain.Memory`
- `GlassRefrain.Encounter`
- `GlassRefrain.VFX`
- `GlassRefrain.UI`
- `GlassRefrain.Tests.EditMode`
- `GlassRefrain.Tests.PlayMode`

### Dependency Direction

Preferred dependency shape:

- `Core` references nothing
- `Infrastructure` references `Core`
- `Bootstrap` references `Core`, `Infrastructure`
- domain assemblies reference `Core`
- presentation assemblies reference `Core` plus presentation-safe domain contracts only
- tests reference the assemblies under test

### Forbidden Dependencies

- `Core -> anything`
- `Combat -> Camera`
- `Combat -> UI`
- `Combat -> VFX`
- `Locomotion -> Camera`
- `Locomotion -> UI`
- `Memory -> Camera`
- `Memory -> UI`
- `Targeting -> Camera`
- `Targeting -> UI`
- any runtime assembly -> test assembly

### Test Asmdef Plan

- `GlassRefrain.Tests.EditMode`
  - Pure C# FSMs
  - contracts
  - validation logic
  - data translation
- `GlassRefrain.Tests.PlayMode`
  - additive scene composition
  - DI composition
  - camera/gameplay/presentation coordination
  - acceptance smoke path

## 4. Scene Architecture

M0 uses additive scene loading from day one.

### Required Scenes

- `Bootstrap`
- `Systems`
- `Gameplay_CombatPrototype`
- `Camera_CombatPrototype`
- `UI_DebugOverlay`
- `Level_TokyoStreet_Blockout`

### Scene Responsibilities

#### Bootstrap

Owns:

- startup entry
- root configuration
- initial additive scene-set load

Does not own:

- combat truth
- locomotion truth
- encounter truth

#### Systems

Owns:

- persistent app-level services
- service adapters
- shared configuration access

Does not own:

- active duel state
- current player combat state
- current target truth

#### Gameplay_CombatPrototype

Owns:

- player root
- enemy root
- encounter root
- gameplay-scoped lifetime scope
- authoritative M0 runtime state

#### Camera_CombatPrototype

Owns:

- Cinemachine Brain host assumptions
- virtual camera objects
- camera coordinators

#### UI_DebugOverlay

Owns:

- debug UI Toolkit or equivalent overlay root
- read-only debug presentation

#### Level_TokyoStreet_Blockout

Owns:

- duel arena geometry
- blockout colliders
- spawn markers
- authored placements

### Additive Scene Loading Boundaries

M0 minimal composition:

1. `Bootstrap`
2. `Systems`
3. `Level_TokyoStreet_Blockout`
4. `Gameplay_CombatPrototype`
5. `Camera_CombatPrototype`
6. `UI_DebugOverlay`

Rules:

- level scenes do not own gameplay truth
- gameplay scene does not own persistent app lifetime
- camera scene does not own target or movement truth
- UI/debug scene does not own gameplay state

## 5. VContainer Lifetime Scope Plan

### ProjectRootLifetimeScope

Belongs in root:

- app bootstrap services
- scene loader/orchestration services
- global config access
- logging
- package adapters safe across all scenes

Must not belong in root:

- current combat state
- current player locomotion state
- current target truth
- encounter lifecycle truth
- current memory response truth

### Gameplay Scope

Belongs in gameplay scope:

- `Input Mapping` runtime adapter
- `Player Locomotion` service/FSM
- `Combat Core` service/FSM
- `Enemy Intent & Telegraph` service/FSM
- `Health / Damage / Hit Reaction` service
- `Lock-On / Target Context` service/FSM
- `Memory State` service/FSM
- `Encounter Framework` service/FSM

### Combat Scope

Separate combat sub-scope is optional for M0.

Recommendation:

- keep combat under gameplay scope for M0
- split only later if multiple encounters or broader combat contexts justify it

### Camera Scope

Belongs in camera scope:

- camera coordinator
- Cinemachine adapters
- camera feedback presentation services
- camera-relative basis provider

### UI / Debug Scope

Belongs in UI/debug scope:

- debug overlay presenters
- read-only snapshot assemblers if UI-owned
- visibility toggles

## 6. Core Contracts

These are conceptual interfaces/contracts only, not implementation code.

### Input Intent

- `IInputIntentSource`
- `InputIntentSnapshot`
- `InputActionIntent`
- `InputRoutingResult`

Owns:

- raw move/look/action intents
- input enabled/disabled context

### Combat Action Request / Result

- `CombatActionRequest`
- `CombatActionType`
- `CombatActionRequestResult`
- `CombatResolutionResult`

Purpose:

- express requested combat actions
- return accepted/rejected state
- expose confirmed resolution

### Action Lock / Recovery Context

- `ActionLockContext`
- `RecoveryContext`
- `RecoverySource`
- `MovementRestrictionContext`

Critical rule:

- `Combat Core` owns when combat-side locks or recovery are requested
- `Player Locomotion` owns how movement expression applies those locks and recovery states

Exchange shape:

- `Combat Core` emits requested combat lock/recovery context
- `Player Locomotion` consumes and expresses movement-side restriction/recovery truth

This removes overlap while preserving ownership.

### Locomotion State Snapshot

- `LocomotionStateSnapshot`
- `FacingContextSnapshot`
- `LocomotionTransitionRecord`

### Dodge Context

- `DodgeRequestContext`
- `DodgePhaseContext`
- `DodgeResultContext`

### Enemy Intent Snapshot

- `EnemyIntentSnapshot`
- `TelegraphStateSnapshot`
- `EnemyAttackTagSet`

### Enemy Punish Window Context

- `EnemyPunishWindowContext`

Critical distinction:

- `EnemyPunishWindow` belongs to enemy-side vulnerability/readability
- `CounterWindow` belongs to player-side combat opportunity validation

### Target Context Snapshot

- `TargetContextSnapshot`
- `TargetAcquireResult`
- `TargetReleaseReason`

### Camera-Relative Movement Basis

- `CameraMovementBasisSnapshot`

Exposes:

- camera forward basis projected onto ground plane
- camera right basis projected onto ground plane
- current basis validity
- source camera mode label

Critical rule:

- camera provides basis as read-only reference data
- `Player Locomotion` interprets movement using that basis
- camera does not decide final movement direction

### Health / Damage / Hit Reaction Context

- `DamageApplicationContext`
- `HealthStateSnapshot`
- `HitReactionContext`
- `DefeatStateContext`

### Memory Reveal Request / Result

- `RevealRequestContext`
- `RevealRequestResult`
- `MemoryStateSnapshot`
- `MemoryResponseContext`

### Encounter State Snapshot

- `EncounterStateSnapshot`
- `EncounterStartContext`
- `EncounterEndContext`
- `EncounterResetContext`

### Debug Snapshot / Event Shape

Recommended shared pattern:

- per-system immutable snapshot DTOs
- optional narrow debug events for transitions and accepted/rejected requests
- one overlay composition service that gathers snapshots without becoming owner

Suggested shape:

- `CombatDebugSnapshot`
- `LocomotionDebugSnapshot`
- `EnemyIntentDebugSnapshot`
- `HealthDebugSnapshot`
- `MemoryDebugSnapshot`
- `TargetDebugSnapshot`
- `CameraDebugSnapshot`
- `EncounterDebugSnapshot`
- `InputDebugSnapshot`
- `DebugTransitionEvent`

Critical rule:

- gameplay systems own debug truth for their domain
- `Debug Overlay` owns grouping and presentation only

## 7. Critical Cross-System Flows

### Light / Heavy Attack Flow

1. `Input Mapping` emits `LightAttack` or `HeavyAttack` intent
2. `Combat Core` receives action request
3. `Combat Core` validates current combat state
4. if accepted, `Combat Core` emits combat action request result plus action lock/recovery request context
5. `Player Locomotion` consumes movement restriction/recovery context
6. animator/presentation observes accepted state only
7. `Debug Overlay` displays input, acceptance, state, restriction source

### Enemy Attack → Dodge Result Flow

1. `Enemy Intent & Telegraph` exposes telegraph and active timing
2. `Input Mapping` emits `Dodge` intent
3. `Combat Core` validates dodge request against state/timing rules
4. `Player Locomotion` expresses dodge movement phase
5. `Combat Core` resolves dodge result using combat truth, not animation truth
6. if player avoids attack, result may support punish readability
7. debug shows dodge request, dodge phase, combat result, enemy punish context

### Enemy Attack → Parry → Counter Flow

1. enemy telegraph becomes readable through `Enemy Intent & Telegraph`
2. `Input Mapping` emits `Parry` intent
3. `Combat Core` validates parry timing attempt
4. if successful, `Combat Core` opens `CounterWindow`
5. optional `Counter` intent or contextual follow-up occurs
6. `Combat Core` validates counter during `CounterWindow`
7. `Player Locomotion` expresses movement commitment/recovery
8. debug shows parry result, `CounterWindow`, accepted/rejected counter

### Successful Counter → Reveal Request → Memory State Acceptance → Memory VFX Response

1. `Combat Core` confirms counter success
2. `Combat Core` emits `RevealRequestContext`
3. `Memory State` accepts, rejects, or ignores request
4. if accepted, `Memory VFX Response` receives accepted memory context
5. VFX plays restrained response
6. camera may provide downstream readability support only
7. debug shows reveal request, accept/reject state, VFX playback state

### Player Hit → Health / Damage → Hit Reaction → Locomotion Recovery

1. `Combat Core` confirms hit result
2. `Health / Damage / Hit Reaction` applies consequence
3. hit reaction and control suppression context are emitted
4. `Player Locomotion` consumes hit reaction/recovery context
5. locomotion expresses movement suppression/recovery truth
6. debug shows damage result, hit reaction source, recovery source

### Target Focus Input → Target Context → Camera / Locomotion Read-Only Flow

1. `Input Mapping` emits `LockOn` intent
2. `Lock-On / Target Context` resolves acquire/release request
3. target truth updates if accepted
4. `Player Locomotion` reads target direction/focus context for orientation support
5. `Lock-On & Combat Camera` reads target context for framing/readability
6. `Combat Core` may observe target context if needed
7. debug shows focus state, target validity, release reasons

### Encounter Start / End / Reset Flow

1. `Encounter Framework` prepares and validates readiness
2. participants register
3. encounter enters active state
4. combat/health/memory systems run during duel
5. encounter observes end/fail/abort/reset conditions
6. encounter emits end/reset context
7. target context, locomotion, and debug react to reset through their own owned state transitions

### Debug Observation Flow

1. each gameplay system maintains its own debug snapshot truth
2. snapshot assemblers or presenters gather read-only snapshots
3. `Debug Overlay` groups and displays active system state
4. no debug presenter mutates gameplay state

## 8. Data Authoring Plan

### Movement Data

- locomotion tuning
- dodge timing/distance
- facing/orientation tuning
- restriction/recovery tuning

### Combat Action Data

- light/heavy action profiles
- parry/counter timing config
- action lock/recovery defaults

### Enemy Attack / Telegraph Data

- telegraph timing
- active/recovery timing
- attack tags
- punish window parameters

### Health / Reaction Data

- health values
- hit reaction categories for M0
- control suppression duration

### Target Context Data

- toggle vs hold focus behavior
- simple validity assumptions
- debug labels

### Camera Presets

- duel framing presets
- target-focus framing presets
- recovery/reveal support presets

### Memory Response Data

- reveal acceptance tuning
- memory cooldown/reset tuning
- VFX duration/intensity labels

### Encounter Config

- participant references
- readiness flags
- start/end/reset rules

### Debug Config

- visible channels
- verbosity level
- toggle behavior

## 9. Testing Strategy

### Edit Mode Tests

Cover:

- Pure C# FSM state transitions
- combat validation
- target acquire/release logic
- reveal acceptance logic
- hit reaction/recovery routing
- debug snapshot assembly logic

### Play Mode Tests

Cover:

- additive scene composition
- VContainer lifetime scopes
- scene-loading readiness
- camera/gameplay/debug coordination
- one-duel integration path

### Smoke Tests

Required M0 smoke:

- load minimal additive scene set
- spawn/register player and enemy
- move, dodge, parry, counter
- accept reveal path
- hit reaction path
- encounter reset path

### Architecture Boundary Tests

Key tests:

- presentation cannot mutate gameplay truth
- root scope does not own duel truth
- target context not owned by camera
- locomotion not owned by combat recovery truth
- debug overlay remains read-only

### Debug Verification

Verify:

- each required snapshot channel appears
- accepted/rejected reasons appear where expected
- snapshots remain aligned with runtime behavior

### First M0 Acceptance Test

A tester can repeatedly fight one simple enemy in the Tokyo Street duel arena and the architecture supports:

- input intent visibility
- locomotion truth visibility
- combat result visibility
- target truth visibility
- enemy intent visibility
- memory response visibility
- encounter reset visibility

## 10. Risk / Mitigation

### Ownership Drift

Risk:

- multiple systems try to own the same truth

Mitigation:

- strict contract ownership tables
- asmdef boundaries
- scene-scope composition only

### Camera / Locomotion Circular Dependency

Risk:

- camera decides movement while locomotion expects read-only basis

Mitigation:

- expose `CameraMovementBasisSnapshot`
- locomotion interprets basis, camera never interprets movement

### Animator Becoming Gameplay Truth

Risk:

- clip length or animation events begin driving combat/recovery truth

Mitigation:

- Pure C# FSM remains authoritative
- animator adapters remain observers only

### Target Focus Auto-Solving Combat

Risk:

- target focus becomes hidden auto-aim or auto-spacing

Mitigation:

- target context owns truth only
- combat validity remains in `Combat Core`
- locomotion spacing remains player-owned

### Combat Core vs Locomotion Recovery Ownership

Risk:

- both systems believe they own recovery

Mitigation:

- `Combat Core` owns request/validation of combat-side lock/recovery context
- `Player Locomotion` owns movement-side expression and current locomotion recovery truth

### Debug Snapshot Too Noisy

Risk:

- overlay becomes unreadable and stops helping

Mitigation:

- per-system DTOs
- grouped channels
- selectable verbosity

### Overbuilding Before M0 Feel Is Proven

Risk:

- architecture becomes a speculative framework

Mitigation:

- one duel first
- minimal asmdefs
- minimal scenes
- small contracts, not giant abstract systems

## 11. Architecture Decisions / ADR Candidates

These should become ADRs:

1. Unity New Input System only
2. Pure C# FSM owns gameplay truth
3. Animator presentation-only
4. Target Context owns target truth
5. Camera owns framing/readability only
6. Combat Core owns combat validation/results
7. VContainer scene-scope composition
8. Root motion non-authoritative/deferred
9. Debug Overlay read-only
10. Additive scene composition for M0 duel prototype
11. Combat lock/recovery request vs locomotion expression split
12. Camera-relative movement basis as read-only camera contract

## 12. Implementation Readiness Verdict

This architecture is ready to become an OpenSpec proposal.

Why:

- the M0 system package is complete
- ownership boundaries are explicit
- the three gate concerns have been tightened into concrete architecture contracts
- scene, asmdef, DI, and contract direction are defined enough for disciplined implementation planning

Remaining questions are normal architecture-detail questions, not blockers:

- exact DTO shapes
- exact input asset naming in Unity
- exact VContainer registration breakdown per scene
- whether gamepad support is shipped in the first playable or added immediately after

## Appendix A: M0 Layer Map

### Foundation Layer

- `Bootstrap`
- `Infrastructure`
- `Input Mapping`
- scene composition
- DI composition

### Core Gameplay Layer

- `Player Locomotion`
- `Combat Core`
- `Enemy Intent & Telegraph`
- `Lock-On / Target Context`
- `Health / Damage / Hit Reaction`
- `Memory State`
- `Encounter Framework`

### Presentation Layer

- `Lock-On & Combat Camera`
- `Memory VFX Response`
- animator adapters
- audio adapters
- `Debug Overlay`

## Appendix B: Engine Risk Inventory

### High Risk Domains

- Input
  - Unity 6 deprecates legacy input
  - architecture locks to Unity New Input System only
- Cinemachine
  - Cinemachine 3 is a major rewrite from 2.x
  - architecture should keep camera adapter-facing and contract-first

### Medium Risk Domains

- rendering/post-process integration
- custom render pass decisions
- physics feel due to solver changes

### Low Risk Domains For This M0

- additive scene role separation
- Pure C# FSM patterns
- read-only debug DTO contracts
