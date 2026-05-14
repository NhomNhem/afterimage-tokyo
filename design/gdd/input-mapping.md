# Input Mapping

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Combat As Interpretation, Melancholic Elegance

## 1. System Summary

`Input Mapping` defines the authoritative M0 input contract for `Glass Refrain` using Unity's New Input System. It owns raw player input actions, action map organization, device-agnostic input intent, input enabled or disabled state, and debug visibility for accepted, rejected, or ignored input routing.

For M0, this system supports one player, one simple enemy, one Tokyo Street duel space, and the core rhythm:

`read → evade/parry → counter → reveal`

Its purpose is not to build a full rebinding framework, accessibility input UI, multiplayer routing layer, or combo macro system. Its purpose is to provide a small, trustworthy source of raw gameplay intent that can be consumed by locomotion, combat, targeting, encounter, and debug systems without quietly owning gameplay truth.

`Input Mapping` emits intent only. It does not own movement truth, combat validity, target truth, camera state, or animation state.

## 2. Design Intent

The purpose of `Input Mapping` in M0 is to make the first duel readable, responsive, and technically honest. The player should feel that inputs are recognized consistently, routed clearly, and either accepted or rejected for understandable reasons. The system should support a disciplined duel loop without hiding gameplay state inside input handling.

At M0, input design should stay conservative. It should favor clarity over feature richness, explicit actions over abstraction, and straightforward routing over a large generic framework. If the player presses dodge, parry, light attack, or lock-on, the project should be able to explain what input occurred, where it was routed, and why it did or did not produce a gameplay result.

This system exists to make all downstream gameplay systems easier to trust. If input truth is ambiguous, it becomes much harder to tune combat feel, debug rejection reasons, or judge whether movement and combat rules are working.

## 3. Player Experience Goals

For M0, input should support the following outcomes:

- movement input feels recognized and stable
- attack, dodge, parry, and lock-on inputs feel intentional and understandable
- rejected input does not feel random
- gameplay systems can apply commitment and recovery without input becoming unclear
- target focus input is understandable even when no valid target exists
- debug can explain what the player pressed and where it went

The player should feel that the controls are deliberate and readable, not permissive in a hidden way.

## 4. M0 Scope

Included in M0:

- Unity New Input System
- one gameplay action map if sufficient
- optional debug or pause action map
- keyboard and mouse first if needed
- optional planned gamepad support
- movement input
- look or camera input if used
- light attack input
- heavy attack input
- dodge input
- parry input
- counter input if separate
- lock-on or target-focus input
- optional debug reset or debug reveal input if approved
- input enabled or disabled context
- input debug truth

## 5. Non-Goals

Out of scope for M0:

- legacy Unity Input Manager
- full rebinding UI
- accessibility remapping UI
- multiplayer input routing
- combo macro input
- large input layering framework
- production controller settings UI
- input prediction or rollback

## 6. Core Input Loop

The recommended M0 input loop is:

`read raw input → emit input intent → route intent to owning gameplay system → receive accepted/rejected outcome if provided → expose debug truth`

For M0:

- raw input should be captured through Unity New Input System actions
- each action should map to clear gameplay intent
- gameplay systems remain responsible for validation
- input debug should record what was pressed and where it was routed

## 7. Action Map Model

M0 does not need a large action-map hierarchy.

Recommended M0 structure:

- `Gameplay`
- `Debug` optional

`Gameplay` may contain:

- `Move`
- `Look`
- `LightAttack`
- `HeavyAttack`
- `Dodge`
- `Parry`
- `Counter`
- `LockOn`
- `Pause` optional
- `Interact` deferred or optional

`Debug` may contain:

- `DebugResetEncounter`
- `DebugToggleOverlay`
- `DebugRevealTrigger` if approved

One simple gameplay map is enough for M0 if it keeps routing understandable.

## 8. M0 Input Action Set

Required M0 actions:

- `Move`
- `LightAttack`
- `HeavyAttack`
- `Dodge`
- `Parry`
- `LockOn`

Conditionally included:

- `Look` if camera input is directly exposed in M0
- `Counter` if separate from parry or counter-window timing context
- `Pause` if needed
- `DebugResetEncounter`
- `DebugToggleOverlay`
- `DebugRevealTrigger` if approved

Action names should stay readable and consistent with the GDD language where possible.

## 9. Movement Input Rules

`Input Mapping` owns raw movement intent only.

For M0:

- `Move` should emit a raw directional input intent
- movement intent should remain device-agnostic
- `Input Mapping` should not decide final movement direction after camera-relative or target-relative interpretation
- `Player Locomotion` owns the gameplay interpretation of movement input

Movement input may still be present while locomotion later rejects movement due to recovery, restriction, or disabled state. That distinction should stay visible in debug.

## 10. Combat Input Intent Rules

`Input Mapping` owns raw combat action intent only.

For M0:

- `LightAttack` emits a light attack request
- `HeavyAttack` emits a heavy attack request
- `Dodge` emits a dodge request
- `Parry` emits a parry request
- `Counter` emits a counter request only if it is intentionally separate

This system must not decide:

- whether the request is valid
- whether the request succeeds
- whether `CounterWindow` is open
- whether reveal context is valid

Those decisions belong downstream.

## 11. Dodge / Parry / Counter Input Rules

These actions are especially sensitive in M0 because they drive duel readability.

Recommended rules:

- `Dodge` always emits raw dodge intent when input is enabled
- `Parry` always emits raw parry intent when input is enabled
- `Counter` is only a separate input if the design explicitly wants one
- downstream systems may reject these intents based on recovery, action lock, invalid context, or missing timing opportunity

For M0, input buffering should remain conservative:

- no large queue
- no hidden chaining behavior
- no input that bypasses action lock or recovery by default

## 12. Lock-On / Target Focus Input Rules

`Input Mapping` owns raw `LockOn` intent.

`Lock-On / Target Context` owns:

- interpreting `LockOn` intent into acquire or release requests
- target focus truth after that request is evaluated

M0 may use either:

- toggle focus behavior
- hold focus behavior

but should choose one simple approach first.

Rejected or ignored target-focus input should be debug-visible when downstream systems provide the reason.

## 13. Input Enable / Disable Rules

`Input Mapping` owns whether raw input is currently enabled or disabled at the input-contract level.

For M0, this may include:

- gameplay input enabled
- gameplay input disabled
- debug input enabled

Important rule:

- disabling input here should remain explicit and debuggable
- disabling raw input is not the same as downstream gameplay rejecting a valid incoming intent

Whenever possible, M0 should prefer keeping input readable and letting downstream systems reject action requests rather than hiding everything behind opaque global disable states.

## 14. Input Rejection / Buffering Rules

For M0, input buffering should be conservative.

Recommended stance:

- no aggressive buffering by default
- no combo macro logic
- no action bypass of recovery or combat locks
- only minimal temporary buffering if clearly needed for feel and explicitly approved

Input rejection rules:

- `Input Mapping` may emit raw intent even if downstream systems later reject it
- if downstream systems provide rejection or ignore reasons, `Input Mapping` and `Debug Overlay` should expose them
- the system should differentiate between:
  - raw input not available because input was disabled
  - raw input available but ignored by no active consumer
  - raw input routed and rejected by gameplay rules

## 15. Relationship To Player Locomotion

`Player Locomotion` consumes:

- raw movement intent
- possibly dodge intent if locomotion owns dodge movement expression

`Player Locomotion` owns:

- movement interpretation
- movement direction/state
- dodge movement expression
- facing/orientation support
- movement restrictions
- recovery movement

`Input Mapping` must not become a hidden movement-state machine.

## 16. Relationship To Combat Core

`Combat Core` consumes:

- attack intent
- parry intent
- counter intent if separate
- dodge-related action intent as needed for validation

`Combat Core` owns:

- combat action validity
- attack/parry/dodge/counter result validation
- action locks
- `CounterWindow`
- reveal request context

`Input Mapping` must not decide combat outcomes.

## 17. Relationship To Lock-On / Target Context

`Lock-On / Target Context` consumes:

- raw `LockOn` intent

`Lock-On / Target Context` owns:

- target focus acquire/release interpretation
- current target truth
- target validity
- target direction

`Input Mapping` does not own target truth.

## 18. Relationship To Lock-On & Combat Camera

`Lock-On & Combat Camera` may consume:

- raw `Look` intent if direct camera input is used in M0
- downstream target-focus state

`Lock-On & Combat Camera` owns:

- framing
- readability
- camera state
- camera-relative basis if exposed

`Input Mapping` does not own camera behavior. It only exposes raw look intent if the M0 camera uses it.

## 19. Relationship To Debug Overlay

`Debug Overlay` owns read-only presentation of:

- raw input intent
- input enabled/disabled state
- routing information if exposed
- rejection or ignore reasons if downstream systems provide them

`Input Mapping` owns the debug truth of the input layer, not the overlay presentation.

## 20. Debug / Readability Requirements

Debug must explain:

- current input map state
- gameplay input enabled?
- debug input enabled?
- last raw movement input
- last raw look input if used
- last `LightAttack` input
- last `HeavyAttack` input
- last `Dodge` input
- last `Parry` input
- last `Counter` input if separate
- last `LockOn` input
- last debug input if relevant
- where the input was routed
- whether the input was ignored or rejected downstream
- rejection or ignore reason if provided

Debug should make it possible to tell whether a problem comes from:

- no input
- disabled input
- routing issue
- downstream gameplay rejection

## 21. Data Authoring Needs

M0 data needs should stay minimal.

Possible tunables:

- action names
- action map names
- input enable/disable mode labels
- toggle or hold behavior assumptions for lock-on if configured here
- simple device support assumptions

M0 does not require:

- rebinding data architecture
- complex device profile libraries
- accessibility profile authoring

## 22. Presentation Boundaries

Presentation systems may react to confirmed gameplay context that originated from input, but they must not own input truth.

For M0:

- UI may eventually show prompts, but no production input UI is required
- `Animator`, `VFX`, and `Audio` must not pretend a gameplay action succeeded just because input occurred
- debug may show input state, but it must not become gameplay UI

## 23. Technical Boundaries

Technical rules for M0:

- use Unity New Input System
- do not design around legacy Input Manager
- keep the input layer explicit and inspectable
- keep action maps small
- avoid overbuilding a generalized command framework before one duel feels good
- keep raw intent separate from gameplay validation

This system should stay small enough to support fast tuning and clear debugging.

## 24. Dependencies

Upstream dependencies:

- Unity New Input System

Downstream consumers:

- `Player Locomotion`
- `Combat Core`
- `Lock-On / Target Context`
- `Lock-On & Combat Camera` if look input is used
- `Debug Overlay`

Coordination only:

- `Encounter Framework`
- `Health / Damage / Hit Reaction`
- `Memory State`

## 25. Risks

Main M0 risks:

- input becomes a hidden gameplay validator
- too much buffering makes combat feel mushy
- too little visibility makes rejected input feel random
- lock-on input truth becomes mixed with target-truth ownership
- camera input interpretation leaks into locomotion or combat ownership
- action maps become overbuilt before the duel loop is proven

Mitigation direction:

- keep input raw and explicit
- keep buffering conservative
- expose routing and rejection reasons
- preserve strict ownership seams

## 26. Open Questions

- should M0 ship keyboard and mouse only first, or include gamepad from day one?
- is `Counter` a separate action or only a contextual combat outcome after parry/dodge?
- does M0 need `Look` as an explicit gameplay action, or is camera mostly passive during the first duel?
- should lock-on use toggle or hold behavior?
- are `Pause` and debug actions required from the first playable build or only from tuning builds?

## 27. Acceptance Criteria For M0

`Input Mapping` passes M0 if:

- Unity New Input System is the chosen input foundation
- raw movement, attack, dodge, parry, and lock-on inputs are readable and debug-visible
- input intent is clearly routed to the correct owning systems
- downstream rejections can be explained when available
- input does not secretly decide movement truth
- input does not secretly decide combat validity
- input does not secretly decide target truth
- buffering remains conservative and does not hide commitment/recovery

`Input Mapping` fails M0 if:

- legacy Input Manager assumptions remain part of the design
- input truth and gameplay truth are mixed together
- rejected action input feels random and cannot be debugged
- input buffering bypasses combat or locomotion commitment
- lock-on input owns target truth instead of requesting it
