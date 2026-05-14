# Combat Core

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Combat As Interpretation, Melancholic Elegance, Personal Restoration Over Power Fantasy

## 1. System Summary

`Combat Core` defines the authoritative M0 combat rules for `Glass Refrain`'s first katana duel prototype. It governs how player combat actions are requested, validated, resolved, and exposed to other systems during the core rhythm:

`read → evade/parry → counter → reveal`

For M0, `Combat Core` supports a minimal but readable duel between the female katana protagonist and one simple enemy in the Tokyo Street duel space. It validates `light attack`, `heavy attack`, dodge result, parry result, counter opportunity, hit resolution, action lock and recovery context, `CounterWindow`, and reveal request context. Its purpose is not to build a full RPG combat framework, but to prove that the first duel feels fair, legible, emotionally restrained, and mechanically trustworthy.

`Combat Core` is the gameplay authority for combat outcomes. It does not own player movement truth, camera framing, enemy intent truth, `Animator State Machine` truth, `VFX` or `Audio` timing truth, or memory reveal validity. `Player Locomotion` owns movement state, dodge movement expression, facing and orientation support, movement restrictions, and recovery movement. `Enemy Intent & Telegraph` owns enemy-side readability, telegraph, commitment, active or recovery states, tags, and punish windows. `Lock-On & Combat Camera` owns framing, readability support, and target-focus presentation support. `Memory State` accepts or rejects reveal context. Presentation systems may communicate combat state, but they remain presentation-only unless explicitly validated by gameplay systems.

In short, `Combat Core` is responsible for deciding whether combat actions and results are valid, while adjacent systems provide movement, enemy readability, framing, memory consequence, and presentation support around those authoritative outcomes.

## 2. Design Intent

Combat Core is the heart of `Glass Refrain`'s M0 prototype. Its purpose is not to establish a large action RPG combat framework, a broad weapon ecosystem, or a progression-heavy battle model. Its purpose is to prove that a small, precise, emotionally readable katana duel loop can carry the identity of the project.

At M0, combat must successfully express the loop `read → evade → counter → reveal`. The player should feel that they are interpreting the enemy rather than simply outputting attacks. Enemy intent matters more than combo length. Success should feel earned through timing, spacing, and reading. Failure should feel understandable, with clear reasons why the player was hit, why a counter window was missed, or why an opening did not appear when expected.

The intended emotional shape of combat is calm before violence. Encounters should begin in a state of observation and tension, then break into short, elegant bursts of action when the player reads correctly and commits at the right moment. The system should feel precise rather than aggressive, reactive rather than chaotic, and elegant without becoming flashy for its own sake. The dominant feeling should be emotional tension and interpretive clarity, not overwhelming power fantasy.

This system primarily serves three project pillars. It supports `Combat As Interpretation` by making swordplay the method through which the player understands enemy emotion and memory-state distortion. It supports `Melancholic Elegance` by emphasizing controlled pacing, readable spacing, and restrained impact over spectacle spam. It supports `Personal Restoration Over Power Fantasy` by framing success as regained fluency and understanding, not raw dominance.

For M0, the design goal is simple and measurable: a tester should be able to fight one simple enemy in the Tokyo Street prototype arena and understand what the enemy intended, when they should evade or parry, when the counter window opened, why they succeeded or failed, and how the reveal or memory response connects to the combat outcome. If the player cannot explain those things after a short play session, the prototype has not yet proven the system.

This section also establishes what Combat Core is not responsible for yet. It does not define a full RPG stat system. It does not define multiple weapons, large combo trees, boss frameworks, or full progression architecture. M0 remains tightly focused on combat feel, duel readability, and the connection between combat outcome and restrained memory reveal.

Technically, the system must remain explicit and frame-readable. Combat truth should live in inspectable state transitions, timing windows, and clearly owned rules rather than in opaque presentation behavior. `R3` may observe combat state for debug visibility or UI-facing readouts, but it must not own hot combat truth. `DOTween` must not drive authoritative combat motion. Camera, UI, and VFX systems may observe combat state and respond to it, but they must not own combat rules or become the source of timing truth.

## 3. Player Experience Goals

The purpose of Combat Core in M0 is to create a duel experience that is readable, fair, emotionally tense, and satisfying in a very small scope. These goals describe what the player and the designer should consistently feel when the system is working.

### Readability

The player should understand what the enemy is about to do before impact through a combination of animation, spacing, timing, and rhythm. Enemy intent must be readable early enough that the player can make an informed defensive decision instead of reacting to surprise damage. The player does not need to know move names or hidden data, but they should be able to feel the difference between pressure, hesitation, commitment, and vulnerability.

### Defensive Confidence

The player should understand when to evade, when to parry, and when they made a mistake. A failed defense should feel fair and explainable rather than arbitrary. If the player is hit, they should be able to identify whether they committed too early, reacted too late, misread spacing, or chose the wrong defensive answer. Defensive play should build trust in the system rather than anxiety about hidden rules.

### Counter Satisfaction

The counter window should feel earned, short, sharp, and satisfying. The player should feel that they created the opening by reading correctly and surviving with intent, not that the game handed them a long free damage phase. A successful counter should produce a strong emotional release after the tension of observation and defense.

### Controlled Elegance

Combat should feel graceful and restrained rather than noisy or spam-driven. The player should feel like they are dancing around danger, repositioning with purpose, and choosing moments of action carefully. The ideal sensation is not endless offense, but controlled tempo, meaningful spacing, and short expressive bursts of violence.

### Emotional Tension

Combat should feel intimate and tense. Even in the first simple enemy prototype, the opponent should feel like an emotional presence within the memory space rather than a generic damage sponge. The exchange should communicate pressure, hesitation, or instability in a way that supports the larger identity of `Glass Refrain`.

### Reveal Connection

A successful combat exchange should connect to a reveal or memory response that shows why combat matters to the game’s identity. M0 does not need a full narrative or contradiction-resolution system, but it does need a visible sign that correct combat interpretation leads to some form of emotional or memory-state change. The player should understand that combat is not isolated from the mystery; it is one of the ways truth is uncovered.

### Debuggable Feel

Designers and testers should be able to observe combat state, enemy intent, timing windows, and counter availability during tuning. The system should support inspection and iteration rather than relying on guesswork. If the combat does not feel right, the team should be able to diagnose whether the issue comes from intent readability, spacing, timing, or reveal communication.

### M0 Tester Success Criteria

A fresh tester should be able to explain:

- what the enemy intended
- what defensive answer was available
- when the counter window appeared
- why they succeeded or failed
- what changed when the reveal happened

If a tester cannot explain those points after a short session, the combat experience is not yet clear enough for M0.

### Scope Guardrails

These player experience goals apply only to the first simple enemy duel prototype. They do not define final numeric tuning values, full progression, multiple weapon fantasies, or boss-scale confrontation structure. The purpose of this section is to make the first duel readable, fair, emotionally coherent, and worth building on.

## 4. M0 Scope

This section defines the exact scope of Combat Core for `M0 — Katana Combat Feel Prototype`. The goal is to prove that `Glass Refrain` can deliver a precise, readable, emotionally coherent katana duel loop in a small playable space. M0 is not trying to solve the entire combat design for the full game. It is trying to prove the first duel.

### Included in M0

#### Playable Katana Protagonist Combat Kit

M0 includes one playable combat kit for the protagonist. This kit should be sufficient to test reactive duel flow, but narrow enough to keep tuning focused.

Included actions:

- movement-ready combat stance
- light attack
- heavy attack
- dodge
- parry
- counter
- basic hit reaction
- basic recovery

The purpose of this kit is not to provide broad expression through many moves. Its purpose is to provide enough options for the player to read, defend, answer, and feel the rhythm of the loop.

#### One Simple Enemy Duel Target

M0 includes one simple enemy intended as a duel target, not a full encounter family.

Included enemy behavior:

- readable idle or approach behavior
- one or two basic attacks
- clear windup
- clear commitment
- clear recovery or punish window
- minimal hit reaction

This enemy exists to test intent readability, defensive decision-making, counter timing, and reveal response. It does not need to represent the full enemy roster or the Memory Keeper structure.

#### Core Combat Loop

M0 Combat Core must support the following loop in playable form:

- read enemy intent
- evade or parry
- counter during a short opening
- trigger a minimal reveal or memory response

This loop is the primary success condition for M0. If it is not clear, repeatable, and satisfying, M0 is not complete.

#### Timing Windows

M0 includes timing windows for the minimum interactions needed to support readable reactive combat. These windows should be authored and inspectable, but final numeric values remain provisional during this phase.

Included window categories:

- attack startup
- active frames
- recovery
- dodge invulnerability or avoidance window
- parry active window
- counter window
- enemy punish window

The purpose of M0 is to prove that these windows can feel fair, readable, and emotionally coherent. It is not to finalize frame data for the whole game.

#### Hit Resolution

M0 includes the minimum hit outcomes necessary to make the duel understandable:

- player hit enemy
- enemy hit player
- parry success
- parry failure
- dodge success
- counter success
- basic stagger or hit reaction

This is enough to test whether combat answers feel meaningful and whether player success or failure is legible.

#### Debug Visibility

M0 includes debug-facing visibility for the core combat loop so the system can be tuned intentionally rather than by guesswork.

Visible debug information should include:

- current player combat state
- current enemy intent state
- active timing window
- parry window
- counter window
- lock-on target if available
- memory or reveal trigger state

The debug layer is part of M0 scope because feel-driven combat cannot be tuned reliably without state visibility.

### Provisional Contracts

Combat Core is allowed to define provisional contracts for adjacent systems that it depends on, but it must not fully design those systems here.

Allowed provisional contract targets:

- Input Mapping
- Player Locomotion
- Health / Damage / Hit Reaction
- Enemy Intent & Telegraph
- Memory State
- Debug Overlay

These contracts should describe what Combat Core needs from those systems in order to function for M0. They should not become complete designs for those systems inside this document.

### Excluded from M0

M0 Combat Core explicitly does not include:

- full RPG stats
- multiple weapons
- large combo trees
- many enemy types
- boss framework
- full skill tree
- full animation system design
- full investigation system
- full district reinterpretation
- save and persistence
- online or multiplayer features
- loot or equipment system

These exclusions are intentional. The combat prototype should stay narrow enough that readability, timing, and emotional clarity can be tuned without the noise of larger progression or content systems.

### M0 Completion Definition

Combat Core is considered complete for M0 when a tester can repeatedly fight one simple enemy in the prototype arena and clearly experience `read → evade/parry → counter → reveal`, with debug visibility for timing and state.

## 5. Non-Goals

M0 Combat Core must stay narrow. Its purpose is to prove feel, readability, and the foundational duel loop, not to solve every future combat or RPG need of `Glass Refrain`. This section defines the problems Combat Core must explicitly avoid trying to solve during M0.

### Not a Full Action RPG Combat Framework

M0 Combat Core is not responsible for defining the complete long-term combat architecture of the game. It only needs to prove that the duel loop is readable, satisfying, and emotionally coherent in a tightly constrained prototype.

### Not a Combo-Heavy Spectacle System

M0 should not attempt to build a combo-heavy expression system with long strings, launcher chains, stylish ranking layers, deep air-juggle routes, or `Devil May Cry`-style mastery scaffolding. While later versions of the game may explore broader expression, M0 is about timing, spacing, and reaction quality rather than combo quantity.

### Not a Full Boss System

M0 does not need to solve Memory Keeper duel structure, boss phase language, or full confrontation escalation. It only needs one simple enemy duel target that can prove readability and counter timing.

### Not a Progression or Skill-Tree System

M0 does not define leveling, stat growth, unlock trees, build crafting, or long-term ability progression. Combat Core is testing immediate feel, not long-term player development.

### Not a Loot or Stat Damage System

Combat Core should not design rarity, equipment scaling, elemental layering, DPS balancing, or spreadsheet-driven RPG damage structures for M0. Those systems would distract from proving whether the base duel loop works.

### Not an Animation-System Replacement

Combat Core may define combat truth, timing windows, and required animation-facing events or states, but it should not fully design the animation controller architecture, animation graph strategy, or complete animation production pipeline here.

### Not a Camera, UI, or VFX Ownership System

Combat Core may expose observable combat state, but Camera, UI, and VFX own their own presentation behavior. Combat Core should not absorb responsibilities that belong to presentation systems, and presentation must not become the owner of combat rules.

### Not a Full Enemy AI Framework

Combat Core may define the minimum enemy-facing contracts needed to support the prototype loop, but it should not fully design enemy behavior architecture. `Enemy Intent & Telegraph` will later own enemy behavior design more completely.

### Not a Full Memory or Narrative System

Combat Core only needs to define the minimum reveal hook that connects combat outcome to the identity of the game. `Memory State`, and later `Truth Restoration`, own the broader meaning, contradiction tracking, and narrative consequence structure.

### Not Multiplayer or Network-Ready

M0 should not carry rollback, prediction, server authority, co-op assumptions, MMO assumptions, or any multiplayer synchronization requirements. Combat Core is strictly single-player for this phase.

### Not Physics Chaos

M0 should avoid ragdoll-driven combat truth, uncontrolled physics reactions, or non-deterministic hit outcomes. The duel loop depends on readable cause and effect, so combat resolution must remain stable and interpretable.

### Not Over-Architected

M0 should not introduce complex ability frameworks, generic RPG action systems, behavior trees, DOTS/ECS combat architecture, or broad dependency graphs before the duel loop feels good. Architecture must remain practical and in service of clarity.

### Scope Protection Rule

If a proposed combat feature does not improve `read → evade/parry → counter → reveal` for one simple enemy in M0, it should be deferred.

## 6. Core Combat Loop

`read → evade → counter → reveal`

This loop defines the smallest complete combat experience that `Glass Refrain` must prove in M0. The loop is not about maintaining constant offense. It is about recognizing danger, selecting the correct defensive answer, earning a short offensive opening, and receiving a minimal reveal response that ties combat to the game's memory identity.

### 6.1 Read

The loop begins with observation. The player reads enemy intent before impact through stance, spacing, windup, rhythm, telegraph, and movement commitment. The enemy must communicate danger early enough that the player can interpret what kind of response is required rather than simply absorb random damage.

The intended player feeling is not panic, but tense recognition. The player should feel that the enemy is telling the truth through motion, and that the combat system is giving them enough information to respond intelligently. If damage arrives without readable warning, the loop has failed at its first step.

### 6.2 Evade / Parry

Once the player has read the enemy, they choose a defensive answer.

- `Dodge / Evade` is the spatial answer. It is used to reposition, slip committed attacks, and create survival space.
- `Parry` is the timing answer. It is used against eligible attacks when the player chooses to meet danger precisely instead of escaping it.

These answers must feel different in purpose and emotional texture. Dodge should feel like controlled displacement and survival through positioning. Parry should feel like deliberate timing and composure under pressure.

Failure must also be readable. If the player is punished, they should be able to understand whether they acted too early, acted too late, chose the wrong answer, or misjudged spacing. Defensive failure should teach, not confuse.

### 6.3 Counter

Correct defensive play opens a short counter window. This opening is the reward for reading correctly, not a default state of the fight. The counter should feel earned, sharp, limited, and satisfying. It should create a burst of release after the tension of observation and defense.

In M0, the counter should remain a short offensive answer rather than expanding into a long combo chain. The goal is to reward correct reading with a clean, expressive burst, not to transform the fight into sustained combo pressure.

Button mashing should not guarantee counter success. The player should feel that they created the opening through timing and interpretation, then capitalized on it with discipline.

### 6.4 Reveal

A successful combat exchange triggers a minimal reveal or memory response. For M0, this does not need to become a full narrative progression system. It only needs to prove that combat outcome is connected to the identity of the game.

Possible M0 reveal responses include:

- brief visual distortion
- enemy hesitation
- memory shimmer
- debug-visible reveal state
- small change in enemy rhythm
- short feedback beat

The important design goal is that the player understands that successful combat interpretation leads to some form of truth exposure, however small. Combat is not isolated from the mystery; it is one of the ways the game reveals it.

### 6.5 Loop Variants

The loop should support the following M0 variants:

- `read → dodge → counter`
- `read → parry → counter`
- `read → fail defensive answer → hit reaction / recovery`
- `read → attack at the wrong time → punished`
- `counter success → minimal reveal response`

These variants are important because M0 is not only testing success states. It is also testing whether failure states remain understandable and whether success meaningfully changes the emotional tone of the exchange.

### 6.6 Loop Timing Philosophy

The loop should follow a clear timing philosophy:

- calm observation first
- short violent answer
- recovery or disengage
- re-read
- no endless pressure

This philosophy keeps combat aligned with `Melancholic Elegance`. The fight should breathe. It should not become a constant stream of offense, noise, or visual clutter. Each successful exchange should create a moment of punctuation before the next reading phase begins.

### 6.7 M0 Success Criteria

A tester should be able to describe:

- what the enemy was about to do
- what answer they chose
- whether the answer was correct
- when the counter window opened
- what reveal feedback occurred

If a tester cannot explain those elements after repeated duel attempts, then the loop is not yet clear enough for M0.

### 6.8 Anti-Patterns

The following outcomes indicate that the loop is failing its purpose:

- enemy attacks with no readable intent
- parry spam solving everything
- dodge spam solving everything
- counter window too long
- attacks cancelling all risk
- reveal feedback obscuring enemy intent
- camera or VFX making the read unclear

These anti-patterns are especially dangerous in M0 because they can create the illusion of combat depth while actually undermining readability, fairness, and emotional interpretation.

## 7. Combat State Model

Combat Core for M0 should be built around an explicit player-facing combat state model. The purpose of this model is to make combat truth inspectable, frame-readable, and easy to tune. States represent gameplay truth, not just presentation. Animation may reflect these states, but animation must not own them. `R3` may observe state changes for debug or UI visibility, but must not drive hot combat transitions. Camera, UI, and VFX may observe combat state, but must not own combat rules.

### 7.1 State Intent

The M0 state model exists to support a readable duel rhythm: observation, commitment, vulnerability, response, and recovery. It should stay narrow and understandable. The goal is not to define a highly cancellable character-action framework at this stage, but to establish a small set of states that clearly explain what the player can do, when they are vulnerable, and why an opening exists.

### 7.2 Provisional Player Combat States

#### Neutral

The default combat-ready state. The player can move, face target, attack, dodge, or parry. This is the primary reading state where the player observes enemy intent and chooses a response.

#### AttackStartup

The player has committed to an attack, but the hit is not active yet. This is a committed pre-impact phase and should generally be vulnerable or partially committed. M0 should keep cancel behavior simple and limited.

#### AttackActive

The attack hit window is active. Hit resolution may occur in this state.

#### AttackRecovery

The attack has finished, but the player has not yet fully returned to `Neutral`. This state is punishable when the attack is used at the wrong time.

#### DodgeStartup

The player begins an evade action, but the avoidance window is not yet active.

#### DodgeActive

The active spatial avoidance window. This may later be implemented through invulnerability, displacement, or a hybrid solution, but the GDD only requires that it functions as the player’s spatial defensive answer.

#### DodgeRecovery

The evade action is ending. The player is returning to `Neutral`, or may transition into `CounterWindow` if the dodge created a valid opening.

#### ParryStartup

The player begins a parry action. This may be a very short startup before the active timing window begins.

#### ParryActive

The precise timing window during which eligible enemy attacks may be parried.

#### ParryRecovery

The recovery after a failed, mistimed, or expired parry. This state should be punishable if the player spams parry or chooses it carelessly.

#### CounterWindow

A short opportunity state opened by successful dodge/parry resolution or by a readable punish opportunity on the enemy. The player may trigger a counter during this state. This state should be brief and meaningful rather than generous.

#### CounterActive

The counter attack is executing. This should be a short, sharp burst rather than a long combo continuation.

#### HitReact

The player has been hit or staggered and temporarily loses control.

#### Downed / Disabled

This is optional for M0 and should remain provisional only if needed by the prototype. It should not be treated as core M0 scope unless the basic duel loop genuinely requires it.

#### RevealBeat

A very short reveal-linked state or overlay state that may occur after successful counter resolution if needed. This should not become a long cutscene or a pacing break. It may later be represented as an event instead of a hard combat state.

### 7.3 Transition Principles

The M0 transition model should remain explicit and easy to reason about.

- `Neutral` can enter `AttackStartup`, `DodgeStartup`, or `ParryStartup`
- `AttackStartup → AttackActive → AttackRecovery → Neutral`
- `DodgeStartup → DodgeActive → DodgeRecovery → Neutral` or `CounterWindow`
- `ParryStartup → ParryActive → ParryRecovery` or `CounterWindow`
- `CounterWindow → CounterActive` or expires to `Neutral`
- `CounterActive → RevealBeat/event → Recovery/Neutral`
- Any vulnerable state may enter `HitReact` if hit
- `HitReact → Recovery/Neutral`

The core design goal is that every major transition should have a readable cause. The player should understand why they entered a punishable state, why a counter became available, or why they lost control after being hit.

### 7.4 State Categories

To help later implementation and debugging, the states should be understood in functional groups rather than as a flat list.

#### Control States

- `Neutral`

These are states where the player retains broad decision-making freedom.

#### Commitment States

- `AttackStartup`
- `AttackActive`
- `AttackRecovery`
- `DodgeStartup`
- `DodgeActive`
- `DodgeRecovery`
- `ParryStartup`
- `ParryActive`
- `ParryRecovery`
- `CounterActive`

These are states where the player has already chosen an action and is living with its consequences.

#### Vulnerability States

- `AttackStartup`
- `AttackRecovery`
- `ParryRecovery`
- `HitReact`
- optional `Downed / Disabled`

These are states where poor timing or poor reads should be punishable.

#### Timing-Window States

- `AttackActive`
- `DodgeActive`
- `ParryActive`
- `CounterWindow`
- `CounterActive`

These are the states most relevant to combat readability and tuning.

#### Presentation / Event Overlay States

- `RevealBeat`

These states or overlays exist to communicate meaning and feedback without becoming the source of combat truth.

### 7.5 Required Debug Exposure

For M0 tuning, the state model should expose enough information that the team can understand why a duel feels good or bad.

The model should make the following observable:

- current player state
- previous state
- time in current state
- active timing window
- whether the player can currently receive input
- whether the player can currently be hit
- whether the player can currently parry
- whether the player can currently counter
- current action source: attack, dodge, parry, counter, hit, or reveal

This information is important because Combat Core is a feel-sensitive system. If the state model cannot be inspected, tuning will drift toward guesswork.

### 7.6 Anti-Patterns

The following patterns should be treated as design failures for M0:

- animation controller owns combat truth
- hidden transition rules
- reactive chains driving hot transitions
- too many cancel rules in M0
- counter becoming available without a readable cause
- state names based only on animation clip names

These anti-patterns make combat harder to reason about and easier to mis-tune. The point of the state model is clarity, not hidden complexity.

### 7.7 Open Questions

The following questions remain intentionally unresolved at this stage:

- Does successful dodge open a counter only for specific attacks, or more broadly for any correctly avoided committed strike?
- Does parry have a short startup, or does it become active immediately on input?
- Is `RevealBeat` a real combat state, or should it remain an event or overlay outside the main state graph?
- Does `CounterWindow` belong entirely to the player state model, or is part of its truth owned by enemy vulnerability or encounter context?
- Should `Downed / Disabled` exist in M0 at all, or remain completely outside the first duel prototype?

## 8. Player Action Set

The M0 player action set defines the minimum combat verbs required to prove the duel loop of `read → evade/parry → counter → reveal`. These actions are not intended to represent the final breadth of `Glass Refrain`'s combat. They are the smallest set of player-facing tools needed to test readability, defensive decision-making, short punish windows, and emotionally coherent combat flow.

### 8.1 Combat Movement / Reposition

The purpose of combat movement is to allow the player to maintain spacing, support enemy-intent reading, and keep the duel feeling controlled and dance-like. Movement is part of combat interpretation, not just traversal. The player should be able to reposition around danger, adjust distance, and stay in a readable relationship to the enemy.

For M0, Combat Core only defines what combat needs from movement. Full locomotion mechanics, acceleration details, and broader movement architecture belong to the later `Player Locomotion` GDD.

### 8.2 Light Attack

The light attack is the fast, low-commitment attack in M0. Its purpose is to act as a basic pressure tool and a clean punish for smaller openings without overwhelming the defensive identity of the system.

M0 expectations:

- short startup
- short active window
- short recovery
- low damage or low stagger compared with heavy attack
- does not create long combo chains

The light attack should feel useful, but it must not dominate the loop or replace the need to read properly.

### 8.3 Heavy Attack

The heavy attack is the slower, more committed attack in M0. Its purpose is to provide a stronger punish or a more deliberate answer after a successful read. It should feel weightier and more consequential than light attack.

M0 expectations:

- longer startup than light attack
- stronger damage or stronger hit reaction than light attack
- more punishable on whiff
- rewards correct timing rather than repeated use

Heavy attack should feel deliberate. It exists to reinforce that commitment matters.

### 8.4 Dodge / Evade

The dodge or evade action is the player's spatial defensive answer. Its purpose is to reposition around danger, avoid committed enemy attacks, and potentially create a counter opportunity when used correctly.

M0 expectations:

- has startup, active, and recovery phases
- may later use invulnerability, hurtbox displacement, or a hybrid solution
- should not solve every attack automatically
- spam dodge should be punishable through recovery or bad repositioning

The dodge should feel like a spatial answer rather than a universal panic button.

### 8.5 Parry

Parry is the player's precise timing defensive answer. Its purpose is to reward correct reading and strong timing with a sharper counter opportunity than dodge.

M0 expectations:

- has a clear active window
- failure is punishable
- not every enemy attack must be parry-eligible
- parry should not be spammable
- parry success should be clear through feedback and debug visibility

Parry should feel higher-risk and more timing-dependent than dodge.

### 8.6 Counter

Counter is the short, satisfying reward after correct defensive play. Its purpose is to express the emotional arc of `read → answer → punish` and connect successful interpretation to the reveal identity of the game.

M0 expectations:

- available only from `CounterWindow`
- short burst rather than a long combo chain
- should feel earned
- should not be available through random mashing

Counter is the emotional and mechanical reward beat of the loop.

### 8.7 Lock-On Toggle / Target Focus

Target focus exists to support duel readability, player facing, and combat camera framing. It helps the player maintain a readable relationship to the enemy so intent is easier to follow.

For M0, Combat Core only defines the need for target focus as part of readable dueling. The full behavior and ownership of lock-on belongs to the existing `Lock-On / Target Context` and `Lock-On & Combat Camera` contracts.

### 8.8 Basic Hit Reaction / Recovery

Basic hit reaction and recovery communicate failure, interrupt player control briefly, and return the player to a readable state. This action space is important because the player must understand not only successful defense, but also the consequences of wrong timing or wrong answers.

M0 expectations:

- short and clear
- not excessively punitive during early feel testing
- sufficient to communicate that the player lost control because of a readable mistake

The full health and damage system remains deferred; M0 only needs a clear and consistent response to being hit.

### 8.9 Action Priority Philosophy

The action set should follow a clear priority philosophy:

- defensive answers matter more than attack spam
- light and heavy attacks are tools, not the main proof target
- counter is the emotional and combat reward
- movement and spacing are part of reading, not just locomotion

This philosophy protects the system from drifting into aggression-first combat before the reactive duel identity is proven.

### 8.10 Provisional Action Table

| Action | Input Intent | Primary Purpose | Enters State | Can Open Counter? | M0 Notes |
|--------|--------------|-----------------|--------------|-------------------|----------|
| Combat Movement / Reposition | Move / face / maintain space | Readability, spacing, controlled duel flow | `Neutral` | Indirectly | Supports reading and defense; detailed locomotion owned later |
| Light Attack | Fast basic attack | Small punish, low-commitment pressure | `AttackStartup` | No direct opening | Should stay short, simple, and non-dominant |
| Heavy Attack | Deliberate committed attack | Stronger punish, stronger consequence | `AttackStartup` | No direct opening | More punishable on whiff than light |
| Dodge / Evade | Spatial defense | Avoid committed attacks, reposition | `DodgeStartup` | Potentially | Opens counter only when used correctly and context allows |
| Parry | Timing defense | Precise answer to eligible attacks | `ParryStartup` | Yes | Higher-risk than dodge; must be readable and punishable on failure |
| Counter | Reward action | Short, satisfying punish after correct defense | `CounterActive` | N/A | Available only from `CounterWindow` |
| Lock-On Toggle / Target Focus | Target attention / facing support | Duel readability and target framing | `Neutral` support behavior | No direct opening | Full lock-on rules belong to later system design |
| Basic Hit Reaction / Recovery | Result of being hit | Communicate failure and loss of control | `HitReact` | No | Must be short, clear, and readable |

### 8.11 Explicit Exclusions

The following actions or action families are explicitly out of scope for M0:

- launcher system
- air combo depth
- stance switching
- weapon switching
- charged skills
- special abilities
- ultimate attacks
- animation cancel tree
- perfect dodge variants beyond a simple counter-opening rule
- execution finishers

These exclusions exist to keep M0 focused on duel clarity rather than breadth.

### 8.12 Open Questions

The following questions remain unresolved for later sections:

- Can light and heavy attacks chain into a very short two-hit string, or should M0 remain purely single-commitment per opening?
- Does dodge success open counter directly, or only against specific enemy attacks and punishable commitments?
- Does parry have a startup, or does it become active immediately?
- Is counter a dedicated input, or a contextual attack from the same offensive input set?
- Is lock-on required for counter readability in M0, or only helpful?

## 9. Timing Windows

Timing windows are the backbone of M0 combat readability. They define when actions begin, when they can succeed, when they become punishable, and how the player learns the rhythm of the duel. For M0, timing windows should be described in provisional, inspectable categories rather than fixed final frame counts. Final values must be tuned through playtesting.

### 9.1 Startup Window

The startup window is the period where an action has begun but its main effect is not yet active.

Used by:

- light attack startup
- heavy attack startup
- dodge startup
- parry startup if used
- enemy attack windup

Design purpose:

- communicates commitment
- creates readability
- creates punishable mistakes
- prevents instant, spammy actions

Startup is one of the main ways the system communicates intent. If startup is unreadable or absent, the duel becomes harder to interpret and easier to spam.

### 9.2 Active Window

The active window is the period where the action’s main effect is currently valid.

Used by:

- attack hit frames
- dodge avoidance or invulnerability
- parry active frames
- counter hit frames
- enemy attack hit frames

Design purpose:

- defines when the action can actually succeed
- should be visible in the debug overlay
- should match animation and feedback as closely as possible

This is the part of the action where combat truth and presentation must align most clearly.

### 9.3 Recovery Window

The recovery window is the period after the main effect has resolved but before the actor is fully back in `Neutral`.

Used by:

- attack recovery
- dodge recovery
- parry recovery
- counter recovery
- enemy punish window

Design purpose:

- creates risk
- prevents spam
- gives the opponent or player a readable answer window

Recovery is essential for making commitment meaningful. Without it, the duel loses tension and the system drifts toward mindless repetition.

### 9.4 Parry Window

The parry window is the precise timing period during which eligible enemy attacks can be parried.

Design purpose:

- rewards timing and reading
- should be short enough to feel precise
- should not be so strict that M0 becomes frustrating before tuning
- failed parry should lead into recovery

Parry should feel like a timing answer, not a broad defensive blanket.

### 9.5 Dodge Avoidance Window

The dodge avoidance window is the period where dodge actually avoids damage, whether through spacing, hurtbox movement, provisional invulnerability, or a hybrid solution.

Design purpose:

- rewards the spatial defensive answer
- should not solve every attack
- may open counter only under clearly defined conditions

Dodge should feel useful and dependable, but not universal.

### 9.6 Counter Window

The counter window is the short response period created by successful defense or a readable enemy punish opportunity.

Design purpose:

- makes correct reading feel rewarded
- should be short and clear
- should not be available without cause
- should be visible in the debug overlay

This window is the mechanical bridge between defense and reward. If it is unclear, the emotional core of the loop weakens.

### 9.7 Enemy Telegraph Window

The enemy telegraph window is the readable pre-impact phase where enemy intent is communicated.

Design purpose:

- supports the `Read` phase
- gives the player fair warning
- must align with enemy animation, VFX, audio, or movement rhythm

This window is one of the most important tuning surfaces in M0 because readable enemy intent is more important than early difficulty.

### 9.8 Reveal Beat Window

The reveal beat window is a short post-counter feedback beat where memory or reveal response occurs.

Design purpose:

- connects combat outcome to game identity
- must not obscure the next enemy read
- should be short and restrained

The reveal beat should punctuate success without breaking the duel rhythm.

### 9.9 Provisional Tuning Philosophy

M0 timing windows should be tuned with readability first and challenge second.

Recommended tuning approach:

- start generous, then tighten after playtesting
- prioritize readability before challenge
- tune enemy telegraph before player strictness

Recommended tuning order:

1. enemy telegraph readability
2. dodge and parry feel
3. counter window satisfaction
4. recovery punishability
5. reveal beat length

This order matters because if the enemy read is unclear, no amount of timing strictness will make the duel feel fair.

### 9.10 Debug Requirements

The debug overlay should expose:

- current state
- time in current state
- active window type
- parry active
- dodge active
- counter available
- enemy telegraph active
- enemy punish window active
- reveal beat active

Timing windows must be observable during tuning so the team can diagnose whether a problem comes from readability, strictness, duration, or bad alignment between animation and combat truth.

### 9.11 Provisional Timing Table

| Window | Applies To | Purpose | M0 Tuning Direction | Debug Requirement |
|--------|------------|---------|---------------------|-------------------|
| Startup Window | Player attacks, dodge, parry, enemy attacks | Communicate commitment and prevent instant actions | Start readable and slightly generous | Show startup state and time in state |
| Active Window | Player hits, dodge avoidance, parry, counter, enemy hits | Define when action can actually succeed | Align tightly with presentation and readability | Show active window type and active duration |
| Recovery Window | Player attacks, dodge, parry, counter, enemy punishability | Create risk and prevent spam | Keep long enough that mistakes are punishable | Show recovery state and time remaining if useful |
| Parry Window | Eligible enemy attacks vs player parry | Reward timing and reading | Start learnable, then tighten if too forgiving | Show parry-active on/off |
| Dodge Avoidance Window | Dodge vs enemy attacks | Reward spatial defense | Keep useful but not universal | Show dodge-active on/off |
| Counter Window | Successful defense or punish opportunity | Create earned offensive reward | Keep short, clear, and cause-based | Show counter-available on/off |
| Enemy Telegraph Window | Enemy pre-impact behavior | Support reading and fair warning | Tune first before player strictness | Show telegraph-active on/off |
| Reveal Beat Window | Post-counter reveal response | Connect combat to identity | Keep short and non-obscuring | Show reveal-beat active |

### 9.12 Anti-Patterns

The following tuning outcomes should be treated as failures:

- instant attacks with no startup
- active windows that do not match animation
- recovery so short that spam becomes optimal
- parry window so wide that it solves everything
- parry window so strict that it cannot be learned
- dodge invulnerability so long that it replaces reading
- counter window too long
- reveal beat hiding the next threat
- tuning difficulty before readability

### 9.13 Open Questions

The following timing questions remain unresolved:

- Does parry have startup, or does it become active immediately?
- Does dodge use invulnerability frames, hurtbox displacement, or both?
- Is enemy punish window owned by enemy state, player `CounterWindow`, or shared interaction context?
- Does counter window duration change depending on whether it came from dodge or parry?
- Does reveal beat pause combat briefly, or play while combat continues?

## 10. Attack / Dodge / Parry / Counter Rules

This section defines the provisional M0 rules for the four core combat answers: `Attack`, `Dodge`, `Parry`, and `Counter`. The goal is to make the duel loop readable and teachable, not to establish a full long-term ability framework. Final timing values and tuning details remain provisional and should be refined through playtesting.

### 10.1 Attack Rules

#### Light Attack

The light attack is the fast, low-commitment offensive option in M0. Its purpose is to punish smaller openings and apply controlled pressure after a correct read. It should feel useful without becoming the dominant answer to all enemy pressure.

M0 rules:

- fast and low-commitment relative to heavy attack
- used to punish small openings
- should not be the main solution to enemy pressure
- can be interrupted or punished if used at the wrong time
- may be allowed as a very short one-to-two hit string, but no large combo tree

The light attack should support the loop without replacing defense and timing.

#### Heavy Attack

The heavy attack is the slower, more committed offensive option in M0. Its purpose is to reward larger openings or serve as a stronger follow-up after a successful read or counter opportunity.

M0 rules:

- slower and more committed than light attack
- used for larger punish windows or stronger follow-up
- should produce stronger feedback than light attack
- more punishable on whiff
- should feel deliberate rather than spammable

Heavy attack should communicate commitment and consequence.

#### Attack Failure Cases

Attacking at the wrong time should create understandable risk.

Failure cases include:

- attacking during active enemy threat and getting hit
- whiffing because of poor spacing and becoming punishable in recovery
- attacking without reading and losing to committed enemy action

Attacks should reward timing, not impatience.

### 10.2 Dodge Rules

Dodge is the player's spatial defensive answer.

Purpose:

- avoid committed enemy attacks
- reposition for counter opportunity
- preserve dance-like combat rhythm

M0 rules:

- dodge has startup, active, and recovery
- dodge success requires timing and/or spacing
- dodge should not solve every attack
- dodge spam should be punishable
- dodge may open `CounterWindow` only when the enemy attack is committed and missed, or when the design marks the attack as dodge-punishable

#### Dodge Failure Cases

Failure cases include:

- dodged too early
- dodged too late
- dodged into danger
- dodged an attack that required parry or stronger spacing discipline
- got punished during recovery

Dodge should feel reliable when used correctly, but not universal.

### 10.3 Parry Rules

Parry is the player's timing defensive answer.

Purpose:

- reward precise reading
- interrupt or deflect eligible enemy attacks
- create a sharp counter opportunity

M0 rules:

- parry only works during `ParryActive`
- not all attacks must be parry-eligible
- failed parry enters `ParryRecovery`
- parry spam should be punishable
- parry success should clearly open `CounterWindow`
- parry feedback must be readable in animation, sound, VFX, and debug overlay

#### Parry Failure Cases

Failure cases include:

- parried too early
- parried too late
- attempted parry against a non-parryable attack
- got punished during recovery

Parry should feel like a precise, high-trust answer rather than a universal shield.

### 10.4 Counter Rules

Counter is the reward after correct defensive reading.

Purpose:

- make correct defense feel earned
- deliver short, sharp satisfaction
- connect combat success to reveal or memory response

M0 rules:

- counter is only available during `CounterWindow`
- counter should be a short burst, not a combo chain
- counter should not be available from neutral mashing
- counter success may trigger `RevealBeat` or a minimal memory response
- counter can use a contextual input or dedicated input; final choice remains open
- counter should have clear hit confirmation

#### Counter Failure Cases

Failure cases include:

- player misses the `CounterWindow`
- counter whiffs due to poor spacing
- counter is attempted without a valid opening
- counter is interrupted if used carelessly after the window expires

Counter should feel like a clean reward for correct interpretation, not a default offensive state.

### 10.5 Defensive Answer Philosophy

The M0 defensive answer philosophy is intentionally simple:

- `dodge` = spatial answer
- `parry` = timing answer
- `counter` = reward answer
- `attack` = pressure and punish tool, not the core defensive solution

This distinction is critical to the identity of the duel loop. If dodge, parry, and attack blur into one generic answer space, the system loses its interpretive clarity.

### 10.6 Provisional Rule Table

| Action | Success Condition | Failure Condition | Opens Counter? | M0 Notes |
|--------|-------------------|------------------|----------------|----------|
| Light Attack | Used during a real opening and connects cleanly | Used during threat, whiffs, or overcommits into recovery | No direct opening | May allow a very short string, but not a combo tree |
| Heavy Attack | Used during a larger opening or stronger punish moment | Whiffs, is too slow, or is used without a read | No direct opening | Stronger feedback, higher commitment |
| Dodge / Evade | Avoids a committed attack through timing and/or spacing | Too early, too late, poor direction, recovery punish | Sometimes | Opens counter only when conditions justify it |
| Parry | Occurs during `ParryActive` against an eligible attack | Too early, too late, wrong attack type, recovery punish | Yes | Higher precision answer than dodge |
| Counter | Used during valid `CounterWindow` and connects | Missed timing, bad spacing, no valid opening, expired window | N/A | Short burst reward, not a combo extension |

### 10.7 Attack Eligibility Tags

For later enemy-facing system design, M0 should use simple provisional attack tags to express how enemy attacks interact with player defensive answers.

- `DodgePunishable`
  - The attack may open a counter if correctly dodged
- `ParryEligible`
  - The attack may be parried during `ParryActive`
- `Unparryable`
  - The attack cannot be parried and should demand another answer
- `SpacingCheck`
  - The attack is primarily answered through spacing or repositioning discipline
- `CounterOnWhiff`
  - A missed committed attack may open a punish window
- `CounterOnParry`
  - A successful parry on this attack explicitly opens counter opportunity

These tags are intentionally simple and provisional. Their purpose is clarity, not exhaustive combat taxonomy.

### 10.8 Anti-Patterns

The following outcomes indicate that the rules are failing M0 goals:

- light attack spam beats enemy pressure
- dodge solves every enemy attack
- parry solves every enemy attack
- counter becomes available without readable cause
- heavy attack becomes optimal in all situations
- the difference between dodge and parry is unclear
- enemy attacks lack eligibility clarity
- reveal triggers from random damage instead of a meaningful exchange

These anti-patterns reduce the system's interpretive depth and should be treated as tuning or design failures.

### 10.9 Open Questions

The following rule questions remain unresolved:

- Is counter a contextual attack, or a dedicated counter input?
- Are dodge-counter and parry-counter the same move, or distinct reward responses?
- Can light attack chain into heavy attack in M0, or should each punish stay one-step simple?
- Do enemy attacks require explicit eligibility tags in authored data from the start?
- Do `Unparryable` attacks need a special visual language?
- Does counter success always trigger reveal progress, or only on specific enemies or windows?

## 11. Hit Resolution

Hit resolution is where Combat Core decides what actually happened in an exchange. For M0, this must remain explicit, authoritative, and debuggable. Animation, VFX, camera, and audio may present the result, but they must not decide the result. There should be one clear hit-resolution path in M0 so that designers and testers can understand why a hit, parry, dodge, counter, or reveal occurred.

### 11.1 Hit Resolution Authority

Combat Core owns the authoritative decision for:

- whether an attack hit
- whether the target was vulnerable
- whether the defender was in dodge active, parry active, or counter-eligible context
- whether the hit is blocked, parried, or evaded
- whether hit reaction should trigger
- whether `CounterWindow` should open
- whether a minimal `RevealBeat` should trigger

Presentation systems own:

- animation feedback
- VFX feedback
- camera impulse
- audio response
- UI and debug display

The purpose of this split is to keep combat truth inspectable and stable. Presentation should communicate the result, not determine it.

### 11.2 Basic M0 Resolution Outcomes

#### PlayerAttackHitsEnemy

This occurs when the player’s attack active frames overlap a valid enemy hurt target while the enemy is vulnerable.

Result:

- enemy receives basic hit reaction
- optional stagger or interrupt may occur if the authored attack behavior allows it

This is the standard successful offensive result for player attacks.

#### PlayerAttackWhiffs

This occurs when the player’s attack active frames find no valid target.

Result:

- player enters normal recovery
- whiff may be punishable

Whiffing should be a readable consequence of poor spacing or bad timing.

#### EnemyAttackHitsPlayer

This occurs when the enemy’s attack active frames overlap the player while the player is vulnerable and has not successfully resolved dodge or parry.

Result:

- player enters `HitReact`
- debug records hit source and timing

This is the standard punishment for failed defensive reading.

#### EnemyAttackWhiffs

This occurs when the enemy attack misses because of spacing, dodge, or positional failure.

Result:

- enemy enters recovery or punish window if the attack is authored that way
- may open `CounterWindow` if the attack is marked `DodgePunishable` or `CounterOnWhiff`

This outcome is important because dodge should create opportunity only when it meaningfully defeated a committed threat.

#### PlayerParrySucceeds

This occurs when the player is in `ParryActive`, the enemy attack is `ParryEligible`, and the timing overlaps a valid parry check.

Result:

- enemy attack is deflected or interrupted
- `CounterWindow` opens

Parry success should be a sharp, unambiguous event.

#### PlayerParryFails

This occurs when the parry is too early, too late, or the attack is not eligible for parry.

Result:

- player enters `ParryRecovery`
- player may still be hit if the enemy active frames connect

Failed parry should feel readable and punishable without becoming arbitrary.

#### PlayerDodgeSucceeds

This occurs when the player avoids the enemy active hit through spacing, hurtbox movement, provisional invulnerability, or a hybrid approach.

Result:

- player avoids the hit
- if the enemy attack is `DodgePunishable` or `CounterOnWhiff`, `CounterWindow` may open

Successful dodge should be meaningful, but not every dodge should automatically become offense.

#### PlayerDodgeFails

This occurs when dodge timing or spacing is wrong.

Result:

- player is hit or left exposed to recovery risk

Failure should remain understandable in terms of timing, positioning, or wrong-answer selection.

#### PlayerCounterHits

This occurs when the player triggers counter during `CounterWindow` and the counter connects with a valid target.

Result:

- enemy receives stronger hit feedback or stronger hit reaction
- minimal `RevealBeat` or memory response may trigger

This is the signature success beat of the M0 duel loop.

#### PlayerCounterWhiffs

This occurs when the player triggers counter during a valid window but misses the target.

Result:

- player enters counter recovery
- no reveal response occurs

Counter should still respect spacing and timing, even when correctly unlocked.

### 11.3 Vulnerability Rules

The following vulnerability rules are provisional and should remain visible during tuning:

- `Neutral`: vulnerable
- `AttackStartup`: vulnerable
- `AttackActive`: usually vulnerable unless future authored attack data says otherwise
- `AttackRecovery`: vulnerable
- `DodgeStartup`: vulnerable
- `DodgeActive`: protected only by authored avoidance, invulnerability, or spatial movement rules
- `DodgeRecovery`: vulnerable
- `ParryStartup`: vulnerable unless M0 later chooses effectively instant active parry
- `ParryActive`: protected only against eligible parry checks
- `ParryRecovery`: vulnerable
- `CounterWindow`: vulnerable unless otherwise authored
- `CounterActive`: may be vulnerable or partially protected; keep provisional for M0
- `HitReact`: already resolving a hit, usually cannot be hit again unless later rules explicitly allow it
- `RevealBeat`: should avoid unfair incoming hits if it briefly interrupts control; exact rule remains open

These rules should remain simple enough that testers can explain them after repeated duel attempts.

### 11.4 Damage / Reaction Philosophy

For M0, damage and reaction should stay simple.

- no final RPG damage formula
- use simple provisional damage and reaction categories
- focus on readability and feel, not numeric balance
- hit reaction should communicate success and failure clearly
- heavy and counter should feel stronger than light, but do not need final values
- avoid juggling, long stun locks, and complex poise rules

Provisional reaction categories:

- `LightHitReact`
- `HeavyHitReact`
- `ParryStagger`
- `CounterStagger`
- `PlayerHitReact`

The point of M0 is to make combat outcomes legible and satisfying, not numerically deep.

### 11.5 Debug Requirements

The debug overlay should show:

- attacker
- defender
- attempted action
- resolution result
- active state at the moment of resolution
- attack tag or eligibility tag
- whether the defender was vulnerable
- whether parry was active
- whether dodge was active
- whether `CounterWindow` opened
- whether `RevealBeat` triggered

This debug surface is necessary because the duel loop depends on readable cause and effect.

### 11.6 Provisional Resolution Table

| Situation | Required Conditions | Result | CounterWindow? | RevealBeat? | M0 Notes |
|-----------|---------------------|--------|----------------|-------------|----------|
| PlayerAttackHitsEnemy | Player attack active, valid enemy hurt target, enemy vulnerable | Enemy takes hit reaction, possible authored interrupt | No | No | Standard player punish result |
| PlayerAttackWhiffs | Player attack active, no valid target | Player recovers, may be punishable | No | No | Whiff should create readable risk |
| EnemyAttackHitsPlayer | Enemy attack active, player vulnerable, no valid defense resolution | Player enters `HitReact` | No | No | Standard punishment for failed read |
| EnemyAttackWhiffs | Enemy attack misses via spacing or dodge | Enemy recovers, may become punishable | Sometimes | No | May open `CounterWindow` if tags allow |
| PlayerParrySucceeds | Player in `ParryActive`, attack `ParryEligible`, valid timing overlap | Attack deflected/interrupted | Yes | No | Sharp success event |
| PlayerParryFails | Mistimed parry or invalid target attack | Player enters `ParryRecovery`, may be hit | No | No | Must stay readable and punishable |
| PlayerDodgeSucceeds | Player avoids valid hit through spacing/avoidance rules | Hit avoided | Sometimes | No | Counter only opens when authored conditions allow |
| PlayerDodgeFails | Wrong timing or spacing | Player hit or left exposed | No | No | Failure should be understandable |
| PlayerCounterHits | Player uses counter during valid `CounterWindow`, valid target connects | Stronger enemy reaction, success beat | N/A | Sometimes | Primary reward beat of loop |
| PlayerCounterWhiffs | Counter triggered but misses | Counter recovery only | N/A | No | Counter still respects spacing |

### 11.7 Anti-Patterns

The following patterns should be treated as failures:

- multiple systems deciding hit results
- animation events directly applying damage without Combat Core validation
- VFX or camera triggering gameplay results
- hidden invulnerability rules
- hit reaction durations that obscure readability
- counter triggering from random damage
- reveal triggering from meaningless hits
- complex damage math before feel is proven
- physics chaos deciding combat outcome

These anti-patterns weaken the trustworthiness of the duel loop.

### 11.8 Open Questions

The following questions remain unresolved for M0:

- Does M0 use hitboxes/hurtboxes, distance checks, or a hybrid check model?
- Does `CounterActive` grant any protection?
- Does `RevealBeat` pause combat, or only play as feedback while combat continues?
- Can enemies be interrupted by light attacks, or only by heavier authored conditions?
- Can the player be hit during `CounterWindow`?
- Do hit reactions use fixed duration or data-authored duration?
- Is dodge success determined by avoided hit, spatial position, enemy whiff state, or a combination?

## 12. Health / Damage / Hit Reaction Provisional Contract

This section defines the minimum contract Combat Core needs from the future `Health / Damage / Hit Reaction` system in order to function during M0. It is a provisional integration boundary, not a full combat-stat design. The purpose of this contract is to preserve readability, clear outcomes, and fast iteration while avoiding premature expansion into RPG math.

### 12.1 Contract Purpose

Combat Core needs the `Health / Damage / Hit Reaction` layer to answer the following questions:

- can this target receive a hit?
- what basic reaction should play?
- is the target interrupted?
- does the hit create stagger?
- should the actor enter `HitReact`?
- is the actor defeated or still active?

For M0, the priority is readability and feel, not numeric balance. The contract exists so that Combat Core can resolve meaningful outcomes without also owning a full health and damage system.

### 12.2 Minimum Required Concepts

#### Health

M0 needs a simple health concept, whether represented as a current/max value or another lightweight placeholder health model.

Requirements:

- enough to know whether the player or enemy can continue
- enough to know when a target is defeated or disabled
- no final progression scaling

#### Damage Event

Combat Core should be able to emit a simple damage or hit event containing:

- attacker
- defender
- source action
- hit type
- provisional damage amount or category
- reaction category
- optional tags

The purpose of this event is to carry enough truth that downstream systems can respond clearly without re-deciding what happened.

#### Hit Type

M0 should support the following provisional hit types:

- `LightHit`
- `HeavyHit`
- `CounterHit`
- `EnemyHit`
- `ParryStagger`
- `EnvironmentalHit` as optional future-only concept

#### Reaction Category

M0 should support the following provisional reaction categories:

- `NoReaction`
- `LightHitReact`
- `HeavyHitReact`
- `ParryStagger`
- `CounterStagger`
- `PlayerHitReact`
- `DefeatReact` provisional

These categories are intended to keep the prototype readable, not to express a full reaction taxonomy.

### 12.3 M0 Damage Philosophy

For M0:

- light attack should communicate contact, but stay modest
- heavy attack should feel more committed and stronger
- counter should feel clearly stronger than normal attacks
- enemy hit should clearly communicate player mistake
- damage numbers are less important than reaction clarity
- floating damage numbers are not required unless useful for debug
- no final balance values should be locked yet

The M0 prototype should prove that the duel feels understandable and satisfying. Numeric depth is secondary.

### 12.4 Hit Reaction Philosophy

Hit reaction should:

- communicate success and failure clearly
- remain short enough to preserve iteration pace
- avoid creating long stun-lock gameplay
- avoid becoming the foundation for air-juggle or combo-loop depth
- support the calm → burst → reset rhythm

Hit reaction should not:

- hide enemy intent for too long
- remove player control excessively
- create physics chaos
- depend on VFX or camera to determine gameplay result

The purpose of reaction in M0 is clarity and punctuation, not spectacle.

### 12.5 Interruption Rules

The following interruption rules should be treated as provisional M0 expectations:

- light attack may cause minor reaction, but may not interrupt all enemy attacks
- heavy attack may interrupt more clearly if the enemy is vulnerable
- counter should interrupt or stagger the enemy clearly
- parry success should cause `ParryStagger` or equivalent enemy reaction
- enemy attack should interrupt the player unless the player is protected by dodge or parry rules
- boss and elite interruption rules are deferred

These rules help preserve the difference between light pressure, committed punishment, and strong defensive reward.

### 12.6 Defeat Rules

For M0:

- enemy can reach a defeated state or simple disabled state
- player defeat can remain placeholder or reset behavior
- no full death system is required yet
- no save/load consequence is required yet
- no narrative fail-state is required yet

The prototype only needs clear resolution of whether an exchange can end the duel target.

### 12.7 Debug Requirements

The debug overlay should expose:

- attacker
- defender
- hit type
- damage category or value if used
- reaction category
- whether the target was interrupted
- whether the target entered `HitReact`
- remaining health if applicable
- defeat or disabled state if reached

This information is necessary to diagnose whether combat outcomes feel wrong because of timing, hit validation, reaction selection, or damage assumptions.

### 12.8 Contract Boundary

Combat Core owns:

- action state
- timing windows
- hit resolution decision
- whether a hit event should be sent

`Health / Damage / Hit Reaction` owns:

- health value
- damage application
- reaction category selection when not already authored by attack data
- defeat or disabled result

Presentation owns:

- animation
- VFX
- audio
- camera response
- UI display

This boundary ensures that one system decides what happened, another system applies its consequence, and presentation communicates the result without becoming the source of truth.

### 12.9 Anti-Patterns

The following patterns should be explicitly avoided in M0:

- designing full RPG formulas in M0
- adding gear scaling
- adding elemental damage
- adding poise or stagger complexity too early
- long stun locks
- ragdoll-driven combat truth
- VFX deciding damage
- animation directly applying health changes without Combat Core validation
- damage numbers becoming more important than feel

These patterns would shift the prototype away from readable duel tuning and toward premature systems complexity.

### 12.10 Open Questions

The following questions remain unresolved:

- Does M0 use numeric HP or simple hit-count health?
- Is enemy interruption authored per attack, per enemy state, or through a simpler rule set?
- Does player hit reaction cancel all queued input?
- Is counter damage expressed as a value, or mainly as a special reaction category?
- Should defeat trigger reveal feedback in M0?
- Does health live temporarily inside Combat Core for speed, or in a separate `Health / Damage` layer from the start?

## 13. Input Mapping Provisional Contract

This section defines the minimum input contract Combat Core needs from the future `Input Mapping` system for M0. Input Mapping is responsible for capturing player intent. Combat Core is responsible for deciding whether that intent is accepted based on current state, timing windows, and combat rules. Input must not own combat truth.

### 13.1 Contract Purpose

Combat Core needs `Input Mapping` to provide clean player intent for:

- movement
- camera or look
- light attack
- heavy attack
- dodge or evade
- parry
- counter
- lock-on toggle
- target switch as optional future input
- debug actions as optional tuning support

For M0, input should primarily support feel iteration and consistent testing. The system must be simple enough that testers can understand why an action happened, and why it did not.

### 13.2 Input Ownership Boundary

`Input Mapping` owns:

- action map definitions
- device bindings
- rebinding later
- raw button and axis reading
- input buffering policy only if explicitly defined later

Combat Core owns:

- whether an input is valid in the current combat state
- whether an input triggers a state transition
- whether an input is ignored, buffered, or rejected
- whether counter input is accepted during `CounterWindow`
- whether attack, dodge, or parry can interrupt or cancel the current state

Presentation owns:

- button prompts
- UI input hints
- debug display

This boundary ensures that player intention is captured externally, but gameplay truth remains inside the combat system.

### 13.3 M0 Required Inputs

#### Movement

- vector input
- primarily consumed by `Player Locomotion`
- Combat Core only needs to know that movement is available during allowed states

Movement supports reading, spacing, and repositioning, but Combat Core should not own locomotion behavior itself.

#### Look / Camera

- camera control input
- primarily owned later by the Camera system
- Combat Core should not depend on camera implementation details

Combat Core only needs this as part of the broader duel readability context, not as a direct dependency.

#### Light Attack

- requests a light offensive action
- enters `AttackStartup` if accepted
- may be ignored during committed states

#### Heavy Attack

- requests a heavier offensive action
- enters `AttackStartup` if accepted
- more committed than light attack

#### Dodge / Evade

- requests the spatial defensive answer
- enters `DodgeStartup` if accepted
- should feel responsive, but must not cancel everything in M0

#### Parry

- requests the timing defensive answer
- enters `ParryStartup` or `ParryActive` depending on later design choice
- should remain distinct from dodge in feel and purpose

#### Counter

- requests the short reward action after correct defense
- only accepted during `CounterWindow`
- may later be a contextual attack or a dedicated input; final choice remains open

#### Lock-On Toggle

- requests target focus behavior
- the existing `Lock-On / Target Context` and `Lock-On & Combat Camera` contracts own targeting truth and framing rules

Combat Core only needs to recognize this as a supported intent for duel readability.

#### Debug Toggle / Debug Step

- optional
- exists for tuning visibility only
- not part of the player-facing combat fantasy

### 13.4 Input Acceptance Philosophy

Input acceptance should remain simple and state-driven for M0.

- `Neutral` accepts movement, attack, dodge, parry, and lock-on
- `AttackStartup`, `AttackActive`, and `AttackRecovery` accept limited or no new combat inputs for M0
- dodge states accept limited or no new combat inputs except future cancel rules if later approved
- parry states accept limited or no new combat inputs except counter on success
- `CounterWindow` accepts counter input
- `HitReact` rejects player combat input
- `RevealBeat` input behavior remains provisional

M0 should avoid complex input buffering and broad cancel trees. Responsiveness should come from clean state timing and clear acceptance rules, not hidden systems that mask poor timing structure.

### 13.5 Input Buffering Policy

For M0:

- use minimal or no buffering at first
- if buffering is added, keep it short and debug-visible
- do not buffer counter outside `CounterWindow` unless explicitly approved later
- do not create fighting-game-level buffer complexity
- input buffering must not hide why actions occurred

The default M0 assumption is that clean combat feel should come from clear state windows, not from invisible forgiveness layers.

### 13.6 Provisional Input Table

| Input | Player Intent | Primary Consumer | Combat Core Acceptance Rule | M0 Notes |
|-------|---------------|------------------|-----------------------------|----------|
| Movement | Reposition, maintain spacing, stay combat-ready | Player Locomotion | Accepted in states where movement is allowed | Required for reading and spacing, but detailed locomotion is external |
| Look / Camera | Maintain view and facing context | Camera system | Not a direct Combat Core dependency | Combat Core should not depend on camera implementation |
| Light Attack | Fast punish / low-commitment offense | Combat Core | Accepted only when state allows attack commitment | Should not override defensive identity |
| Heavy Attack | Slower committed punish | Combat Core | Accepted only when state allows stronger commitment | More deliberate and riskier than light |
| Dodge / Evade | Spatial defense | Combat Core | Accepted when current state allows defensive transition | Must stay responsive without becoming universal cancel |
| Parry | Timing defense | Combat Core | Accepted when state allows parry attempt | Distinct answer from dodge |
| Counter | Reward action after correct defense | Combat Core | Accepted only during `CounterWindow` | Final input form remains open |
| Lock-On Toggle | Request target focus | `Input Mapping`, `Lock-On / Target Context`, `Lock-On & Combat Camera` | Accepted as a request, not as direct combat truth | Lock-on input intent is defined by `Input Mapping`. Target focus truth is owned by `Lock-On / Target Context`. Camera framing and readability behavior is owned by `Lock-On & Combat Camera`. `Combat Core` may observe target context if needed, but lock-on does not decide combat validity. |
| Debug Toggle / Step | Tuning visibility | Debug systems | Optional | Not part of player-facing fantasy |

### 13.7 Debug Requirements

The debug overlay should show:

- last input received
- whether the input was accepted or rejected
- rejection reason
- current combat state
- buffered input if any
- `CounterWindow` availability
- lock-on target request if relevant

This debug visibility is necessary because input feel problems are often confused with state-model or timing problems unless rejection reasons are visible.

### 13.8 Anti-Patterns

The following patterns should be treated as design failures:

- input directly changing animation without Combat Core validation
- input system owning combat rules
- hidden buffering causing surprising actions
- dodge or parry canceling every mistake
- counter input accepted outside `CounterWindow`
- lock-on required for every combat action unless intentionally designed
- overly complex action maps before M0 feel is proven

These anti-patterns make the duel harder to tune and weaken trust in the system.

### 13.9 Open Questions

The following input questions remain unresolved:

- Is counter a dedicated input, or a contextual light/heavy action during `CounterWindow`?
- Does M0 use input buffering at all?
- Can dodge or parry cancel attack recovery later, even if not allowed in the first pass?
- Is lock-on required for counter readability?
- Does parry use press, hold, or tap timing?
- Is heavy attack tap-only, with hold or charge explicitly deferred?
- Does target switching exist in M0?

## 14. Player Locomotion Provisional Contract

This section defines the minimum locomotion contract Combat Core needs from the future `Player Locomotion` system in order to support the M0 duel loop. `Player Locomotion` owns movement implementation. Combat Core owns combat state, timing, and action permission. Locomotion exists here as a support system for combat readability, spacing, facing, dodge movement, and recovery rhythm. This section does not define a full traversal or exploration movement model.

### 14.1 Contract Purpose

Combat Core needs `Player Locomotion` to support:

- combat-ready movement
- spacing control
- facing or aiming toward target
- dodge displacement or evasive movement
- movement restrictions during committed states
- recovery and disengage rhythm
- lock-on compatible movement

For M0, locomotion should make the duel feel controlled, readable, and dance-like. The player should feel capable of adjusting space intentionally rather than drifting or skating through the encounter.

### 14.2 Ownership Boundary

`Player Locomotion` owns:

- movement velocity
- acceleration and deceleration
- rotation and facing implementation
- ground movement
- dodge movement implementation
- collision or movement controller integration
- animation-facing movement parameters if needed

Combat Core owns:

- when movement is allowed
- when movement is restricted
- when dodge begins and ends as a combat state
- whether a combat action state allows locomotion influence
- whether the player is in recovery, hit react, counter, or neutral

Camera owns:

- camera-relative movement interpretation if needed
- camera framing
- lock-on camera behavior

Input Mapping owns:

- movement input vector
- look input vector

This boundary exists so that movement quality can evolve without allowing locomotion to silently become the owner of combat rules.

### 14.3 M0 Locomotion Requirements

#### Combat-Ready Movement

- player can move during `Neutral`
- movement should support reading enemy intent
- movement should not feel floaty or overly fast
- movement should allow micro-spacing around enemy attacks

M0 movement should support careful duel positioning rather than broad traversal expression.

#### Facing / Orientation

- player should face movement direction or target depending on lock-on and context
- during lock-on, player should maintain readable facing toward target
- during attack, parry, or counter, facing may be constrained or corrected

The purpose of facing in M0 is clarity. The player and enemy should remain legible to each other.

#### Spacing

- player should be able to create and close distance deliberately
- spacing should matter for dodge success, whiff punish, and counter reach
- poor spacing should be a readable failure condition

Spacing is not secondary in `Glass Refrain`. It is one of the main ways the player reads and answers danger.

#### Dodge Movement

- dodge should provide a clear spatial answer
- dodge may later use displacement, invulnerability, hurtbox adjustment, or a hybrid solution
- exact implementation is deferred
- Combat Core only requires that dodge has startup, active, and recovery phases

The locomotion layer does not need to decide combat truth. It needs to deliver the movement behavior that lets Combat Core's dodge states feel real.

#### Committed-State Movement Restrictions

- attacks should restrict movement enough to create commitment
- heavy attack should restrict movement more than light attack
- parry should restrict movement during active and recovery
- hit reaction should restrict control
- counter should feel directed and intentional

Movement restriction is part of how the duel communicates consequence and weight.

#### Recovery / Reset Rhythm

- after attack, dodge, parry, counter, or hit reaction, locomotion should help return to a readable `Neutral` state
- combat should follow `calm → burst → recovery → re-read`

Locomotion must support the pacing philosophy of the combat loop, not fight against it.

### 14.4 Provisional Movement Permissions By State

| Combat State | Movement Permission | Facing Permission | M0 Notes |
|--------------|---------------------|-------------------|----------|
| `Neutral` | Full combat movement allowed | Full facing control or target-facing support | Primary reading and spacing state |
| `AttackStartup` | Limited | Limited or guided toward target | Creates commitment before strike becomes active |
| `AttackActive` | Limited or heavily constrained | Usually constrained | Prevents attacks from becoming fully mobile pressure tools |
| `AttackRecovery` | Restricted until recovery ends | Partial or recovering | Important punishability state |
| `DodgeStartup` | Dodge-specific movement begins | Dodge-direction dependent | Transitional setup into spatial defense |
| `DodgeActive` | Dodge movement active | Usually tied to dodge direction | Main spatial avoidance phase |
| `DodgeRecovery` | Limited until reset | Partial | Prevents dodge spam from becoming dominant |
| `ParryStartup` | Limited or none | Usually constrained toward threat | Prepares timing-based defense |
| `ParryActive` | Minimal or none | Constrained | Focus remains on timing answer, not movement drift |
| `ParryRecovery` | Limited or none | Partial | Punishable if parry is mistimed or spammed |
| `CounterWindow` | Usually limited but readable | May allow target-facing correction | Short reward opportunity, not full freeform control |
| `CounterActive` | Directed and intentional | Usually aligned to target or attack direction | Should feel sharp, not loose or wandering |
| `HitReact` | None or extremely limited | Not player-controlled | Communicates loss of control |
| `RevealBeat` | Provisional | Provisional | Must not create unfair confusion; final behavior remains open |

### 14.5 Lock-On Compatibility

For M0:

- locomotion should support target-relative or camera-relative movement while locked-on
- lock-on should not be required for every combat action unless later approved
- facing should remain readable when locked-on
- strafing or side movement may be useful, but full lock-on movement design belongs to the existing `Lock-On / Target Context` and `Lock-On & Combat Camera` contracts

The important requirement is that lock-on supports readability rather than creating stiffness or over-automation.

### 14.6 Debug Requirements

The debug overlay should expose:

- current locomotion mode
- movement input vector
- current speed
- facing target or facing mode
- whether movement is allowed
- whether rotation is allowed
- whether dodge movement is active
- whether lock-on movement mode is active
- movement restriction reason

This information is important because poor combat feel is often caused by movement permission or facing logic rather than by attack timing alone.

### 14.7 Anti-Patterns

The following patterns should be treated as failures:

- locomotion deciding combat state
- movement canceling every combat commitment
- dodge movement solving every enemy attack
- floaty movement that weakens duel tension
- overly rigid movement that prevents spacing expression
- camera-owned movement rules leaking into combat
- attack animations moving the player without Combat Core and Locomotion agreement
- physics chaos determining combat spacing

These anti-patterns make spacing unreadable and weaken the emotional discipline of the duel.

### 14.8 Open Questions

The following locomotion questions remain unresolved:

- Does M0 use a character controller, Rigidbody, or custom movement controller?
- Is movement camera-relative or target-relative during lock-on?
- Is dodge direction input-relative, camera-relative, or target-relative?
- Do attacks include root motion or code-driven motion?
- Does counter auto-align to target?
- Can the player rotate during attack startup?
- Does lock-on movement use strafing from the start?

## 15. Enemy Intent Provisional Contract

This section defines the minimum contract Combat Core needs from the future `Enemy Intent & Telegraph` system in order to support M0. `Enemy Intent & Telegraph` will later own enemy behavior design in greater detail. For now, Combat Core only defines what it needs from enemy intent so that the `read → evade/parry → counter → reveal` loop can function clearly.

### 15.1 Contract Purpose

Combat Core needs `Enemy Intent & Telegraph` to provide:

- readable enemy intent before impact
- attack commitment
- telegraph timing
- attack eligibility tags
- punish windows
- parry, dodge, and counter interaction hooks
- basic enemy hit reaction support

For M0, one simple enemy is enough. The goal is not enemy variety. The goal is readable duel rhythm.

### 15.2 Ownership Boundary

`Enemy Intent & Telegraph` owns:

- enemy state selection
- enemy windup and readable tell design
- enemy attack rhythm
- enemy attack commitment
- attack eligibility tags
- punish window authoring
- emotional rhythm later

Combat Core owns:

- how player states interact with enemy attack windows
- whether player defense succeeds
- whether `CounterWindow` opens
- hit resolution rules
- player-facing combat state

Presentation owns:

- enemy animation
- telegraph VFX
- warning audio
- camera, UI, and VFX feedback

This boundary keeps enemy behavior authored on the enemy side while preserving Combat Core as the owner of player-facing combat truth.

### 15.3 M0 Enemy Requirements

#### Idle / Readable Presence

- enemy should not constantly attack
- enemy should give the player time to read
- idle and approach behavior should communicate threat without chaos

The player must feel that the enemy is present and dangerous, but not random or overwhelming.

#### Approach / Spacing Behavior

- enemy can move into attack range
- enemy should not teleport or snap unfairly
- spacing should matter

Approach behavior should support duel spacing rather than erase it.

#### One or Two Basic Attacks

- each attack has clear windup
- each attack has commitment
- each attack has active hit window
- each attack has recovery or punish window
- at least one attack should be parry-eligible or dodge-punishable

This is enough for M0. The first enemy does not need a large move set to prove readability.

#### Readable Telegraph

- a visual, motion, or rhythm cue should appear before impact
- timing should be learnable
- telegraph should align with hit timing

The telegraph is the foundation of the `Read` step in the loop.

#### Attack Commitment

- once committed, the enemy should not instantly cancel into another threat in M0
- commitment is what enables the player to read, avoid, and punish

Commitment is one of the key fairness tools in the prototype.

#### Punish Window

- after whiff, parry, or committed attack recovery, the player should understand when a counter is possible

Punishability must feel authored and readable rather than arbitrary.

### 15.4 Attack Eligibility Tags

The enemy side should expose simple provisional interaction tags to clarify how attacks relate to player answers.

- `DodgePunishable`
  - this attack may open a counter opportunity when correctly dodged
- `ParryEligible`
  - this attack can be successfully parried during valid parry timing
- `Unparryable`
  - this attack cannot be parried and should force another defensive answer
- `SpacingCheck`
  - this attack primarily tests distance, angle, or repositioning discipline
- `CounterOnWhiff`
  - this attack may create counter opportunity when it fully misses due to spacing or dodge
- `CounterOnParry`
  - this attack explicitly opens counter opportunity on successful parry

These tags should remain simple in M0. Their purpose is readability, not system tax complexity.

### 15.5 Enemy Intent States For M0

The following provisional enemy intent states are sufficient for M0:

- `EnemyIdle`
- `EnemyApproach`
- `EnemyTelegraph`
- `EnemyAttackStartup`
- `EnemyAttackActive`
- `EnemyAttackRecovery`
- `EnemyStagger`
- `EnemyPunishWindow`
- `EnemyDefeated / Disabled`

This is not a full AI framework. It is a small readable state set that gives Combat Core enough structured enemy behavior to support the duel loop.

### 15.6 Emotional Intent Placeholder

`Glass Refrain` will later use emotional memory states to change behavior rhythm, hesitation, aggression, and punish timing. M0 does not need that full structure yet.

For M0:

- the enemy does not need full emotional AI
- enemy intent should still feel deliberate, tense, and readable
- later emotional states may change rhythm, hesitation, aggression, or punish timing
- M0 should keep one neutral or default emotional rhythm

This preserves the project tone without overbuilding the first enemy.

### 15.7 Debug Requirements

The debug overlay should expose:

- current enemy intent state
- current enemy attack
- whether telegraph is active
- whether attack is active
- attack eligibility tags
- whether the attack is parry-eligible
- whether the attack is dodge-punishable
- whether punish window is active
- whether the enemy is vulnerable
- whether the enemy is staggered
- last player response result

This is critical because combat feel depends on matching the player’s interpretation to the enemy’s actual authored intent.

### 15.8 Anti-Patterns

The following outcomes should be treated as failures:

- enemy attacks with no readable telegraph
- enemy cancels that invalidate player reading
- random attack timing that feels unfair
- enemy pressure that never resets
- every attack being parryable
- every attack being dodge-punishable
- unclear unparryable attacks
- hit timing not matching animation
- enemy AI owning player combat truth
- emotional behavior added before basic readability works

These anti-patterns make the duel harder to learn and weaken the identity of the system.

### 15.9 Open Questions

The following questions remain unresolved:

- does the M0 enemy have one attack or two?
- should the first enemy include an unparryable attack?
- is enemy intent data-authored from the start, or initially hard-wired for speed?
- does enemy punish window open `CounterWindow` directly, or only mark vulnerability that Combat Core interprets?
- is enemy stagger duration fixed or data-authored?
- should enemy rhythm include slight hesitation to support `Glass Refrain`'s tone?
- are emotional intent tags needed in M0, or deferred entirely?

## 16. Memory Reveal Hook

This section defines the minimum memory or reveal connection Combat Core needs for M0. Combat Core does not own the full `Memory State` system. It only exposes or triggers a minimal reveal hook when a meaningful combat exchange succeeds. `Memory State` will later own memory truth and state change more fully. VFX, UI, audio, and camera may present the reveal, but they must not decide combat truth.

### 16.1 Reveal Hook Purpose

The reveal hook exists to prove the following:

- combat is not just damage
- correct reading can expose emotional or memory truth
- counters matter beyond health reduction
- the enemy feels like an emotional or memory presence
- the game’s identity connects combat outcome to memory distortion

For M0, this hook should remain minimal and restrained. It is not a narrative system yet. It is a proof-of-identity signal.

### 16.2 What Can Trigger Reveal In M0

The following are valid provisional reveal triggers for M0:

- successful counter after parry
- successful counter after dodge-punishable enemy whiff
- enemy stagger caused by a meaningful counter
- enemy defeat, if needed
- manually triggered debug reveal for testing

Reveal should not trigger from:

- random light attack damage
- any generic hit
- failed parry
- failed dodge
- passive time passing
- VFX-only events

The reveal hook should only answer meaningful combat interpretation, not generic contact.

### 16.3 Minimum M0 Reveal Response

The M0 reveal response may use one or more of the following:

- brief memory shimmer
- enemy hesitation
- short distortion pulse
- debug-visible reveal state
- small change in enemy rhythm
- one ghost or echo flash
- temporary desaturation or tint
- short audio sting

The response should stay short and readable. It should not become a cutscene, block the player for long, or hide the next enemy read. The purpose is to punctuate combat success with memory identity, not to interrupt the duel completely.

### 16.4 Reveal Ownership Boundary

Combat Core owns:

- detecting meaningful combat success
- exposing a `RevealRequested`-style event, flag, or equivalent concept
- identifying the combat source that caused the reveal
- reporting whether the reveal came from counter, parry-counter, dodge-counter, or defeat

`Memory State` owns:

- whether the reveal is accepted
- what memory state changes
- whether reveal progress changes
- whether the enemy or district state shifts

Presentation owns:

- shader and VFX response
- audio response
- camera feedback
- UI and debug display

This boundary is important because it prevents presentation from becoming gameplay truth and prevents Combat Core from swallowing the full memory system too early.

### 16.5 Reveal Data Needed By M0

Combat Core should be able to expose a conceptual reveal payload containing:

- source actor
- target actor
- source action
- resolution result
- reveal trigger type
- current memory state
- optional intensity
- optional reveal id
- optional debug reason

This is conceptual data only. It exists so that Memory State and presentation can respond with clarity later.

### 16.6 Reveal Beat Timing

`RevealBeat` should:

- happen after successful counter confirmation
- be short and readable
- support the `calm → burst → reveal → reset` rhythm
- avoid unfair incoming hits if player control is briefly interrupted
- avoid obscuring enemy telegraphs

Whether `RevealBeat` is a real combat state or a presentation or event overlay remains open. The important requirement for M0 is that the beat be readable without disrupting the duel more than necessary.

### 16.7 M0 Success Criteria

A tester should be able to say:

- “I countered correctly”
- “that triggered the memory response”
- “the enemy or world briefly changed because of the exchange”
- “combat is tied to uncovering something”

The tester does not need to understand full story meaning yet. They only need to feel the connection between successful combat interpretation and the reveal response.

### 16.8 Anti-Patterns

The following reveal behaviors should be treated as failures:

- reveal triggering from every hit
- reveal becoming a long cutscene
- reveal VFX hiding enemy intent
- reveal controlled only by VFX without combat validation
- memory system changing combat state invisibly
- reveal progress becoming a full narrative system in M0
- counter feeling disconnected from reveal feedback
- reveal feedback being so subtle that testers miss it

These anti-patterns either weaken readability or overinflate scope.

### 16.9 Open Questions

The following reveal questions remain unresolved:

- Is `RevealBeat` a real player state or a presentation overlay?
- Does reveal pause combat briefly?
- Does reveal change enemy rhythm in M0?
- Should enemy defeat always trigger reveal?
- Does reveal have intensity levels?
- Does Memory State accept every reveal request, or filter them?
- In M0, does reveal feedback belong mostly to VFX, audio, UI, or enemy behavior?

## 17. Debug / Readability Requirements

Debug visibility is mandatory for M0. The goal of the combat prototype is not just to feel good in isolated moments, but to become understandable enough that designers and testers can quickly identify why something feels correct, unfair, muddy, or disconnected from the intended loop. Combat feel depends on being able to observe state, timing windows, enemy intent, hit resolution, and reveal triggers directly. Debug and UI systems may observe combat state, but they must not own combat truth.

### 17.1 Debug Purpose

Debug tools for M0 should help designers and testers answer the following questions quickly:

- what state is the player in?
- what state is the enemy in?
- what timing window is active?
- why was an input accepted or rejected?
- why did a hit succeed or fail?
- why did parry or dodge succeed or fail?
- why did `CounterWindow` open or not open?
- why did reveal trigger or not trigger?

If those questions cannot be answered during a short playtest, the prototype is too opaque to tune efficiently.

### 17.2 Required Player Combat Debug Data

The debug layer should expose:

- current player combat state
- previous player combat state
- time in current state
- current action source
- whether the player can receive input
- whether the player can move
- whether the player can rotate
- whether the player can be hit
- whether parry is active
- whether dodge is active
- whether counter is available
- whether reveal beat is active
- last accepted input
- last rejected input
- rejection reason

This data is necessary because input feel and combat feel are inseparable during tuning.

### 17.3 Required Enemy Debug Data

The debug layer should expose:

- current enemy intent state
- current enemy attack
- whether enemy telegraph is active
- whether enemy attack is active
- whether enemy recovery or punish window is active
- whether the enemy is vulnerable
- whether the enemy is staggered
- enemy attack eligibility tags:
  - `DodgePunishable`
  - `ParryEligible`
  - `Unparryable`
  - `SpacingCheck`
  - `CounterOnWhiff`
  - `CounterOnParry`

The purpose of this layer is to let the team compare what the player thought the enemy was doing against what the enemy system was actually expressing.

### 17.4 Required Timing Window Debug Data

The debug layer should expose:

- startup window active
- active window active
- recovery window active
- parry window active
- dodge avoidance window active
- counter window active
- enemy telegraph window active
- enemy punish window active
- reveal beat window active
- time remaining in the active window if available

This is especially important because many combat feel problems come from window timing that is technically present but unreadable in practice.

### 17.5 Required Hit Resolution Debug Data

The debug layer should expose:

- attacker
- defender
- attempted action
- resolution result
- active state at the moment of resolution
- whether defender was vulnerable
- whether parry was active
- whether dodge was active
- whether `CounterWindow` opened
- whether `RevealBeat` triggered
- hit type
- reaction category
- interruption result

This layer should make it possible to answer not only what happened, but why it happened.

### 17.6 Required Reveal Debug Data

The debug layer should expose:

- whether reveal was requested
- whether reveal was accepted
- whether reveal was rejected
- reveal trigger type
- source action
- source result
- current memory state
- reveal intensity if used
- debug reason

Because the reveal hook is part of `Glass Refrain`'s identity, it must be possible to verify that reveal responses happen for meaningful reasons rather than by accident.

### 17.7 Debug Presentation Modes

For M0, debug presentation can stay simple:

- on-screen text overlay
- small timing-window labels
- colored state labels if useful
- console logs only as secondary support
- optional gizmos for hitbox or hurtbox inspection later

The debug layer does not need polished production UI. It only needs to make combat understandable and tunable. It should also remain separate from the final HUD design.

### 17.8 Readability Test Checklist

During playtest, the tester or designer should actively check:

- can the enemy intent be read before impact?
- did the defensive answer feel fair?
- was the counter window noticeable?
- did the hit result match expectation?
- did the reveal response happen only after meaningful success?
- did VFX, camera, or UI obscure any combat read?
- did failure feel explainable?

This checklist should be treated as a recurring validation loop during M0 iteration.

### 17.9 Ownership Boundary

Combat Core owns:

- state data
- timing data
- resolution data
- reveal request data

Debug Overlay owns:

- presentation of debug data
- filtering and formatting
- visibility toggles

Debug Overlay must not:

- change combat state
- force hit results
- open `CounterWindow`
- trigger reveal by itself except through an explicit manual debug command if one is intentionally allowed

The debug layer exists to observe and explain, not to become a hidden part of gameplay logic.

### 17.10 Anti-Patterns

The following patterns should be treated as failures:

- tuning by feel only with no state visibility
- hidden timing windows
- unclear input rejection
- hit results with no reason
- reveal triggers with no source
- debug overlay changing gameplay
- console logs replacing readable in-game debug
- VFX readability problems not being testable
- only testing successful outcomes and not testing failures

These anti-patterns make the system harder to trust and slower to improve.

### 17.11 Open Questions

The following debug questions remain unresolved:

- does the M0 debug overlay use UI Toolkit or a simpler developer overlay solution?
- are hitbox and hurtbox gizmos required in M0?
- should timing windows show remaining time, or only active versus inactive?
- should input rejection reasons be visible in the overlay by default?
- should reveal debug show full memory-state detail, or only trigger state?
- should debug tools be available in prototype builds, or editor only?

## 18. Data Authoring Needs

This section defines the minimum combat data that should be authored, tuned, or configured for M0. The purpose is to make Combat Core adjustable during implementation and playtesting without building a full long-term ability or RPG framework too early. The priority is fast tuning of feel, readability, and cause-and-effect clarity.

### 18.1 Data Authoring Purpose

Combat Core needs authored or tunable data so designers can adjust:

- action timing
- attack commitment
- hit and reaction category
- dodge, parry, and counter windows
- enemy attack eligibility
- recovery and punish windows
- reveal trigger behavior
- debug readability

For M0, the purpose of data authoring is fast tuning and clarity, not full RPG scalability.

### 18.2 Minimum M0 Data Categories

#### Player Action Data

Used for:

- light attack
- heavy attack
- dodge
- parry
- counter

Should include:

- action id or name
- startup duration
- active duration
- recovery duration
- movement restriction
- facing restriction
- input acceptance notes
- optional debug label

This category gives the team control over the basic player verbs without requiring a large combat ability framework.

#### Attack Data

Used for:

- player light attack
- player heavy attack
- player counter
- enemy basic attacks

Should include:

- hit type
- reaction category
- damage category or value if used
- range or reach placeholder
- interruption behavior
- recovery or punish behavior
- eligibility tags if the attack belongs to an enemy

This data exists to make attack outcomes understandable and tunable.

#### Defense Window Data

Used for:

- dodge active or avoidance
- parry active
- counter window

Should include:

- active duration
- success condition
- failure result
- whether it can open counter
- debug label

This category is critical because the core M0 feel depends on readable defensive timing.

#### Enemy Attack Data

Used for:

- one or two M0 enemy attacks

Should include:

- telegraph duration
- startup duration
- active duration
- recovery duration
- attack eligibility tags:
  - `DodgePunishable`
  - `ParryEligible`
  - `Unparryable`
  - `SpacingCheck`
  - `CounterOnWhiff`
  - `CounterOnParry`
- punish window behavior
- stagger response
- debug label

This category supports readable enemy pressure without requiring a full enemy roster system.

#### Hit Reaction Data

Used for:

- `LightHitReact`
- `HeavyHitReact`
- `ParryStagger`
- `CounterStagger`
- `PlayerHitReact`
- provisional `DefeatReact`

Should include:

- reaction category
- approximate duration
- interrupt behavior
- movement or facing restriction
- recovery return state
- debug label

This category should stay simple and focused on readability.

#### Reveal Hook Data

Used for:

- minimal memory or reveal response

Should include:

- valid trigger type
- accepted source result
- reveal intensity if used
- reveal beat duration
- debug label
- whether a reveal request is sent to `Memory State`

This category should stay small enough that reveal remains a signal, not a system explosion.

#### Debug Display Data

Used for:

- making tuning readable

Should include:

- labels
- state names
- window names
- color or grouping notes if useful
- visibility toggles

This category supports tuning efficiency rather than gameplay behavior.

### 18.3 What Should Be Hardcoded Temporarily

For M0, it is acceptable to temporarily hardcode:

- one player action set
- one enemy type
- one default memory state
- one reveal response
- simple health or hit-count values
- simple reaction categories

However, timing and core rule data should be easy to tune once implementation begins. The main rule is that values central to feel should not become buried in hard-to-adjust logic.

### 18.4 What Should Not Be Authored Yet

Do not author full systems for:

- weapon databases
- skill trees
- gear stats
- elemental damage
- status effects
- combo trees
- RPG scaling curves
- large enemy roster
- boss phase data
- narrative memory graph
- save progression data
- full district reinterpretation data

These systems are intentionally outside M0 scope and would add noise to the duel prototype.

### 18.5 Data Ownership Boundary

Combat Core owns or consumes:

- player action timing data
- attack timing data
- defensive window data
- counter window rules
- hit resolution tags and categories

`Enemy Intent` owns or consumes:

- enemy attack rhythm
- telegraph timing
- attack selection behavior
- punish window authoring

`Health / Damage / Hit Reaction` owns or consumes:

- health values
- damage category or value
- reaction category
- defeat or disabled behavior

`Memory State` owns or consumes:

- reveal trigger acceptance
- memory state response
- reveal progress placeholder

Presentation owns or consumes:

- animation clips
- VFX references
- audio cues
- camera impulse settings
- UI labels

This boundary helps preserve clean combat truth while still allowing designers to tune meaningful values.

### 18.6 Provisional Data Table

| Data Category | Used By | Minimum Fields | Why It Matters For M0 | Can Be Hardcoded Temporarily? |
|---------------|---------|----------------|------------------------|-------------------------------|
| Player Action Data | Combat Core | action id, startup, active, recovery, movement restriction, facing restriction, input notes, debug label | Tunes core player verbs and commitment feel | Partially |
| Attack Data | Combat Core, Enemy Intent | hit type, reaction category, damage category/value, range placeholder, interruption behavior, punish behavior, tags | Defines how attacks differ in feel and consequence | Partially |
| Defense Window Data | Combat Core | active duration, success condition, failure result, can open counter, debug label | Essential for readable dodge/parry/counter timing | Should be tunable |
| Enemy Attack Data | Enemy Intent, Combat Core | telegraph, startup, active, recovery, eligibility tags, punish behavior, stagger response, debug label | Drives readable enemy pressure and punish windows | One simple enemy can start partially hardcoded |
| Hit Reaction Data | Health / Damage / Hit Reaction, Combat Core | reaction category, duration, interrupt behavior, movement/facing restriction, return state, debug label | Makes success/failure legible | Partially |
| Reveal Hook Data | Combat Core, Memory State | trigger type, source result, intensity, beat duration, debug label, request flag | Connects combat success to identity | Yes, minimally |
| Debug Display Data | Debug Overlay | labels, state names, window names, grouping notes, toggles | Makes tuning understandable | Yes |

### 18.7 Tuning Notes

The following tuning guidance should apply during M0:

- start with readable and generous values
- tune one action at a time
- tune enemy telegraph before player strictness
- keep debug labels human-readable
- avoid data complexity until feel is proven
- prefer fewer, clearer authored values over many hidden modifiers

The purpose of M0 tuning is to make the duel understandable first, then satisfying, then demanding.

### 18.8 Anti-Patterns

The following patterns should be avoided:

- building a full ability database before M0 feel works
- hardcoding all timing values deep in code
- hiding important combat tags from designers
- creating too many parameters before playtesting
- mixing presentation references with combat truth data
- allowing VFX or audio data to determine combat result
- adding progression stats before the base duel loop is fun
- designing boss data before one simple enemy works

These anti-patterns increase complexity without improving the prototype’s core proof target.

### 18.9 Open Questions

The following data questions remain unresolved:

- Should M0 data become ScriptableObjects immediately, or begin as simpler constants/config values first?
- Are enemy attack tags authored data from day one?
- Are reaction durations authored or fixed?
- Does reveal trigger data belong primarily in Combat Core or in `Memory State`?
- Do debug labels live in data, or are they generated from state names?
- Is attack range or reach authored as data, or derived from hitbox setup?
- Should tuning data be separated from animation data from the start?

## 19. Presentation Boundaries

This section defines the boundary between Combat Core and the presentation layer for M0. Combat Core owns combat truth. Presentation systems communicate combat truth. Animation, VFX, camera, UI, and audio must never become the authority for hit results, `CounterWindow`, parry success, dodge success, or reveal validity.

### 19.1 Boundary Purpose

Presentation should make combat feel:

- readable
- elegant
- responsive
- emotionally restrained
- aligned with the `calm → burst → recovery → reveal` rhythm

Presentation must not own:

- combat state
- hit resolution
- vulnerability
- counter availability
- reveal trigger validity
- damage application

The purpose of this boundary is to preserve trust in the duel loop. Feedback should clarify what happened, not secretly decide it.

### 19.2 Combat Core Owns

Combat Core owns:

- player combat state
- timing windows
- action acceptance or rejection
- hit resolution result
- dodge, parry, and counter success
- `CounterWindow` opening
- `RevealRequested` context
- authoritative combat debug data

This is the truth layer that presentation must follow.

### 19.3 Animation Owns

Animation owns:

- visual pose
- attack animation playback
- dodge, parry, and counter animation playback
- hit reaction animation
- enemy telegraph animation
- timing readability support

Animation must not:

- apply damage directly without Combat Core validation
- independently decide hit success
- secretly extend or shorten gameplay windows
- create hidden invulnerability
- cancel combat states without Combat Core approval

Animation events may be used only as presentation sync or as requests validated by Combat Core, not as final gameplay authority.

### 19.4 VFX / Shader / Memory Visuals Own

VFX owns:

- impact effects
- parry sparks or flash
- dodge trail if used
- counter accent
- memory shimmer or distortion
- reveal pulse
- environmental visual response

VFX must not:

- trigger damage by itself
- open `CounterWindow`
- decide reveal acceptance
- hide enemy telegraphs
- obscure the next combat read
- become louder than the combat truth

VFX should support meaning and punctuation without overtaking readability.

### 19.5 Camera Owns

Camera owns:

- framing
- lock-on readability
- camera impulse or shake
- target focus presentation
- combat readability support

Camera must not:

- determine lock-on combat validity by itself
- decide hit or counter result
- hide attack startup or telegraph
- overuse shake during precise timing windows
- make dodge or parry timing unreadable

Camera serves readability first and mood second in M0.

### 19.6 UI / Debug Overlay Owns

UI owns:

- HUD presentation if needed
- debug overlay display
- state and window labels
- input rejection reasons
- reveal and debug status

UI must not:

- change combat state
- force hit results
- trigger reveal except through an explicit manual debug command if allowed
- own gameplay truth
- become required for normal player understanding once final presentation improves

UI is an observer and explainer, not a rules owner.

### 19.7 Audio Owns

Audio owns:

- attack sound
- hit confirm sound
- parry success and failure sound
- dodge cue
- counter accent
- reveal sting
- ambience support

Audio must not:

- be the only indicator of critical combat truth
- mask enemy telegraph cues
- suggest success when Combat Core says failure
- drive gameplay result timing by itself

Audio should reinforce clarity and emotional rhythm, not replace them.

### 19.8 Presentation Sync Philosophy

The presentation layer should follow these principles:

- presentation should follow Combat Core state changes
- presentation can request actions, but Combat Core validates them
- presentation can exaggerate feedback after the result is known
- gameplay windows should be debug-visible even if animation is still rough
- early M0 should prefer clarity over polish
- beautiful feedback is valuable only if it preserves readability

This philosophy keeps the prototype honest while still allowing strong sensory feedback.

### 19.9 M0 Presentation Minimum

For M0, presentation only needs:

- clear player attack feedback
- clear enemy telegraph
- clear dodge and parry success/failure feedback
- clear counter hit confirmation
- clear hit reaction
- clear minimal reveal response
- readable camera framing
- debug overlay

M0 does not require:

- final animation quality
- final VFX
- final UI HUD
- full cinematic camera
- final audio mix
- polished memory distortion system

The prototype only needs enough presentation to make the loop legible and identifiable as `Glass Refrain`.

### 19.10 Presentation Boundary Table

| Presentation Area | Allowed To Own | Must Not Own | M0 Requirement | Risk If Boundary Is Violated |
|-------------------|----------------|--------------|----------------|------------------------------|
| Animation | Pose, playback, telegraph readability, visual sync | Damage, hit success, hidden invulnerability, combat state truth | Clear action and telegraph readability | Combat truth becomes hidden in animation timing |
| VFX / Shader | Impact accents, reveal pulse, memory shimmer, visual punctuation | Damage, `CounterWindow`, reveal validity, telegraph suppression | Clear hit/reveal support without noise | Readability collapses under visual noise or false feedback |
| Camera | Framing, lock-on readability, impulse, target focus presentation | Hit validity, counter validity, timing truth | Keep the duel readable during timing-critical moments | Player cannot read attacks or windows clearly |
| UI / Debug | State display, labels, debug filtering, reveal/debug status | Gameplay truth, combat result forcing, autonomous reveal | Show critical M0 debug and readability info | Designers cannot diagnose why the loop feels wrong |
| Audio | Hit confirms, parry cues, counter accent, reveal sting, ambience support | Gameplay timing authority, contradictory success/failure messaging | Reinforce combat result and tone | Player reads the wrong outcome from sound cues |

### 19.11 Anti-Patterns

The following patterns should be treated as failures:

- animation events directly applying damage
- VFX triggering reveal without Combat Core
- camera shake hiding attack reads
- UI becoming the only way to understand combat
- audio cue contradicting combat result
- presentation secretly changing timing windows
- root motion moving the player without Combat Core and Locomotion agreement
- beautiful feedback masking unfair rules
- debugging combat through animation only

These anti-patterns weaken readability and make the prototype harder to trust.

### 19.12 Open Questions

The following presentation questions remain unresolved:

- are animation events allowed as validated timing requests?
- is root motion used for attacks or counters?
- is camera impulse tied to hit type, reaction category, or both?
- is reveal VFX triggered by Combat Core directly, or through `Memory State`?
- does M0 use UI Toolkit or a simpler developer overlay for debug?
- are audio cues authored per action, or per resolution result?
- does lock-on camera belong entirely to the Camera GDD, or partly to this Combat Core contract?

## 20. Technical Boundaries

Technical boundaries exist to keep Combat Core small, authoritative, and stable during M0. They are not meant to freeze the final architecture of the whole project. They exist to ensure that the first duel prototype is implemented in a way that preserves combat truth, supports debugging, and avoids avoidable rewrites later.

### 20.1 Boundary Purpose

Technical boundaries should ensure:

- Combat Core remains authoritative for combat truth
- presentation observes but does not own gameplay
- implementation stays debuggable
- M0 stays small and testable
- future architecture can evolve without rewriting the whole combat loop

These boundaries protect the prototype from being solved through hidden dependencies, presentation tricks, or overbuilt systems.

### 20.2 Combat Core Technical Principles

Combat Core should be:

- explicit
- deterministic enough for local single-player feel testing
- frame-readable
- easy to debug
- small enough for M0
- separated from presentation
- data-tunable where timing matters
- not dependent on animation, VFX, camera, or UI to decide rules

The implementation should favor clarity and inspectability over abstraction density.

### 20.3 Assembly / Dependency Direction

Combat Core may depend on:

- Core primitives and contracts
- minimal Unity types only where unavoidable
- `R3` only for observation or debug-facing streams if useful

Combat Core should not depend on:

- UI
- Camera
- VFX
- Audio
- Bootstrap
- Editor-only code
- `DOTween`
- `Cinemachine`
- full Memory implementation
- full Enemy AI implementation

Presentation systems may observe Combat Core through:

- read-only state
- events or signals
- debug snapshots
- presentation DTOs
- explicit interfaces or contracts

This keeps the combat domain stable and prevents outward-facing systems from becoming hidden gameplay owners.

### 20.4 VContainer / Lifetime Boundary

Combat services should live in gameplay or combat scene scope, not project root scope.

Rules:

- combat truth must not be registered globally by accident
- root scope owns application lifetime only
- scene, gameplay, and combat scopes own combat runtime state
- generated DI registration later should be used carefully only for pure C# services
- MonoBehaviours, scene references, hitboxes, cameras, and VFX presenters should remain explicitly composed

This keeps Combat Core aligned with the project's approved scene and DI structure.

### 20.5 R3 / Reactive Boundary

`R3` may:

- expose read-only observations of combat state
- support debug overlay, UI, VFX, and camera observation

`R3` should not:

- replace the core combat state machine
- become the owner of hot combat truth
- create reactive chains that make timing results hard to trace

Combat Core should remain explicit and inspectable even if reactive observation is added around it.

### 20.6 DOTween Boundary

`DOTween` may be used later for presentation polish.

`DOTween` must not drive:

- authoritative combat movement
- dodge timing
- hit timing
- parry timing
- `CounterWindow` timing

It may support UI, VFX, or camera presentation only when it does not alter combat truth.

### 20.7 Animation / Root Motion Boundary

Animation may visually support actions, but it must not become the owner of gameplay timing.

Rules:

- root motion, if used, must be coordinated with `Player Locomotion` and Combat Core
- animation events may request timing sync only if Combat Core validates them
- animation should not secretly own hit frames, invulnerability, or recovery timing

This is especially important in M0, where rough animation is acceptable but hidden gameplay timing is not.

### 20.8 Physics / Hit Detection Boundary

For M0, the final hit-detection method remains open. Viable options include:

- hitboxes and hurtboxes
- distance and angle checks
- hybrid checks

Regardless of the final detection method:

- physics should assist detection, not create chaotic combat truth
- Combat Core should validate hit results against current state, timing, and vulnerability

The prototype should favor clarity and consistency over physically noisy simulation.

### 20.9 Memory Boundary

Combat Core may request reveal, but it must not become the full memory system.

Rules:

- Combat Core may request reveal
- `Memory State` decides memory consequence
- full memory truth restoration is outside Combat Core
- Combat Core must not become a narrative progression system
- reveal context should be explicit enough for Memory State to evaluate later

This preserves the identity link without pulling story-state ownership into combat logic.

### 20.10 Testing Boundary

Combat Core should be testable without final animation, VFX, camera, or full presentation support.

Requirements:

- state transitions should be inspectable
- timing windows should be testable with controlled inputs
- hit resolution should be testable without polished presentation
- debug snapshots should support M0 playtest iteration

The combat loop must remain understandable even in partially dressed prototype conditions.

### 20.11 Technical Anti-Patterns

The following patterns should be treated as failures:

- Combat Core depending on UI, Camera, or VFX
- project root owning combat runtime state
- reactive streams hiding combat truth
- `DOTween` driving gameplay windows
- animation events applying damage directly
- physics collisions alone deciding combat results
- service locator use for combat state
- overbuilding a generic ability framework before M0
- implementing boss, multiplayer, or RPG scaling before one duel works
- hardcoding timing so deeply it cannot be tuned

These anti-patterns either weaken the prototype's clarity or inflate its complexity before the core loop is proven.

### 20.12 Open Questions

The following technical questions remain unresolved:

- does M0 hit detection use hitboxes, distance checks, or hybrid checks?
- is the combat state machine pure C#, or partly MonoBehaviour-driven?
- is timing data ScriptableObject-based from the start?
- is `R3` used immediately, or only after the state model stabilizes?
- is root motion used at all in M0?
- are debug snapshots implemented later as DTOs, events, or logs?
- does `Memory State` live in Combat scope or Memory scope?

## 21. Dependencies

This section defines what Combat Core depends on, what depends on Combat Core, and which relationships should remain provisional contracts during M0. The purpose is to keep ownership clear so Combat Core stays focused on the duel loop instead of expanding into neighboring systems.

### 21.1 Dependency Purpose

This section should clarify:

- which systems Combat Core needs to function
- which systems consume Combat Core output
- which systems are provisional contracts in M0
- which systems are deferred until after M0
- which boundaries must remain protected

The main goal is to prevent Combat Core from silently becoming Input, Locomotion, Enemy AI, Memory, or Presentation design by accident.

### 21.2 Upstream Dependencies

#### Input Mapping

Combat Core needs:

- movement intent
- light attack intent
- heavy attack intent
- dodge intent
- parry intent
- counter intent
- lock-on toggle or request intent

`Input Mapping` owns capture and bindings. Combat Core owns acceptance and rejection.

#### Player Locomotion

Combat Core needs:

- movement permission support
- facing and orientation support
- dodge displacement support
- committed-state movement restrictions
- recovery and reset rhythm

`Player Locomotion` owns movement implementation. Combat Core owns combat-state permissions.

#### Health / Damage / Hit Reaction

Combat Core needs:

- damage event handling
- reaction category handling
- health and defeat result
- hit react entry support

Combat Core decides the hit result. `Health / Damage / Hit Reaction` applies health and reaction consequences.

#### Enemy Intent & Telegraph

Combat Core needs:

- enemy telegraph window
- enemy attack active and recovery windows
- attack eligibility tags
- punish window state
- enemy vulnerability and stagger state

`Enemy Intent & Telegraph` owns enemy behavior and rhythm. Combat Core owns player-facing resolution.

#### Memory State

Combat Core needs:

- reveal request acceptance
- minimal memory response state
- reveal and debug status

Combat Core requests reveal. `Memory State` owns memory consequence.

### 21.3 Downstream Consumers

The following systems consume Combat Core output:

#### Debug Overlay

Consumes:

- combat state
- timing windows
- input acceptance and rejection
- hit resolution
- counter window
- reveal request and result

#### UI / HUD

Consumes:

- optional combat state
- player status
- target status
- counter or reveal hints if needed

#### Camera / Lock-On

Consumes:

- target focus request or result
- combat engagement context
- hit, counter, and reveal events for framing or impulse
- readable state cues

#### VFX / Shader

Consumes:

- hit result
- parry, dodge, and counter result
- reveal request and result
- memory response state

#### Audio

Consumes:

- action result
- hit confirm
- parry, counter, and reveal events

#### Enemy Presentation

Consumes:

- stagger result
- punish state
- reaction category
- reveal effect cue if needed

These are consumers of combat truth, not owners of combat truth.

### 21.4 Provisional M0 Contracts

The following systems should be treated as provisional contracts rather than fully solved designs during M0:

- `Input Mapping`
- `Player Locomotion`
- `Health / Damage / Hit Reaction`
- `Enemy Intent & Telegraph`
- `Memory State`
- `Lock-On & Combat Camera`
- `Debug Overlay`
- presentation systems

For each of these:

- Combat Core may define minimum needs
- the dedicated GDD or architecture later owns the full design
- any temporary M0 assumption must be revisited before vertical slice

This is one of the key protections against M0 scope creep.

### 21.5 Systems That Should Not Be Dependencies For M0

Combat Core should not depend on:

- full RPG progression
- skill tree
- equipment or loot
- save/load
- quest system
- full narrative graph
- district reinterpretation system
- boss phase framework
- multiplayer or networking
- final HUD
- final cinematic system
- final audio mix
- analytics or telemetry

These systems are outside the purpose of the M0 duel prototype.

### 21.6 Dependency Table

| System | Relationship To Combat Core | Combat Core Needs | System Owns | M0 Status |
|--------|-----------------------------|-------------------|-------------|-----------|
| Input Mapping | Upstream dependency | Player intent for movement and combat actions | Input capture, bindings, later rebinding | Provisional contract |
| Player Locomotion | Upstream dependency | Spacing, facing, dodge movement, movement restriction support | Movement implementation and controller behavior | Provisional contract |
| Health / Damage / Hit Reaction | Upstream dependency | Consequence handling after resolved hits | Health values, reaction application, defeat result | Provisional contract |
| Enemy Intent & Telegraph | Upstream dependency | Telegraph, attack windows, eligibility tags, punish state | Enemy behavior, attack rhythm, telegraph design | Provisional contract |
| Memory State | Upstream dependency | Reveal acceptance and minimal memory response state | Memory consequence and reveal response ownership | Provisional contract |
| Debug Overlay | Downstream consumer | N/A | Debug presentation and readability support | Provisional contract |
| Lock-On & Combat Camera | Downstream consumer with support contract | Target focus context and combat engagement cues | Target framing, lock-on presentation, camera readability | Provisional contract |
| VFX / Shader | Downstream consumer | N/A | Visual feedback and reveal presentation | Provisional contract |
| UI / HUD | Downstream consumer | N/A | Player-facing display and debug display | Provisional contract |
| Audio | Downstream consumer | N/A | Sound feedback and tension support | Provisional contract |
| Encounter Framework | Adjacent future dependency | Combat result and encounter-state hooks | Encounter composition, pacing, fight context | Deferred after core M0 proof |
| Progression / RPG Systems | Not a valid M0 dependency | None | Long-term growth, stats, unlocks | Deferred |
| District Reinterpretation | Not a valid M0 dependency | None for core duel feel | District-state shifts and changed space meaning | Deferred |

### 21.7 Dependency Risk Notes

The following dependency risks should be watched closely:

- Combat Core can become too large if contracts are not respected
- Camera, VFX, and UI can accidentally become gameplay authority
- Enemy Intent can become unreadable if not coordinated with timing rules
- Health / Damage can become RPG balance too early
- Memory reveal can become narrative progression too early
- Lock-on can become required for all combat if not controlled
- Debug can become stale if it is not tied to authoritative state

These are the most likely failure modes when the system begins to integrate with neighboring systems.

### 21.8 Anti-Patterns

The following patterns should be treated as failures:

- Combat Core directly controlling UI, camera, or VFX
- Input Mapping deciding combat validity
- Locomotion canceling combat states without approval
- Enemy AI deciding player hit, parry, or counter results
- Health system deciding hit validity
- Memory system triggering reveal without valid combat context
- Progression stats altering M0 feel before the base loop works
- boss framework influencing one-enemy M0 design too early

These anti-patterns blur ownership and make the system harder to tune or trust.

### 21.9 Open Questions

The following dependency questions remain unresolved:

- Which provisional dependency GDD should be written immediately after Combat Core?
- Should `Lock-On & Combat Camera` remain one combined GDD, or later split into two?
- Does `Health / Damage / Hit Reaction` deserve its own full GDD before implementation?
- Should `Memory State` be designed before the full `Enemy Intent` GDD?
- Should `Encounter Framework` own enemy spawning and combat start/end for M0?
- Should `Debug Overlay` become a standalone system GDD?
- Should `Progression` remain completely deferred until after M0?

## 22. Risks

This section identifies the main risks that could derail `M0 — Katana Combat Feel Prototype`. These risks are specific to the first duel loop and its immediate implementation boundaries. Each risk matters because M0 succeeds or fails on feel clarity, readability, and scope discipline rather than on content volume.

### 22.1 Combat Feel Risk

**Risk:** The combat may feel stiff, floaty, spammy, or unresponsive.

**Why it matters:** M0 exists primarily to prove katana combat feel.

**What could go wrong:**

- movement feels too floaty
- attack recovery is too short or too long
- dodge or parry timing is unclear
- counter window is not satisfying
- hit reactions are too weak or too disruptive

**Mitigation direction:**

- tune with debug overlay active
- start generous, then tighten
- test one enemy and one player kit only
- prioritize feel before content volume

### 22.2 Enemy Readability Risk

**Risk:** Enemy intent may not be readable before impact.

**Why it matters:** The core loop depends on `read → evade/parry → counter → reveal`.

**What could go wrong:**

- weak telegraph
- unclear animation timing
- attack active window does not match visuals
- enemy pressure never resets
- camera or VFX hides tells

**Mitigation direction:**

- tune enemy telegraph first
- debug enemy intent state
- keep the M0 enemy simple
- require clear windup, commitment, and recovery

### 22.3 Dodge / Parry Balance Risk

**Risk:** Dodge or parry may become the single dominant answer.

**Why it matters:** Dodge should be the spatial answer, while parry should be the timing answer.

**What could go wrong:**

- dodge invulnerability is too generous
- parry window is too wide
- all attacks are parryable
- all attacks are dodge-punishable
- recovery is too safe

**Mitigation direction:**

- use attack eligibility tags
- keep failure states punishable
- test dodge-only and parry-only playstyles
- tune recovery and attack tags carefully

### 22.4 Counter Reward Risk

**Risk:** Counter may feel either too weak or too available.

**Why it matters:** Counter is the emotional and mechanical reward of the loop.

**What could go wrong:**

- `CounterWindow` is too long
- counter damage or reaction is too weak
- counter is available from random actions
- counter whiffs too often because of spacing
- counter is not tied clearly to reveal response

**Mitigation direction:**

- `CounterWindow` must have a clear cause
- counter success should have strong feedback
- debug counter availability
- tie reveal only to meaningful counter success

### 22.5 Reveal Integration Risk

**Risk:** Reveal may feel disconnected, too subtle, too loud, or too frequent.

**Why it matters:** Reveal is what makes the prototype feel like `Glass Refrain` instead of generic action combat.

**What could go wrong:**

- reveal triggers from generic hits
- reveal feedback is too subtle
- reveal becomes a cutscene
- reveal obscures the next enemy read
- `Memory State` responsibilities are unclear

**Mitigation direction:**

- restrict reveal to meaningful combat success
- keep reveal short and restrained
- expose reveal debug status
- let `Memory State` decide acceptance

### 22.6 Scope Creep Risk

**Risk:** Combat Core may expand into a full RPG, ability, or boss framework too early.

**Why it matters:** M0 should prove one duel loop, not the entire game.

**What could go wrong:**

- adding skill tree structure
- adding combo trees
- adding boss phases
- adding many enemies
- adding progression stats
- overbuilding generic ability systems

**Mitigation direction:**

- one player kit
- one simple enemy
- minimal reveal response
- no progression or stat scaling
- defer boss, multi-enemy, and skill systems

### 22.7 Presentation Authority Risk

**Risk:** Animation, VFX, camera, UI, or audio may accidentally own gameplay truth.

**Why it matters:** Combat truth must stay explicit, debuggable, and authoritative.

**What could go wrong:**

- animation events apply damage directly
- VFX triggers reveal
- camera hides telegraph
- root motion moves the player without agreement
- UI changes gameplay state

**Mitigation direction:**

- Combat Core validates outcomes
- presentation only observes and presents results
- debug authoritative state directly
- animation events are requests only if allowed

### 22.8 Technical Architecture Risk

**Risk:** Implementation may become difficult to test, tune, or maintain.

**Why it matters:** M0 needs fast iteration.

**What could go wrong:**

- reactive chains hide state
- `DOTween` drives gameplay timing
- service locator usage spreads combat truth
- combat state is registered globally
- too many dependencies accumulate
- timing is hardcoded too deeply

**Mitigation direction:**

- use an explicit state machine
- keep runtime state in gameplay or combat scope
- use `R3` for observation only
- use `DOTween` for presentation only
- keep timing data easy to tune
- support tests and debug snapshots later

### 22.9 Debug Visibility Risk

**Risk:** Designers may be unable to tell why something happened.

**Why it matters:** Combat feel cannot be tuned blindly.

**What could go wrong:**

- hidden timing windows
- missing input rejection reasons
- no hit resolution reason
- no enemy intent debug
- no reveal trigger debug

**Mitigation direction:**

- make debug overlay required for M0
- expose state, timing, input, hit, counter, and reveal
- test failure cases, not only success cases

### 22.10 Risk Table

| Risk | Why It Matters | Failure Mode | Mitigation | M0 Severity |
|------|----------------|--------------|------------|-------------|
| Combat Feel | M0 exists to prove duel feel | Combat feels stiff, floaty, spammy, or dull | Tune with debug, start generous, keep scope small | High |
| Enemy Readability | Core loop begins with `Read` | Player cannot understand intent before impact | Tune telegraph first, keep enemy simple, align visuals and timing | High |
| Dodge / Parry Balance | Defensive identity must stay clear | One defensive answer dominates everything | Use tags, punish failure, test one-answer playstyles | High |
| Counter Reward | Counter is the reward beat | Counter feels weak, random, or too available | Keep clear cause, strong feedback, visible windows | High |
| Reveal Integration | Combat must feel like `Glass Refrain` | Reveal feels disconnected or noisy | Restrict triggers, keep reveal short, debug acceptance | Medium |
| Scope Creep | M0 must stay small | Prototype expands into RPG/boss framework | One player kit, one enemy, defer progression systems | High |
| Presentation Authority | Truth must stay authoritative | Animation/VFX/camera quietly own gameplay results | Validate in Combat Core, keep presentation observational | Medium |
| Technical Architecture | Fast iteration is required | State becomes hard to test or tune | Explicit state machine, simple dependencies, tunable data | Medium |
| Debug Visibility | Tuning depends on explanation | Designers cannot explain outcomes | Required debug overlay, visible failure reasons | High |

### 22.11 Highest Priority Risks

The highest-priority M0 risks are:

- enemy intent readability
- combat feel
- dodge/parry/counter balance
- debug visibility
- scope creep

These are the risks most likely to determine whether the M0 prototype succeeds or fails.

### 22.12 Anti-Patterns

The following patterns should be treated as warning signs:

- adding more enemies before one enemy feels good
- tuning difficulty before readability
- making counter flashy but mechanically unclear
- making reveal beautiful but unrelated to combat success
- relying on final animation quality to fix unclear rules
- treating debug overlay as optional
- allowing presentation to become gameplay authority
- implementing progression before the base combat loop is fun

These anti-patterns often disguise unresolved core problems instead of solving them.

### 22.13 Open Questions

The following risk-oriented questions remain unresolved:

- which risk should be validated first in the prototype?
- what minimum playtest session proves M0 combat feel?
- does debug overlay need to exist before meaningful combat tuning begins?
- should reveal be tested in the first combat prototype, or only after core feel stabilizes?
- should the first enemy include both dodge and parry lessons?
- how much animation polish is required before combat feel can be judged fairly?
- when should tuning stop and vertical slice planning begin?

## 23. Open Questions

This section consolidates the unresolved Combat Core questions from the earlier sections and organizes them by decision priority. The purpose is not to answer every question immediately. The purpose is to make implementation blockers visible, identify what can safely be decided through tuning, and prevent accidental scope creep.

### 23.1 Must Answer Before M0 Implementation

These questions should be answered before implementation planning begins, or explicitly accepted as prototype assumptions:

- Is counter a dedicated input or a contextual attack during `CounterWindow`?
- Does parry have startup or become active immediately?
- Does M0 use hitboxes/hurtboxes, distance checks, or a hybrid approach?
- Does M0 use numeric HP or simple hit-count health?
- Is debug overlay required before meaningful playtesting begins?
- Does `Memory State` live in Combat scope or Memory scope?
- Is reveal included in the first playable combat prototype, or added after base feel stabilizes?
- Does the M0 enemy need one attack or two?
- Are enemy attack tags authored data from day one?
- Is the combat state machine pure C# or partly MonoBehaviour-driven?

These questions matter because they directly shape implementation approach, testability, and whether the prototype can even prove the intended loop.

### 23.2 Can Answer During M0 Tuning

These questions do not need to be finalized before implementation starts. They can be explored through playtesting and tuning:

- How strict should parry timing be?
- How generous should dodge avoidance be?
- How long should `CounterWindow` last?
- Should dodge success open counter directly or only against specific attacks?
- Should counter window duration differ by defense type?
- Should the player be vulnerable during `CounterWindow`?
- Should `CounterActive` grant protection?
- Should light/heavy chain into a very short two-hit string?
- Can light attacks interrupt enemies?
- How much animation polish is required before judging combat feel?
- How many playtest runs are enough to pass M0?

These questions are best answered by trying the duel and observing whether the intended feel emerges.

### 23.3 Defer Until After M0

These questions should not block M0 and should remain deferred:

- full boss duel framework
- full RPG progression
- skill tree
- equipment/loot
- stance switching
- weapon switching
- full memory restoration system
- district reinterpretation
- large enemy roster
- production HUD
- final VFX/audio
- save/load consequence
- multiplayer/networking
- long combo trees
- advanced animation cancel rules

These are valuable future concerns, but they are outside the proof target of the first duel prototype.

### 23.4 Cross-System Questions

The following questions should be answered in other system GDDs rather than fully inside Combat Core.

#### Enemy Intent & Telegraph

- Do attacks need explicit eligibility tags from the start?
- Should the first enemy include an unparryable attack?
- Should enemy rhythm include hesitation for `Glass Refrain` tone?
- Are emotional intent tags needed in M0, or deferred?

#### Lock-On & Combat Camera

- Is lock-on required for counter readability?
- Should lock-on be required for counter in M0?
- Is movement camera-relative or target-relative during lock-on?
- Does lock-on movement use strafing from the start?

#### Player Locomotion

- Does M0 use Character Controller, Rigidbody, or custom controller?
- Is dodge direction input-relative, camera-relative, or target-relative?
- Do attacks use root motion or code-driven motion?
- Does counter auto-align to target?

#### Health / Damage / Hit Reaction

- Are reaction durations fixed or data-authored?
- Does player hit reaction cancel queued input?
- Is counter damage a value or mainly a special reaction category?
- Does enemy defeat trigger reveal?

#### Memory State

- Is `RevealBeat` a real combat state or presentation overlay?
- Does reveal pause combat briefly?
- Does reveal change enemy rhythm in M0?
- Does `Memory State` accept every reveal request or filter them?

#### Debug Overlay

- UI Toolkit or a simpler developer overlay?
- Are hitbox/hurtbox gizmos required?
- Should timing windows show remaining time?
- Are input rejection reasons visible by default?
- Are debug tools available in builds or editor only?

These questions should be handed to the owning system once Combat Core’s minimum contracts are understood.

### 23.5 Recommended Decision Order

The recommended decision order before implementation is:

1. counter input model
2. parry startup/active behavior
3. hit detection method
4. debug overlay requirement
5. enemy attack count and tags
6. reveal-in-first-prototype decision
7. health model
8. locomotion controller choice
9. root motion policy
10. `Memory State` scope

This order is intended to resolve the highest-impact implementation blockers first while leaving tuning-heavy questions for iteration.

### 23.6 Non-Blocking Notes

- Not every open question needs an answer before the first playable build.
- Questions in the tuning category should be treated as experiments rather than planning blockers.
- Questions in the deferred category should stay deferred unless they directly improve the M0 duel loop.
- Cross-system questions should be routed to the owning GDD instead of being solved informally inside Combat Core.

The goal is not total certainty. The goal is to avoid hidden blockers and prevent accidental expansion of scope.

### 23.7 Open Question Table

| Question | Category | Blocks M0 Implementation? | Owner System | Recommended Timing |
|----------|----------|---------------------------|--------------|--------------------|
| Is counter dedicated or contextual? | Must Answer Before M0 Implementation | Yes | Combat Core | Before implementation |
| Does parry have startup or immediate active frames? | Must Answer Before M0 Implementation | Yes | Combat Core | Before implementation |
| What hit detection method does M0 use? | Must Answer Before M0 Implementation | Yes | Combat Core / Health / Enemy Intent | Before implementation |
| Is debug overlay required before meaningful playtesting? | Must Answer Before M0 Implementation | Yes | Combat Core / Debug Overlay | Before implementation |
| Does the first enemy have one attack or two? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph | Before implementation |
| Are enemy attack tags authored from day one? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph | Before implementation |
| Is reveal in the first playable prototype? | Must Answer Before M0 Implementation | Yes | Combat Core / Memory State | Before implementation |
| Does M0 use numeric HP or hit-count health? | Must Answer Before M0 Implementation | Yes | Health / Damage / Hit Reaction | Before implementation |
| Does `Memory State` live in Combat or Memory scope? | Must Answer Before M0 Implementation | Yes | Memory State / DI architecture | Before implementation |
| Is the combat state machine pure C# or partly MonoBehaviour-driven? | Must Answer Before M0 Implementation | Yes | Combat Core / architecture | Before implementation |
| How strict should parry timing be? | Can Answer During M0 Tuning | No | Combat Core | During tuning |
| How generous should dodge avoidance be? | Can Answer During M0 Tuning | No | Combat Core / Locomotion | During tuning |
| How long should `CounterWindow` last? | Can Answer During M0 Tuning | No | Combat Core | During tuning |
| Should dodge success open counter directly? | Can Answer During M0 Tuning | No | Combat Core / Enemy Intent | During tuning |
| Should counter window duration differ by defense type? | Can Answer During M0 Tuning | No | Combat Core | During tuning |
| Should player be vulnerable during `CounterWindow`? | Can Answer During M0 Tuning | No | Combat Core | During tuning |
| Should `CounterActive` grant protection? | Can Answer During M0 Tuning | No | Combat Core | During tuning |
| Can light/heavy chain into a very short string? | Can Answer During M0 Tuning | No | Combat Core | During tuning |
| Can light attacks interrupt enemies? | Can Answer During M0 Tuning | No | Combat Core / Health / Enemy Intent | During tuning |
| How much animation polish is required before judging feel? | Can Answer During M0 Tuning | No | Animation / Combat Core | During tuning |
| How many playtest runs are enough to pass M0? | Can Answer During M0 Tuning | No | Combat Core / QA judgment | During tuning |
| Full boss framework questions | Defer Until After M0 | No | Boss Duel Framework | After M0 |
| Full progression questions | Defer Until After M0 | No | Progression systems | After M0 |
| Full memory restoration questions | Defer Until After M0 | No | Memory State / Truth Restoration | After M0 |
| Large enemy roster questions | Defer Until After M0 | No | Enemy roster systems | After M0 |

### 23.8 Final Summary

Combat Core is ready to move to dependency-system design once the must-answer implementation questions are reviewed and either decided or explicitly accepted as prototype assumptions.

## 24. Acceptance Criteria For M0

This section defines the practical conditions under which `Combat Core` is considered successful enough at the M0 stage to move forward. The purpose is not to demand final polish or full-system completeness. The purpose is to determine whether the core duel loop is proven enough to justify building the next dependent systems.

### 24.1 M0 Acceptance Purpose

Acceptance criteria for M0 should answer the following:

- does the core combat loop work?
- is the enemy readable?
- do dodge and parry feel fair?
- does counter feel earned?
- does reveal connect combat to `Glass Refrain`'s identity?
- can designers debug and tune the system?
- is the scope still contained?

If these questions cannot be answered positively in a small repeatable duel prototype, Combat Core should not be considered ready to anchor downstream work.

### 24.2 Core Loop Acceptance

M0 Combat Core passes the core-loop requirement if the player can reliably experience:

`read → evade/parry → counter → reveal`

Required:

- enemy intent is visible before impact
- player can choose a defensive answer
- dodge and/or parry can succeed based on timing or spacing
- successful defense can create `CounterWindow`
- counter can hit and produce clear feedback
- meaningful counter can trigger minimal reveal response
- combat returns to a readable reset or neutral rhythm

This is the central proof target of the entire prototype.

### 24.3 Player Action Acceptance

Player actions are acceptable if:

- movement supports spacing and reading
- light attack feels fast and low-commitment
- heavy attack feels more deliberate and punishable
- dodge feels responsive but not universal
- parry feels precise but learnable
- counter is only available from a valid `CounterWindow`
- hit reaction communicates failure clearly
- lock-on or target focus supports readability if used

The player does not need a broad move set. The actions only need to be distinct, understandable, and capable of producing the duel rhythm.

### 24.4 Enemy Intent Acceptance

Enemy intent is acceptable if:

- the M0 enemy has readable idle or approach behavior
- attack telegraph is visible before active hit
- attack active timing matches the expected visual cue
- attack recovery or punish window is understandable
- at least one attack supports meaningful dodge, parry, and counter interaction
- enemy pressure resets enough for the player to re-read
- failure feels explainable rather than random

This is the other half of the duel loop. If the enemy cannot be read, Combat Core is not ready.

### 24.5 Hit Resolution Acceptance

Hit resolution is acceptable if:

- hit, miss, parry, dodge, and counter outcomes are authoritative
- Combat Core validates results
- presentation does not decide damage or reveal
- vulnerability rules are consistent enough for testing
- player and enemy hit reactions match the resolved result
- debug data explains why each result occurred

This criterion protects the system from becoming visually impressive but mechanically untrustworthy.

### 24.6 Reveal Hook Acceptance

Reveal hook is acceptable if:

- reveal only triggers from meaningful combat success
- reveal does not trigger from random or generic hits
- reveal response is noticeable to testers
- reveal is short and restrained
- reveal does not hide the next enemy read
- the tester understands that combat success caused a memory response

The reveal does not need full narrative meaning yet. It only needs to clearly connect combat success to the game’s identity.

### 24.7 Debug Acceptance

Debug and readability tooling is acceptable if it can show:

- player combat state
- enemy intent state
- current timing window
- last input accepted or rejected and why
- hit resolution result
- parry, dodge, and counter status
- `CounterWindow` availability
- reveal requested, accepted, or rejected state

Debug does not need production UI polish. It only needs to make tuning understandable.

### 24.8 Scope Acceptance

M0 remains acceptable only if it does not expand into:

- full RPG stats
- skill tree
- equipment or loot
- large combo trees
- multiple weapons
- boss framework
- multiple enemy roster
- full memory or narrative system
- district reinterpretation
- final HUD
- final animation, VFX, or audio polish
- multiplayer or networking

If these systems begin to define the prototype, M0 has lost focus.

### 24.9 Playtest Acceptance Checklist

A tester should be able to answer `yes` to the following:

- I understood when the enemy was about to attack.
- I understood whether dodge or parry was a valid answer.
- I could tell why I got hit.
- I could tell when I earned a counter.
- Counter felt more rewarding than a normal hit.
- The reveal response was connected to successful combat.
- The fight returned to a readable rhythm after each exchange.
- Debug information helped explain unclear moments.

This checklist is intended as a practical M0 playtest gate.

### 24.10 Failure Conditions

Combat Core should not pass M0 if:

- enemy attacks feel random or unreadable
- dodge or parry solves every situation
- counter appears without clear cause
- hit results feel inconsistent
- reveal triggers from meaningless hits
- presentation hides combat truth
- debug cannot explain failures
- implementation requires final assets to judge basic feel
- scope has expanded beyond one player kit and one simple enemy

Any one of these failure conditions is enough to justify more tuning before moving on.

### 24.11 Acceptance Table

| Area | Acceptance Criteria | How To Verify | Pass/Fail Signal | M0 Priority |
|------|---------------------|---------------|------------------|-------------|
| Core Loop | Player can repeatedly experience `read → evade/parry → counter → reveal` | Repeated duel playtest with debug visible | Pass if the loop is understandable and repeatable | Must Pass |
| Player Actions | Movement, attack, dodge, parry, and counter feel distinct and readable | Focused hands-on playtest | Pass if actions feel purposeful and non-overlapping | Must Pass |
| Enemy Intent | Enemy telegraphs and punish windows are readable | Observe tester reactions and debug state | Pass if attacks are understandable before impact | Must Pass |
| Dodge / Parry | Defensive answers feel fair and non-dominant | Test dodge-heavy and parry-heavy play separately | Pass if each answer has strengths, limits, and failure clarity | Must Pass |
| Counter | Counter feels earned and satisfying | Verify `CounterWindow` readability and payoff | Pass if counter is clear, limited, and rewarding | Must Pass |
| Hit Resolution | Results are authoritative and explainable | Use debug data during success and failure cases | Pass if outcomes match state and timing truth | Must Pass |
| Reveal Hook | Successful combat causes meaningful reveal response | Trigger counters and inspect reveal behavior | Pass if testers notice and connect reveal to success | Must Pass |
| Debug Visibility | Designers can explain what happened | Run tuning session with debug overlay | Pass if unclear moments can be diagnosed quickly | Must Pass |
| Scope Control | Prototype remains narrowly focused | Review current feature set against exclusions | Pass if no major out-of-scope systems creep in | Must Pass |
| Technical Boundary | Combat truth remains separate from presentation authority | Review implementation approach against GDD boundaries | Pass if Combat Core remains authoritative | Should Pass |

### 24.12 Minimum “Good Enough” Definition

Combat Core M0 is good enough when one simple enemy duel repeatedly demonstrates a readable `read → evade/parry → counter → reveal` loop, with debug-visible state, timing, and resolution data, without relying on final presentation polish or expanding into full RPG systems.

### 24.13 Deferred Acceptance

The following are explicitly not required for Combat Core M0:

- final balance
- final animation quality
- full enemy roster
- boss encounter
- full lock-on polish
- full memory system
- full UI or HUD
- save/load
- progression
- production VFX or audio

These belong to later milestones and should not block M0 acceptance.

### 24.14 Open Questions

The following acceptance questions remain unresolved:

- what minimum number of playtest runs is enough to pass M0?
- does reveal need to be included in the first playable prototype, or can it land after base feel stabilizes?
- do both dodge and parry need to be proven in M0, or can one be stronger initially?
- does counter need a unique animation, or can placeholder attack feedback be enough?
- is debug overlay required before the first meaningful playtest?
- who has authority to approve Combat Core M0 as good enough?
- what exact threshold decides when tuning stops and design moves to the next system?
