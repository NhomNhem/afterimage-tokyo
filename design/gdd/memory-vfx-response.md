# Memory VFX Response

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Melancholic Elegance, Combat As Interpretation

## 1. System Summary

`Memory VFX Response` defines the M0 presentation response for accepted `Memory State` reveal events in `Glass Refrain`'s first katana duel prototype. It owns visual response selection for accepted reveal context, restrained timing of VFX presentation, simple debug-visible memory VFX state, and optional tuning for intensity and cooldown behavior.

For M0, this system exists only to help the player feel that a meaningful reveal moment has occurred after valid combat and memory context have already been confirmed during the core rhythm:

`read → evade/parry → counter → reveal`

It does not own reveal validity, combat success, damage, enemy stagger, camera framing, or memory progression. It is a downstream presentation response only.

## 2. Design Intent

The purpose of `Memory VFX Response` in M0 is to add a small but emotionally legible visual consequence to an accepted reveal moment without overwhelming the duel. When the player successfully reaches a meaningful combat outcome and `Memory State` accepts the reveal context, the prototype should provide a restrained visual response that suggests fracture, distortion, or emotional truth surfacing.

The response should feel melancholic, elegant, and brief. It should deepen the identity of the duel rather than interrupt it. If the effect becomes loud, long, disorienting, or authoritative, it will weaken both combat readability and the restrained emotional tone the prototype is trying to prove.

At M0, one good response is enough. The goal is not a full VFX pipeline or cinematic signature. The goal is to prove that combat consequence can produce a small memory-side visual echo that feels coherent and readable.

## 3. Player Experience Goals

For M0, `Memory VFX Response` should support the following player-facing outcomes:

- a successful reveal moment feels distinct from a normal hit
- the reveal response feels emotionally restrained rather than explosive
- the effect is visible enough to be understood, but brief enough not to interrupt duel clarity
- the player does not confuse the effect with damage, stagger, or `CounterWindow`
- the effect does not hide enemy recovery, player recovery, punish windows, or the next telegraph

When the system is working, the player should feel a brief emotional disturbance, not a cutscene.

## 4. M0 Scope

Included in M0:

- one restrained memory VFX response
- brief accepted-reveal visual feedback
- simple VFX state tracking
- simple debug-visible requested/playing/cooldown behavior
- simple tuning for intensity and duration if needed

## 5. Non-Goals

Out of scope for M0:

- full VFX pipeline
- final shader polish
- cinematic reveal sequence
- cutscene system
- full district reinterpretation
- persistent world change
- narrative clue UI
- required audio response
- final post-processing stack
- renderer-feature-heavy presentation architecture

## 6. Core Memory VFX Loop

The recommended M0 loop is:

`Memory State accepts reveal → Memory VFX Response receives accepted context → choose restrained visual response → play brief effect → enter cooldown/reset`

This loop should remain short, readable, and fully downstream of accepted memory context.

## 7. Memory VFX State Model

Recommended M0 states:

- `MemoryVFXIdle`
- `MemoryVFXRequested`
- `MemoryVFXPlaying`
- `MemoryVFXCoolingDown`
- `MemoryVFXRejected`
- `MemoryVFXIgnored`

State intent:

- `MemoryVFXIdle`: no active reveal VFX response
- `MemoryVFXRequested`: accepted reveal context has been received and a response is pending
- `MemoryVFXPlaying`: the visual response is actively presenting
- `MemoryVFXCoolingDown`: the effect has completed and is temporarily gated from immediate replay if needed
- `MemoryVFXRejected`: a request was not valid for VFX playback under current rules
- `MemoryVFXIgnored`: a request or context was intentionally not acted upon

`Rejected` and `Ignored` may remain mostly debug-facing in M0, but they are useful for traceability.

## 8. Accepted Reveal Response Rules

`Memory VFX Response` should only play after accepted `Memory State` context.

Recommended accepted inputs:

- `Memory State` accepted a valid reveal request
- the accepted state is currently allowed to produce a response
- the effect can play without harming current duel readability

Recommended M0 accepted visual response:

- brief restrained distortion
- subtle glass, refraction, shimmer, or fracture cue if available
- short enemy or world ripple if simple
- no long screen takeover
- no camera-disorienting effect

The effect should visually communicate that a meaningful memory-side beat occurred, not that gameplay authority changed.

## 9. Rejected / Ignored Reveal Response Rules

The system should reject or ignore response playback when:

- `Memory State` did not accept reveal context
- the source event was a generic hit
- the source event was a failed dodge
- the source event was a failed parry
- the source event came from presentation-only systems
- the system is already playing or cooling down and replay is not allowed

Rejected or ignored reveal response must not silently imply that a reveal still occurred.

If useful, debug should record:

- the source memory context
- whether the effect was rejected or ignored
- the reason it was skipped

## 10. VFX Timing Rules

Timing must follow accepted gameplay context, not lead it.

For M0:

- VFX begins only after accepted `Memory State` reveal context
- the effect should be brief
- the effect should finish quickly enough that the player can still read recovery, punish, or the next telegraph
- VFX timing should not become the hidden owner of reveal truth

The timing rule is simple:

- first truth comes from `Memory State`
- then presentation follows

## 11. VFX Intensity / Restraint Rules

The visual response must remain restrained.

For M0, preferred qualities are:

- melancholic
- elegant
- readable
- brief
- emotionally distinct

The effect must not:

- cover the whole screen for long
- imply heavy damage on its own
- imply stagger on its own
- hide player recovery
- hide enemy punish state
- hide the next telegraph
- feel like a reward explosion

This is a small emotional fracture, not a spectacle beat.

## 12. Relationship To Memory State

`Memory State` owns:

- reveal request acceptance or rejection
- current memory state
- reveal response state
- reveal cooldown or reset
- memory debug truth

`Memory VFX Response` owns:

- what restrained visual response to present after accepted memory context
- whether it is currently idle, requested, playing, cooling down, rejected, or ignored

`Memory VFX Response` must never infer reveal validity by itself.

## 13. Relationship To Combat Core

`Combat Core` owns:

- combat validity and results
- `CounterWindow`
- reveal request context

`Memory VFX Response` must not:

- imply `CounterWindow`
- imply damage
- imply combat success before upstream acceptance

It only reacts after accepted memory context has already been established.

## 14. Relationship To Health / Damage / Hit Reaction

`Health / Damage / Hit Reaction` owns:

- damage
- health
- hit reaction
- defeat or disabled consequence

`Memory VFX Response` must not:

- apply damage
- imply health changes by itself
- imply stagger or hit reaction by itself
- replace consequence readability

It may coexist with consequence, but it does not own consequence.

## 15. Relationship To Enemy Intent & Telegraph

`Enemy Intent & Telegraph` owns:

- telegraph
- commitment
- active/recovery timing
- attack tags
- `EnemyPunishWindow`

`Memory VFX Response` must not hide:

- enemy recovery
- punish window readability
- next telegraph

If the effect harms enemy readability, it is too strong for M0.

## 16. Relationship To Player Locomotion

`Player Locomotion` owns:

- movement truth
- recovery movement
- hit reaction movement response

`Memory VFX Response` must not interrupt or secretly drive locomotion truth.

The effect may occur while the player is recovering or resetting, but it must not obscure whether the player has regained control.

## 17. Relationship To Lock-On & Combat Camera

`Lock-On & Combat Camera` owns:

- framing
- readability
- camera support after valid context

`Memory VFX Response` may visually complement camera support, but it must not own framing and must not turn accepted reveal into a camera-dominating event.

VFX and camera should remain coordinated by shared accepted context, not by mutual authority.

## 18. Relationship To Debug Overlay

`Debug Overlay` owns read-only presentation of memory VFX state.

`Memory VFX Response` should expose:

- current VFX state
- source accepted memory context
- current intensity label if used
- whether playback was skipped, rejected, or ignored
- cooldown state if used

This makes it possible to debug whether memory presentation is missing because of upstream acceptance, local VFX gating, or intentional cooldown.

## 19. Data Authoring Needs

M0 data needs should stay small.

Possible tunables:

- effect duration
- cooldown duration if used
- simple intensity label or scalar
- debug labels
- one response variant selection if needed

M0 does not require:

- a large VFX library
- many reveal tiers
- per-enemy reveal VFX sets
- large authored effect graphs

## 20. Presentation Boundaries

This system is presentation-only.

It may communicate:

- accepted reveal response
- subtle emotional fracture
- restrained visual consequence

It must not communicate as authoritative:

- reveal validity
- damage
- stagger
- `CounterWindow`
- target truth
- locomotion truth

`Animator`, `Audio`, and `UI` remain adjacent presentation systems and must not become reveal authority either.

## 21. Technical Boundaries

For M0, the technical design should remain simple.

Recommended rules:

- do not require a full VFX pipeline
- do not require production renderer features
- keep playback logic explicit and debug-visible
- consume accepted memory context from clear contracts
- avoid hidden cross-authority behavior between VFX, camera, and combat systems

The system should be simple enough to prove one believable reveal response without committing to a final rendering architecture.

## 22. Dependencies

Upstream dependencies:

- `Memory State`
- accepted reveal context

Read-only coordination:

- `Combat Core`
- `Health / Damage / Hit Reaction`
- `Enemy Intent & Telegraph`
- `Player Locomotion`
- `Lock-On & Combat Camera`

Downstream consumers:

- `Debug Overlay`

## 23. Risks

Main M0 risks:

- VFX plays without accepted `Memory State` context
- VFX is too loud and harms duel readability
- VFX is too subtle and fails to communicate anything
- VFX implies damage, stagger, or counter truth
- VFX timing becomes more authoritative than memory-state timing
- the effect becomes a pseudo-cutscene instead of a brief response

Mitigation direction:

- keep `Memory State` authoritative
- keep effect duration short
- keep intensity restrained
- make skipped/rejected behavior debug-visible
- test against enemy telegraph and recovery readability

## 24. Open Questions

- should M0 use one world-space effect, one screen-space effect, or a minimal hybrid?
- does M0 need explicit cooldown from day one, or is one accepted playback path enough?
- should enemy defeat be allowed to drive the same reveal VFX response as counter-based acceptance?
- does the first playable need a placeholder audio companion cue, or should this remain purely visual?
- should the effect anchor more to the enemy, the player, or the immediate duel space?

## 25. Acceptance Criteria For M0

`Memory VFX Response` passes M0 if:

- a valid accepted `Memory State` reveal can trigger one restrained visual response
- generic hits do not trigger the effect
- failed dodge or failed parry do not trigger the effect
- presentation-only events do not trigger the effect
- the response is brief, readable, and emotionally distinct
- the response does not hide recovery, punish windows, or the next telegraph
- the response does not imply damage, stagger, or `CounterWindow` by itself
- debug can explain requested, playing, cooldown, rejected, or ignored state

`Memory VFX Response` fails M0 if:

- it behaves like reveal authority
- it plays on generic combat noise instead of accepted memory context
- it overwhelms the duel visually
- it harms camera or combat readability
- it cannot explain why the effect did or did not play
