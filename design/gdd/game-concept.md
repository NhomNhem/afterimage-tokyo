# Glass Refrain

## Concept Summary

`Glass Refrain` is a single-player semi-linear action RPG about a female katana wielder investigating a rain-soaked Tokyo district trapped in conflicting memories. Through precise, dance-like reactive combat and emotionally charged duels against `Memory Keepers`, she cuts through false truths, restores fragments of identity, and uncovers why the city's fractures are spreading toward a drowned seaside past.

## Genre

- Single-player semi-linear action RPG

## Core Fantasy

A female katana wielder investigates distorted memories in a rain-soaked Tokyo district, cutting through false truths and duel-bound Memory Keepers to restore fragments of her identity.

## Elevator Pitch

A katana-wielding woman investigates a Tokyo street trapped in conflicting memories, carving through distorted truths and duel-bound memory keepers as the city's fractures spread toward a drowned seaside past.

## Tone

- Sad
- Mysterious
- Melancholic
- Restrained
- Elegant

## Setting

### Act 1

- Rain-soaked Tokyo Street district

### Future Spaces

- Seaside memory zones
- Abandoned stations
- Flooded coastal towns

### World Nature

The world is shaped by contradictory memories and emotional distortion. Space, behavior, and meaning shift as truths are restored and false versions of events lose their hold.

## Core Loop Stack

### Core Loop

`read → evade → counter → reveal`

### 30-Second Combat Loop

- Read enemy intent
- Evade or parry
- Counter during a precise window
- Reveal emotional or memory truth through combat outcome

### 5-Minute District Loop

- Explore distortion
- Uncover contradiction
- Interpret emotional truth
- Fight emotional echoes
- Restore partial truth
- Reinterpret the district

### Session Loop

- Enter a memory incident
- Investigate a fractured district
- Fight emotional echoes
- Confront a Memory Keeper
- Restore partial truth
- Revisit changed space
- Leave with deeper understanding

### Long-Term Progression

Identity restoration comes first, combat mastery second. The player does not simply become stronger; she remembers differently, and that recovered understanding expands combat fluency, emotional context, and the meaning of the spaces she crosses.

## Combat Direction

### Combat Identity

- Inspired by `Blade & Soul`, but not built around nonstop aggression
- Dance-like reactivity
- Emotional dueling
- Calm observation followed by short violent bursts
- Precision over button mashing
- Enemy intent and emotional rhythm matter

### Desired Feel

Combat should feel composed and controlled until moments of sudden, elegant violence. The player fantasy is not overwhelming enemies with endless pressure, but reading distorted intent and cutting through it with precision.

### Combat Principles

- Readable enemy intent
- Meaningful evade and parry windows
- Short expressive combo strings
- Strong spacing and footwork
- Intimate duel rhythm
- Counterplay as emotional interpretation, not just damage output

## Memory Distortion Direction

### Primary Distortion Axis

Enemy intent changes based on emotional memory state.

Examples:

- Fear creates defensive spacing
- Anger creates aggressive pressure
- Guilt creates hesitation
- Despair creates reckless attacks

The player is not only reading animations. They are reading emotional truth through combat behavior.

### Secondary Distortion Axis

Arena and level logic change to support reinterpretation.

Examples:

- Altered routes
- Blocked paths
- Flooded zones
- Distorted elevation
- Impossible geometry
- Changed duel spacing

These changes support emotional and combat interpretation rather than replacing it.

## Pillars

### 1. Combat As Interpretation

Sword combat is not only challenge; it is how the player reads emotional truth.

### 2. Melancholic Elegance

The game should feel controlled, intimate, and cinematic, with beauty held in tension with sadness.

### 3. Distorted Memory Spaces

Levels are unstable memory-zones that change meaning through restored truth.

### 4. Mystery Through Contradiction

Progression comes from uncovering conflicting versions of events and gradually understanding why they differ.

### 5. Personal Restoration Over Power Fantasy

The protagonist's growth should feel like becoming more complete, not merely more powerful.

## Anti-Pillars

- Not open world
- Not endless-aggression combat
- Not puzzle-heavy investigation
- Not loot-driven stat chase
- Not spectacle-spam bosses

## M0 Milestone

### Name

`M0 — Katana Combat Feel Prototype`

### Goal

The player controls the katana protagonist in a Tokyo Street prototype arena and fights one simple enemy with satisfying movement, camera, lock-on, dodge, parry, light/heavy attacks, hit reaction, readable enemy intent, and one restrained memory-distortion visual response.

### Required Systems

#### Standalone System GDDs

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

#### Architecture / Technical Setup Artifacts

- Core Runtime Foundation
- Scene Composition

#### Prototype Content Requirements

- Level Blockout / prototype level content

### Deferred After M0

- Full District Reinterpretation
- Investigation and clue progression
- Narrative progression framework
- Boss duel framework beyond a simple prototype enemy
- Save and persistence
- Broader enemy roster
- Full HUD
- Multiple districts
- Seaside content
- Official VContainer source-generation optimization
- `di-smoke` validation

## Technical Foundation

- Unity 6000.3.x
- URP
- Input System
- Cinemachine
- VContainer
- R3
- ObservableCollections
- ZLinq
- DOTween
- Shader Graph
- Custom HLSL only when needed
- Unity Awaitable first
- UniTask only when async complexity justifies it
- Additive scene loading from day one
- UI Tool Kit
- Cinemachine
- `Bootstrap` / `Systems` / `Gameplay` / `Camera` / `UI` / `Level` scene separation
- `ProjectRootLifetimeScope` via `VContainerSettings`
- Scene scopes own gameplay lifetime
- Combat truth must never be registered globally
- `NhemDangFugBixs.VContainer.SourceGenerator` planned as a later DI architecture guardrail
- Official `VContainer.SourceGenerator` is an optional later optimization

## Production Framing

`Glass Refrain` is a long-term indie action RPG, but production begins with a narrow vertical-slice-first strategy. The first priority is proving combat feel, enemy readability, camera restraint, and a small but convincing memory-distortion response inside Tokyo Act 1. Broader district reinterpretation, narrative progression, and full RPG structure expand only after the core duel loop is strong.
