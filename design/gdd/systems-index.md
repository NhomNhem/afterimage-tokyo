# Glass Refrain Systems Index

## Overview

This document decomposes `Glass Refrain` into individual systems, maps their dependencies, and establishes a design priority order. It is intentionally combat-first and M0-first. The purpose of this index is to keep the project focused on proving the duel loop before expanding into broader action RPG scope.

## System Categories

### Foundation

#### Core Runtime Foundation

- **Description:** Bootstrap flow, additive scene-set loading, project root lifetime, persistent application services, and scene ownership boundaries.
- **Source:** Explicit

#### Input Mapping

- **Description:** Input System action mapping and control routing for movement, combat, targeting, and debug actions.
- **Source:** Explicit

#### Scene Composition

- **Description:** Separation of `Bootstrap`, `Systems`, `Gameplay`, `Camera`, `UI`, and `Level` scenes with clear gameplay and presentation ownership.
- **Source:** Explicit

### Core Gameplay

#### Player Locomotion

- **Description:** Movement, facing, spacing, repositioning, and combat-ready footwork for the protagonist.
- **Source:** Explicit

#### Combat Core

- **Description:** Dodge, parry, counter, light/heavy attacks, short combo strings, and frame-readable attack flow.
- **Source:** Explicit

#### Health / Damage / Hit Reaction

- **Description:** Damage contracts, hit reactions, vulnerability windows, recovery states, and combat consequence handling.
- **Source:** Implicit

#### Lock-On / Target Context

- **Description:** Owns target focus truth for the duel: target focus active, current target, target validity, and target direction.
- **Source:** Explicit

#### Enemy Intent & Telegraph

- **Description:** Readable enemy windups, attack commitment, punish windows, and emotional combat rhythm.
- **Source:** Explicit

#### Lock-On & Combat Camera

- **Description:** Owns duel framing, combat readability, telegraph visibility support, dodge/parry/counter readability, punish/reveal framing support, and camera feedback after confirmed context. Consumes `Lock-On / Target Context` for target-truth input.
- **Source:** Explicit

### Memory / Mystery

#### Memory State

- **Description:** Tracks current distortion state, emotional memory-state context, and restoration or reveal behavior.
- **Source:** Explicit

#### Memory VFX Response

- **Description:** Controlled visual feedback for memory-state change, reveal events, and restrained distortion response.
- **Source:** Explicit

#### Investigation / Contradiction Reading

- **Description:** Environmental contradictions, memory echoes, and interpretive clue framing that support district investigation.
- **Source:** Implicit

#### District Reinterpretation

- **Description:** Recontextualized routes, altered district meaning, and memory-state-driven spatial change.
- **Source:** Explicit

#### Truth Restoration

- **Description:** Full system for converting duel outcomes, contradiction tracking, and restored memory fragments into changed district meaning and progression.
- **Source:** Implicit

### Encounter / Content

#### Encounter Framework

- **Description:** Encounter setup, trigger conditions, enemy placement logic, and fight progression structure.
- **Source:** Implicit

#### Boss Duel Framework

- **Description:** Memory Keeper duel structure, phase interpretation, and reveal-driven confrontation logic.
- **Source:** Explicit

#### Enemy Roster Framework

- **Description:** Structure for multiple enemy types that express different emotional rhythms and memory-state behaviors.
- **Source:** Implicit

#### District Content Authoring

- **Description:** Authored data/config structure for incidents, districts, encounters, telegraphs, and distortions.
- **Source:** Implicit

### Progression / Meta

#### Identity Restoration Progression

- **Description:** Long-term self-reconstruction that changes how the protagonist understands herself, space, and combat.
- **Source:** Explicit

#### Combat Mastery Progression

- **Description:** Expansion of stance flow, counters, and expressive combat options as the player regains fluency.
- **Source:** Explicit

#### Narrative Progression Framework

- **Description:** Story-state tracking, incident progression, and act advancement.
- **Source:** Explicit

#### Save / Persistence

- **Description:** Persistence of restored truths, progression, district state, and player unlocks.
- **Source:** Explicit

### Presentation

#### HUD / Player-Facing UI

- **Description:** Combat HUD, lock-on cues, state displays, and later player-facing progression/menu UI.
- **Source:** Implicit

#### Debug Overlay

- **Description:** Debug-facing readouts for timing, targeting, intent, and memory-state visibility.
- **Source:** Explicit

#### Audio Mood & Combat Feedback

- **Description:** Combat impact, memory reveal tone, ambient melancholy, and duel tension feedback.
- **Source:** Implicit

### Tooling / Validation

#### DI Composition Guardrails

- **Description:** VContainer composition rules, future generated registration guardrails, and DI boundary safety.
- **Source:** Explicit

#### DI Smoke / Validation

- **Description:** Future DI preflight validation once assemblies and composition boundaries stabilize.
- **Source:** Explicit

#### Content / Config Validation

- **Description:** Validation for authored attack data, telegraphs, memory-state configs, and district content definitions.
- **Source:** Implicit

## M0 Required Artifacts

### M0 Standalone System GDDs

- Input Mapping
- Player Locomotion
- Combat Core
- Health / Damage / Hit Reaction
- Lock-On / Target Context
- Enemy Intent & Telegraph
- Lock-On & Combat Camera
- Memory State
- Memory VFX Response
- Encounter Framework
- Debug Overlay

### M0 Architecture / Technical Setup Artifacts

- Core Runtime Foundation
- Scene Composition

### M0 Prototype Content Requirements

- Level Blockout / prototype level content

### M0 Visibility Note

- `Gameplay State Visibility` and earlier `Combat State Visibility` language are covered by `Debug Overlay` for M0 and should not be treated as separate standalone GDD requirements unless the project explicitly re-splits them later.

### Gate-Check Artifact Expectation

- `/gate-check` should expect standalone `design/gdd/*.md` files only for the systems listed under `M0 Standalone System GDDs`.
- `Core Runtime Foundation` and `Scene Composition` should be reviewed as architecture or technical-setup artifacts during `/create-architecture` and related setup work, not as missing `/design-system` GDD blockers.
- `Level Blockout / prototype level content` is required for M0 validation, but it should be treated as prototype content scope rather than a missing standalone system GDD unless the project explicitly decides otherwise later.

## Deferred Systems

### Deferred After M0

- Investigation / Contradiction Reading
- District Reinterpretation
- Truth Restoration as a full standalone system
- Boss Duel Framework beyond a simple prototype enemy
- Enemy Roster Framework beyond the first prototype enemy
- Identity Restoration Progression
- Combat Mastery Progression
- Narrative Progression Framework
- Save / Persistence
- HUD / Player-Facing UI
- Audio Mood & Combat Feedback
- District Content Authoring beyond prototype needs
- DI Smoke / Validation
- Official `VContainer.SourceGenerator` optimization

## Dependency Map

### Foundation Layer

- Core Runtime Foundation
- Input Mapping
- Scene Composition

### Authoritative Ownership

- `Combat Core` owns combat action validity, timing/result resolution, `CounterWindow`, and reveal request context
- `Player Locomotion` owns movement truth, movement interpretation, facing support, dodge movement expression, movement restrictions, and recovery movement
- `Enemy Intent & Telegraph` owns enemy telegraph, commitment, active/recovery timing, attack tags, and punish windows
- `Lock-On / Target Context` owns target focus active, current target, target validity, and target direction
- `Lock-On & Combat Camera` owns framing and duel readability only
- `Memory State` owns reveal acceptance/rejection and provisional memory consequence for M0

### Read-Only Coordination

- `Player Locomotion` depends on `Input Mapping`
- `Combat Core` coordinates with `Player Locomotion` through movement/facing, dodge, and recovery context
- `Enemy Intent & Telegraph` coordinates with `Combat Core` through attack tags, timing, punish, and reaction context
- `Lock-On / Target Context` coordinates with `Player Locomotion`, `Combat Core`, and `Lock-On & Combat Camera` as the shared target-truth source
- `Lock-On & Combat Camera` consumes `Lock-On / Target Context`, combat context, enemy-intent context, and locomotion context for readability
- `Health / Damage / Hit Reaction` consumes resolved combat results and returns consequence context

### Feature Layer

- Memory State depends on `Core Runtime Foundation`
- Memory VFX Response depends on `Memory State`
- Encounter Framework depends on `Combat Core` and `Enemy Intent & Telegraph`
- Investigation / Contradiction Reading depends on `Memory State`
- District Reinterpretation depends on `Memory State` and later full `Truth Restoration`
- Boss Duel Framework depends on `Combat Core`, `Enemy Intent & Telegraph`, and later `Truth Restoration`
- Enemy Roster Framework depends on `Enemy Intent & Telegraph`
- District Content Authoring depends on memory, encounter, and district system needs

### Downstream Consumers

- Debug Overlay depends on combat, locomotion, enemy-intent, target, and memory-state visibility
- HUD / Player-Facing UI depends on combat, targeting, and progression systems
- Audio Mood & Combat Feedback depends on combat, encounter, and memory-state transitions
- Memory VFX Response depends on `Memory State`

### Meta Layer

- Identity Restoration Progression depends on later full `Truth Restoration`
- Combat Mastery Progression depends on `Combat Core` and `Identity Restoration Progression`
- Narrative Progression Framework depends on `Investigation / Contradiction Reading` and later `Truth Restoration`
- Save / Persistence depends on progression and district systems
- DI Composition Guardrails depend on stable project structure and composition boundaries
- DI Smoke / Validation depends on stable asmdefs and DI boundaries
- Content / Config Validation depends on stable data authoring formats

## Bottleneck Systems

These systems carry elevated risk because many others depend on them:

- Combat Core
- Enemy Intent & Telegraph
- Memory State
- Encounter Framework

## Priority Assignment

### M0

- Input Mapping
- Player Locomotion
- Combat Core
- Health / Damage / Hit Reaction
- Lock-On / Target Context
- Enemy Intent & Telegraph
- Lock-On & Combat Camera
- Memory State
- Memory VFX Response
- Debug Overlay
- Encounter Framework
- Core Runtime Foundation
- Scene Composition
- Level Blockout / prototype level content

**Why:** These are the minimum M0 artifacts required to prove the `read → evade → counter → reveal` combat loop in a playable Tokyo Street prototype arena. Standalone GDDs cover duel-facing gameplay systems, architecture artifacts cover runtime/setup structure, and prototype content requirements cover the actual playable arena.

### Vertical Slice

- Investigation / Contradiction Reading
- Truth Restoration
- District Reinterpretation
- Boss Duel Framework
- HUD / Player-Facing UI
- Audio Mood & Combat Feedback
- District Content Authoring

**Why:** These systems transform the prototype from a combat feel test into a real `Glass Refrain` slice with mystery, reinterpretation, and emotional payoff.

### Alpha

- Enemy Roster Framework
- Identity Restoration Progression
- Combat Mastery Progression
- Narrative Progression Framework
- Save / Persistence

**Why:** These systems support the broader semi-linear action RPG structure once the slice-level identity is proven.

### Full Vision

- DI Composition Guardrails
- DI Smoke / Validation
- Content / Config Validation
- broader district and seaside content expansion

**Why:** These systems improve safety, scalability, and long-term production readiness after the core game direction is stable.

## Recommended `/design-system` Order

1. Combat Core
2. Enemy Intent & Telegraph
3. Player Locomotion
4. Health / Damage / Hit Reaction
5. Lock-On / Target Context
6. Lock-On & Combat Camera
7. Memory State
8. Memory VFX Response
9. Encounter Framework
10. Debug Overlay
11. Input Mapping
12. Investigation / Contradiction Reading
13. Truth Restoration
14. District Reinterpretation
15. Boss Duel Framework
16. Identity Restoration Progression
17. HUD / Player-Facing UI

## Suggested Future OpenSpec Changes

- `project-foundation`
- `combat-core-m0`
- `enemy-intent-telegraph-m0`
- `lockon-camera-m0`
- `lockon-target-context-m0`
- `memory-state-m0`
- `memory-vfx-response-m0`
- `debug-readability-m0`
- `vcontainer-guardrails`
- `district-reinterpretation-foundation`
- `boss-duel-framework`
- `identity-restoration-progression`

## Manual Review Notes

- `Truth Restoration` is folded into `Memory State` for M0 as a minimal reveal/restoration behavior.
- `Truth Restoration` should become its own system later for the vertical slice and full game, once contradiction tracking, duel outcomes, district reinterpretation, and narrative progression are active concerns.
- M0 remains combat-first. This index intentionally avoids expanding into full RPG framework design before the duel loop is proven.
- Presentation systems may observe gameplay state, but must not own gameplay truth.
- M0 GDD ownership is intentionally split between `Lock-On / Target Context` as target-truth ownership and `Lock-On & Combat Camera` as framing/readability ownership. Architecture may later split implementation modules further, but GDD ownership should remain explicit.
- For M0 gate purposes, only the systems under `M0 Standalone System GDDs` should be expected as `design/gdd/*.md` files. `Core Runtime Foundation` and `Scene Composition` belong to architecture/technical setup, and `Level Blockout / prototype level content` is a prototype content requirement rather than a standalone system GDD.
- `Debug Overlay` is the canonical M0 visibility system. Older labels such as `Gameplay State Visibility` or `Combat State Visibility` should be treated as superseded naming unless the project later reintroduces them as separate systems by explicit decision.
