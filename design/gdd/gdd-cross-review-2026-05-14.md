# Glass Refrain M0 Cross-GDD Review Report

> **Date**: 2026-05-14
> **Scope**: `Glass Refrain` M0 — Katana Combat Feel Prototype
> **Reviewer**: Codex
> **Verdict**: `READY FOR /gate-check`

## 1. Executive Summary

### Overall Readiness

The current `Glass Refrain` M0 GDD set now describes a coherent one-player, one-enemy, one-arena prototype with clear ownership for combat validity, locomotion truth, enemy readability, health consequence, memory response, targeting, camera framing, encounter lifecycle, input intent, and developer-facing debug visibility.

The design package is now ready for `/gate-check`. The main duel-facing system set is complete at the standalone GDD level, naming is normalized, and the remaining gaps are architecture-prep questions rather than gate blockers.

### Biggest Strengths

- The M0 scope is consistently narrow across the authored duel-facing docs.
- `Combat Core`, `Player Locomotion`, `Enemy Intent & Telegraph`, `Health / Damage / Hit Reaction`, `Memory State`, `Encounter Framework`, and `Debug Overlay` now describe clean high-level ownership seams.
- `Input Mapping`, `Lock-On / Target Context`, and `Memory VFX Response` are now present as standalone M0 GDDs, which closes the previous artifact-completeness gap.
- The pure gameplay-truth direction remains consistent:
  - gameplay truth should remain explicit
  - `Animator State Machine` is presentation only
  - root motion remains open but non-authoritative
- The duel rhythm `read → evade/parry → counter → reveal` is consistently present in the system docs.
- `Input Mapping` now explicitly records Unity New Input System as the M0 input foundation and rejects the legacy Input Manager.

### Biggest Blockers

No blocker-level issues were found in the current standalone M0 GDD package.

The remaining concerns are architecture-prep concerns:

- finalizing the cross-system action lock / recovery contract
- deciding the exact camera-relative movement-basis contract
- deciding the eventual debug snapshot/event shapes

## 2. Reviewed Documents

- [game-concept.md](/J:/afterimage-tokyo/design/gdd/game-concept.md)
- [systems-index.md](/J:/afterimage-tokyo/design/gdd/systems-index.md)
- [combat-core.md](/J:/afterimage-tokyo/design/gdd/combat-core.md)
- [enemy-intent-telegraph.md](/J:/afterimage-tokyo/design/gdd/enemy-intent-telegraph.md)
- [lock-on-combat-camera.md](/J:/afterimage-tokyo/design/gdd/lock-on-combat-camera.md)
- [player-locomotion.md](/J:/afterimage-tokyo/design/gdd/player-locomotion.md)
- [health-damage-hit-reaction.md](/J:/afterimage-tokyo/design/gdd/health-damage-hit-reaction.md)
- [input-mapping.md](/J:/afterimage-tokyo/design/gdd/input-mapping.md)
- [memory-state.md](/J:/afterimage-tokyo/design/gdd/memory-state.md)
- [memory-vfx-response.md](/J:/afterimage-tokyo/design/gdd/memory-vfx-response.md)
- [encounter-framework.md](/J:/afterimage-tokyo/design/gdd/encounter-framework.md)
- [debug-overlay.md](/J:/afterimage-tokyo/design/gdd/debug-overlay.md)
- [lock-on-target-context.md](/J:/afterimage-tokyo/design/gdd/lock-on-target-context.md)

## 3. Cross-GDD Consistency Findings

### M0 Scope

The authored duel-facing docs consistently describe:

- one player
- one simple enemy
- one Tokyo Street duel space
- grounded movement
- target focus / lock-on support
- combat camera readability
- light/heavy attack
- dodge
- parry
- counter
- simple hit reaction/recovery
- restrained memory reveal response
- encounter lifecycle
- debug visibility

This is a strength.

### Combat Rhythm

The rhythm `read → evade/parry → counter → reveal` is consistently represented in the authored system docs. [game-concept.md](/J:/afterimage-tokyo/design/gdd/game-concept.md) still uses the shorter top-level loop `read → evade → counter → reveal`, but its 30-second combat loop already includes “evade or parry,” so this is acceptable shorthand rather than a contradiction.

### Tokyo Street Duel Prototype

The authored docs consistently target a Tokyo Street duel prototype and repeatedly reinforce one player / one enemy / one arena assumptions.

### Memory Reveal Restraint

The newer system docs agree that reveal should be:

- meaningful
- validated through gameplay context
- short
- restrained
- non-cinematic for M0

This is consistent across `Combat Core`, `Memory State`, `Lock-On & Combat Camera`, and `Player Locomotion`.

### No Full RPG Framework

The authored docs consistently defer:

- full RPG stats/progression
- loot/economy
- boss frameworks
- multi-enemy systems
- full narrative memory graph
- final polish

This is strongly aligned.

### Naming And Artifact Completeness

The current standalone M0 GDD list in [systems-index.md](/J:/afterimage-tokyo/design/gdd/systems-index.md) is now fully represented by authored docs.

Canonical naming is normalized across the current M0 set:

- `Combat Core`
- `Input Mapping`
- `Lock-On / Target Context`
- `Lock-On & Combat Camera`
- `Memory State`
- `Memory VFX Response`
- `Debug Overlay`

This was a meaningful cleanup and is now a strength rather than a blocker.

## 4. Ownership Boundary Findings

### `Combat Core`

The newer docs consistently agree that `Combat Core` owns:

- combat validity/results
- timing/result resolution
- `CounterWindow`
- reveal request context

This boundary is strong.

### `Player Locomotion`

The docs consistently agree that `Player Locomotion` owns:

- movement truth
- movement interpretation
- dodge movement expression
- movement restriction/recovery expression
- facing/orientation support

This boundary is strong.

### `Enemy Intent & Telegraph`

The docs consistently agree that `Enemy Intent & Telegraph` owns:

- telegraph
- commitment
- active/recovery timing
- attack tags
- `EnemyPunishWindow`

This boundary is strong.

### `Health / Damage / Hit Reaction`

The newer docs consistently agree that `Health / Damage / Hit Reaction` owns:

- health values
- damage application after confirmed result
- hit reaction classification
- defeated/disabled consequence

This boundary is now clear.

### `Memory State`

The newer docs consistently agree that `Memory State` owns:

- reveal acceptance/rejection
- memory response state
- cooldown/guard if needed

The conceptual ownership is consistent and the canonical `Memory State` name is now established across the reviewed M0 core docs.

### `Lock-On / Target Context`

The newer docs consistently agree that `Lock-On / Target Context` owns:

- target focus active
- current target
- target validity
- target direction

This was one of the most important cleanups and is now mostly stable.

The standalone [lock-on-target-context.md](/J:/afterimage-tokyo/design/gdd/lock-on-target-context.md) GDD now closes the previous gap between ownership language and artifact completeness.

### `Lock-On & Combat Camera`

The newer docs consistently agree that `Lock-On & Combat Camera` owns:

- framing/readability
- duel visibility support
- camera feedback after confirmed context

The newer camera doc now reflects this well.

### `Encounter Framework`

The new encounter doc clearly owns:

- encounter lifecycle
- registration
- readiness
- start/end/reset reason

and does not overclaim combat or target truth.

### `Debug Overlay`

The new debug doc clearly owns:

- read-only presentation
- grouping
- labels
- toggles

and not gameplay truth.

### `Input Mapping`

The newer docs consistently agree that `Input Mapping` owns:

- Unity New Input System action map structure
- raw input intent
- input enabled or disabled state
- input-layer debug truth

This boundary is clean and explicitly avoids the legacy Input Manager.

### Presentation Systems

The authored docs consistently defend the boundary that:

- `Animator`
- `VFX`
- `Audio`
- `UI`

are presentation-only unless reacting to confirmed gameplay context.

### Boundary Risk Still Present

No blocker-level ownership conflict stands out in the current M0 package.

The remaining risks are implementation-shape questions rather than GDD ownership contradictions:

- how action lock and recovery context are exchanged between `Combat Core` and `Player Locomotion`
- how camera-relative basis is exposed to locomotion when needed

## 5. M0 Scope Findings

### Anything Over-Scoped

No major duel-facing doc is badly over-scoped at this point. The authored M0 docs are disciplined.

### Anything Under-Defined

No major under-defined area remains at the standalone M0 GDD level.

The remaining under-defined pieces are architecture-shape questions, not missing design-system artifacts.

### Anything Deferred Correctly

The following are consistently deferred correctly:

- full traversal
- boss framework
- multi-enemy systems
- final animation polish
- root motion production pipeline
- full RPG stats/progression
- final HUD
- narrative memory graph
- save/persistence

### Anything That Should Not Block M0

The following should not block M0:

- advanced emotional AI
- cinematic reveal sequencing
- full clue/contradiction systems
- large debug tool stacks
- final presentation polish

## 6. Debug / Readability Findings

### Combat Result / Debug

`Combat Core` and `Debug Overlay` now align well on:

- combat state/result
- `CounterWindow`
- reveal request context

### Locomotion / Debug

`Player Locomotion` and `Debug Overlay` align well on:

- locomotion state
- dodge request/phase
- movement restriction source
- recovery source
- mismatch visibility if available

### Enemy Telegraph / Debug

`Enemy Intent & Telegraph` and `Debug Overlay` align well on:

- telegraph
- commitment
- active/recovery
- attack tags
- `EnemyPunishWindow`

### Health / Reaction / Debug

`Health / Damage / Hit Reaction` and `Debug Overlay` align well on:

- health values
- hit reaction source
- consequence state
- disabled/defeated state

### Memory Reveal / Debug

`Memory State` and `Debug Overlay` align well on:

- reveal request source
- accept/reject/ignore
- current memory response state

### Target / Camera / Debug

`Lock-On / Target Context`, `Lock-On & Combat Camera`, and `Debug Overlay` now align reasonably well on:

- target focus state
- target validity
- camera state

### Encounter / Debug

`Encounter Framework` and `Debug Overlay` align well on:

- encounter state
- start/end/reset reasons
- readiness blockers

### Shared Overlay / Readability

The new `Debug Overlay` doc provides a good organizing surface for the duel systems. `Gameplay State Visibility` and `Combat State Visibility` are now reconciled as superseded naming covered by `Debug Overlay` for M0.

## 7. Missing Contract Findings

### Action Lock / Recovery Context

Still a cross-system contract that exists conceptually but is not fully normalized across all authored docs. It is good enough for design progression, but should be tightened before architecture.

### `EnemyPunishWindow` vs `CounterWindow`

This is much clearer than before. The docs now mostly distinguish:

- enemy exposure state
- player counter opportunity state

This is no longer a blocker, but it still deserves explicit architecture treatment.

### Reveal Request vs Reveal Acceptance

This is now one of the strongest cross-system seams:

- `Combat Core` requests
- `Memory State` accepts/rejects/responds

This is a strength.

### Target Context

The core ownership is now clear and backed by a standalone GDD.

### Camera-Relative Movement Basis

Still a valid open contract between locomotion and camera. Not a gate blocker, but it should be resolved or explicitly assumed before architecture.

### Hit Reaction Context

Now much clearer after the new `Health / Damage / Hit Reaction` doc, but exact event/snapshot shape remains architecture work, not fully design-resolved.

### Debug Snapshot Shape

Now conceptually covered by `Debug Overlay`, but not yet normalized into an architecture-level snapshot/event contract. This is not a gate blocker.

### Encounter Start / End / Reset Context

Now clearly documented in `Encounter Framework`. This is no longer a blocker.

### Input Intent Contract

This is now clearly documented in `Input Mapping` using Unity New Input System language. Raw intent, enabled/disabled state, downstream rejection visibility, and conservative buffering stance are all explicit enough for gate purposes.

## 8. Stale Placeholder / Polish Findings

### `[To be designed]`

No cross-GDD blocker-level `[To be designed]` placeholders were found in the reviewed authored system set.

### `TODO`

No blocker-level `TODO` placeholders were found in the reviewed authored system set.

### Stale Next-Step Instructions

The stale next-step issue previously found in `Player Locomotion` was already cleaned up.

### Outdated “Later GDD” Wording

No blocker-level “later GDD” wording remains.

One minor legacy phrase still appears in [combat-core.md](/J:/afterimage-tokyo/design/gdd/combat-core.md) where a table cell says “full behavior deferred to later GDD” for lock-on toggle behavior. This is a small polish issue, not a gate blocker.

### Inconsistent Naming

No major naming drift remains in the cleaned M0 core set.

### Ownership Wording Drift

Conceptually, ownership is much cleaner now. The remaining concerns are architecture-prep details, not ownership drift.

## 9. Required Fixes Before /gate-check

No true blockers were found before `/gate-check`.

## 10. Recommended Fixes Before /create-architecture

- Tighten the explicit cross-system contract for:
  - action lock / recovery context
  - camera-relative movement basis
  - debug snapshot/event shape
- Persist individual `/design-review` verdicts for each MVP doc
- Optionally clean the one minor stale “later GDD” phrase in [combat-core.md](/J:/afterimage-tokyo/design/gdd/combat-core.md) for polish consistency

## 11. Deferred Items

These should not block M0:

- full traversal
- boss framework
- multi-enemy systems
- final animation polish
- root motion production pipeline
- full RPG stats/progression
- final HUD
- narrative memory graph
- save/persistence

## 12. Final Readiness Verdict

**READY FOR /gate-check**

### Exact Blockers

None.

Re-run `/$gate-check`.
