# Lock-On & Combat Camera

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Combat As Interpretation, Melancholic Elegance

## 1. System Summary

`Lock-On & Combat Camera` defines how camera framing and target-focus presentation support duel readability in `Glass Refrain`. Its purpose is to make the player’s combat view stable, legible, and emotionally appropriate during the first M0 duel prototype so that `Combat Core` and `Enemy Intent & Telegraph` can actually be understood in play.

For M0, this system exists to support the loop `read → evade/parry → counter → reveal` by ensuring the player can see what matters at the right time. The player should be able to track enemy presence, approach, telegraph, commitment, active threat, recovery, punish opportunity, and reveal disruption without the camera fighting them or hiding the critical moment.

For M0, target focus truth is provisionally owned by `Lock-On / Target Context`. This GDD owns how camera framing and readability respond to that target context. It does not make target validity, movement, or combat-result decisions.

This system does not own combat truth. It does not decide hit results, enemy intent, player action validity, `CounterWindow`, or reveal validity. Those remain owned by `Combat Core` and the enemy-side authored systems. `Lock-On & Combat Camera` exists to make those authoritative states readable and emotionally coherent from the player’s point of view.

In short, this is the readability layer for the duel view. If the first enemy and first combat loop are authored well but the camera hides the important information, the prototype will still fail. This system exists to prevent that.

## 2. Design Intent

The design intent of `Lock-On & Combat Camera` is to help the player read intent rather than to create spectacle first. In M0, the camera should serve the duel. It should frame the player and enemy clearly enough that spacing, threat timing, defensive opportunity, and punish states can be learned without confusion.

Target focus should support controlled katana dueling. The player should feel able to stay mentally connected to the enemy during tense, short exchanges without relying on a flashy or over-automated camera system. The camera should help preserve the feeling of deliberate footwork and tight emotional tension instead of turning the prototype into a cinematic showcase.

Tonally, the camera should preserve the melancholic and elegant identity of `Glass Refrain`. This means restrained motion, stable readability, and emotionally coherent framing. Even when the duel becomes violent for a moment, the camera should not panic, over-shake, or chase spectacle at the cost of clarity.

For M0, the camera and lock-on layer should be simple, stable, and readable. It does not need advanced target logic, boss-phase framing, multi-enemy cycling, or production polish. It needs to do one thing well: make one duel understandable. Readability matters before cinematic polish.

## 3. Player Experience Goals

The player experience goals for this system are about visual trust. The player should feel that the camera is helping them understand the duel rather than competing with it.

### Enemy Visibility

The player should be able to see the enemy before and during telegraph. The camera should not allow the core threat to slip off-screen during the moments when reading matters most.

### Spacing Readability

The player should be able to judge distance and spacing clearly enough to understand whether they are safe, threatened, or in position to punish. The duel should feel spatially readable rather than flat or ambiguous.

### Facing And Target Focus Clarity

The player should understand who they are focused on and how their character is oriented relative to the enemy. Target focus should support controlled dueling rather than disorienting camera correction.

### Defensive Outcome Visibility

The player should be able to see dodge, parry, and counter outcomes clearly. If the player answered correctly, the camera should let that success be legible. If they failed, the camera should not obscure why.

### Punish Opportunity Visibility

The player should be able to see when the enemy is in recovery or punishable. The camera should not hide the reward side of the duel loop after the player correctly reads and answers a threat.

### Reveal Readability

The player should be able to see reveal disruption or memory-fracture feedback without losing the next read. Reveal should be visible, but not at the cost of the following enemy telegraph or reset state.

### Input Cooperation

The camera should not fight player input. Even in a simple prototype, the player should feel that their movement and view control are cooperating rather than competing.

### Intent Protection

The camera should not hide enemy intent. If the enemy is readable in authored data but not readable on-screen, this system has failed its purpose.

## 4. M0 Scope

This section defines exactly what `Lock-On & Combat Camera` includes for `M0 — Katana Combat Feel Prototype`. The goal is to support one readable duel space with one player and one enemy.

### Included In M0

#### One Duel Camera Setup

M0 includes one core combat camera setup suitable for a single duel in one prototype arena. It only needs to support the first readable katana encounter, not the full game camera stack.

#### One Target Focus / Lock-On Mode

M0 includes one basic target focus or lock-on mode. This mode should help the player maintain readable orientation to the enemy without introducing advanced targeting complexity.

#### Basic Target Selection For One Enemy

The system only needs basic target selection for one enemy. It does not need multi-target cycling, enemy-priority logic, or battlefield-wide target management.

#### Camera-Relative Or Target-Relative Support

M0 may use camera-relative or target-relative support, but the final choice can remain open for now. The system only needs enough structure to keep movement, orientation, and enemy visibility readable during the duel.

#### Readable Framing During Neutral / Approach

The camera should frame the player and enemy clearly during presence, spacing, and approach so the player can establish the duel before the first committed threat.

#### Readable Framing During Telegraph / Commitment

The camera should keep the enemy visible and readable during telegraph and commitment, since those are the key fairness phases of the loop.

#### Readable Feedback During Hit / Parry / Counter / Reveal

The camera should support readable feedback for hit, parry, counter, and reveal disruption without overreacting. The player should feel the exchange, but not lose the next piece of information.

#### Debug Visibility For Target, State, And Framing

M0 includes debug-facing visibility for current target, target-focus state, and relevant camera readability signals. Designers should be able to tell whether framing or target focus is contributing to readability problems.

### M0 Completion Target For This System

`Lock-On & Combat Camera` is in scope for M0 when one duel camera setup and one simple target-focus mode are enough to keep the first enemy readable through neutral, telegraph, commitment, punishment, and reveal support.

## 5. Non-Goals

`Lock-On & Combat Camera` must stay narrowly focused for M0. It exists to make one duel readable, not to solve every future camera and targeting problem in `Glass Refrain`.

### Not A Boss Camera Framework

M0 does not need boss-phase framing logic, duel-arena camera scripts, cinematic escalation cameras, or dramatic boss-introduction behavior.

### Not Multi-Enemy Target Cycling

M0 does not need advanced multi-target selection, cycling, or priority sorting. One enemy is enough.

### Not A Cinematic Cutscene Camera

This system does not define story cutscenes, scripted dramatic pans, or full narrative camera language. Those belong elsewhere and later.

### Not Full Camera Polish

M0 does not require final smoothing, polish passes, subtle camera acting, or production camera feel. It needs readable, stable functionality first.

### Not An Advanced Camera Collision System

M0 does not need a robust final camera collision and obstruction framework. Basic readability matters more than full traversal-grade camera robustness at this stage.

### Not Full Accessibility Camera Options

This pass does not define full accessibility feature sets such as extensive camera remapping, sensitivity presets, motion options, or alternative targeting modes.

### Not Photo Mode

M0 does not include photo mode, capture framing tools, free camera, or screenshot systems.

### Not Production Lock-On UI

This system does not require final lock-on reticles, full production target markers, or final HUD integration.

### Not Final HUD

The M0 camera and lock-on layer should not depend on a finished HUD or final combat interface design.

### Not Complex Aim Assist

M0 does not need deep aim assist, soft targeting ladders, snap assistance layers, or targeting correction systems designed for large encounter variety.

### Not A Ranged Combat Camera

This pass does not define camera behavior for ranged weapons, aiming states, projectile combat, or mixed-range battles.

### Not An Open-World Exploration Camera

M0 does not need a full exploration camera for large-scale traversal, hub navigation, or semi-open-space play. It only needs one duel-space framing solution.

### Not A Multiplayer Camera

M0 does not support split-screen, shared-screen, spectator, or any networked camera logic.

### Scope Protection Rule

If a camera or lock-on feature does not improve readability of one player versus one simple enemy in the first duel prototype, it should be deferred.

## 6. Core Camera / Lock-On Loop

The purpose of the M0 camera and lock-on loop is to keep the duel understandable from moment to moment. This system does not create combat truth. It creates a stable, readable point of view from which the player can find the enemy, judge spacing, read telegraph, answer with confidence, recognize success or failure, and return to a neutral rhythm without losing orientation.

### 6.1 Core Loop Overview

The M0 camera / lock-on loop should support this readability flow:

`find target → frame duel → read intent → support answer → confirm result → preserve reveal → reset readability`

This maps directly onto the combat loop:

- `find target` and `frame duel` support `read`
- `read intent` supports enemy telegraph and commitment
- `support answer` helps dodge, parry, and counter visibility
- `confirm result` makes hit, parry, dodge, counter, and stagger outcomes legible
- `preserve reveal` lets memory disruption be seen without hiding danger
- `reset readability` returns the duel to calm, readable framing

The camera should therefore behave like a readability partner. It should not chase spectacle, overreact to every exchange, or demand that the player fight the view while also fighting the enemy.

### 6.2 Find Target Phase

The first responsibility of the system is to identify and maintain focus on the current duel target. In M0, this can remain simple because there is only one meaningful enemy in the prototype space.

During this phase:

- the camera or target-focus layer should establish who the current duel subject is
- target focus should help the player orient themselves toward that enemy
- the player should not need to search the arena for the only relevant threat
- target focus must remain a readability aid rather than a gameplay authority

This phase does not decide combat validity. It does not decide whether the player can hit, parry, counter, or reveal. It only helps the player stay visually connected to the enemy that matters.

### 6.3 Frame Duel Phase

Once the target is established, the camera should frame the duel clearly enough that both the player and enemy remain understandable in space. The purpose of framing is not to create a dramatic shot. It is to preserve duel legibility.

During this phase:

- the player and enemy should be kept readable when possible
- spacing should be visible enough to support judging distance and threat
- the enemy’s body and weapon should not be casually hidden
- the camera should reinforce the feeling of a controlled katana duel
- framing should stay restrained rather than excessively cinematic

If the player cannot tell how far they are from the enemy or whether the enemy is threatening from the current position, the framing has failed the duel.

### 6.4 Read Intent Phase

The read-intent phase is where the camera most directly supports fairness. The enemy’s telegraph, windup, stance shift, and visible commitment need to stay on screen in a way the player can actually interpret.

During this phase:

- the camera should prioritize enemy telegraph visibility
- enemy windup, stance, and commitment should remain readable
- timing-critical reads should not be disrupted by unnecessary angle changes
- the player should be able to judge both timing and spacing from the current view

This phase is especially important because `Enemy Intent & Telegraph` may be authored correctly and still fail in play if the camera turns a readable attack into an unreadable one.

### 6.5 Support Answer Phase

Once the player begins responding with dodge, parry, or counter intent, the camera should become stable and cooperative. The player should feel that the camera is helping preserve the exchange, not adding new difficulty through motion or disorientation.

During this phase:

- the camera should remain stable during dodge, parry, and counter timing windows
- the view should not swing wildly during precise defensive inputs
- dodge movement should remain spatially understandable
- facing during parry and counter should remain legible
- target focus may help maintain duel orientation if that improves clarity

This does not mean the camera must become static. It means the camera must not introduce noise during the most timing-sensitive part of the loop.

### 6.6 Confirm Result Phase

After the answer resolves, the player needs to see what happened. The camera should support the legibility of hit, whiff, parry, dodge, counter, and stagger outcomes without overcommitting to spectacle.

During this phase:

- hit and whiff results should be visible
- parry, dodge, counter, and stagger outcomes should be easy to read
- camera feedback may lightly support result clarity
- impulse, shake, or motion emphasis should remain restrained
- result feedback should not hide the next enemy read

The player should be able to tell whether they succeeded or failed from the view itself, not only from debug or audio.

### 6.7 Preserve Reveal Phase

When reveal disruption or memory-fracture feedback occurs, the camera should allow it to register without letting it take ownership of the moment. In M0, reveal is part of the identity of the duel, but it must not become a cutscene.

During this phase:

- reveal disruption should be visible and understandable
- the camera should not turn reveal into a full cinematic beat
- reveal feedback must not hide enemy reset or the next threat
- light camera emphasis is acceptable only after valid combat success

The purpose of this phase is to let the player feel that something meaningful was disturbed while still protecting the duel’s next readable moment.

### 6.8 Reset Readability Phase

After the exchange completes, the camera should return to stable, readable framing. The player and enemy should both be easy to locate again, and the duel should feel ready to begin another readable cycle.

During this phase:

- the camera returns to a stable duel view
- player and enemy location should be easy to understand
- spacing should again feel legible
- the system should support `calm → threat → answer → punish/reveal → reset`

This reset matters because a readable combat loop is not only about the attack moment. It is also about how cleanly the duel returns to tension afterward.

### 6.9 M0 Loop Variants

The camera and lock-on loop should be able to support several simple M0 exchange patterns:

- `target focus → enemy approach → telegraph visible → player parry → counter visible → reveal visible → reset`
- `target focus → enemy attack → player dodge → enemy whiff/recovery visible → counter opportunity visible → reset`
- `target focus → player fails answer → hit reaction visible → enemy reset readable`
- `no lock-on / soft target focus → camera still keeps enemy readable enough for M0 testing`

These variants exist to prove that the camera can support the duel loop even when the player succeeds, fails, or uses different defensive answers.

### 6.10 Relationship To Combat Core And Enemy Intent

`Lock-On & Combat Camera` observes combat and enemy state. It does not decide any gameplay result.

- `Combat Core` owns combat truth, hit results, dodge and parry validation, `CounterWindow`, and reveal validity
- `Enemy Intent & Telegraph` owns telegraph, commitment, attack window, punish, and enemy-side readability truth
- `Lock-On & Combat Camera` supports readability, orientation, and feedback only

The camera therefore does not decide hit, dodge, parry, counter, punish, or reveal validity. It exists to make the authoritative state from adjacent systems readable in play.

### 6.11 Debug Requirements

For M0, the debug layer should expose enough camera-facing information to explain why readability succeeded or failed.

Debug should show:

- current target
- `lock-on active?`
- current camera mode or state
- current framing mode
- `is enemy visible?`
- `is player visible?`
- `enemy telegraph visible?`
- `target focus active?`
- `camera blocked / occluded?` if tracked later
- last combat event that triggered camera feedback

This information should help designers answer whether a readability problem comes from combat design, enemy intent, or the camera view itself.

### 6.12 Anti-patterns

The following behaviors should be treated as failure cases for M0:

- camera hides enemy windup
- camera prioritizes cinematic motion over readability
- camera shake occurs during parry timing
- camera cuts away or overcommits during reveal
- lock-on decides combat validity
- target focus makes all combat actions require lock-on
- camera drifts enough that spacing cannot be judged
- reveal feedback blocks the next read
- boss-camera behavior is overbuilt into M0

### 6.13 Open Questions

The following questions remain open for later sections or later system decisions:

- whether M0 requires hard lock-on or only soft target focus
- whether player movement is camera-relative or target-relative during lock-on
- whether the enemy must always remain fully on screen during telegraph
- whether camera impulse is needed for parry or counter in M0
- whether reveal receives a camera emphasis or only VFX/audio support
- whether camera reset is instant, damped, or state-driven
- whether camera behavior is allowed to change during `EnemyTelegraph`

## 7. Camera State Model

The purpose of the M0 camera state model is to describe the small set of readable camera and target-focus states needed to support the first duel prototype. This is not a full camera architecture and not a `Cinemachine` plan. It is a design-level model for how the camera shifts its emphasis across a duel while remaining stable, restrained, and readable.

### 7.1 CameraNeutral / Soft Follow

`CameraNeutral / Soft Follow` is the default readable follow state. It exists to keep player movement understandable before or between high-tension combat beats while still preserving awareness of the current enemy when combat is active.

Its purpose is to:

- provide stable baseline follow behavior
- keep player locomotion readable
- support calm pre-engagement framing
- preserve general enemy awareness when possible

Rules for this state:

- it may transition to `TargetFocus / Lock-On` when a valid enemy is engaged
- it should not fight player look input
- it should not hide the current enemy if combat is active
- it should preserve readable spatial orientation in the duel space

This is the state the system returns to when no stronger readability demand is active.

### 7.2 TargetFocus / Lock-On

`TargetFocus / Lock-On` is the primary duel-orientation state. Its purpose is to keep one enemy as the readable combat subject so the player can understand spacing, facing, and threat direction during the exchange.

Its purpose is to:

- maintain one clear duel target
- support readable facing and target orientation
- make enemy telegraph and approach easier to track
- reduce confusion about who the player is dueling

Rules for this state:

- M0 has only one enemy, so target selection can remain simple
- target focus must not decide combat validity
- lock-on should support readability without making all combat actions depend on lock-on
- the camera should still preserve player orientation and spacing comprehension

For M0, this state is primarily a readability aid, not a mechanical gate.

### 7.3 TelegraphFraming

`TelegraphFraming` exists to preserve visibility of enemy windup, stance, and commitment. This state most directly supports the player’s `Read` phase by protecting the enemy’s attack preparation from being hidden or visually diluted.

Its purpose is to:

- keep enemy telegraph visible
- protect readable enemy body and weapon language
- preserve timing clarity before active threat
- reduce camera motion during the most important read

Rules for this state:

- it should avoid major camera swings during telegraph
- enemy body and weapon should remain readable
- it may prioritize enemy visibility over visual flourish
- it must not hide player positioning or erase spacing understanding

This state should make the player feel that the game is helping them understand danger rather than dramatizing it.

### 7.4 AnswerSupport

`AnswerSupport` exists to keep dodge, parry, and counter input moments readable. This state protects the timing-critical response phase from camera behavior that would make precision harder to judge.

Its purpose is to:

- preserve timing clarity during defensive response
- keep movement direction understandable
- support readable player facing during parry or counter
- reduce visual noise during critical input windows

Rules for this state:

- the camera should remain stable during timing-critical windows
- dodge, parry, and counter direction should stay understandable
- excessive shake, zoom, or rotation should be avoided
- target focus may help preserve duel orientation if it improves clarity

This state should support player confidence rather than visual drama.

### 7.5 ResultFeedback

`ResultFeedback` exists to visually support the outcome of the exchange once a hit, whiff, parry, dodge success, counter, or stagger result has been validated by upstream systems.

Its purpose is to:

- help the player recognize the outcome of the exchange
- reinforce success or failure clarity
- support emotional release after a correct answer
- remain restrained enough to preserve the next read

Rules for this state:

- it may use restrained framing adjustment or mild impulse
- it should not obscure the next enemy read
- it must always follow `Combat Core` result truth
- it must not decide or imply a result that was not validated

The outcome should feel visible, but never at the cost of fairness.

### 7.6 PunishReadability

`PunishReadability` exists to keep enemy recovery and punish posture visible after a committed mistake, whiff, parry, or stagger outcome. This state helps the player recognize that the enemy is exposed.

Its purpose is to:

- preserve visibility of enemy vulnerability
- make counter opportunity understandable
- keep spacing readable during punish moments
- support the reward side of the duel loop

Rules for this state:

- the enemy’s exposed posture should remain in view
- spacing should stay understandable enough for player response
- `CounterWindow` must still be validated by `Combat Core`
- the camera may support visibility of punish, but must not create the punish itself

This state exists because the duel should communicate not only danger, but also earned opportunity.

### 7.7 RevealSupport

`RevealSupport` exists to preserve visibility of reveal disruption after meaningful combat success. It supports `Glass Refrain`’s identity by letting the player register memory fracture or emotional disturbance without taking control away from the duel.

Its purpose is to:

- make reveal disruption visible
- support the emotional identity of the combat loop
- preserve the link between counter success and memory disturbance
- avoid turning the moment into a cinematic interruption

Rules for this state:

- it should be short and restrained
- it should not hide enemy reset or next threat
- it may emphasize reveal only after valid reveal context
- it should never become a cutscene substitute in M0

This state should register meaning, not steal pacing.

### 7.8 CameraReset

`CameraReset` exists to return the camera to stable, readable duel framing after the exchange resolves. Its role is to restore orientation without abrupt disorientation or visual confusion.

Its purpose is to:

- restore stable duel framing
- make player and enemy readable again
- re-establish spacing clarity
- prepare the next readable cycle

Rules for this state:

- it should avoid abrupt disorientation
- it should restore player and enemy readability
- it may transition back to `TargetFocus / Lock-On` or `CameraNeutral / Soft Follow`
- it should preserve the emotional rhythm of `calm → threat → answer → punish/reveal → reset`

This is the state that closes one exchange cleanly so the next one can begin clearly.

### 7.9 State Transition Overview

The normal M0 camera path should be simple and readable:

- `CameraNeutral / Soft Follow → TargetFocus / Lock-On → TelegraphFraming → AnswerSupport → ResultFeedback → PunishReadability → RevealSupport` optional `→ CameraReset → TargetFocus / Lock-On`
- `TargetFocus / Lock-On → TelegraphFraming → AnswerSupport → ResultFeedback → CameraReset`
- `CameraNeutral / Soft Follow → TargetFocus / Lock-On` when combat engagement begins

Important branch cases include:

- player fails answer `→ ResultFeedback → CameraReset`
- enemy whiffs `→ PunishReadability → CameraReset`
- successful counter `→ ResultFeedback → RevealSupport → CameraReset`
- lock-on disengaged `→ CameraNeutral / Soft Follow`

These paths are not meant to be overcomplicated. They only need to describe how the camera stays aligned with duel readability in one-on-one combat.

### 7.10 Combat / Enemy State Interaction Notes

Camera states observe `Combat Core` and `Enemy Intent & Telegraph`. They do not own gameplay state.

- camera states observe combat and enemy-side state changes
- camera does not decide combat state
- `EnemyTelegraph` may request `TelegraphFraming`
- `CounterWindow` or `EnemyPunishWindow` may request `PunishReadability`
- `RevealRequested` or `RevealAccepted` may request `RevealSupport`
- camera requests should be ignored if they would harm readability or conflict with a higher-priority readability state

The most important boundary is that camera behavior must remain subordinate to readability, not to spectacle or event chaining.

### 7.11 State Priority Philosophy

The M0 priority philosophy should remain simple:

- readability beats spectacle
- telegraph visibility beats camera flourish
- result feedback must not hide the next threat
- reveal support must not become cinematic control
- player orientation must remain understandable

If two camera desires conflict, the system should prefer the one that keeps the duel clearer.

### 7.12 Debug Requirements

For M0, the debug layer should expose:

- current camera state
- previous camera state
- time in current camera state
- `lock-on / target focus active`
- current target
- camera state reason
- `enemy visible?`
- `player visible?`
- `telegraph framing active?`
- `result feedback active?`
- `reveal support active?`
- `reset active?`
- last combat or enemy event driving the camera change

This should make it possible to understand whether a readability failure came from combat, enemy intent, or camera state selection.

### 7.13 Provisional Camera State Table

| Camera State | Purpose | Trigger Source | Must Keep Visible | M0 Notes |
| --- | --- | --- | --- | --- |
| `CameraNeutral / Soft Follow` | Stable default follow and orientation | Default movement and non-critical combat moments | Player, general enemy awareness | Baseline duel-space readability state |
| `TargetFocus / Lock-On` | Maintain one readable duel target | Combat engagement, valid target focus request | Player and current enemy | One-target only for M0 |
| `TelegraphFraming` | Protect enemy telegraph readability | Enemy telegraph or commitment request | Enemy body, weapon, player spacing | Readability-first state |
| `AnswerSupport` | Preserve dodge, parry, and counter readability | Timing-critical player response window | Player facing, enemy threat line | Avoid dramatic motion here |
| `ResultFeedback` | Confirm hit, parry, dodge, counter, or stagger outcome | Validated combat result | Immediate exchange outcome | Must remain restrained |
| `PunishReadability` | Show enemy recovery and exposure clearly | Enemy whiff, punish, or stagger opportunity | Enemy vulnerability, player spacing | Does not create `CounterWindow` |
| `RevealSupport` | Show reveal disruption without taking over | Valid reveal-support context | Reveal disruption and next threat context | Optional and short in M0 |
| `CameraReset` | Return to stable readable duel framing | Exchange completion or emphasis end | Player, enemy, spacing | Prepares next loop cleanly |

### 7.14 Anti-patterns

The following patterns should be treated as failures for M0:

- too many camera states before M0 needs them
- camera state deciding combat result
- `TelegraphFraming` hiding player position
- `ResultFeedback` hiding enemy recovery
- `RevealSupport` becoming cutscene camera
- lock-on state overriding player readability
- `CameraReset` causing disorientation
- camera state transitions triggered by VFX alone
- boss-camera assumptions leaking into M0

### 7.15 Open Questions

The following questions remain unresolved:

- whether `TargetFocus` and `Lock-On` are the same state in M0
- whether `TelegraphFraming` is a real state or only a priority modifier
- whether `PunishReadability` is separate from `ResultFeedback`
- whether `RevealSupport` is a true camera state or only a presentation overlay
- whether camera reset is time-based or event-driven
- whether the player can manually break lock-on during `ResultFeedback`
- whether camera state priority should become explicit data later

## 8. Lock-On Targeting Rules

The purpose of M0 lock-on and target-focus rules is to define how the player and camera stay visually connected to the single relevant enemy in the first duel prototype. This system exists to support readability, spacing awareness, and combat orientation. It does not exist to decide gameplay outcomes.

### 8.1 Lock-On Purpose

Lock-on or target focus exists to:

- help the player keep the enemy readable
- support spacing judgment
- support facing and orientation
- make telegraph and commitment easier to read
- help the camera frame the duel
- support the controlled feeling of katana combat

It should not:

- make all combat actions require lock-on unless that is explicitly approved later
- decide whether attacks hit
- decide whether counter is valid
- replace player reading or awareness

Its purpose is to reduce visual confusion, not to automate combat understanding.

### 8.2 M0 Targeting Scope

For M0, target selection remains intentionally small:

- one player
- one enemy
- one active duel target
- no target cycling required
- no multiple lock points required
- no boss body-part targeting
- no target priority system beyond choosing the single valid enemy
- no production lock-on UI required

This keeps the system focused on proving readability in one duel instead of solving the full targeting problem for the game.

### 8.3 Target Acquisition Rules

Target focus can be acquired when a valid enemy exists in the duel space. In M0, a valid target should be:

- active rather than defeated or disabled
- relevant to the current duel
- within reasonable camera and combat relevance
- available as the current combat subject

For M0, target acquisition may be a simple manual toggle, a simple automatic soft-focus behavior, or both depending on what feels most readable in testing. The important rule is that acquisition must be understandable and debug-visible.

Target acquisition does not guarantee:

- that the player is in combat range
- that an attack will hit
- that parry or dodge will succeed
- that counter is valid

It only establishes a readable focus relationship between player, enemy, and camera.

### 8.4 Target Maintenance Rules

Once target focus is active, the camera and orientation layer should try to preserve a readable duel relationship between player and enemy.

While focus is maintained:

- the camera should try to keep both player and enemy readable
- the enemy should remain the current target while active and relevant
- target focus should support facing and framing
- target focus should not override `Combat Core` state or validation
- if the enemy telegraphs, target focus should help preserve that visibility
- if the player dodges, parries, or counters, target focus should keep orientation understandable

Maintenance is about visual continuity. It should reduce disorientation without becoming an invisible gameplay decision-maker.

### 8.5 Target Release Rules

Target focus may release when:

- the player toggles lock-off
- the enemy is defeated or disabled
- the enemy becomes invalid
- the encounter ends
- a debug reset occurs
- future camera constraints make target maintenance impossible, if such constraints are later added

For M0:

- release rules should stay simple
- release should be predictable
- release should not occur during timing-critical moments unless there is no reasonable alternative

The player should not feel that the camera silently abandoned the duel during the one moment they needed it most.

### 8.6 Hard Lock-On vs Soft Target Focus

Two conceptual approaches are acceptable for M0:

#### Hard Lock-On

Hard lock-on means:

- the player has an explicit locked target
- the camera strongly frames the duel around player and enemy
- facing and combat orientation are more controlled

This can be useful for strict one-on-one readability, but it carries the risk of feeling rigid or fighting player camera control if tuned too aggressively.

#### Soft Target Focus

Soft target focus means:

- the camera biases toward the enemy without strict lock
- the system is less intrusive
- the player retains more natural camera ownership

This can be useful for early prototyping if hard lock feels heavy, but it risks allowing telegraph or spacing information to drift out of view if the bias is too weak.

#### Recommended M0 Direction

The recommended direction for M0 is:

- start with simple target focus or soft lock if possible
- move toward harder lock-on only if readability clearly needs it
- keep the final decision open until camera and locomotion feel are tested together

This preserves flexibility while keeping readability as the deciding principle.

### 8.7 Lock-On And Combat Validity

Lock-on and target focus do not own combat truth.

- lock-on does not decide hit result
- lock-on does not decide parry or dodge success
- lock-on does not open `CounterWindow`
- lock-on does not validate reveal
- `Combat Core` owns combat validity
- `Enemy Intent & Telegraph` owns telegraph, attack, and punish truth
- lock-on only supports orientation, framing, and readability

This boundary is critical. If lock-on begins deciding gameplay outcomes, the player can no longer trust the combat system’s explicit rules.

### 8.8 Lock-On And Facing Support

Target focus may support the player’s facing relationship to the enemy during neutral and combat states, but this support must remain coordinated with `Combat Core` and `Player Locomotion`.

For M0:

- lock-on may help the player face the target
- facing support should preserve duel readability
- attack, parry, and counter-facing behavior must be coordinated with other systems
- counter auto-alignment remains an open question
- the camera should not force facing changes that make player control harder to understand

The goal is orientation support, not control theft.

### 8.9 Lock-On And Enemy Telegraph

During enemy telegraph, target focus should support readability rather than adding more motion.

During telegraph:

- target focus should help keep enemy windup visible
- sudden camera transitions should be avoided
- enemy body and weapon should remain readable
- player positioning should still remain visible
- lock-on should not zoom or rotate so aggressively that timing becomes harder to judge

Telegraph support is one of the most important reasons this system exists in the first place.

### 8.10 Debug Requirements

For M0, debug should expose:

- `lock-on active?`
- `soft focus active?`
- current target
- `target valid?`
- target acquisition reason
- target release reason
- target distance
- `target visible?`
- `target within camera relevance?`
- lock-on mode
- last lock-on input or request
- whether target focus is affecting facing or framing

This should help the team understand whether a readability failure comes from targeting behavior, camera behavior, or combat design.

### 8.11 Targeting Table

| Rule Area | M0 Behavior | Why It Matters | Must Not Do | Debug Requirement |
| --- | --- | --- | --- | --- |
| `Acquisition` | Acquire the single valid duel enemy through simple toggle or soft focus | Establishes readable combat subject | Must not imply combat range or hit validity | Show target, reason, and mode |
| `Maintenance` | Keep current enemy as focus while active and relevant | Preserves orientation and spacing understanding | Must not override `Combat Core` truth | Show active target and focus state |
| `Release` | Release on manual lock-off, invalid target, defeat, encounter end, or debug reset | Prevents stale or confusing target state | Must not drop focus unpredictably in critical moments | Show release reason |
| `Hard Lock-On` | Strong duel framing around explicit target | May improve one-on-one readability | Must not fight player control excessively | Show hard-lock mode active |
| `Soft Target Focus` | Bias camera toward enemy without strict lock | May feel lighter and less intrusive | Must not let enemy drift out of readable view | Show soft-focus mode active |
| `Facing Support` | May help maintain readable orientation toward enemy | Helps player understand duel direction | Must not secretly decide action validity | Show whether focus is affecting facing |
| `Telegraph Support` | Preserve windup and weapon readability during threat setup | Supports fair read phase | Must not hide player position or spacing | Show telegraph visibility status |
| `Combat Validity Boundary` | Observe and support only | Protects ownership boundaries with `Combat Core` | Must not decide hit, parry, dodge, counter, or reveal | Show state without altering it |

### 8.12 Anti-patterns

The following are failure patterns for M0:

- lock-on deciding combat hit validity
- lock-on being required for every attack without design approval
- target focus hiding enemy telegraph
- target release during timing-critical moments
- overbuilding multi-target cycling for M0
- hard lock fighting player control
- soft focus letting the enemy drift out of frame
- lock-on camera hiding spacing
- target UI becoming required before basic readability works
- boss lock-on assumptions leaking into M0

### 8.13 Open Questions

The following questions remain unresolved:

- whether M0 should start with hard lock-on or soft target focus
- whether lock-on is manually toggled or automatically engaged in the duel prototype
- whether lock-on is required for counter readability
- whether counter auto-aligns to the locked target
- whether movement becomes target-relative during lock-on
- whether target focus can be broken during `ResultFeedback` or `RevealSupport`
- whether a visible lock-on marker is needed for M0

## 9. Target Focus / Facing Support

The purpose of target focus and facing support in M0 is to help the player stay oriented in a readable duel without automating the combat for them. This section defines how camera and target focus may support facing, spacing awareness, dodge readability, and counter readability while keeping movement ownership in `Player Locomotion` and combat truth ownership in `Combat Core`.

### 9.1 Facing Support Purpose

Target focus should help the player:

- know which enemy is the current duel target
- understand where the player is facing
- judge spacing
- keep enemy telegraph readable
- align attacks, parries, and counters visually enough to feel fair
- maintain controlled katana duel orientation

It should not:

- auto-solve positioning
- force every combat action to connect
- replace player spacing discipline
- override `Combat Core` action rules

Its job is to make orientation clearer, not to remove the need for player judgment.

### 9.2 M0 Facing Modes

For M0, the system can be described through three simple conceptual facing modes.

#### Free Facing / Movement Facing

In `Free Facing / Movement Facing`, the player faces movement direction or input direction. This is useful outside explicit lock-on or in a lighter soft-focus mode where the player retains more freedom of orientation.

This mode:

- gives the player more natural movement freedom
- is useful outside strict duel framing
- may reduce duel readability if the enemy relationship becomes visually loose

#### Target-Facing / Lock-On Facing

In `Target-Facing / Lock-On Facing`, the player tends to face the current duel target. This can help preserve one-on-one readability, support telegraph interpretation, and keep attacks or defensive actions visually coherent.

This mode:

- supports duel readability
- helps maintain facing toward the enemy
- may help attack, parry, and counter direction feel more intentional
- risks feeling rigid if overapplied

#### Action-Constrained Facing

In `Action-Constrained Facing`, the player’s facing may be limited, stabilized, or lightly corrected during attack, parry, counter, or hit-reaction states.

This mode:

- must remain coordinated with `Combat Core` and `Player Locomotion`
- may improve readability during committed action moments
- must not secretly change combat validity

For M0:

- facing rules should stay simple
- readability should matter more than realism
- complex aim assist should be avoided

### 9.3 Target Focus And Player Movement

Target focus may support either camera-relative or target-relative movement in M0, but the final choice remains open until camera and locomotion feel are tested together.

The important rules are:

- movement should preserve spacing readability
- the player should be able to reposition around the enemy
- target focus should not make movement feel stuck or over-constrained
- dodge direction must remain understandable

This system may support readable orientation, but movement implementation still belongs to `Player Locomotion`.

### 9.4 Target Focus And Attacks

Target focus may help attacks visually face toward the enemy so the duel feels intentional and readable, but it must not turn attacks into automatic hits.

For M0:

- target focus may lightly support attack-facing clarity
- attack hit validity is still decided by `Combat Core` and hit-detection rules
- light and heavy attacks should not auto-hit just because target focus is active
- any facing correction should remain small and readable
- heavy attack should still feel committed and punishable

The goal is not to guarantee success. The goal is to make intent and failure visually understandable.

### 9.5 Target Focus And Parry

Target focus may help the player visually understand parry direction and duel orientation, especially when the enemy is committing to a readable attack. This can support fairness by making the confrontation easier to parse.

For M0:

- target focus may support parry readability if needed
- parry success still depends on `Combat Core` state, timing, eligibility, and enemy attack tags
- lock-on should not make parry succeed automatically
- parry feedback should remain visible within the camera framing

The camera may clarify the moment, but it must not decide the result.

### 9.6 Target Focus And Dodge

Dodge direction in M0 may end up input-relative, camera-relative, or target-relative. That decision remains open, but target focus must keep the resulting motion understandable.

For M0:

- target focus should keep dodge movement understandable
- dodge should not become automatic evade just because lock-on is active
- the camera should preserve visibility of the enemy’s active threat and the player’s displacement
- spacing before and after dodge should remain readable

Dodge should feel like a deliberate answer, not an automatic escape granted by target focus.

### 9.7 Target Focus And Counter

Counter may need clearer facing support than other actions because it is the most reward-oriented answer in the loop. Some degree of facing support or limited auto-alignment may help the counter read as intentional rather than awkward.

For M0:

- target focus may help the counter visually face the enemy
- counter validity remains owned by `Combat Core`
- target focus can help counter look intentional and earned
- counter should not teleport or snap unfairly unless that is explicitly designed later
- whether lock-on is required for counter readability remains open

This keeps counter readable without quietly turning it into a scripted auto-hit.

### 9.8 Facing And Enemy Telegraph

During enemy telegraph, target focus should help the player stay oriented without over-rotating the view or distorting timing perception.

During telegraph:

- target focus should keep enemy body and weapon readable
- player facing should remain understandable
- the camera should not rotate so aggressively that timing becomes harder to judge
- facing support should help the player trust the read

This is one of the key moments where orientation support and readability support become the same problem.

### 9.9 Debug Requirements

For M0, debug should expose:

- current facing mode
- `target focus active?`
- current target
- player facing direction
- target direction
- facing alignment angle if useful
- movement mode
- `attack facing correction active?`
- `parry facing support active?`
- dodge direction mode
- `counter alignment active?`
- reason facing changed or was constrained

This should make it possible to diagnose whether confusion came from locomotion behavior, target focus, or camera framing.

### 9.10 Facing Support Table

| Area | Facing / Orientation Need | Allowed Support | Must Not Do | M0 Notes |
| --- | --- | --- | --- | --- |
| `Neutral movement` | Keep player orientation understandable while moving in duel space | Free facing or soft target bias | Must not make movement feel stuck | Baseline locomotion readability |
| `Target focus` | Maintain clear relationship to current enemy | Bias or face toward target | Must not secretly decide combat validity | One target only in M0 |
| `Light / Heavy attack` | Make attack intent and facing readable | Small facing support or correction | Must not auto-hit because target focus is active | Heavy should still feel committed |
| `Parry` | Keep defensive direction readable | Facing support if needed for readability | Must not make parry succeed automatically | `Combat Core` still validates success |
| `Dodge` | Keep displacement and escape direction clear | Support readable direction and enemy visibility | Must not become auto-evade | Direction model still open |
| `Counter` | Make the reward action look intentional | Limited alignment support if needed | Must not teleport or unfairly snap | Counter validity remains external |
| `Hit Reaction` | Preserve orientation clarity after failure | Maintain readable recovery framing | Must not erase spacing understanding | Supports fair failure reading |
| `Enemy Telegraph` | Keep enemy threat line readable | Preserve readable facing and framing | Must not over-rotate camera | Critical fairness moment |
| `Reveal Support` | Preserve meaning without losing duel context | Maintain readable target relationship | Must not become cinematic control | Reveal must not erase next read |

### 9.11 Anti-patterns

The following behaviors should be treated as failures for M0:

- target focus auto-solving positioning
- lock-on making every attack connect
- facing correction causing unfair snap rotation
- dodge direction becoming unclear
- parry success depending on camera angle instead of `Combat Core` rules
- counter teleporting to the target without explicit design approval
- target-relative movement feeling too rigid
- camera-relative movement making enemy telegraph hard to track
- facing support hiding spacing mistakes
- lock-on being required for all combat actions without explicit design approval

### 9.12 Open Questions

The following questions remain unresolved:

- whether M0 movement is camera-relative or target-relative while focused
- whether attack-facing correction is allowed
- whether counter auto-aligns to target
- whether parry has direction requirements in M0
- whether dodge direction is input-relative, camera-relative, or target-relative
- whether target focus is required for counter readability
- whether facing constraints become data-authored later

## 10. Enemy Telegraph Readability Rules

The purpose of telegraph readability rules in M0 is to ensure that the camera and target-focus layer preserve the fairness of enemy intent. `Enemy Intent & Telegraph` owns the actual telegraph, commitment, attack windows, tags, and punish logic. `Lock-On & Combat Camera` exists to make those authored truths visible and understandable from the player’s point of view.

### 10.1 Telegraph Readability Purpose

The camera should help the player read:

- enemy windup
- body posture
- weapon motion
- movement direction
- commitment
- active threat timing
- recovery and punish posture

The camera should not:

- hide the enemy during telegraph
- create misleading timing
- over-rotate during timing-critical moments
- prioritize cinematic motion over readable threat
- make player failure feel caused by the camera

The core rule is simple: if the enemy is authored to be fair, the camera must not make that fairness unreadable.

### 10.2 Telegraph Visibility Requirements

During `EnemyTelegraph`:

- the enemy should remain visible whenever possible
- enemy weapon and body should stay readable
- player position should remain understandable
- enemy-to-player spacing should remain readable
- major camera occlusion should be avoided
- excessive zoom, shake, or orbit should be avoided
- target focus should support telegraph visibility rather than fight it

This is the most important fairness-support phase of the camera system.

### 10.3 Camera Behavior During Telegraph

During telegraph, the camera should remain stable and legible. The player should be able to watch the enemy prepare danger without also tracking unnecessary camera behavior.

For M0:

- the camera should remain stable during telegraph
- the camera may gently reframe if the enemy is drifting out of view
- sudden cuts or large rotations should be avoided
- dramatic result feedback must not begin before the result exists
- timing clarity should always matter more than style
- if the camera cannot fully show both player and enemy, enemy telegraph visibility takes priority, but player position must not become confusing

The player should feel guided toward the read, not visually pushed around.

### 10.4 Commitment Visibility

During `EnemyCommit / AttackStartup`, the camera should preserve the line of action so the player can understand that the threat is no longer only a warning. Commitment is the trust phase of the attack, and the camera must help maintain that trust.

During commitment:

- the line of action should remain readable
- enemy movement direction should remain understandable
- weapon release or attack start should be visible
- the camera should not hide whether the enemy has truly committed
- angle changes should be avoided at the exact commitment moment

If the player cannot tell whether the enemy is still warning or is now fully acting, the camera has weakened the duel’s clarity.

### 10.5 Active Threat Visibility

During `EnemyAttackActive`, the camera should preserve the player’s understanding of the actual threat. The player should be able to see why the exchange resolved the way it did.

During active threat:

- the threat should remain readable
- the player should be able to see why hit, dodge, or parry succeeded or failed
- enemy active motion should not be hidden by shake or VFX emphasis
- active threat visibility should support `Combat Core` result clarity

The camera should not add ambiguity during the exact moment the system is judging the exchange.

### 10.6 Recovery / Punish Visibility

After the active threat passes, the camera should preserve the enemy’s recovery and punish posture long enough for the player to understand whether an opportunity exists.

After active threat:

- enemy recovery posture should stay visible
- enemy whiff should be readable if relevant
- punish opportunity should not be hidden by premature camera reset
- the camera should not immediately return to neutral if doing so hides recovery
- the camera should support the transition into `PunishReadability` when needed

This is essential because the reward side of the duel is only meaningful if the player can see it.

### 10.7 Camera Priority During Telegraph

For M0, the camera should follow this priority order during telegraph and immediate attack flow:

1. enemy telegraph visibility
2. player orientation and spacing
3. active threat clarity
4. recovery and punish visibility
5. result feedback
6. visual elegance and style

Style is valuable only if it preserves fairness. If elegance makes the threat harder to read, the camera should choose clarity instead.

### 10.8 Telegraph Failure Cases

The following are camera-related telegraph failures:

- enemy windup is off-screen
- enemy weapon is hidden by player framing or camera angle
- the camera rotates during parry timing
- a zoom change hides spacing
- camera shake begins before hit result
- reveal or VFX feedback hides the next telegraph
- lock-on drifts away from the enemy during telegraph
- camera reset hides recovery or punish posture

If any of these occur regularly, the camera is undermining the duel loop.

### 10.9 Relationship To Enemy Intent & Telegraph

The relationship between the two systems must remain explicit:

- `Enemy Intent & Telegraph` exposes telegraph state and timing
- the camera may observe `EnemyTelegraph`, `EnemyCommit`, `EnemyAttackActive`, `EnemyRecovery`, and `EnemyPunishWindow`
- the camera does not create or extend telegraph windows
- the camera does not decide whether an attack is parryable or dodge-punishable
- the camera must reflect enemy-side truth without altering it

This keeps readability support separate from gameplay ownership.

### 10.10 Debug Requirements

For M0, debug should expose:

- `enemy telegraph active?`
- `enemy visible during telegraph?`
- `enemy weapon/body visible?`
- `player visible?`
- `spacing visible?`
- camera state during telegraph
- `target focus active?`
- `telegraph framing active?`
- `camera occlusion/blocking?` if tracked later
- last camera action during telegraph
- whether the camera changed angle during a timing-critical window

This should help designers determine whether an unfair-feeling exchange came from combat timing or from the camera view.

### 10.11 Telegraph Readability Checklist

During testing, a tester should be able to answer yes to the following:

- I could see the enemy before the attack.
- I could see the enemy windup.
- I could tell when the enemy committed.
- I could see when the threat became active.
- I understood whether I was in range.
- I understood why my dodge or parry succeeded or failed.
- I could see the enemy recovery or punish posture.
- The camera did not make the attack feel unfair.

If these answers are not consistently true, the duel is not yet camera-readable enough for M0.

### 10.12 Telegraph Readability Table

| Telegraph Moment | Camera Responsibility | Must Keep Visible | Must Avoid | M0 Priority |
| --- | --- | --- | --- | --- |
| `Enemy Presence` | Preserve baseline enemy awareness | Enemy, player orientation, general spacing | Hiding the current threat subject | `Should Pass` |
| `Enemy Approach` | Keep distance and line of threat readable | Enemy movement, player relation, spacing | Orbiting that confuses approach path | `Should Pass` |
| `EnemyTelegraph` | Protect windup readability | Enemy body, weapon, player position, spacing | Over-rotation, zoom noise, telegraph loss | `Must Pass` |
| `EnemyCommit / Startup` | Preserve commitment visibility | Enemy line of action and attack start | Angle changes at commitment moment | `Must Pass` |
| `EnemyAttackActive` | Keep threat outcome understandable | Active motion, player response relation | Shake or framing that hides cause | `Must Pass` |
| `EnemyRecovery` | Preserve recovery visibility | Enemy posture and recovery line | Instant reset that erases consequence | `Should Pass` |
| `EnemyPunishWindow` | Keep exposure readable | Enemy vulnerability and spacing | Hiding punish with reset or effects | `Must Pass` |
| `EnemyReset` | Return to stable duel readability | Player, enemy, spacing re-established | Disorienting recovery to neutral | `Nice To Have` |

### 10.13 Anti-patterns

The following patterns should be treated as failures for M0:

- camera hiding windup
- camera orbiting during parry timing
- lock-on framing the player but not the enemy
- camera shake before hit result
- cinematic zoom hiding spacing
- reveal emphasis hiding the next enemy telegraph
- camera reset hiding punish window
- VFX and camera together obscuring weapon motion
- telegraph being readable only through UI or debug
- assuming final animation polish will fix bad framing

### 10.14 Open Questions

The following questions remain unresolved:

- whether enemy weapon visibility is required for every M0 telegraph
- whether the camera can gently reframe during `EnemyTelegraph`
- whether camera movement should freeze or merely damp during timing-critical windows
- whether telegraph visibility requires hard lock-on
- whether camera occlusion handling is required for M0 or deferred
- whether attack range should be visible through debug gizmos
- whether punish visibility belongs mostly here or mostly in section `12. Punish / Reveal Camera Support`

## 11. Dodge / Parry / Counter Camera Support

The purpose of this section is to define how `Lock-On & Combat Camera` supports the player’s response moments without taking ownership of those responses. `Combat Core` owns dodge, parry, and counter validity. `Enemy Intent & Telegraph` owns the enemy-side threat, commitment, recovery, punish, and stagger context. The camera exists to make those moments visible, oriented, and understandable.

### 11.1 Support Purpose

The camera should help the player:

- see the incoming threat
- understand dodge direction and displacement
- understand parry timing and result
- see counter alignment and impact
- understand why success or failure happened
- stay oriented after the exchange

The camera should not:

- decide dodge success
- decide parry success
- decide counter validity
- auto-correct failed positioning into success
- hide timing-critical information
- overuse shake or zoom during response windows

The camera should make the exchange legible, not easier by secretly bending the rules.

### 11.2 Dodge Camera Support

During dodge, the player needs to understand both where the threat is and where they moved in response to it. The camera should preserve that relationship clearly enough that dodge feels like a spatial answer rather than a visually confusing escape.

During dodge:

- the camera should keep enemy threat and player displacement readable
- the player should understand where they moved
- enemy active threat should remain visible if possible
- dodge should not feel like teleportation caused by camera movement
- the camera should avoid large rotations during dodge
- if dodge causes an enemy whiff, the camera should preserve enemy recovery and punish visibility

The player should be able to tell whether they escaped correctly because of spacing and timing, not because the view became noisy.

### 11.3 Parry Camera Support

During parry, the most important job of the camera is to protect timing clarity. The player must be able to see the threat arrive, attempt the answer, and understand the result without early visual exaggeration muddying the moment.

During parry:

- the camera should keep enemy attack timing readable
- the camera should not rotate or shake before the parry result is known
- parry success should be visible through enemy and player reaction
- parry failure should remain explainable through timing, spacing, or tag context
- the camera may support parry result with restrained feedback only after the `Combat Core` result is known

The camera must not front-run the outcome by visually implying success before success has been validated.

### 11.4 Counter Camera Support

Counter is the sharpest reward moment in the M0 duel loop, so the camera should help it read as precise and earned without turning it into spectacle-first choreography.

During counter:

- the camera should keep player and enemy relationship readable
- counter alignment should look intentional
- counter impact should be visible
- the camera should not hide enemy stagger or reaction
- counter should not become visually confusing because of snap rotation or excessive zoom
- the camera may support counter impact with mild feedback after result confirmation

The counter should feel exact and meaningful, not overproduced.

### 11.5 Failure Readability

The camera must support failure clarity with the same seriousness as success clarity.

For M0:

- failed dodge should show why the player was still hit or misplaced
- failed parry should show whether timing, spacing, or tag meaning was wrong
- failed counter should show whether the enemy was not punishable, the player was out of range, or the timing was late
- the camera should not make failure feel unfair

If the player loses trust in failure explanation, the duel loop stops being teachable.

### 11.6 Result Feedback Rules

Result feedback should:

- follow `Combat Core` result
- remain restrained
- happen only after confirmed result
- preserve the next enemy read
- avoid hiding punish or recovery
- avoid overriding player-control readability

For M0, result feedback may include:

- small framing adjustment
- mild camera impulse
- short emphasis on impact
- brief focus stabilization

For M0, result feedback should not include:

- cinematic cutaway
- heavy slow motion
- long zoom
- screen-filling shake
- forced camera orbit
- loss of player or enemy visibility

Feedback should reinforce the truth of the exchange without replacing it.

### 11.7 Transition Back To Readability

After dodge, parry, or counter, the camera should return to readable duel framing without erasing what just happened.

After response resolution:

- the camera should return to stable duel readability
- player and enemy should be easy to locate
- enemy recovery or punish posture should remain visible if still active
- reveal support should only occur if valid reveal context exists
- reset should not erase the player’s understanding of the last result

The exchange should feel complete, but the next read should still be protected.

### 11.8 Relationship To Combat Core

The boundary with `Combat Core` must remain explicit:

- `Combat Core` sends or exposes confirmed action and result context
- the camera reacts to confirmed results
- the camera does not infer success from animation, VFX, or audio alone
- the camera does not open `CounterWindow`
- the camera does not validate reveal
- camera feedback must not contradict `Combat Core` result

This ensures the player never receives mixed messages about what actually happened.

### 11.9 Relationship To Enemy Intent & Telegraph

The boundary with `Enemy Intent & Telegraph` is equally important:

- `Enemy Intent & Telegraph` exposes active, recovery, punish, and stagger context
- the camera may use that context to preserve visibility
- the camera does not extend punish windows
- the camera does not decide enemy vulnerability
- the camera should not hide `EnemyPunishWindow` or `EnemyStagger`

The camera helps show the opportunity, but it does not create it.

### 11.10 Debug Requirements

For M0, debug should expose:

- last player response type: `dodge`, `parry`, or `counter`
- last `Combat Core` result
- camera state during response
- `camera feedback triggered?`
- feedback source event
- `enemy visible during response?`
- `player visible during response?`
- `spacing visible?`
- `punish window visible after response?`
- `camera moved during timing-critical window?`
- `reveal support requested after counter?`

This should make it possible to inspect whether an unclear exchange was caused by combat rules, enemy behavior, or camera support.

### 11.11 Dodge / Parry / Counter Support Table

| Player Response | Camera Responsibility | Must Keep Visible | Must Avoid | Result Feedback Allowed | M0 Priority |
| --- | --- | --- | --- | --- | --- |
| `Dodge Start` | Preserve threat and intended escape direction | Enemy threat, player start position, spacing | Large rotations or premature reset | Minimal or none | `Must Pass` |
| `Dodge Movement` | Keep displacement understandable | Player path, enemy active threat, spacing outcome | Camera motion that makes dodge feel like teleport | Minimal stabilization only | `Must Pass` |
| `Dodge Success / Whiff` | Preserve enemy whiff and exposure readability | Enemy miss, recovery posture, player result position | Hiding punish with reset or shake | Mild post-result emphasis | `Must Pass` |
| `Dodge Failure / Hit` | Show why dodge failed | Enemy hit relation, player position, threat line | VFX or motion obscuring cause | Mild post-hit feedback only | `Must Pass` |
| `Parry Attempt` | Protect timing readability | Enemy attack line, player relation, commitment moment | Rotation or shake before outcome | None before result | `Must Pass` |
| `Parry Success` | Show clear defensive success and follow-up context | Enemy deflect or stagger, player orientation, punish line | Over-cinematic flourish | Mild impulse or stabilization | `Must Pass` |
| `Parry Failure` | Preserve failure explanation | Threat line, player relation, enemy follow-through | Ambiguous feedback implying success | Mild post-failure feedback only | `Must Pass` |
| `Counter Start` | Preserve readable alignment into reward action | Player-enemy relation, target line, spacing | Snap rotation or zoom confusion | Mild support after confirmation | `Should Pass` |
| `Counter Impact` | Show earned impact and enemy reaction | Enemy stagger, player impact line, duel context | Hiding stagger with zoom or shake | Mild impulse or short emphasis | `Must Pass` |
| `Counter Failure` | Show why counter was invalid or late | Range relation, enemy state, player position | Feedback implying success when rejected | Minimal failure emphasis only | `Must Pass` |
| `Post-Exchange Reset` | Return to readable duel framing | Player, enemy, spacing, punish if still active | Reset that erases consequence | Brief stabilization only | `Should Pass` |

### 11.12 Anti-patterns

The following should be treated as failures for M0:

- camera shake before parry result
- dodge camera rotation hiding enemy active frames
- counter zoom hiding enemy stagger
- camera feedback implying success when `Combat Core` rejected the action
- failure hidden by VFX or camera motion
- lock-on auto-solving failed counter range
- result feedback hiding punish window
- reveal emphasis triggering after invalid counter
- over-cinematic slow motion in M0
- camera fighting player control during response windows

### 11.13 Open Questions

The following questions remain unresolved:

- whether dodge camera should stay fully stable or lightly follow displacement
- whether parry success needs camera impulse in M0
- whether counter impact needs camera emphasis or only animation, VFX, and audio
- whether failed parry needs distinct camera treatment
- whether camera feedback should become data-authored later
- whether result feedback should be disabled during early timing tests
- whether reveal support should follow counter immediately or only after stagger confirmation

## 12. Punish / Reveal Camera Support

The purpose of punish and reveal camera support in M0 is to make enemy exposure and memory disruption readable without letting the camera take control of gameplay truth. `Enemy Intent & Telegraph` owns enemy recovery, punish state, stagger, vulnerability hints, and enemy-side reveal-support context. `Combat Core` owns `CounterWindow`, counter validity, hit results, and reveal request context. `Memory State` owns memory consequence. `Lock-On & Combat Camera` exists only to support visibility, framing, and restrained emotional readability.

### 12.1 Punish / Reveal Support Purpose

The camera should help the player:

- see when the enemy is exposed
- understand why the enemy is punishable
- see counter opportunity clearly
- see counter impact and stagger
- notice reveal disruption after meaningful success
- return to the next readable duel state

The camera should not:

- decide enemy vulnerability
- open `CounterWindow`
- extend punish windows
- validate reveal
- turn reveal into a cutscene
- hide the next enemy read

Its job is to preserve meaning, not to create it.

### 12.2 Punish Readability Support

During recovery or punish, the player needs to see that the enemy has made a mistake or become exposed. The camera should support that recognition clearly enough that the reward side of the duel remains understandable.

During recovery or punish:

- the enemy’s exposed posture should remain visible
- enemy whiff should be readable if relevant
- player-to-enemy spacing should remain understandable
- the camera should avoid resetting away from punish too early
- the camera should not over-focus the player if that hides enemy vulnerability
- target focus should help preserve enemy visibility

The player should be able to read the opening as a consequence of what just happened, not as a mysterious state change.

### 12.3 Counter Opportunity Visibility

The camera should support counter opportunity by:

- keeping enemy recovery or stagger in view
- keeping player orientation understandable
- preserving spacing information
- avoiding shake or zoom that hides the opening
- making the cause of punish readable, such as whiff, parry, stagger, recovery, or overcommitment

The camera must not:

- imply that a counter is valid when `Combat Core` has rejected it
- make all recovery look like `CounterWindow`
- hide the distinction between `EnemyPunishWindow` and the player’s `CounterWindow`

This distinction is important because the enemy being exposed and the player being allowed a special counter are related, but not identical.

### 12.4 Reveal Support Purpose

Reveal support should:

- make meaningful combat success feel connected to memory disruption
- support `Glass Refrain`’s sad and mysterious tone
- feel restrained, brief, and elegant
- preserve player and enemy readability
- avoid interrupting the combat loop longer than necessary

Reveal support should not:

- become a cinematic cutscene
- steal camera control for too long
- hide enemy reset
- hide a new threat
- trigger without valid reveal context
- become required to understand the combat result

Reveal should add meaning to the exchange, not replace the duel with presentation.

### 12.5 Reveal Camera Behavior

When reveal context is valid:

- the camera may lightly emphasize enemy stagger or reveal disruption
- the camera may briefly stabilize framing
- the camera may allow restrained impact emphasis
- the camera should keep both player and enemy understandable when possible
- the camera should return to readable duel framing afterward
- reveal feedback should not obscure the next telegraph

The ideal feeling is that something fragile has shifted, but the duel still remains readable.

### 12.6 Reveal Timing Rules

For M0, reveal timing should remain conservative:

- reveal camera support should happen only after valid combat success and reveal context
- reveal should generally follow confirmed counter, stagger, or reveal acceptance
- reveal should not start during timing-critical dodge or parry windows
- reveal should not delay the next read unless that is intentionally approved later
- reveal should remain short enough to preserve combat flow

This keeps reveal meaningful without allowing it to interrupt the loop that made it meaningful.

### 12.7 Relationship To Enemy Intent, Combat Core, And Memory State

The boundaries between systems must remain explicit:

- `Enemy Intent & Telegraph` exposes recovery, punish, stagger, and reveal-support context
- `Combat Core` validates counter and reveal request context
- `Memory State` accepts or rejects memory consequence
- the camera observes accepted or supporting events
- the camera does not decide punish, counter, or reveal truth

This prevents presentation from becoming the hidden owner of combat meaning.

### 12.8 Camera State Interaction

The expected camera-state flow for punish and reveal support is:

- `EnemyRecovery` or `EnemyPunishWindow` may request `PunishReadability`
- successful counter may request `ResultFeedback`
- accepted reveal context may request `RevealSupport`
- `RevealSupport` should transition into `CameraReset`
- `CameraReset` should return to `TargetFocus / Lock-On` or `CameraNeutral / Soft Follow` depending on engagement state

This keeps the camera aligned with readable duel rhythm rather than chaining effect states endlessly.

### 12.9 Debug Requirements

For M0, debug should expose:

- `EnemyPunishWindow active?`
- punish source
- `CounterWindow active?`
- `enemy visible during punish?`
- `spacing visible during punish?`
- camera state during punish
- `reveal support requested?`
- `reveal support accepted?`
- reveal support source
- `reveal camera emphasis active?`
- reveal duration or timer if used
- whether reveal hid enemy reset or the next telegraph

This should help the team determine whether punish and reveal are readable because of system truth or only because of temporary presentation tricks.

### 12.10 Punish / Reveal Support Table

| Moment | Camera Responsibility | Must Keep Visible | Must Not Do | M0 Priority |
| --- | --- | --- | --- | --- |
| `Enemy Recovery` | Preserve readable post-attack vulnerability | Enemy recovery posture, player spacing | Reset too early away from exposure | `Must Pass` |
| `Enemy Whiff` | Show that the attack missed and overcommitted | Enemy miss, player position, spacing outcome | Hide whiff with camera motion | `Must Pass` |
| `EnemyPunishWindow` | Keep enemy exposure readable | Enemy vulnerability, player relation, spacing | Imply punish vanished when still active | `Must Pass` |
| `CounterWindow Support` | Preserve the visual basis for possible counter | Enemy exposure cause, player orientation | Imply counter validity when rejected | `Must Pass` |
| `Counter Impact` | Show successful punish reward clearly | Counter hit line, enemy stagger, duel relation | Heavy zoom or shake that hides stagger | `Should Pass` |
| `Enemy Stagger` | Preserve vulnerability and reaction clarity | Enemy stagger posture, player position | Hide stagger behind emphasis or reset | `Must Pass` |
| `Reveal Support Start` | Introduce reveal emphasis without breaking rhythm | Enemy disruption, player-enemy relation | Start reveal without valid context | `Should Pass` |
| `Reveal Disruption` | Preserve restrained memory-fracture readability | Reveal effect, enemy readability, next-read context | Become cutscene control | `Should Pass` |
| `Reveal End / Camera Reset` | Return to duel readability cleanly | Player, enemy, spacing, engagement state | Erase consequence or hide next threat | `Must Pass` |
| `Next Read` | Protect the next readable combat moment | New telegraph, enemy reset, player orientation | Let reveal block new threat clarity | `Must Pass` |

### 12.11 Failure Conditions

Punish and reveal camera support fails if:

- the player cannot tell the enemy is exposed
- recovery is hidden by camera reset
- the camera implies counter is valid when it is not
- reveal triggers without valid combat context
- reveal hides the next enemy telegraph
- reveal lasts so long that it breaks duel rhythm
- camera effect makes success or failure unclear
- final VFX or camera polish is required to understand punish state

If any of these conditions persist, the camera is undermining the reward and meaning side of the duel loop.

### 12.12 Anti-patterns

The following should be treated as failures for M0:

- camera resetting before punish is readable
- reveal becoming a cutscene
- reveal camera triggering from VFX alone
- camera hiding enemy stagger
- camera implying all recovery is counter-valid
- camera zoom hiding spacing during punish
- heavy shake during counter impact
- reveal feedback blocking the next telegraph
- `Memory State` forcing camera behavior before M0 needs it
- polished reveal masking unclear combat result

### 12.13 Open Questions

The following questions remain unresolved:

- whether reveal camera support is needed in M0 or whether VFX and audio alone are enough
- whether reveal support should follow counter immediately or only after stagger confirmation
- whether reveal requires `Memory State` acceptance before camera emphasis
- whether `PunishReadability` is truly separate from `ResultFeedback`
- whether `CounterWindow` should have a camera cue or only enemy presentation and debug support
- whether reveal duration becomes fixed first or data-authored later
- whether `CameraReset` after reveal should be instant, damped, or event-driven

## 13. Camera Movement / Framing Rules

The purpose of baseline camera movement and framing rules in M0 is to protect duel readability before any production polish exists. This section defines how the camera should behave in the first duel space so the player can consistently read enemy intent, judge spacing, understand response outcomes, and return to stable orientation after exchanges.

### 13.1 Movement / Framing Purpose

Camera movement and framing should:

- keep the duel readable
- preserve player orientation
- preserve enemy telegraph visibility
- make spacing understandable
- support dodge, parry, and counter result clarity
- return smoothly to stable framing after exchanges
- match `Glass Refrain`’s restrained and melancholic tone

Camera movement and framing should not:

- chase spectacle before clarity
- hide enemy windup
- hide player position
- make spacing hard to judge
- fight player control
- overuse shake, zoom, or orbit
- require final polish to become understandable

The camera should feel like a calm partner in the duel, not a second opponent.

### 13.2 Baseline Framing Rules

For M0, the baseline framing should prioritize the duel relationship itself.

The baseline rules are:

- player and enemy should both be visible whenever possible
- enemy telegraph visibility takes priority during telegraph
- player orientation and spacing remain important even when enemy visibility is prioritized
- the camera should preserve the line of action
- unnecessary angle changes should be avoided during timing-critical moments
- framing should support a controlled katana duel rather than chaotic brawling

The player should feel that the space between combatants has meaning and can be read.

### 13.3 Camera Distance Rules

Camera distance should support both detail and spacing comprehension.

For M0:

- distance should allow enemy body and weapon readability
- distance should allow player movement and dodge displacement to remain readable
- the camera should not be so close that spacing becomes unclear
- the camera should not be so far that telegraph detail is lost
- final distance tuning should happen later through playtesting

No exact numeric distance is required at this stage, but the first prototype must be easy to read both as a threat view and a spacing view.

### 13.4 Camera Height / Angle Rules

Camera height and angle should support grounded duel readability rather than dramatic distortion.

For M0:

- camera height and angle should show enemy windup and player position clearly
- the angle should avoid hiding weapon motion behind the player
- the camera should not become too top-down unless intentionally approved later
- the camera should not become too low or cinematic if that hides spacing or timing
- the angle should preserve a grounded duel feeling

The player should feel embedded in the exchange, but not visually trapped inside it.

### 13.5 Orbit / Rotation Rules

Orbit and rotation should remain restrained during combat.

For M0:

- large rotations should be avoided during `EnemyTelegraph`, parry timing, dodge timing, and counter timing
- the camera may gently reframe if the target is drifting out of readable view
- player manual look input should not be fought aggressively
- camera rotation should preserve timing clarity rather than chase motion

The camera may move when necessary, but it should not make timing-sensitive reads harder.

### 13.6 Damping / Responsiveness Rules

The camera should feel stable without becoming sluggish.

For M0:

- camera response should feel stable, not sluggish
- response should be smooth enough to avoid disorientation
- response should be fast enough to keep the enemy readable
- timing-critical states may require reduced camera movement or stronger stabilization
- exact damping values are deferred to prototype tuning

This is a feel-sensitive area, so the rules here should guide tuning rather than over-prescribe it.

### 13.7 Zoom Rules

Zoom may support framing, but it should remain subtle and heavily constrained in M0.

For M0:

- zoom may support framing only in restrained ways
- there should be no dramatic zoom during timing-critical windows
- zoom should not hide spacing
- zoom should not imply a result before `Combat Core` confirms it
- reveal zoom, if any, should be brief and restrained

Zoom should clarify focus, not create fake intensity.

### 13.8 Camera Shake / Impulse Rules

Shake and impulse may support confirmed results, but only after the combat truth is known.

For M0:

- shake or impulse may support confirmed hit, parry, counter, or reveal feedback
- shake should happen only after confirmed result
- shake must not occur before timing result is known
- shake must not hide enemy recovery or the next telegraph
- M0 should use minimal impulse until readability is proven

Any use of impulse in the first prototype should be treated as support, not as a substitute for clear framing.

### 13.9 Occlusion / Blocking Rules

Major occlusion of enemy telegraph is a readability failure.

For M0:

- the duel space itself may be composed simply to avoid complex occlusion
- advanced collision or occlusion handling is deferred unless blocking becomes a prototype blocker
- if occlusion is later tracked, it should be visible in debug

The first solution should be readable duel-space composition, not immediate escalation into a complex camera-collision system.

### 13.10 Reset / Recentering Rules

After each exchange, the camera should return to stable readable duel framing without erasing important consequence states.

For M0:

- reset should return the camera to stable readable framing
- reset should not hide active recovery or punish windows
- reset should avoid sudden disorientation
- reset may later become time-based, event-driven, or state-driven
- reset should support `calm → threat → answer → result → reset`

The camera reset should feel like the duel regaining breath, not the system forgetting what just happened.

### 13.11 Tone / Style Rules

The camera should support the project’s tone through restraint and composition rather than through aggressive effect work.

For M0:

- the camera should feel restrained, elegant, and readable
- style should come from control and composition, not excessive effects
- combat should feel like a focused duel, not a shaky action montage
- cinematic emphasis may be allowed later only if it preserves fairness
- melancholic tone must not reduce clarity

Tone should deepen the duel, not obscure it.

### 13.12 Debug Requirements

For M0, debug should expose:

- current camera state
- current framing mode
- distance to player
- distance to target
- `enemy visible?`
- `player visible?`
- `spacing visible?`
- camera angle or heading if useful
- `zoom active?`
- `shake / impulse active?`
- `camera reset active?`
- occlusion or blocking if tracked later
- last reason the camera moved or reframed

This should help the team tell whether a readability problem comes from state logic, framing choice, or duel-space composition.

### 13.13 Movement / Framing Table

| Area | M0 Rule | Why It Matters | Must Avoid | Tuning Status |
| --- | --- | --- | --- | --- |
| `Baseline framing` | Keep player and enemy readable, with telegraph visibility prioritized when needed | Supports overall duel comprehension | Framing that loses the threat subject | `Must Be Debugged` |
| `Distance` | Keep both spacing and telegraph detail readable | Prevents loss of either spatial or threat information | Too close for spacing or too far for windup | `Prototype Tune` |
| `Height / angle` | Preserve windup, player position, and grounded duel view | Protects fairness and orientation | Top-down or cinematic angle that hides timing | `Prototype Tune` |
| `Orbit / rotation` | Use restrained reframe only when readability needs it | Prevents camera-caused timing confusion | Orbiting during timing-critical windows | `Must Be Debugged` |
| `Damping / responsiveness` | Stay smooth but readable and responsive | Balances stability with target visibility | Sluggishness or jitter | `Prototype Tune` |
| `Zoom` | Use only restrained framing support | Protects spacing and timing clarity | Dramatic zoom or premature result implication | `Defer` |
| `Shake / impulse` | Only support confirmed results minimally | Reinforces impact without hiding truth | Shake before result confirmation | `Must Be Debugged` |
| `Occlusion` | Prefer simple duel-space composition first | Avoids overbuilding collision systems early | Assuming camera systems alone fix bad space design | `Defer` |
| `Reset / recentering` | Return to stable duel view without hiding consequence | Preserves loop rhythm and punish readability | Reset that erases recovery or punish | `Must Be Debugged` |
| `Tone / style` | Keep the camera restrained and elegant | Protects project identity without losing fairness | Style overriding readability | `Prototype Tune` |

### 13.14 Anti-patterns

The following should be treated as failures for M0:

- camera too close to read spacing
- camera too far to read telegraph
- orbiting during parry timing
- shake before result confirmation
- zoom hiding enemy recovery
- reset hiding punish window
- dramatic reveal camera hiding the next read
- over-reliance on cinematic framing
- assuming camera collision solves bad duel-space composition
- style overriding fairness

### 13.15 Open Questions

The following questions remain unresolved:

- approximate camera distance for the first prototype
- whether M0 uses hard-lock framing or soft-follow framing
- whether timing-critical windows reduce camera movement
- whether manual look input is allowed during target focus
- whether camera shake is disabled during early timing tests
- whether reveal uses camera zoom or only presentation effects
- whether occlusion handling is deferred entirely for M0

## 14. Debug / Readability Requirements

The purpose of camera debug and readability tooling in M0 is to make the duel view inspectable. `Lock-On & Combat Camera` cannot be tuned responsibly if the team cannot see what the camera believed it was doing, why it changed, what it was trying to frame, and whether it interfered with a timing-critical moment.

### 14.1 Debug Purpose

Debug and readability tooling should help designers answer:

- what is the camera currently doing
- why did the camera change state
- what target is being focused
- was the enemy visible during telegraph
- was the player visible during response
- did camera movement happen during timing-critical windows
- did result feedback trigger from a valid event
- did camera reset hide punish, recovery, or reveal
- did reveal support hide the next read

Debug should not:

- become required for player understanding
- change gameplay state
- force camera states
- decide combat validity
- replace real camera readability testing

Debug exists to explain the camera, not to become the camera’s excuse.

### 14.2 Required Camera State Debug

For M0, camera state debug should expose:

- current camera state
- previous camera state
- time in state
- camera state reason
- requested camera state, if any
- accepted or rejected camera state request, if tracked
- state priority reason, if relevant
- last combat or enemy event driving state change

This should make it possible to explain why the camera behaved a certain way during a specific exchange.

### 14.3 Required Target Focus Debug

Target-focus debug should expose:

- `lock-on active?`
- `soft focus active?`
- current target
- `target valid?`
- target distance
- `target visible?`
- target acquisition reason
- target release reason
- lock-on mode
- last lock-on input or request
- whether target focus is influencing framing
- whether target focus is influencing facing

This should make it clear whether a readability problem came from framing, target focus, or both.

### 14.4 Required Visibility Debug

Visibility debug should expose:

- `enemy visible?`
- `player visible?`
- `enemy weapon/body visible during telegraph?`
- `spacing visible?`
- `enemy telegraph visible?`
- `enemy recovery/punish visible?`
- `player displacement visible during dodge?`
- `counter impact visible?`
- `reveal disruption visible?`
- `next read visible after reveal?`
- occlusion or blocking if tracked later

This category matters because the duel cannot be tuned fairly if visibility itself is only guessed at.

### 14.5 Required Timing-Critical Debug

Timing-critical debug should expose:

- `enemy telegraph active?`
- `enemy commitment active?`
- `enemy attack active?`
- `enemy recovery active?`
- `EnemyPunishWindow active?`
- `CounterWindow active?`
- player response window active if available from `Combat Core`
- `camera moved during telegraph?`
- `camera moved during parry timing?`
- `camera moved during dodge timing?`
- `camera moved during counter timing?`
- whether camera shake, zoom, or impulse triggered before or after result confirmation

This is one of the highest-value debug areas because even small movement at the wrong time can make the duel feel unfair.

### 14.6 Required Feedback Debug

Feedback debug should expose:

- last player response type
- last `Combat Core` result
- `camera feedback triggered?`
- feedback type
- feedback source event
- feedback timing
- `result feedback active?`
- `reveal support requested?`
- `reveal support accepted?`
- `reveal camera emphasis active?`
- `reset active?`
- reset reason

This should help the team confirm that all camera emphasis is following valid state rather than racing ahead of it.

### 14.7 Required Framing / Movement Debug

Framing and movement debug should expose:

- current framing mode
- distance to player
- distance to target
- camera heading or angle if useful
- `zoom active?`
- `shake/impulse active?`
- `orbit/reframe active?`
- damping or stabilization mode if relevant
- `camera reset/recenter active?`
- last reason the camera moved or reframed

This should help determine whether the camera’s base motion rules are supporting or hurting duel readability.

### 14.8 Debug Readability Checklist

A designer should be able to answer:

- Did the camera keep the enemy readable during telegraph?
- Did camera movement interfere with dodge, parry, or counter timing?
- Did target focus preserve or hurt spacing readability?
- Did feedback trigger only after valid combat result?
- Did reveal support preserve the next read?
- Did reset hide punish or recovery?
- Was failure caused by player timing, spacing, or tags rather than camera behavior?
- Can unclear moments be explained by debug state?

If these questions cannot be answered reliably, the camera debug layer is not yet doing its job.

### 14.9 Debug Output Format Guidance

For M0, debug output may remain simple:

- simple overlay text
- state labels
- timing labels
- lightweight gizmos if useful

No final HUD polish is required. Instead:

- debug should be human-readable
- debug names should match GDD state names where possible
- debug should prioritize high-signal data over clutter
- designers should be able to toggle camera debug independently if possible

The goal is fast interpretation, not an elaborate instrumentation interface.

### 14.10 Debug Table

| Debug Area | Required Data | Why It Matters | M0 Priority | Notes |
| --- | --- | --- | --- | --- |
| `Camera State` | Current state, previous state, time in state, reason, last driving event | Explains why the camera behaved as it did | `Must Have` | Use GDD state names where possible |
| `Target Focus` | Lock-on status, focus mode, target, validity, acquire/release reasons | Explains target framing and orientation behavior | `Must Have` | One-target only in M0 |
| `Visibility` | Enemy, player, weapon/body, spacing, punish, reveal visibility | Determines whether readability is being preserved | `Must Have` | Visibility should not be guessed |
| `Telegraph Timing` | Telegraph active, commitment active, telegraph movement interference | Protects fairness during read phase | `Must Have` | Critical for timing trust |
| `Response Timing` | Camera movement during dodge, parry, counter windows | Shows whether camera harmed player answer timing | `Must Have` | High diagnostic value |
| `Result Feedback` | Feedback active, type, timing, source event | Verifies feedback follows valid result | `Must Have` | Prevents misleading emphasis |
| `Punish / Reveal` | Punish visibility, reveal request/acceptance/emphasis, next-read visibility | Protects reward and meaning side of loop | `Should Have` | Important once counter/reveal exist |
| `Framing / Movement` | Distances, heading, zoom, shake, orbit, stabilization, reframe reason | Helps tune baseline duel framing | `Should Have` | Core tuning support |
| `Occlusion` | Blocking or occlusion state if tracked | Helps explain visibility failure | `Nice To Have` | Can be deferred if duel space is simple |
| `Reset` | Reset active, reset reason, whether punish/reveal was still active | Explains whether reset erased consequence | `Must Have` | Important for post-exchange readability |

### 14.11 Debug Failure Conditions

Camera debug is insufficient if:

- the current camera state cannot be identified
- target-focus state is unclear
- camera movement during timing-critical windows cannot be inspected
- enemy visibility during telegraph cannot be evaluated
- result feedback source cannot be explained
- reset reason cannot be identified
- reveal support cannot be traced to valid context
- debug data does not match actual camera behavior
- debug is so noisy that designers stop using it

If any of these happen, the debug layer is no longer supporting intentional tuning.

### 14.12 Anti-patterns

The following should be treated as failures for M0:

- debug overlay becoming gameplay UI
- debug changing camera behavior
- using vague state names
- hiding target release or acquisition reasons
- not logging camera movement during timing-critical windows
- result feedback with no source event
- reveal camera support with no valid context trace
- stale debug data
- debug that only engineers can understand
- too much visual clutter during playtest

### 14.13 Open Questions

The following questions remain unresolved:

- whether camera debug is part of the shared M0 combat overlay or a separate camera overlay
- whether visibility checks are manual and designer-observed or instrumented later
- whether weapon or body visibility can be tracked technically in M0
- whether camera movement during critical windows needs explicit logging
- whether camera debug should be available in development builds
- whether debug gizmos for range and spacing belong here or to `Combat Core` / `Enemy Intent & Telegraph`
- whether reset or reveal failure should be recorded as runtime debug flags or only as test notes

## 15. Data Authoring Needs

The purpose of camera data authoring in M0 is to expose only the minimum tuning surfaces needed to make the first duel readable. This is not a full camera framework and not an implementation spec. It is a design-level definition of which camera behaviors should be easy to inspect and adjust during prototype iteration.

### 15.1 Data Authoring Purpose

Camera data should allow designers to tune:

- target focus behavior
- framing priorities
- camera distance, height, and angle
- responsiveness and damping
- timing-critical stabilization
- result feedback intensity
- reveal support behavior
- reset and recenter behavior
- debug display configuration

Camera data should not:

- own combat truth
- decide enemy intent
- decide player action validity
- decide `CounterWindow`
- validate reveal
- replace playtesting

The purpose of authoring data is to make camera readability easier to tune, not to push camera systems into gameplay ownership.

### 15.2 M0 Camera Preset Data

For M0, it is useful to think in terms of a very small set of conceptual camera presets:

- `neutral / soft follow`
- `target focus / lock-on`
- `telegraph framing`
- `response support`
- `result feedback`
- `punish readability`
- `reveal support`
- `reset`

Each preset may conceptually contain:

- framing intent
- distance range
- height or angle intent
- responsiveness or damping intent
- stabilization behavior
- feedback allowance
- debug label

These do not need to become a large preset library. They only need to provide enough tuning separation that the first duel can be iterated clearly.

### 15.3 Target Focus Data

Minimum tunable target-focus data may include:

- `soft focus` versus `hard lock` mode
- target acquisition range or relevance
- target release behavior
- framing strength toward target
- facing support strength if allowed
- target visibility priority
- lock-on marker requirement flag if needed later

This data must not decide hit, parry, dodge, or counter validity. It only supports target readability and orientation.

### 15.4 Framing Priority Data

Minimum tunable framing-priority data may include relative priority for:

- enemy visibility
- player visibility
- enemy weapon or body visibility during telegraph
- spacing readability
- active threat readability
- punish or recovery visibility
- reveal visibility
- style or elegance

For M0, framing priority should strongly favor enemy telegraph visibility and spacing readability over cinematic style.

### 15.5 Timing-Critical Stabilization Data

Minimum tunable stabilization data may include:

- stabilization during `EnemyTelegraph`
- stabilization during `EnemyCommit / AttackStartup`
- stabilization during dodge, parry, and counter response windows
- whether camera movement is reduced or damped during timing-critical states
- whether shake or zoom is disabled during early timing tests

These settings should preserve readability without freezing the camera so hard that the duel becomes disorienting or unnatural.

### 15.6 Result Feedback Data

Minimum tunable result-feedback data may include:

- hit feedback intensity
- parry feedback intensity
- counter feedback intensity
- stagger feedback intensity
- whiff feedback support if any
- maximum shake or impulse allowance
- feedback duration
- feedback cooldown or suppression rules if needed

This data should only be used after valid `Combat Core` or `Enemy Intent & Telegraph` context confirms that a readable event has actually happened.

### 15.7 Punish / Reveal Data

Minimum tunable punish and reveal data may include:

- punish readability emphasis
- recovery visibility priority
- reveal support duration
- reveal emphasis strength
- reveal camera stabilization
- reveal reset behavior

Reveal camera support must require valid reveal context and must not become a cutscene in M0.

### 15.8 Reset / Recentering Data

Minimum tunable reset and recentering data may include:

- reset timing
- reset damping
- reset target state
- reset reason label
- whether reset waits for punish or recovery visibility
- whether reset differs after reveal

Reset must not hide punish windows or erase the next readable threat.

### 15.9 Debug Display Data

Minimum tunable debug-display configuration may include:

- camera debug enabled
- target focus debug enabled
- visibility debug enabled
- timing-critical movement debug enabled
- result feedback debug enabled
- reveal or reset debug enabled
- debug verbosity level
- debug labels matching GDD state names

This debug configuration exists to improve diagnosis speed, not to become a permanent gameplay-facing layer.

### 15.10 Hardcoded vs Authored Guidance

For M0, it is acceptable to hardcode temporarily:

- one duel camera setup
- one target focus mode
- simple reset behavior
- simple debug labels
- minimal result feedback

The following should remain easy to tune even if the first implementation begins simply:

- distance, height, and angle
- target focus strength
- camera responsiveness
- telegraph stabilization
- shake or impulse intensity
- reveal support duration
- reset damping or timing
- visibility priorities

The following should not be deeply hardcoded because they are likely to change during playtesting:

- timing-critical stabilization behavior
- feedback intensity
- target release rules
- reveal support behavior
- state names and debug labels
- any values likely to move as the team learns what makes the duel readable

### 15.11 Data Table

| Data Area | Tunable Values | Why It Matters | M0 Requirement | Can Be Deferred? |
| --- | --- | --- | --- | --- |
| `Camera Presets` | Small set of duel-state framing intents, damping intents, and debug labels | Organizes camera behavior by readable duel phase | Required | No |
| `Target Focus` | Focus mode, acquire/release behavior, framing strength, visibility priority | Supports orientation and target readability | Required | No |
| `Framing Priority` | Enemy visibility, player visibility, spacing, punish, reveal, style weight | Protects fairness and telegraph readability | Required | No |
| `Stabilization` | Telegraph stabilization, response-window stabilization, movement reduction rules | Prevents camera-caused timing confusion | Required | No |
| `Result Feedback` | Intensity, duration, max impulse, suppression rules | Controls how much feedback supports confirmed outcomes | Required | No |
| `Punish Readability` | Exposure emphasis, recovery visibility priority | Keeps reward windows understandable | Required | No |
| `Reveal Support` | Reveal duration, emphasis strength, stabilization, reset behavior | Supports project identity without breaking duel flow | Recommended | Yes |
| `Reset / Recentering` | Timing, damping, target state, wait behavior, reason label | Returns camera to stable readable framing | Required | No |
| `Debug Display` | Toggles, verbosity, label naming | Enables intentional tuning and diagnosis | Required | No |
| `Occlusion / Blocking` | Any simple visibility flags or fallback priorities if needed | Helps explain visibility failure if space causes issues | Optional | Yes |

### 15.12 Anti-patterns

The following should be treated as failures for M0:

- building a full camera data framework before one duel works
- hiding all important values in code
- making camera data decide combat validity
- authoring cinematic feedback before readability is proven
- too many presets for M0
- data split across too many places
- debug labels that do not match GDD state names
- reveal support data triggering without valid context
- target focus data overriding `Combat Core`
- tuning style before telegraph readability

### 15.13 Open Questions

The following questions remain unresolved:

- whether M0 camera data starts as simple constants or authored assets
- whether camera presets should exist before prototype tuning
- whether debug configuration is shared with the combat debug overlay
- whether target focus mode is data-authored or fixed for M0
- whether stabilization behavior needs its own preset
- whether result feedback should be disabled during early timing tests
- whether reveal support data is needed in M0 or can be deferred

## 16. Presentation Boundaries

The purpose of presentation boundaries in M0 is to keep the duel readable by making ownership explicit. `Lock-On & Combat Camera` owns camera state, target-focus visual support, framing priorities, readability support, and camera feedback decisions. Presentation systems may support those decisions, reinforce mood, and help the player feel the exchange, but they must not silently become the source of combat truth or camera truth.

### 16.1 Boundary Purpose

Presentation boundaries should ensure:

- the camera preserves combat readability
- presentation supports camera intent without overriding it
- `Animation`, `VFX`, `Audio`, `UI`, and `Debug` remain clearly separated from camera truth
- combat-result feedback follows valid `Combat Core`, `Enemy Intent & Telegraph`, and `Memory State` context
- reveal support remains restrained and readable

The goal is not to reduce presentation value. The goal is to make sure presentation deepens readability instead of masking or rewriting it.

### 16.2 Lock-On & Combat Camera Owns

`Lock-On & Combat Camera` owns:

- current camera state
- camera state transitions
- target-focus visual support and lock-on readability state
- camera framing priorities
- camera movement and stabilization intent
- camera feedback after confirmed result
- punish and reveal visibility support
- reset and recentering behavior
- camera debug data

`Lock-On / Target Context` provisionally owns target focus truth for M0, including `target focus active`, `current target`, `target validity`, and `target direction`. `Lock-On & Combat Camera` reads that context for framing and readability only.

`Lock-On & Combat Camera` does not own:

- target focus active
- current target
- target validity
- target direction
- player combat state
- enemy intent state
- hit detection
- dodge, parry, or counter validity
- attack tags
- `EnemyPunishWindow`
- `CounterWindow`
- reveal validity
- memory consequence

This keeps the camera as a readability system rather than a hidden combat system.

### 16.3 Animation Boundary

`Animation` owns:

- player and enemy pose
- action readability through motion
- hit, parry, counter, and stagger animation support
- reveal disruption animation support

`Animation` may:

- provide visual timing cues
- request camera emphasis later if such requests are validated
- help make camera framing meaningful

`Animation` must not:

- force camera state changes without valid context
- apply combat results
- open `CounterWindow`
- trigger reveal camera support by itself
- hide the telegraph while expecting the camera to fix it
- contradict camera readability priorities

Animation can support the moment, but it cannot authoritatively define what the camera must believe happened.

### 16.4 VFX / Shader Boundary

`VFX / Shader` owns:

- telegraph accents
- hit, parry, and counter feedback accents
- reveal disruption visuals
- atmospheric mood support
- optional target or readability accents if needed

`VFX / Shader` may:

- support camera feedback visually
- help reveal feel connected to memory disruption
- help communicate enemy state when aligned with `Enemy Intent & Telegraph`

`VFX / Shader` must not:

- trigger reveal camera support without valid reveal context
- obscure enemy telegraph
- hide player or enemy spacing
- imply counter validity when `Combat Core` rejected it
- become the only readable source of enemy intent
- force camera zoom or shake directly

If the VFX become clearer than the enemy’s actual readable motion, the duel is already in trouble.

### 16.5 Audio Boundary

`Audio` owns:

- telegraph cues
- combat-result cues
- parry, counter, stagger, and reveal cues
- ambience and emotional tone

`Audio` may:

- reinforce camera feedback timing
- support result clarity after confirmed events
- support reveal mood

`Audio` must not:

- be the only timing cue
- trigger camera feedback by itself
- imply success or failure against `Combat Core` result
- mask important telegraph cues
- force cinematic camera behavior

Audio should strengthen readability, not replace it.

### 16.6 UI / HUD Boundary

`UI / HUD` owns:

- optional lock-on marker if needed
- optional target status display if needed
- optional player-facing readability aids later

`UI / HUD` must not:

- become required to understand enemy telegraph in M0
- decide target validity
- decide lock-on validity
- open `CounterWindow`
- validate combat results
- replace camera, player, or enemy readability

The duel should still be understandable even if UI support is minimal or absent.

### 16.7 Debug Boundary

`Debug` owns:

- displaying camera state
- displaying target focus state
- displaying visibility and readability data
- displaying event sources and reasons
- showing camera feedback traces

`Debug` may:

- expose camera behavior for designers
- support playtest diagnosis
- show labels or gizmos if useful

`Debug` must not:

- change camera behavior except through explicit debug commands if allowed
- become player-facing required UI
- present stale or non-authoritative data as truth
- override `Combat Core`, `Enemy Intent & Telegraph`, or `Memory State`

Debug is there to explain the camera, not to secretly drive it.

### 16.8 Combat Feedback Boundary

For hit, parry, dodge, and counter feedback:

- `Combat Core` confirms result
- `Enemy Intent & Telegraph` may expose enemy reaction, punish, or stagger context
- the camera may provide restrained feedback after confirmation
- `Animation`, `VFX`, and `Audio` may support the confirmed result
- `UI` and `Debug` may display supporting information

Camera and presentation must not:

- imply success before confirmation
- contradict confirmed result
- hide why failure happened
- make invalid actions look valid

The player should never receive mixed signals between camera emphasis and gameplay truth.

### 16.9 Reveal Feedback Boundary

For reveal support:

- `Combat Core` provides meaningful success and reveal-request context
- `Memory State` accepts or rejects memory consequence
- `Enemy Intent & Telegraph` may expose reveal-supporting enemy reaction
- the camera may briefly support reveal visibility
- `VFX`, `Audio`, `Shader`, and `Animation` may support emotional reveal presentation

Camera and presentation must not:

- trigger reveal from VFX alone
- create reveal camera emphasis without valid context
- turn reveal into a cutscene in M0
- hide the next read
- make reveal more important than combat readability

Reveal must remain a readable consequence of the duel, not a presentation takeover.

### 16.10 Boundary Table

| Area | Owns | May Request / Support | Must Not Own | M0 Notes |
| --- | --- | --- | --- | --- |
| `Lock-On & Combat Camera` | Camera state, target-focus visual support, framing priorities, stabilization intent, camera feedback, reset behavior, camera debug data | React to valid combat, enemy, and memory context | Combat validity, enemy intent truth, punish truth, reveal validity, target truth | Primary readability owner for the duel view |
| `Animation` | Pose, motion readability, reaction animation support | Timing cues, visual support, validated emphasis requests later | Combat result truth, camera state truth, `CounterWindow`, reveal validity | Must not expect camera to repair unreadable motion |
| `VFX / Shader` | Telegraph accents, impact accents, reveal visuals, mood support | Reinforce confirmed feedback and readable state | Camera truth, target validity, counter validity, reveal validity | Must never become the only readable signal |
| `Audio` | Telegraph cues, result cues, ambience, reveal tone | Reinforce confirmed timing and mood | Combat truth, camera truth, forced camera behavior | Supportive only |
| `UI / HUD` | Optional target marker or status aids | Supplemental clarity if needed | Target validity, lock-on validity, combat result validation | Not required for M0 readability |
| `Debug` | Display of camera state, focus state, visibility, reasons, traces | Diagnosis, testing, labels, gizmos | Gameplay truth, autonomous camera behavior | Design-facing only |
| `Combat Core` | Combat state, hit results, dodge/parry/counter validity, `CounterWindow`, reveal request context | Drive confirmed camera feedback context | Camera state, framing priorities, target focus behavior | Gameplay authority |
| `Enemy Intent & Telegraph` | Telegraph, commitment, attack windows, punish state, stagger context, tags | Provide readable enemy-state context | Camera truth, counter validity, reveal validity | Enemy-side readability authority |
| `Memory State` | Memory consequence acceptance or rejection | Confirm reveal consequence context | Camera behavior, combat truth, enemy intent truth | Lightweight M0 consequence owner |

### 16.11 Anti-patterns

The following should be treated as failures for M0:

- `VFX` triggering camera reveal support directly
- `Animation` forcing camera state transitions without valid gameplay context
- `Audio` implying parry success before `Combat Core` confirms it
- a `UI` lock-on marker becoming required for basic enemy readability
- debug overlay becoming gameplay UI
- camera feedback contradicting animation result
- camera hiding enemy telegraph because VFX is expected to communicate it
- reveal presentation becoming a cutscene
- target marker deciding target validity
- presentation polish masking unclear camera framing

### 16.12 Open Questions

The following questions remain unresolved:

- whether a lock-on marker is needed for M0
- whether `VFX` can request camera emphasis or may only respond to camera and combat events
- whether animation events may request camera feedback later
- whether reveal support needs camera emphasis or only `VFX` and `Audio`
- whether `UI / HUD` should show target status in M0
- whether debug commands may force camera states during testing
- whether presentation contracts should be formalized before implementation

## 17. Technical Boundaries

The purpose of technical boundaries for `Lock-On & Combat Camera` is to protect the design intent of the M0 duel when implementation begins later. These boundaries ensure that the camera stays a readability-support system, that gameplay truth remains owned elsewhere, and that the first duel camera remains small, testable, and tunable instead of expanding into a full cinematic or boss-camera framework.

### 17.1 Boundary Purpose

Technical boundaries should ensure:

- the camera supports readability without owning combat truth
- `Combat Core` and `Enemy Intent & Telegraph` do not depend on camera implementation
- the camera observes state and events through clear contracts
- camera runtime state is scoped to gameplay or combat scene context rather than global project-root truth
- M0 remains simple, testable, and tunable

These boundaries are important because camera systems are especially prone to silently accumulating hidden authority unless their contracts stay explicit.

### 17.2 Camera Technical Principles

`Lock-On & Combat Camera` should be:

- explicit
- state-readable
- debug-visible
- tunable
- presentation-facing but not presentation-owned
- dependent on combat and enemy read-only context rather than authoritative combat logic
- small enough for one duel prototype

It should not:

- own player action validity
- own enemy intent
- own hit resolution
- own attack tags
- own `CounterWindow`
- own reveal validity
- force `Combat Core` to depend on the camera
- become a cinematic camera framework in M0

This keeps the camera system legible both to designers and to future programmers.

### 17.3 Assembly / Dependency Direction

Within the current project architecture intent, `Lock-On & Combat Camera` may depend on:

- core primitives and contracts
- read-only `Combat Core` result and context contracts
- read-only `Enemy Intent & Telegraph` state and context contracts
- `Player / Target Context` contracts
- minimal Unity types where needed
- `Cinemachine` later inside the camera layer only
- `R3` only for observation or debug streams if useful

`Lock-On & Combat Camera` should not be depended on by:

- `Combat Core`
- `Enemy Intent & Telegraph`
- `Health / Damage / Hit Reaction`
- `Memory State` truth
- `Player Locomotion` core logic

`Lock-On & Combat Camera` should not directly depend on:

- `UI` implementation
- `VFX` implementation
- `Audio` implementation
- `Bootstrap`
- editor-only code in runtime logic
- `DOTween` for authoritative camera state
- full boss framework
- full RPG progression
- full narrative memory graph

The dependency flow should stay one-way: camera consumes readable context, but does not become a prerequisite for gameplay systems.

### 17.4 Cinemachine Boundary

`Cinemachine` may be used later as the camera implementation and tooling layer, but it must remain subordinate to the design-level camera contract.

The intended boundary is:

- `Cinemachine` may execute camera design
- `Cinemachine` should not define gameplay truth
- `Cinemachine` components and presets should remain isolated to the camera layer
- `Combat Core` and `Enemy Intent & Telegraph` should not reference `Cinemachine`
- camera state names and debug concepts should remain design-level rather than tied only to `Cinemachine` component names

`Cinemachine` must not:

- decide hit, parry, dodge, or counter validity
- decide target validity
- open `CounterWindow`
- validate reveal
- hide timing-critical state behind inaccessible blending

This allows the implementation tool to change later without rewriting the design language of the system.

### 17.5 VContainer / Lifetime Boundary

Camera runtime state should belong to gameplay-level scene context, not to the global application root.

For M0:

- camera runtime state belongs in gameplay or camera scene scope, not project root scope
- `ProjectRoot` must not own active duel camera truth
- `ProjectRoot` may provide general app services only
- camera scene scope may later own the camera service, controller, or presenter
- target-focus runtime state should be scene-owned, encounter-owned, or camera-scope-owned rather than global
- generated DI should later be used carefully only for pure C# services
- scene cameras, `Cinemachine` components, and Unity references should remain explicitly composed

This keeps the duel camera replaceable and local instead of becoming an application-global singleton behavior.

### 17.6 R3 / Reactive Boundary

`R3` may be useful for camera observation, but it must not make camera truth harder to inspect.

For M0:

- `R3` may expose read-only camera state, target-focus state, and debug observations
- `R3` may observe `Combat Core` and `Enemy Intent & Telegraph` events if contracts allow
- `R3` may support debug overlay and presentation listeners
- `R3` should not hide camera state transitions
- reactive chains that make camera priority or feedback timing hard to explain should be avoided
- hot timing-critical decisions should remain traceable and debug-visible

The readability layer should remain explainable even if reactive observation is used around it.

### 17.7 DOTween Boundary

`DOTween` may be used later for non-authoritative polish only if needed, but it must not become the source of camera truth.

For M0:

- `DOTween` may be used later for presentation polish only
- `DOTween` must not drive authoritative camera state transitions
- `DOTween` must not decide feedback timing before `Combat Core` confirmation
- `DOTween` must not drive combat windows, target validity, `CounterWindow`, or reveal validity
- `DOTween` use should be isolated to presentation polish and may be disabled or limited during early readability tests

This keeps tweening as optional polish rather than hidden state logic.

### 17.8 Player Locomotion Boundary

`Player Locomotion` owns player movement implementation.

The camera boundary is:

- the camera may later influence framing and provide camera-relative context
- the camera must not own movement rules
- target-relative or camera-relative movement remains a cross-system decision
- dodge direction and counter alignment must be coordinated with `Combat Core` and `Player Locomotion`
- the camera should not silently correct locomotion mistakes into success

The player should be able to trust that movement outcomes came from locomotion and combat rules, not from hidden camera assistance.

### 17.9 Combat Core / Enemy Intent Boundary

The camera depends on confirmed context from gameplay systems, not on inferred truth.

- `Combat Core` owns player combat state, action validation, hit, parry, dodge, and counter result, `CounterWindow`, and reveal request context
- `Enemy Intent & Telegraph` owns telegraph, commitment, attack windows, tags, recovery, punish, and enemy reaction context
- the camera observes confirmed or resulting context
- the camera must not infer authority from animation, VFX, audio, or lock-on marker alone
- camera feedback should always trace back to valid event and context

This is the core anti-drift rule of the whole system.

### 17.10 Memory / Reveal Boundary

`Memory State` owns memory consequence.

For M0:

- the camera may support reveal only after valid reveal context
- reveal camera support remains short and restrained
- the camera must not become a narrative or cutscene director
- reveal camera support may be deferred entirely if VFX and audio are enough for M0

The first duel only needs the camera to preserve meaning, not to stage a narrative sequence.

### 17.11 Testing Boundary

The camera system should remain testable before final content exists.

For M0:

- the camera should be testable with placeholder animation, VFX, and audio
- camera readability should be testable before final assets
- telegraph visibility should be testable with one `Basic Attack A`
- response feedback should be testable with controlled dodge, parry, and counter outcomes
- debug must explain camera state and feedback source
- early timing tests may disable shake, zoom, and reveal emphasis

This keeps readability testing from being blocked by polish or content completeness.

### 17.12 Technical Anti-patterns

The following should be treated as failures for M0:

- `Combat Core` depending on camera implementation
- `Enemy Intent & Telegraph` depending on `Cinemachine`
- camera state registered globally in `ProjectRoot`
- `Cinemachine` blending hiding timing-critical transitions
- `DOTween` driving result feedback before confirmed result
- `R3` chains hiding camera state priority
- the camera directly opening `CounterWindow`
- a lock-on marker deciding target validity
- the camera using `VFX` or `Audio` as authoritative event source
- building boss-camera architecture before the M0 duel works
- overbuilding a multi-target camera framework
- requiring camera polish before readability can be tested

### 17.13 Open Questions

The following questions remain unresolved:

- whether the camera has its own assembly or sits under a broader `Presentation/Camera` assembly
- whether M0 uses `Cinemachine` immediately or begins with simpler camera control
- whether the camera state machine is pure C# or partly `MonoBehaviour`-driven
- whether camera runtime state lives in camera scope, gameplay scope, or encounter scope
- whether `R3` is used immediately or only after the state model stabilizes
- whether the debug overlay observes camera through DTO snapshots, events, or read-only state
- whether shake, zoom, and reveal emphasis should be disabled during the first combat timing tests

## 18. Dependencies

The purpose of this section is to define exactly what `Lock-On & Combat Camera` depends on for M0, what may consume its readable output, and which relationships remain provisional until architecture and implementation are formalized. The camera system should remain focused on readability, orientation, framing, feedback support, punish or reveal visibility, and debug visibility.

### 18.1 Dependency Purpose

This dependency map should clarify:

- which systems the camera needs to observe
- which systems consume camera-readable output
- which relationships are provisional M0 contracts
- which systems are deferred until after M0
- which dependency boundaries must remain protected

The goal is to keep the camera small and aligned with the duel loop instead of letting it expand into a combat, animation, or cinematic orchestration system.

### 18.2 Upstream Dependencies

`Lock-On & Combat Camera` depends on several upstream systems or contracts, but only in read-only or observational ways.

#### Combat Core

The camera may need from `Combat Core`:

- confirmed player-response result
- hit, parry, dodge, and counter outcome
- `CounterWindow` state if exposed for readability
- reveal request context if relevant
- timing-critical response state if exposed

`Combat Core` owns combat truth. The camera reacts only to confirmed or read-only context.

#### Enemy Intent & Telegraph

The camera may need from `Enemy Intent & Telegraph`:

- enemy state
- telegraph active
- commitment active
- attack active and recovery state
- `EnemyPunishWindow` state
- enemy stagger or reaction state
- reveal-support context if relevant

`Enemy Intent & Telegraph` owns enemy-side truth. The camera preserves visibility only.

#### Player / Target Context

The camera may need:

- player position
- target position
- current target reference or context
- distance and spacing context
- facing or orientation context if exposed

Player and target systems own actual movement and target-validity rules.

#### Player Locomotion

The camera may need:

- dodge movement context
- movement mode context if camera-relative or target-relative movement is used
- player displacement context
- facing or alignment context if exposed

`Player Locomotion` owns movement implementation.

#### Memory State

The camera may need:

- reveal accepted or rejected status
- reveal disruption context
- memory response state if reveal camera support is used

`Memory State` owns memory consequence.

#### Debug Overlay

The camera needs:

- a display path for camera state
- target-focus state
- visibility and readability data
- feedback reason traces

`Debug Overlay` owns display only.

### 18.3 Downstream Consumers

The following systems may consume camera output, camera-readable state, or camera debug data.

#### Debug Overlay

`Debug Overlay` may consume:

- camera state
- target-focus state
- visibility and debug data
- camera feedback reason
- reset or reveal support state

#### UI / HUD

`UI / HUD` may consume:

- lock-on marker state
- optional target-focus status
- optional player-facing target indicator later

#### VFX / Shader

`VFX / Shader` may consume:

- camera feedback timing
- reveal support timing
- framing or visibility hints if needed later

#### Audio

`Audio` may consume:

- confirmed feedback timing
- reveal support timing
- camera emphasis moments if needed later

#### Animation / Presentation

`Animation / Presentation` may consume:

- camera emphasis state for coordination later
- result or reveal support moments if needed

#### Testing / Playtest Tools

`Testing / Playtest Tools` may consume:

- camera debug data
- visibility failure notes
- timing-critical movement traces

These downstream relationships should remain supportive. Camera output should not become a hidden gameplay dependency.

### 18.4 Provisional M0 Contracts

The following contracts should be treated as provisional in M0:

- `Combat Core` result and context contract
- `Enemy Intent & Telegraph` state and context contract
- `Player / Target Context`
- `Player Locomotion` movement and facing context
- `Memory State` reveal context
- `Debug Overlay` display contract
- `UI` lock-on marker, if needed
- `VFX` and `Audio` feedback sync, if needed

For each of these provisional contracts:

- the camera system may define minimum needs
- the dedicated GDD or future architecture owns the full long-term design
- temporary M0 assumptions must be revisited before vertical slice

This allows the duel prototype to move forward without pretending every cross-system seam is already final.

### 18.5 Systems That Should Not Be Dependencies For M0

`Lock-On & Combat Camera` should not depend on:

- a full boss camera framework
- multi-target cycling
- boss body-part targeting
- cinematic cutscene system
- production HUD
- final animation system
- final VFX or audio pipeline
- full memory graph
- district reinterpretation
- RPG progression
- skill tree
- equipment or loot
- ranged combat camera
- multiplayer camera
- open-world exploration camera
- photo mode
- analytics or telemetry

If a dependency does not make one duel more readable in M0, it should stay out of scope.

### 18.6 Dependency Table

| System | Relationship To Lock-On & Combat Camera | Camera Needs | System Owns | M0 Status |
| --- | --- | --- | --- | --- |
| `Combat Core` | Upstream gameplay authority | Confirmed response results, `CounterWindow` context, reveal request context | Combat truth and action validity | Provisional contract |
| `Enemy Intent & Telegraph` | Upstream enemy readability authority | Telegraph, commitment, active, recovery, punish, stagger context | Enemy-side truth and attack readability | Provisional contract |
| `Player / Target Context` | Upstream positioning and reference source | Player/target position, spacing, facing context | Position and target reference truth | Provisional contract |
| `Player Locomotion` | Upstream movement context source | Dodge displacement, movement mode, alignment context | Movement implementation | Provisional contract |
| `Memory State` | Upstream reveal consequence authority | Reveal accepted/rejected state, reveal context if used | Memory consequence | Provisional contract |
| `Debug Overlay` | Downstream display consumer | Display path for camera/debug state | Debug presentation | Provisional contract |
| `UI / HUD` | Downstream optional consumer | Lock-on marker or target-focus state if needed | Player-facing UI | Optional / provisional |
| `VFX / Shader` | Downstream presentation consumer | Camera feedback or reveal timing if needed | Visual support and mood | Optional / provisional |
| `Audio` | Downstream presentation consumer | Camera emphasis timing if needed | Audio support and tone | Optional / provisional |
| `Animation / Presentation` | Downstream coordination consumer | Camera emphasis state if needed later | Motion and presentation support | Optional / provisional |
| `Testing / Playtest Tools` | Downstream diagnostic consumer | Camera debug data and traces | Test observation and reporting | Recommended |
| `Boss Camera Framework` | Explicit non-dependency | None | Future boss readability and spectacle needs | Deferred |
| `Cinematic Camera System` | Explicit non-dependency | None | Future cutscene or dramatic camera control | Deferred |
| `Multi-Target Targeting` | Explicit non-dependency | None | Future multi-enemy targeting logic | Deferred |

### 18.7 Dependency Risk Notes

The following dependency risks should be kept in mind:

- the camera can accidentally become combat authority if boundaries blur
- `Combat Core` can become coupled to camera concepts if camera-specific ideas leak upstream
- enemy telegraph can become unreadable if the camera lacks sufficient `Enemy Intent` context
- `Player Locomotion` can feel wrong if movement mode and facing support are not coordinated
- debug can become stale if it is not tied to authoritative camera state
- a `UI` lock-on marker can become a crutch instead of actual camera readability
- `VFX` and `Audio` can imply false result if they are not tied to confirmed context
- reveal support can pull the camera toward cinematic scope too early

These are design risks as much as technical ones.

### 18.8 Anti-patterns

The following should be treated as failures for M0:

- `Combat Core` depending on the camera
- `Enemy Intent & Telegraph` sending camera-only truth instead of readable enemy state
- the camera deciding target validity instead of observing target context
- the camera requiring final `VFX` or `Audio` to be readable
- a `UI` marker replacing camera framing
- `VFX` or `Audio` triggering camera feedback directly
- `Memory State` forcing a reveal camera cutscene
- `Player Locomotion` secretly changing movement because camera state changed
- building boss or multi-target camera before one duel works
- camera debug reading stale duplicated state

### 18.9 Open Questions

The following questions remain unresolved:

- whether the camera should observe `Combat Core` through events, snapshots, or read-only state
- whether the camera should observe `Enemy Intent & Telegraph` directly or through a shared combat readability context
- whether `Player / Target Context` needs its own small contract section
- whether `Player Locomotion` must be designed before finalizing camera-relative versus target-relative movement
- whether `Debug Overlay` should be shared with `Combat Core` and `Enemy Intent & Telegraph`
- whether a `UI` lock-on marker is needed for M0
- whether `VFX` and `Audio` need camera timing hooks or can simply react to `Combat Core` events
- whether reveal camera support requires `Memory State` acceptance before emphasis

## 19. Risks

The purpose of this section is to identify the specific M0 risks that could cause `Lock-On & Combat Camera` to fail as a readability layer for the first duel. These risks are not broad production risks. They are focused on one player, one enemy, one duel space, one target-focus mode, `Basic Attack A` readability, response visibility, and punish or reveal readability.

### 19.1 Telegraph Visibility Risk

**Risk:**
The camera may hide or weaken the enemy telegraph.

**Why it matters:**
If the player cannot see windup, posture, weapon motion, commitment, or active threat timing, the combat loop will feel unfair even if the underlying combat rules are correct.

**What could go wrong:**

- enemy windup is off-screen
- weapon or body is hidden by camera angle
- the camera orbits during timing-critical windows
- target focus drifts away
- camera distance is too close or too far
- `VFX`, shake, or zoom obscure the read

**Mitigation direction:**

- prioritize telegraph visibility over style
- keep the camera stable during `EnemyTelegraph`
- debug enemy visibility, weapon/body visibility, and critical-window movement
- test `Basic Attack A` readability before adding extra camera feedback

### 19.2 Camera Fighting Player Control Risk

**Risk:**
The camera or lock-on may feel like it is fighting player movement or intention.

**Why it matters:**
The player must feel in control during a precise katana duel. If the camera feels like a second controller, the duel becomes frustrating instead of elegant.

**What could go wrong:**

- hard lock is too rigid
- target-relative movement feels restrictive
- manual look input is overridden too aggressively
- recentering happens at the wrong time
- camera rotates during dodge, parry, or counter

**Mitigation direction:**

- start with soft target focus if possible
- keep hard lock optional until readability clearly requires it
- avoid large rotation during response windows
- decide camera-relative versus target-relative movement through prototype testing

### 19.3 Spacing Readability Risk

**Risk:**
The player may not understand distance, range, or dodge displacement.

**Why it matters:**
Spacing is needed for dodge, whiff punish, counter opportunity, and fair failure. If spacing is visually unclear, the player loses trust in both success and failure.

**What could go wrong:**

- camera is too close
- camera is too zoomed
- enemy and player are not visible together
- dodge displacement is hidden
- lock-on framing over-focuses one actor
- effects hide the gap between player and enemy

**Mitigation direction:**

- tune distance, height, and angle for spacing readability
- keep both player and enemy visible whenever possible
- preserve dodge displacement visibility
- use debug spacing or range indicators if needed

### 19.4 Lock-On Rigidity Risk

**Risk:**
Hard lock-on may make combat feel stiff or over-controlled.

**Why it matters:**
`Glass Refrain` should feel elegant and controlled, not mechanically trapped. If lock-on becomes too forceful, the camera solves readability by reducing player comfort.

**What could go wrong:**

- target focus always forces camera orientation
- the player cannot comfortably reposition
- movement becomes too target-relative
- camera ignores player intention
- lock-on is required for every action

**Mitigation direction:**

- start with soft focus or lightweight lock-on
- do not require lock-on for all combat actions unless later approved
- keep target focus as readability support rather than action validity
- test player comfort before hardening lock-on behavior

### 19.5 Soft Focus Drift Risk

**Risk:**
Soft target focus may fail to keep the enemy readable.

**Why it matters:**
If the enemy drifts out of view during telegraph, the duel fails its basic fairness goal even if the control feel is lighter.

**What could go wrong:**

- focus strength is too weak
- enemy approach or telegraph is not prioritized
- player movement pulls the camera away
- no stronger anchoring exists during critical states

**Mitigation direction:**

- allow stronger focus during `EnemyTelegraph`
- use `TelegraphFraming` priority
- debug target visibility and focus strength
- upgrade to harder lock only if soft focus fails readability tests

### 19.6 Response Feedback Timing Risk

**Risk:**
Camera feedback may trigger too early, too late, or from invalid context.

**Why it matters:**
Feedback should clarify success or failure, not lie to the player. If the camera implies a result before the systems confirm it, the duel becomes untrustworthy.

**What could go wrong:**

- camera shake occurs before `Combat Core` confirms result
- `VFX` or `Audio` trigger camera feedback directly
- result feedback is not tied to a `Combat Core` event
- feedback implies success when action failed
- delayed feedback makes impact unclear

**Mitigation direction:**

- allow feedback only after confirmed result
- trace feedback source in debug
- disable shake or zoom during early timing tests if needed
- keep feedback restrained until readability is proven

### 19.7 Punish Window Visibility Risk

**Risk:**
The camera may hide enemy recovery or punish opportunity.

**Why it matters:**
The reward side of the duel loop depends on the player seeing the opening. If enemy vulnerability is hidden, counter learning collapses.

**What could go wrong:**

- camera resets too early
- result feedback hides recovery
- camera over-focuses the player after dodge or parry
- enemy exposed posture is off-screen
- zoom or shake hides spacing during punish

**Mitigation direction:**

- prioritize `PunishReadability` after whiff, parry, or stagger
- do not reset until punish or recovery is visible
- keep enemy exposure and spacing visible
- debug `EnemyPunishWindow` and `CounterWindow` visibility

### 19.8 Reveal Over-Cinematic Risk

**Risk:**
Reveal support may become too cinematic and interrupt combat readability.

**Why it matters:**
Reveal should support the project’s mystery tone without breaking duel rhythm. If reveal takes over the camera, the combat loop loses continuity.

**What could go wrong:**

- reveal camera behaves like a cutscene
- the camera steals control too long
- reveal hides enemy reset or next telegraph
- reveal triggers without valid `Memory` or `Combat` context
- reveal zoom or shake becomes excessive

**Mitigation direction:**

- keep reveal short, restrained, and optional in M0
- require valid reveal context
- return quickly to readable duel framing
- defer reveal camera emphasis if `VFX` and `Audio` are enough

### 19.9 Boundary Blur Risk

**Risk:**
The camera may accidentally own combat, target, or reveal truth.

**Why it matters:**
`Combat Core`, `Enemy Intent & Telegraph`, and `Memory State` must remain authoritative. If the camera becomes a hidden authority, the whole system becomes harder to debug and trust.

**What could go wrong:**

- lock-on decides hit or counter validity
- a target marker decides target validity
- the camera opens `CounterWindow`
- the camera triggers reveal
- camera state changes player movement or combat rules invisibly

**Mitigation direction:**

- keep the camera on read-only or confirmed context
- let `Combat Core` own action and result validity
- let `Enemy Intent & Telegraph` own telegraph and punish truth
- let `Memory State` own memory consequence
- keep debug traces for feedback and context source

### 19.10 Debug Insufficiency Risk

**Risk:**
The team may not be able to explain camera readability failures.

**Why it matters:**
Without debug, camera tuning becomes subjective, slower, and less trustworthy. The duel camera is too timing-sensitive to tune only by feel.

**What could go wrong:**

- no current camera state display
- no target-focus debug
- no critical-window movement trace
- no feedback source trace
- no visibility checks
- stale or duplicated debug data

**Mitigation direction:**

- implement high-signal debug early
- use GDD state names in debug
- expose target, visibility, critical-window movement, feedback source, and reset reason
- keep debug simple and designer-readable

### 19.11 Scope Creep Risk

**Risk:**
The camera system may expand into boss, cinematic, multi-target, or production-camera scope too early.

**Why it matters:**
M0 only needs to prove one readable duel. If the system expands too early, effort is spent on future complexity instead of first-duel fairness.

**What could go wrong:**

- building boss camera architecture
- adding multi-target cycling
- designing cinematic reveal camera
- building production lock-on UI
- implementing complex occlusion systems
- building a full camera preset framework

**Mitigation direction:**

- stay with one player, one enemy, and one duel space
- defer boss, multi-target, and cinematic systems
- use minimal camera data and simple target focus
- validate `Basic Attack A` readability before expanding

### 19.12 Risk Table

| Risk | Why It Matters | Failure Mode | Mitigation | M0 Severity |
| --- | --- | --- | --- | --- |
| `Telegraph Visibility` | Protects fairness of the read phase | Windup, posture, or weapon motion become unreadable | Prioritize telegraph visibility, stabilize during telegraph, debug visibility | `High` |
| `Camera Fighting Player Control` | Preserves player ownership of the duel | Camera feels like it resists movement or response intent | Start soft, avoid aggressive rotation, prototype movement modes | `High` |
| `Spacing Readability` | Needed for dodge, whiff punish, and fair failure | Player cannot judge distance or displacement | Tune framing for spacing, keep both actors readable, debug spacing | `High` |
| `Lock-On Rigidity` | Prevents duel from feeling trapped | Hard lock makes movement stiff or over-controlled | Keep lock-on lightweight until proven needed | `Medium` |
| `Soft Focus Drift` | Protects enemy visibility without rigid lock | Enemy drifts out of view during telegraph | Strengthen focus during critical states, escalate only if needed | `Medium` |
| `Response Feedback Timing` | Keeps feedback truthful | Feedback triggers from invalid or mistimed context | Confirm result first, trace source, restrain early feedback | `High` |
| `Punish Window Visibility` | Protects the reward side of the loop | Recovery or exposure is hidden | Prioritize punish readability, delay reset, debug visibility | `High` |
| `Reveal Over-Cinematic` | Prevents reveal from breaking the duel | Reveal steals control or hides next read | Keep reveal short, optional, and validated | `Medium` |
| `Boundary Blur` | Protects authoritative system ownership | Camera becomes hidden combat or reveal authority | Use read-only context, preserve system boundaries, trace source | `High` |
| `Debug Insufficiency` | Enables intentional tuning | Team cannot explain readability failures | Add high-signal debug early and keep it readable | `High` |
| `Scope Creep` | Keeps M0 focused on one duel | Camera expands into boss/cinematic/multi-target systems | Defer future scope and validate one duel first | `Medium` |

### 19.13 Highest Priority Risks

The top M0 camera risks are:

- `Telegraph visibility`
- `Camera fighting player control`
- `Spacing readability`
- `Response feedback timing`
- `Punish window visibility`
- `Debug insufficiency`
- `Boundary blur`

These are the risks most likely to make the first duel unreadable or untrustworthy even if other systems are functioning correctly.

### 19.14 Anti-patterns

The following should be treated as failures for M0:

- tuning camera style before telegraph readability
- adding hard lock before soft focus is tested
- using camera shake before result confirmation
- reveal becoming a cutscene
- camera reset hiding punish window
- `UI` marker replacing camera framing
- lock-on deciding combat validity
- camera movement during parry timing
- building boss or multi-target camera before one duel works
- debugging camera only by feel with no state or visibility data

### 19.15 Open Questions

The following questions remain unresolved:

- which camera risk should be validated first in prototype
- whether soft focus can pass `Basic Attack A` readability
- when hard lock-on becomes necessary
- whether camera shake should be disabled for first timing tests
- whether reveal camera support is needed for M0
- how much debug is required before serious camera tuning
- what threshold marks camera readability as good enough for M0

## 20. Open Questions

The purpose of this section is to consolidate the unresolved questions around `Lock-On & Combat Camera` and organize them by decision priority. Not every question needs to be answered immediately, but the team should be able to see clearly which questions block M0 implementation planning, which can be answered through tuning, which should be deferred, and which belong to neighboring systems.

### 20.1 Must Answer Before M0 Implementation

The following questions should be reviewed before implementation begins because they materially affect how the first duel camera is built:

- Does M0 start with soft target focus or hard lock-on?
- Is lock-on manually toggled, automatically engaged, or both?
- Is target focus required for the first duel prototype?
- Does M0 movement use camera-relative or target-relative movement while focused?
- Is manual camera or look input allowed during target focus?
- Does camera behavior change during `EnemyTelegraph`, or only stabilize existing framing?
- Is `TelegraphFraming` a real camera state or a priority modifier?
- Is `PunishReadability` a separate camera state or part of `ResultFeedback`?
- Is `RevealSupport` a real camera state or presentation overlay?
- Does reveal camera support exist in M0, or are `VFX` and `Audio` enough?
- Is camera debug part of the shared M0 combat overlay or a separate camera overlay?
- Does the camera use `Cinemachine` immediately or start with a simpler prototype controller?
- Where does camera runtime state live for M0: camera scope, gameplay scope, or encounter scope?

These questions matter because they define the smallest viable shape of the M0 camera system.

### 20.2 Can Answer During M0 Tuning

The following questions are best answered through feel iteration rather than up-front design certainty:

- approximate camera distance for the first prototype
- camera height and angle for readable katana duel framing
- how strong target focus should be
- how much camera movement is allowed during `EnemyTelegraph`
- whether timing-critical windows reduce camera movement or freeze it
- how much rotation or orbit is acceptable during dodge, parry, and counter
- whether parry success needs camera impulse
- whether counter impact needs camera emphasis
- whether failed parry needs distinct camera treatment
- whether reveal uses camera zoom or only presentation effects
- whether camera reset is instant, damped, time-based, event-driven, or state-driven
- whether result feedback should be disabled during early timing tests
- whether placeholder animation, `VFX`, and `Audio` are enough for camera readability testing
- how many playtest passes are enough to validate camera readability

These should be treated as tuning questions with explicit prototype assumptions rather than hidden unresolved behavior.

### 20.3 Defer Until After M0

The following questions should not block the first duel prototype:

- boss camera framework
- multi-target cycling
- boss body-part targeting
- cinematic cutscene camera
- full camera collision or occlusion system unless it becomes a blocker
- production lock-on UI
- full accessibility camera options
- photo mode
- ranged combat camera
- multiplayer camera
- open-world exploration camera
- advanced camera preset framework
- production animation, `VFX`, and `Audio` synchronization
- complex reveal cinematic direction
- final HUD target-status system

If any of these begin shaping M0 implementation, the camera system has likely started drifting out of scope.

### 20.4 Cross-System Questions

Some questions belong primarily to neighboring GDDs even though they affect camera behavior.

#### Combat Core

- Does counter auto-align to target, or require strict spacing?
- Does `CounterWindow` need any camera-readable state?
- Should camera feedback follow `Combat Core` event, result snapshot, or read-only state?
- Should camera shake or impulse be disabled during early combat timing tests?

#### Enemy Intent & Telegraph

- Does `EnemyTelegraph` request `TelegraphFraming` directly, or does the camera observe telegraph state?
- Does `EnemyPunishWindow` request `PunishReadability`, or does the camera observe punish state?
- Is enemy weapon/body visibility required for every M0 telegraph?
- Should attack range be visible through debug gizmos?

#### Player Locomotion

- Is movement camera-relative or target-relative during focus?
- Does dodge direction use input-relative, camera-relative, or target-relative logic?
- Does player facing get constrained during lock-on?
- Are facing constraints data-authored later?

#### Memory State

- Does reveal camera support require `Memory State` acceptance?
- Does reveal camera support happen after counter immediately or after stagger confirmation?
- Is reveal support mostly camera, `VFX`/`Audio`, shader, or memory presentation?
- Can reveal camera support be deferred for M0?

#### Debug Overlay

- Is camera debug shared with `Combat Core` / `Enemy Intent & Telegraph` debug?
- Are visibility checks manual or instrumented?
- Should camera critical-window movement be explicitly logged?
- Should camera debug be available in development builds?
- Are reset/reveal failures runtime debug flags or playtest notes?

#### Presentation

- Is a lock-on marker needed for M0?
- Can `VFX` request camera emphasis, or only respond to confirmed camera/combat events?
- Can animation events request camera feedback later?
- Does `UI / HUD` show target status in M0?
- Should presentation contracts be formalized before implementation?

These questions should not be solved in isolation if the neighboring system owns the actual truth or implementation constraint.

### 20.5 Recommended Decision Order

The recommended decision order before implementation is:

1. soft focus versus hard lock-on
2. manual toggle versus automatic target focus
3. camera-relative versus target-relative movement
4. `TelegraphFraming` as state versus priority modifier
5. `PunishReadability` as state versus `ResultFeedback` extension
6. `RevealSupport` as state versus deferred presentation overlay
7. `Cinemachine` immediately versus simpler prototype controller
8. camera debug overlay ownership
9. camera runtime state scope
10. whether shake, zoom, and reveal emphasis are disabled during first timing tests

This order favors decisions that most directly shape how the first readable duel is built and tested.

### 20.6 Non-Blocking Notes

Not every question here needs an immediate final answer.

Important guidance:

- the goal is to prevent hidden blockers
- unresolved tuning questions can become explicit prototype assumptions
- deferred questions should not leak into M0 implementation
- camera readability should be validated with `Basic Attack A` before expanding
- lock-on should remain a readability tool rather than combat authority

This section exists to make uncertainty visible and manageable, not to eliminate all uncertainty up front.

### 20.7 Open Question Table

| Question | Category | Blocks M0 Implementation? | Owner System | Recommended Timing |
| --- | --- | --- | --- | --- |
| Soft target focus or hard lock-on? | `Must Answer` | Yes | `Lock-On & Combat Camera` | Before prototype implementation |
| Manual toggle or automatic target focus? | `Must Answer` | Yes | `Lock-On & Combat Camera` | Before prototype implementation |
| Is target focus required for first duel prototype? | `Must Answer` | Yes | `Lock-On & Combat Camera` | Before prototype implementation |
| Camera-relative or target-relative movement while focused? | `Must Answer` | Yes | `Lock-On & Combat Camera` + `Player Locomotion` | Before prototype implementation |
| Is manual look input allowed during target focus? | `Must Answer` | Yes | `Lock-On & Combat Camera` | Before prototype implementation |
| Does camera behavior change during `EnemyTelegraph`, or only stabilize? | `Must Answer` | Yes | `Lock-On & Combat Camera` + `Enemy Intent & Telegraph` | Before prototype implementation |
| Is `TelegraphFraming` a state or priority modifier? | `Must Answer` | Yes | `Lock-On & Combat Camera` | Before prototype implementation |
| Is `PunishReadability` separate from `ResultFeedback`? | `Must Answer` | Yes | `Lock-On & Combat Camera` | Before prototype implementation |
| Is `RevealSupport` a state or presentation overlay? | `Must Answer` | Yes | `Lock-On & Combat Camera` + `Presentation` | Before prototype implementation |
| Does reveal camera support exist in M0? | `Must Answer` | Yes | `Lock-On & Combat Camera` + `Memory State` | Before prototype implementation |
| Shared camera debug overlay or separate overlay? | `Must Answer` | Yes | `Debug Overlay` + `Lock-On & Combat Camera` | Before prototype implementation |
| `Cinemachine` immediately or simpler prototype controller? | `Must Answer` | Yes | `Lock-On & Combat Camera` | Before prototype implementation |
| Where does camera runtime state live? | `Must Answer` | Yes | `Lock-On & Combat Camera` + architecture | Before prototype implementation |
| Approximate first camera distance? | `Tune During M0` | No | `Lock-On & Combat Camera` | Early playtest tuning |
| Camera height / angle for duel framing? | `Tune During M0` | No | `Lock-On & Combat Camera` | Early playtest tuning |
| How strong should target focus be? | `Tune During M0` | No | `Lock-On & Combat Camera` | Early playtest tuning |
| How much movement is allowed during `EnemyTelegraph`? | `Tune During M0` | No | `Lock-On & Combat Camera` | Early playtest tuning |
| Reduce movement or freeze during critical windows? | `Tune During M0` | No | `Lock-On & Combat Camera` | Early playtest tuning |
| How much orbit is acceptable during response windows? | `Tune During M0` | No | `Lock-On & Combat Camera` | Early playtest tuning |
| Does parry success need camera impulse? | `Tune During M0` | No | `Lock-On & Combat Camera` | After baseline readability works |
| Does counter impact need camera emphasis? | `Tune During M0` | No | `Lock-On & Combat Camera` | After baseline readability works |
| Does failed parry need distinct camera treatment? | `Tune During M0` | No | `Lock-On & Combat Camera` | After baseline readability works |
| Reveal zoom or presentation effects only? | `Tune During M0` | No | `Lock-On & Combat Camera` + `Presentation` | After base duel readability works |
| How should reset behave? | `Tune During M0` | No | `Lock-On & Combat Camera` | During iteration |
| Disable result feedback during early timing tests? | `Tune During M0` | No | `Lock-On & Combat Camera` + `Combat Core` | First timing passes |
| Are placeholder assets enough for readability testing? | `Tune During M0` | No | `Lock-On & Combat Camera` + `Presentation` | First prototype validation |
| How many playtest passes validate camera readability? | `Tune During M0` | No | design/testing | During tuning |
| Boss camera framework? | `Defer After M0` | No | future camera systems | After M0 |
| Multi-target cycling? | `Defer After M0` | No | future targeting systems | After M0 |
| Boss body-part targeting? | `Defer After M0` | No | future targeting systems | After M0 |
| Cinematic cutscene camera? | `Defer After M0` | No | future presentation systems | After M0 |
| Full occlusion/collision system? | `Defer After M0` | No, unless blocker | future camera tech | After M0 unless blocked |
| Production lock-on UI? | `Defer After M0` | No | `UI / HUD` | After M0 |
| Full accessibility camera options? | `Defer After M0` | No | future camera/UI systems | After M0 |
| Photo mode? | `Defer After M0` | No | future camera systems | After M0 |
| Ranged combat camera? | `Defer After M0` | No | future combat/camera systems | After M0 |
| Multiplayer camera? | `Defer After M0` | No | future multiplayer systems | After M0 |
| Open-world exploration camera? | `Defer After M0` | No | future traversal systems | After M0 |
| Advanced camera preset framework? | `Defer After M0` | No | future camera architecture | After M0 |
| Production animation/VFX/audio sync? | `Defer After M0` | No | future presentation systems | After M0 |
| Complex reveal cinematic direction? | `Defer After M0` | No | future narrative/presentation systems | After M0 |
| Final HUD target status system? | `Defer After M0` | No | `UI / HUD` | After M0 |
| Does counter auto-align or require strict spacing? | `Cross-System` | Maybe | `Combat Core` | Before or during implementation planning |
| Does `CounterWindow` need camera-readable state? | `Cross-System` | Maybe | `Combat Core` | Before implementation planning |
| Should camera feedback follow events, snapshots, or read-only state? | `Cross-System` | Maybe | `Combat Core` + camera architecture | Before implementation planning |
| Should shake/impulse be disabled during early combat timing tests? | `Cross-System` | Maybe | `Combat Core` + camera | Before first timing tests |
| Does `EnemyTelegraph` request `TelegraphFraming` directly? | `Cross-System` | Maybe | `Enemy Intent & Telegraph` | Before implementation planning |
| Does `EnemyPunishWindow` request `PunishReadability` directly? | `Cross-System` | Maybe | `Enemy Intent & Telegraph` | Before implementation planning |
| Is enemy weapon/body visibility required for every M0 telegraph? | `Cross-System` | Maybe | `Enemy Intent & Telegraph` + camera | Before telegraph tuning |
| Should attack range be visible through debug gizmos? | `Cross-System` | Maybe | `Enemy Intent & Telegraph` + `Debug Overlay` | Before serious tuning |
| Does dodge direction use input/camera/target-relative logic? | `Cross-System` | Yes | `Player Locomotion` | Before implementation planning |
| Does player facing get constrained during lock-on? | `Cross-System` | Maybe | `Player Locomotion` + camera | Before implementation planning |
| Are facing constraints data-authored later? | `Cross-System` | No | `Player Locomotion` + camera | During implementation planning |
| Does reveal support require `Memory State` acceptance? | `Cross-System` | Maybe | `Memory State` | Before reveal implementation |
| Does reveal support follow counter immediately or after stagger? | `Cross-System` | Maybe | `Memory State` + `Combat Core` + camera | Before reveal implementation |
| Is reveal support mostly camera, VFX/audio, shader, or memory presentation? | `Cross-System` | Maybe | `Memory State` + `Presentation` | Before reveal implementation |
| Can reveal camera support be deferred for M0? | `Cross-System` | Maybe | `Memory State` + camera | Before reveal implementation |
| Are visibility checks manual or instrumented? | `Cross-System` | Maybe | `Debug Overlay` | Before serious tuning |
| Should camera critical-window movement be explicitly logged? | `Cross-System` | Maybe | `Debug Overlay` + camera | Before serious tuning |
| Should camera debug be available in development builds? | `Cross-System` | No | `Debug Overlay` | Before broader playtesting |
| Are reset/reveal failures runtime flags or playtest notes? | `Cross-System` | No | `Debug Overlay` + testing | During tuning |
| Is a lock-on marker needed for M0? | `Cross-System` | Maybe | `Presentation` + `UI / HUD` | Before UI support decisions |
| Can `VFX` request camera emphasis? | `Cross-System` | No | `Presentation` | Before presentation sync rules finalize |
| Can animation events request camera feedback later? | `Cross-System` | No | `Presentation` | Before presentation sync rules finalize |
| Does `UI / HUD` show target status in M0? | `Cross-System` | No | `UI / HUD` | After core readability works |
| Should presentation contracts be formalized before implementation? | `Cross-System` | Maybe | `Presentation` + architecture | Before implementation if coordination is unclear |

### 20.8 Final Summary

`Lock-On & Combat Camera` is ready for M0 implementation planning once the must-answer questions are reviewed and either decided or explicitly accepted as prototype assumptions.

## 21. Acceptance Criteria For M0

The purpose of these acceptance criteria is to define when `Lock-On & Combat Camera` is good enough to support the first readable duel prototype. M0 does not require final polish, cinematic sophistication, or broad targeting scope. It requires a camera and target-focus layer that can reliably support one duel without hiding the combat truth authored elsewhere.

### 21.1 M0 Acceptance Purpose

These criteria should answer:

- can the player see enemy telegraph clearly
- can the player judge spacing
- does target focus help orientation without fighting the player
- does the camera preserve dodge, parry, and counter readability
- does result feedback happen after valid outcomes
- does punish or recovery remain visible
- does reveal support preserve the next read
- can debug explain camera behavior
- is the scope still contained to one simple duel

If the answer to these questions is consistently yes in a one-enemy duel, the camera layer has done its M0 job.

### 21.2 Core Camera Loop Acceptance

M0 camera passes if one simple duel can repeatedly demonstrate:

`find target → frame duel → read intent → support answer → confirm result → preserve punish/reveal → reset readability`

Required:

- target can be acquired or focused predictably
- player and enemy are readable during neutral and approach
- enemy telegraph stays visible
- dodge, parry, and counter moments remain understandable
- result feedback does not obscure recovery or the next read
- punish and reveal support remain restrained and readable
- reset returns the duel to stable readable framing

The loop does not need to feel finished. It does need to feel trustworthy and teachable.

### 21.3 Target Focus / Lock-On Acceptance

Target focus is acceptable if:

- the current target is clear enough for both player and designer
- target focus helps maintain enemy readability
- target focus does not decide combat validity
- target focus does not make all actions auto-connect
- target focus does not fight player control excessively
- release and acquisition behavior are predictable
- target state is debug-visible

If focus helps orientation but does not become hidden authority, it is serving M0 correctly.

### 21.4 Telegraph Readability Acceptance

Telegraph readability is acceptable if:

- enemy windup remains visible during `Basic Attack A`
- enemy body and weapon motion are readable enough to support timing
- the camera does not rotate aggressively during telegraph
- the camera does not hide player position or spacing
- active threat timing is understandable
- the player can explain why dodge or parry succeeded or failed
- telegraph readability does not rely only on `UI` or debug

This is one of the most important pass conditions because telegraph fairness is the camera’s core readability obligation.

### 21.5 Spacing / Movement Readability Acceptance

Spacing readability is acceptable if:

- the player can judge distance to the enemy
- dodge displacement is visible
- enemy approach direction is understandable
- player orientation is clear during target focus
- camera distance and angle do not hide range
- the player can tell when they are too close, too far, or misaligned

If spacing is unreadable, dodge and punish meaning become unreliable even when the systems are technically correct.

### 21.6 Dodge / Parry / Counter Acceptance

Camera support is acceptable if:

- dodge movement remains readable
- parry timing and result remain visible
- counter alignment and impact remain visible
- failed dodge, parry, and counter remain explainable
- camera feedback follows confirmed `Combat Core` result
- camera shake or zoom does not happen before result confirmation
- counter or reveal feedback does not hide enemy stagger or the next read

The camera must support both success clarity and failure clarity.

### 21.7 Punish / Reveal Acceptance

Punish and reveal support is acceptable if:

- enemy recovery or punish posture remains visible
- `EnemyPunishWindow` is not hidden by reset or result feedback
- the camera does not imply `CounterWindow` when `Combat Core` rejects it
- reveal support only happens after valid reveal context
- reveal support is short and restrained
- reveal does not hide enemy reset or the next telegraph
- reveal camera support may be deferred if `VFX` and `Audio` already provide enough clarity

This keeps the reward and meaning side of the duel readable without inflating it into cinematic scope.

### 21.8 Debug Acceptance

Debug is acceptable if designers can inspect:

- current camera state
- current and previous target-focus state
- target validity and visibility
- camera state reason
- enemy, player, and spacing visibility
- telegraph visibility
- critical-window camera movement
- result feedback source
- reset reason
- reveal support source and timing

Debug does not need final UI polish. It does need to be trustworthy and usable.

### 21.9 Scope Acceptance

M0 remains acceptable only if it does not include:

- boss camera framework
- multi-target cycling
- boss body-part targeting
- cinematic cutscene camera
- production lock-on UI
- final HUD target status
- full accessibility camera options
- photo mode
- ranged combat camera
- multiplayer camera
- open-world exploration camera
- advanced camera preset framework
- production animation, `VFX`, and `Audio` synchronization

If these start shaping implementation, the camera system has left M0 scope.

### 21.10 Playtest Acceptance Checklist

A tester should be able to answer yes to the following:

- I could tell which enemy I was focused on.
- I could see the enemy before the attack.
- I could read the enemy windup.
- I could judge distance and spacing.
- I understood my dodge movement.
- I understood whether my parry worked or failed.
- I could see counter impact.
- I could see when the enemy was punishable.
- Camera feedback did not lie about success or failure.
- Reveal support did not hide the next threat.
- The camera returned to readable framing after exchanges.
- Debug explained unclear camera moments.

If multiple testers cannot answer yes to most of these, the camera is not yet good enough for M0.

### 21.11 Failure Conditions

`Lock-On & Combat Camera` M0 should not pass if:

- enemy telegraph is frequently hidden
- camera movement causes dodge, parry, or counter failure to feel unfair
- target focus fights the player more than it helps
- spacing cannot be judged
- feedback triggers before confirmed result
- the camera implies invalid counter or reveal success
- punish window is hidden by camera reset
- reveal becomes a cutscene
- debug cannot explain camera state or feedback source
- final polish is required to judge basic camera readability

Any one of these may be enough to block M0 if it is severe and persistent.

### 21.12 Acceptance Table

| Area | Acceptance Criteria | How To Verify | Pass/Fail Signal | M0 Priority |
| --- | --- | --- | --- | --- |
| `Core Camera Loop` | Duel repeatedly supports find, frame, read, answer, confirm, punish/reveal, reset | Repeated one-enemy playtests | Pass if the loop remains readable end-to-end | `Must Pass` |
| `Target Focus / Lock-On` | Focus improves orientation without becoming hidden authority | Targeted playtests and debug review | Pass if focus helps more than it fights | `Must Pass` |
| `Telegraph Readability` | `Basic Attack A` windup and timing remain readable | Fresh-tester observation and debug review | Pass if telegraph is consistently visible and fair | `Must Pass` |
| `Spacing Readability` | Player can judge range and displacement | Dodge and approach playtests | Pass if spacing mistakes are understandable | `Must Pass` |
| `Dodge Support` | Dodge motion and failure remain readable | Dodge-focused response tests | Pass if dodge clarity survives camera motion | `Must Pass` |
| `Parry Support` | Parry timing and result remain visible | Parry timing tests | Pass if the camera does not distort timing trust | `Must Pass` |
| `Counter Support` | Counter alignment, impact, and failure remain understandable | Counter-window tests | Pass if counter reads as intentional and valid only when confirmed | `Should Pass` |
| `Punish Visibility` | Recovery, whiff, and punish posture remain visible | Whiff/parry/stagger tests | Pass if the opening can be seen and explained | `Must Pass` |
| `Reveal Support` | Reveal remains restrained and does not hide next read | Reveal-capable exchange tests | Pass if reveal adds meaning without stealing readability | `Should Pass` |
| `Debug Visibility` | Designers can explain state, movement, feedback, and reset | Debug review during playtests | Pass if unclear moments can be diagnosed quickly | `Must Pass` |
| `Scope Control` | System remains one-duel-focused | Scope review against GDD | Pass if no boss/multi-target/cinematic drift appears | `Must Pass` |
| `Combat Boundary` | Camera never owns combat truth | Cross-system behavior review | Pass if all outcomes trace back to authoritative systems | `Must Pass` |

### 21.13 Minimum “Good Enough” Definition

`Lock-On & Combat Camera` M0 is good enough when one simple duel using `Basic Attack A` allows the player to consistently see the enemy, read telegraph, judge spacing, understand dodge/parry/counter results, recognize punish opportunity, and return to readable framing after reveal/reset without relying on final camera polish or expanding into boss, multi-target, or cinematic systems.

### 21.14 Deferred Acceptance

The following are explicitly not required for `Lock-On & Combat Camera` M0:

- hard lock-on if soft focus already passes readability
- multi-target cycling
- boss camera behavior
- cinematic reveal camera
- production lock-on marker
- final camera polish
- final HUD target status
- full occlusion or collision system unless it blocks the prototype
- advanced camera accessibility settings
- photo mode
- ranged camera support
- multiplayer camera support

These may matter later, but they are not acceptance gates for the first readable duel.

### 21.15 Open Questions

The following questions remain unresolved:

- how many playtest runs are enough to pass camera readability
- whether soft focus alone is enough for M0
- whether hard lock-on is required before implementation
- whether camera shake should remain disabled during first timing tests
- whether reveal camera support is needed or deferred
- who approves camera readability as good enough
- what exact threshold ends camera tuning and moves to implementation planning
