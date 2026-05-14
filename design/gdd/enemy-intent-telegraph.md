# Enemy Intent & Telegraph

> **Status**: In Design
> **Author**: User + Codex
> **Last Updated**: 2026-05-14
> **Implements Pillar**: Combat As Interpretation, Melancholic Elegance, Distorted Memory Spaces

## 1. System Summary

`Enemy Intent & Telegraph` defines how enemies communicate what they are about to do before combat impact occurs. Its purpose is to make `Combat Core` readable, fair, and emotionally legible by ensuring that enemy-side behavior exposes clear danger, commitment, and punish opportunities instead of producing random or visually confusing pressure.

For `Glass Refrain`, this system primarily supports the `read` phase of `read → evade/parry → counter → reveal`. It gives the player enough information to interpret enemy motion, attack rhythm, and vulnerability so that defensive choices feel informed rather than guessed. The player should feel that the enemy is telling the truth through movement and timing, even when that truth is emotionally distorted.

For M0, this system exists to support one small duel prototype, not a full enemy ecosystem. It must define how one simple enemy presents intent, commits to one or two attacks, exposes dodge or parry opportunities, and returns to a readable rhythm after each exchange. Its job is not to overwhelm the player, but to create a tense and understandable conversation through threat.

This system does not own player combat truth. It does not decide whether the player successfully dodged, parried, countered, or triggered reveal. Those outcomes remain owned by `Combat Core`. `Enemy Intent & Telegraph` owns enemy-side communication and authored enemy-side attack behavior, while `Combat Core` owns player-facing combat resolution.

## 2. Design Intent

The design intent of `Enemy Intent & Telegraph` is to make the enemy feel deliberate, tense, and readable. In `Glass Refrain`, the player should not feel like they are reacting to arbitrary aggression or to surprise damage hidden behind animation noise. They should feel like they are interpreting intent through stance, rhythm, spacing, and attack commitment.

For M0, the enemy must help prove that the duel loop can carry the game’s identity. The first enemy does not need complexity, large move variety, or advanced AI. It needs clarity. It must present threat in a way that gives the player time to observe, answer, and understand why an opening appeared or why a failure occurred. Readability matters before difficulty. A fair, readable enemy with a simple pattern is more valuable to M0 than a more impressive but less legible opponent.

The emotional shape of enemy behavior should support `calm → threat → answer → punish/reveal`. The enemy should not attack constantly or with chaotic cadence. There should be enough space in the rhythm for tension to build, for the player to recognize commitment, and for the duel to reset into another read. This is part of the melancholic, restrained tone of `Glass Refrain`: violence is brief and meaningful, not endless pressure spam.

Even in this simple prototype, the enemy should feel emotionally appropriate to the project. The opponent should feel like a memory or emotional presence contained within the space, not a generic training dummy or a noisy action-game sponge. That does not require a full emotional AI system in M0, but it does require that the enemy’s behavior feel intentional, tense, and shaped by mood rather than by randomness.

This system therefore prioritizes readable telegraphing, visible attack commitment, understandable punish windows, and restrained rhythm over challenge escalation, pattern complexity, or boss-like spectacle. If the player cannot explain what the enemy was about to do before impact, the system has failed its primary purpose.

## 3. Player Experience Goals

The enemy-side experience goals for M0 are about trust, readability, and emotional tension. The first enemy should teach the player that danger in `Glass Refrain` can be interpreted and answered.

### Readable Intent

The player should be able to read enemy intent before impact. The enemy should communicate threat through a combination of stance, spacing, windup, movement commitment, and timing rhythm. The player does not need hidden knowledge to survive; they should be able to understand danger from what the enemy is visibly doing.

### Recognizable Commitment

The player should understand when an enemy attack has meaningfully committed. Once the enemy enters a committed attack sequence, the player should be able to tell that the threat is underway and that a defensive answer is required. Commitment should feel visible, not hidden behind ambiguous movement or noise.

### Defensive Clarity

The player should understand whether dodge or parry is a valid answer to what the enemy is doing. Even if not every attack is immediately mastered, the player should feel that the system is teaching them whether the danger is better answered spatially, through timing, or through spacing discipline.

### Punish Recognition

The player should be able to recognize when the enemy has become punishable. A whiff, deflection, committed recovery, or visible hesitation should create a readable sense that a counter opportunity exists. The player should feel that openings are earned from understanding the enemy, not granted arbitrarily.

### Explainable Failure

Failure should feel explainable. If the player gets hit, misses a punish, or chooses the wrong defensive answer, they should be able to identify why. The enemy should not create the feeling that damage came from randomness, hidden timing, or unclear state changes.

### Reset Rhythm

Enemy pressure should reset enough to allow re-reading. The duel should not collapse into endless aggression. After each committed exchange, the player should have enough space to re-establish understanding of the enemy’s state before the next threat begins.

### Emotional Presence

The enemy should feel like a memory or emotional presence rather than a generic punching bag. Even in M0, the first enemy should contribute to the tone of restrained tension, unstable memory, and personal interpretation that defines `Glass Refrain`.

### M0 Tester Readability Goal

A fresh tester should be able to explain:

- what the enemy was about to do
- when the enemy truly committed
- whether dodge or parry seemed like the right answer
- when the enemy became punishable
- why they succeeded or failed during the exchange

If a tester cannot explain those points after a short duel session, the system is not yet readable enough for M0.

## 4. M0 Scope

This section defines exactly what `Enemy Intent & Telegraph` includes for `M0 — Katana Combat Feel Prototype`. The goal is to support one readable duel opponent that makes the `Combat Core` loop testable and emotionally coherent.

### Included in M0

#### One Simple Enemy

M0 includes one simple enemy only. This enemy is a duel target, not the start of a roster. Its purpose is to prove readability, commitment, punish windows, and counter opportunity support in a constrained environment.

#### Idle / Readable Presence

The enemy should have a readable idle or threat-presence state. It should feel active and dangerous without attacking constantly. The player should have time to observe and establish tension before each exchange.

#### Approach / Spacing Behavior

The enemy should be able to approach or maintain combat-relevant spacing. This behavior only needs to be sufficient to support readable engagement. It does not need to be a full navigation or pursuit system. The enemy should not snap, teleport, or close space unfairly in M0.

#### One or Two Basic Attacks

The M0 enemy should have one or two basic attacks only. Each attack should exist to teach readable threat, defensive answers, and punish windows. A second attack is acceptable if it improves clarity about dodge vs parry, but variety is not the goal.

#### Clear Telegraph Window

Each attack must have a readable telegraph window before the hit becomes active. This is required to support the `read` phase of the duel loop. Telegraph clarity matters more than attack count.

#### Clear Startup / Active / Recovery

Each enemy attack must clearly express:

- startup or windup
- active hit window
- recovery

These phases must be understandable enough that the player can learn where danger begins and where opportunity returns.

#### Clear Punish Window

At least one enemy action path must expose a punish or counter opportunity after a committed mistake, whiff, parry, or recovery state. The player should be able to learn that enemy commitment creates openings.

#### Attack Eligibility Tags

M0 should support the following provisional enemy attack tags:

- `DodgePunishable`
- `ParryEligible`
- optional `Unparryable`
- optional `SpacingCheck`
- `CounterOnWhiff`
- `CounterOnParry`

These tags exist to keep enemy-side authored behavior clear and to support Combat Core’s defensive and counter rules. M0 does not need a rich taxonomy beyond what helps prove the duel loop.

#### Basic Stagger / Hit Reaction

The enemy should support basic stagger or hit reaction outcomes that make successful player interaction readable. This does not need to become a full enemy reaction system yet. It only needs to make counters, parries, and punishes legible.

#### Debug Visibility

M0 includes debug-facing visibility for enemy state and timing readability. Designers and testers should be able to see what the enemy is currently doing, whether a telegraph or punish window is active, and which attack tags are in play.

### M0 Completion Target For This System

`Enemy Intent & Telegraph` is considered in scope for M0 when one simple enemy can repeatedly communicate readable danger, commit to one or two authored attacks, expose at least one meaningful defensive and punish interaction, and reset to a readable duel rhythm.

## 5. Non-Goals

`Enemy Intent & Telegraph` must stay tightly scoped for M0. This system exists to make one duel readable and fair, not to solve all future enemy behavior for `Glass Refrain`.

### Not a Full Enemy AI Framework

M0 does not require a complete enemy AI architecture, behavior tree library, utility system, or generalized combat brain. It only needs enough authored behavior to make one enemy readable and consistent.

### Not a Boss Duel Framework

This document does not design Memory Keeper boss structure, phase logic, escalation rules, or boss reveal scripting. Boss duel design belongs to a later system pass after the basic duel loop is proven.

### Not Many Enemy Archetypes

M0 does not include a broad roster, enemy taxonomy, or class-based enemy families. One simple enemy is enough. Enemy variety should not be used to compensate for unclear readability in the first duel.

### Not Combo-Heavy Enemy Patterns

This system does not need long chains, pressure strings, air pursuit, spectacle-heavy sequences, or oppressive pattern density. M0 enemy behavior should stay simple enough that the player can understand cause and effect.

### Not Advanced Emotional AI

Although the enemy should feel emotionally appropriate to `Glass Refrain`, M0 does not need advanced emotional-state simulation, memory-driven mood transitions, or authored emotional behavior sets. One neutral or default emotional rhythm is sufficient for now.

### Not Procedural Attack Selection

M0 does not need procedural pattern generation, dynamic move weighting complexity, or reactive authored-combinatorial behavior. Simple, deliberate authored attack selection is enough.

### Not Stealth or Investigation AI

This system does not define search states, patrol logic, suspicion behavior, clue guarding, or environmental investigation behaviors. Those concerns belong to later exploration or narrative-facing systems.

### Not Group Tactics

M0 does not need multi-enemy coordination, flanking, aggro sharing, spacing negotiation between enemies, or squad rhythm. The duel is one-on-one.

### Not a Ranged Enemy System

This pass does not define projectile logic, ranged spacing behavior, zoning pressure, or mixed melee-ranged combat readability. The first enemy should stay close, readable, and duel-focused.

### Not Full Animation or VFX Polish

The system does not require final animation quality, final telegraph VFX language, or production-level impact polish. It requires clarity first. Presentation should support readability, but polish should not become a substitute for clear rules.

### Not Final Balancing

M0 does not need final timing balance, difficulty tuning, or complete punish-risk calibration. It only needs to be readable and testable enough that the team can judge the duel loop.

### Not a Narrative Memory Graph

This system does not define full memory logic, contradiction chains, reveal progression graphs, or emotional-state narrative consequences. It only supports the enemy-side behavior needed for the first reveal-capable duel.

### Scope Protection Rule

If a proposed enemy feature does not make one simple duel more readable, fair, or emotionally coherent for `read → evade/parry → counter → reveal`, it should be deferred.

## 6. Core Enemy Intent Loop

The purpose of the enemy intent loop in M0 is to make the duel readable from the enemy side. This loop defines how the first simple enemy moves from visible tension into committed danger, then back into punishable recovery or readable reset. It is not a full AI loop. It is a duel-rhythm loop that exists to support `Combat Core`'s `read → evade/parry → counter → reveal`.

### 6.1 Enemy Intent Loop Overview

The M0 enemy loop should follow this shape:

`presence → approach/space → telegraph → commit → active threat → recovery/punish → reset or stagger/reveal`

This maps directly to the player loop:

- `presence` and `approach/space` support the player's `read`
- `telegraph` and `commit` support the choice to `evade` or `parry`
- `active threat` tests timing and spacing
- `recovery/punish` supports `counter`
- `stagger/reveal` supports `reveal`
- `reset` returns the duel to readable tension

The important design principle is that the enemy should feel like it is telling the player what kind of exchange is about to happen. The enemy loop should not feel random, constant, or noisy. It should create a legible rhythm that allows the player to interpret danger, answer it, and understand the consequence.

### 6.2 Presence Phase

The loop begins with presence. In this phase, the enemy is visible, threatening, and emotionally charged, but not yet committed to immediate attack. The player should feel tension and danger without being forced into instant reaction.

Presence serves several purposes:

- gives the player time to observe
- establishes the enemy as a meaningful emotional or memory presence
- supports the melancholic, restrained pacing of the duel
- creates anticipation before commitment

The enemy should not remain passive forever, but it also should not attack the moment the encounter begins with no time for the player to read the situation. Presence is where the duel breathes before violence happens.

### 6.3 Approach / Space Phase

After presence, the enemy may adjust spacing toward attack range or maintain an authored duel distance. This phase exists to make spacing meaningful and readable. The enemy should not teleport, snap unfairly into attack range, or attack from an unclear distance that the player could not reasonably interpret.

Approach and spacing should communicate intent in advance:

- the enemy closes distance with readable movement
- the player retains room to reposition
- the duel establishes where threat is about to emerge
- spacing itself becomes part of the read

This phase should support the feeling that the enemy is preparing to threaten the player, not cheating its way into range. If the enemy can attack from anywhere without readable spatial logic, the duel loses trust immediately.

### 6.4 Telegraph Phase

The telegraph phase is the core fairness mechanism of the system. In this phase, the enemy communicates that an attack is coming before impact occurs. The telegraph can be expressed through motion, stance, pause, glow, audio, a change in rhythm, or some combination of these, but it must remain learnable and consistent enough that the player can build confidence from repetition.

Most importantly, the telegraph must align with the real timing of the attack. If the visual or rhythmic cue suggests one thing while the actual hit timing says another, the system stops being teachable.

This phase supports the player's defensive decision. It should answer the question: "What is the enemy about to do, and do I have enough time to recognize it?" If the answer is no, the enemy loop is not yet fit for M0.

### 6.5 Commit Phase

The commit phase begins when the enemy has chosen an attack and starts executing it. In M0, commitment should be visible and trustworthy. Once committed, the enemy should not freely cancel out of the attack just because the player responded correctly. The player needs to believe that a correct read has value.

Commitment matters because it creates risk for both sides:

- the player risks getting hit if their answer is wrong
- the enemy risks becoming punishable if the player reads correctly

This is one of the most important rhythm points in the duel. If enemy commitment is unreliable, the player cannot trust telegraphs, cannot learn punish timing, and cannot feel that the combat is fair.

### 6.6 Active Threat Phase

The active threat phase is the short period where the enemy attack can actually hit. This is the point where player timing and spacing are tested. The attack is no longer just being announced; it has become real danger.

For M0, active threat should be short, clear, and legible. The player should understand that they are now inside the danger window. Combat Core resolves whether dodge or parry succeeded, whether the player was vulnerable, and whether the result opens a punish opportunity, but `Enemy Intent & Telegraph` must make the threat itself understandable.

This phase should not overstay its welcome. If the active threat is too muddy or too prolonged, it becomes harder for the player to recognize where the real danger began and when the exchange should transition back into opportunity.

### 6.7 Recovery / Punish Phase

After a committed attack resolves, the enemy enters recovery. This is the phase where the player may recognize that the enemy is vulnerable, off-balance, or committed long enough to punish. Not every recovery needs to be equally open, but M0 should include at least one clear punish case that teaches the player that correct defense creates offense.

This phase is where counter opportunity becomes meaningful:

- a whiffed committed attack may expose the enemy
- a parried attack may create an obvious punish state
- a long recovery may visibly invite a counter

The player should be able to recognize this opportunity through the enemy’s behavior, not only through hidden rules. If punish windows exist mechanically but are unreadable from the enemy side, the loop will feel arbitrary.

### 6.8 Stagger / Reveal Phase

When the player succeeds decisively, the enemy may enter a short stagger or disruption phase. This phase communicates that the enemy has been meaningfully interrupted, countered, or emotionally destabilized. It can also support or trigger the minimal reveal response required for M0.

In M0, this phase should remain restrained:

- it may show vulnerability
- it may show momentary hesitation or distortion
- it may support reveal request or memory shimmer
- it should not become a long cutscene or a hard stop

The goal is to prove that the enemy is not just losing health, but momentarily exposing instability or memory disruption. After that signal is communicated, the duel should return to readable rhythm quickly.

### 6.9 Reset Phase

After recovery or stagger, the duel should reset into readable tension. Reset is what prevents the enemy from feeling like endless pressure. It allows the player to re-establish understanding of spacing, threat, and rhythm before the next committed action begins.

Reset does not mean the enemy becomes harmless. It means the duel becomes legible again. The player should feel calm returning after the burst of danger, so that the next read matters.

This preserves the intended rhythm:

`calm → threat → answer → punish/reveal → reset`

If reset never happens, the duel collapses into pressure spam and the emotional shape of `Glass Refrain` is lost.

### 6.10 M0 Loop Variants

M0 should support a few simple readable loop variants:

- `presence → approach → telegraph → attack → recovery → reset`
- `presence → approach → telegraph → attack → whiff → punish → counter → reveal → reset`
- `presence → telegraph → parryable attack → parry success → counter → reveal → reset`
- `presence → telegraph → player fails answer → player hit react → reset`

These variants matter because the loop must explain both success and failure. The player should learn not only when the enemy is punishable, but also why their own answer failed.

### 6.11 Anti-Patterns

The following patterns would break the intended enemy-side loop for M0:

- enemy attacking instantly from idle
- enemy skipping telegraph
- enemy canceling committed attacks without clear rule
- enemy chaining pressure forever
- enemy recovery being too short to understand
- punish window being mechanically real but visually invisible
- telegraph not matching hit timing
- random rhythm replacing readable intent
- stagger or reveal disrupting the next read for too long

Any of these would weaken player trust and make Combat Core harder to evaluate fairly.

### 6.12 Open Questions

The following loop-level questions remain unresolved:

- how long should the presence phase last?
- does the M0 enemy begin already in range, or approach first?
- should the first enemy pause briefly before attacking?
- does every attack need a fully distinct telegraph?
- should punish window readability be shown through animation, VFX, debug, or all three?
- does stagger or reveal alter the enemy's next loop timing?
- does reset return to full neutral or a pressured neutral?

## 7. Enemy State Model

This section defines the explicit M0 enemy intent states that support the loop `presence → approach/space → telegraph → commit → active threat → recovery/punish → stagger/reveal → reset`. These states describe enemy-side truth and readability, not a full AI implementation. The goal is to give the first duel opponent a small, inspectable behavior model that supports fair combat reads.

### 7.1 EnemyIdle / Presence

`EnemyIdle / Presence` is the default readable threat state. In this state, the enemy is active, visible, and emotionally present, but not yet executing an attack. The purpose of this state is to establish mood, tension, and observation time so the player can read the opponent before danger escalates.

Rules:

- may transition to `EnemyApproach / Spacing`
- may transition directly to `EnemyTelegraph` if already in valid range
- should not last forever
- should not jump straight to an unreadable active hit in M0

This state is where the duel breathes before commitment begins.

### 7.2 EnemyApproach / Spacing

`EnemyApproach / Spacing` is the state where the enemy adjusts distance toward a useful attack range or maintains authored duel spacing. Its purpose is to create spatial pressure without becoming unfair. The player should still be able to reposition and understand how spacing is shaping the next threat.

Rules:

- may transition to `EnemyTelegraph` when the enemy is in valid attack range
- should not teleport or snap into threat range unfairly
- should remain readable as movement pressure rather than surprise attack resolution

This state supports the player’s read by making space itself meaningful.

### 7.3 EnemyTelegraph

`EnemyTelegraph` is the state where the enemy communicates that an attack is coming. This is the enemy’s main fairness state. The purpose is to give the player time to identify the threat and prepare an answer through dodge, parry, or spacing discipline.

Rules:

- must be visually or rhythmically distinct
- must align with the real timing of the future active hit
- may include stance, pause, motion, VFX, audio, or rhythm cue
- transitions to `EnemyCommit / AttackStartup`

If this state is unclear, the rest of the duel loop becomes unreliable.

### 7.4 EnemyCommit / AttackStartup

`EnemyCommit / AttackStartup` begins once the enemy has chosen an attack and starts executing it. Its purpose is to make the player’s read trustworthy. By entering this state, the enemy is no longer merely suggesting danger; it has committed to it.

Rules:

- should not freely cancel in M0
- contains startup commitment before the hit becomes active
- transitions to `EnemyAttackActive`

This state is what gives enemy actions consequence and allows correct player reads to matter.

### 7.5 EnemyAttackActive

`EnemyAttackActive` is the short state where the enemy attack can actually hit the player. This is the moment of real threat. Combat Core resolves whether the player’s dodge, parry, spacing, or vulnerability state produced success or failure, but this enemy state is what exposes the dangerous window.

Rules:

- active window should be short and clear
- must align with visible timing and attack readability
- transitions to `EnemyAttackRecovery`
- may transition to `EnemyStagger` if interrupted, parried, or countered in a way that authoritatively produces that result

This state should feel sharp, not muddy.

### 7.6 EnemyAttackRecovery

`EnemyAttackRecovery` is the state after the active hit has resolved but before the enemy has fully returned to readable neutral. Its purpose is to expose consequence for committed action. The enemy has acted and now carries some level of risk.

Rules:

- may transition to `EnemyPunishWindow` if authored
- may return directly to `EnemyIdle / Presence` or reset path
- should not instantly chain fresh pressure in M0 without a readable reset

This state should make whiffed or defended aggression feel meaningful.

### 7.7 EnemyPunishWindow

`EnemyPunishWindow` is the explicit enemy-side opportunity state where the player can recognize that a punish or counter is available. This may occur after a whiff, a parried attack, or a visibly overcommitted recovery. Its purpose is to make offensive opportunity readable rather than hidden.

Rules:

- may open or support player `CounterWindow` depending on Combat Core rules and enemy attack tags
- must be debug-visible
- should become readable through animation or presentation support later
- transitions to `EnemyIdle / Presence`, `EnemyApproach / Spacing`, or `EnemyStagger` depending on what happens next

This state teaches the player that enemy commitment creates openings.

### 7.8 EnemyStagger

`EnemyStagger` is the short reaction state that communicates meaningful player success. The enemy has been interrupted, destabilized, parried cleanly, or struck by a meaningful counter. The purpose of this state is to make the player’s success readable and to support enemy-side vulnerability or reveal-related feedback.

Rules:

- should be short and readable
- should not become the basis of long stun-lock loops
- may transition to `EnemyRevealBeat`
- may transition to recovery, reset, or `EnemyDefeated / Disabled` depending on outcome

This state should feel decisive without becoming a combo trap.

### 7.9 EnemyRevealBeat

`EnemyRevealBeat` is the short optional state where the enemy expresses memory disruption, emotional fracture, or instability after a meaningful exchange. Its purpose is to support the reveal identity of `Glass Refrain` on the enemy side.

Rules:

- optional for M0 if reveal is handled as a presentation overlay instead of a hard enemy state
- should be short and restrained
- should not obscure the next enemy read
- transitions back to readable reset or to `EnemyDefeated / Disabled`

This state exists to support reveal, not to interrupt the duel with a cutscene.

### 7.10 EnemyDefeated / Disabled

`EnemyDefeated / Disabled` is the state where the enemy is no longer active in the M0 encounter. For the prototype, this can remain simple and placeholder-level. It only needs to communicate that the duel target is no longer an active threat.

Rules:

- may be a simple disabled or defeated endpoint
- may trigger reveal if accepted by `Memory State`
- does not require a full death or narrative consequence system in M0

This state is an encounter endpoint, not yet a story system.

### 7.11 State Transition Overview

The normal M0 path should look like this:

`EnemyIdle / Presence → EnemyApproach / Spacing → EnemyTelegraph → EnemyCommit / AttackStartup → EnemyAttackActive → EnemyAttackRecovery → EnemyPunishWindow or EnemyIdle / Presence → reset`

Success and failure branches should remain simple and readable:

- parry success → `EnemyStagger` or `EnemyPunishWindow`
- dodge whiff punish → `EnemyPunishWindow`
- player counter hit → `EnemyStagger → EnemyRevealBeat` optional
- enemy hits player → `EnemyAttackRecovery → reset`
- enemy defeated → `EnemyDefeated / Disabled`

These branches matter because the enemy state model must explain both readable danger and readable opportunity.

### 7.12 Combat Core Interaction Notes

Enemy state does not decide player success or failure by itself. `Combat Core` validates whether the player was hit, whether dodge or parry succeeded, whether a counter opportunity opened, and whether reveal should be requested.

What enemy state should expose:

- telegraph state
- active threat state
- recovery state
- punish availability
- vulnerability context
- attack eligibility tags

What `Combat Core` should decide:

- whether the player's defensive answer succeeded
- whether a hit resolves
- whether `CounterWindow` opens
- whether reveal request is valid

This keeps enemy behavior readable without letting enemy-side logic take ownership of player combat truth.

### 7.13 Debug Requirements

The debug overlay should expose:

- current enemy state
- previous enemy state
- time in current state
- current attack id or name
- telegraph active
- attack active
- recovery active
- punish window active
- stagger active
- reveal beat active
- vulnerability state
- attack eligibility tags

Without this visibility, enemy readability problems will be much harder to diagnose during M0 tuning.

### 7.14 Provisional State Table

| State | Purpose | Can Threaten Player? | Can Be Punished? | Exposes Counter Opportunity? | M0 Notes |
|------|---------|----------------------|------------------|------------------------------|----------|
| `EnemyIdle / Presence` | Establish threat, mood, and observation time | No | Usually no | No | Default readable tension state |
| `EnemyApproach / Spacing` | Adjust spacing and prepare readable range | Indirectly | Usually no | No | Movement pressure only |
| `EnemyTelegraph` | Communicate coming attack | Not yet | Usually no | No | Fairness-critical read state |
| `EnemyCommit / AttackStartup` | Begin committed attack execution | Impending threat | Usually limited | No | Trust-building commitment state |
| `EnemyAttackActive` | Expose actual hit threat | Yes | Usually limited unless interrupted | Indirectly, through authored interactions | Short and clear in M0 |
| `EnemyAttackRecovery` | Resolve commitment and expose consequence | No direct hit threat | Sometimes | Sometimes | May lead into explicit punish |
| `EnemyPunishWindow` | Clearly expose punish opportunity | No | Yes | Yes | Should be highly readable in M0 |
| `EnemyStagger` | Communicate meaningful player success | No | Yes | Already earned or resolving | Must stay short |
| `EnemyRevealBeat` | Express memory disruption or fracture | No | Usually not the focus | Supports reveal outcome | Optional hard state for M0 |
| `EnemyDefeated / Disabled` | End active threat in the encounter | No | No | No | Simple endpoint only |

### 7.15 Anti-Patterns

The following patterns would weaken the M0 enemy state model:

- enemy states that are not debug-visible
- idle directly jumping to active hit
- active hit lasting too long
- recovery being visually invisible
- punish window existing mechanically but not readably
- stagger becoming a long stun-lock loop
- reveal beat becoming a cutscene
- enemy state deciding player combat truth
- too many states for one M0 enemy

The state model should stay small enough to reason about and clear enough to trust.

### 7.16 Open Questions

The following questions remain unresolved:

- are `EnemyCommit` and `EnemyAttackStartup` separate states or one combined state?
- is `EnemyPunishWindow` separate from `EnemyAttackRecovery`, or just a readable subset of it?
- is `EnemyRevealBeat` a real enemy state or a presentation overlay?
- can `EnemyStagger` and `EnemyPunishWindow` overlap?
- is enemy vulnerability primarily state-based or attack-data-based?
- can the enemy transition directly from `EnemyIdle / Presence` to `EnemyTelegraph`?
- can the enemy be interrupted during `EnemyTelegraph`?

## 8. M0 Enemy Action Set

This section defines the exact M0 action set for the first simple enemy. The purpose of this enemy is not to provide variety for its own sake. The purpose is to prove readable intent, committed attacks, punish windows, and the enemy-side support needed for `Combat Core`'s `read → evade/parry → counter → reveal` loop.

The first enemy should stay small enough that each action teaches something clearly. If the enemy has too many moves, too many branches, or too many exceptions, it becomes harder to tell whether the duel feels good because of the core loop or in spite of noise.

### 8.1 Idle / Threat Presence

`Idle / Threat Presence` is the enemy’s baseline action of being present in the duel without yet attacking. Its purpose is to establish mood, tension, and space for observation. This action supports the melancholic pacing of `Glass Refrain` by allowing the player to feel the enemy before immediately being tested by it.

M0 rules:

- enemy can wait briefly before acting
- enemy should look threatening but readable
- enemy should not attack instantly without readable buildup
- idle should transition into approach or telegraph

This action is not passive filler. It is the first teaching moment of the duel.

### 8.2 Approach / Spacing Step

`Approach / Spacing Step` is the action where the enemy moves into a useful attack distance or re-establishes spacing after reset. Its purpose is to create readable spatial pressure and teach the player that range matters.

M0 rules:

- enemy approaches clearly
- no unfair teleporting or snapping
- approach speed should be readable
- enemy may stop briefly before telegraphing
- spacing should create real whiff and punish outcomes

This action should make the enemy feel intentional rather than mechanically glued to the player.

### 8.3 Basic Attack A — Readable Slash

`Basic Attack A` is the primary M0 teaching attack. This should be the first move the player learns to read, answer, and punish. Its job is not to surprise the player. Its job is to teach the loop cleanly.

Suggested role:

- medium-speed attack
- obvious windup
- `ParryEligible`
- `CounterOnParry`
- optionally `DodgePunishable`
- optionally `CounterOnWhiff`

M0 rules:

- must have a distinct telegraph
- must commit once started
- should be learnable after a few attempts
- should not chain immediately into another attack

This attack should be the clearest expression of enemy intent in the whole prototype.

### 8.4 Basic Attack B — Optional Spacing / Heavy Threat

`Basic Attack B` is an optional second attack included only if it improves readability testing. Its purpose is to create contrast with `Basic Attack A` and to test whether the player can recognize a different kind of threat, especially one that emphasizes spacing or dodge timing over parry timing.

Suggested role:

- slower, more committed attack
- wider or longer reach
- `DodgePunishable` or `SpacingCheck`
- optional `Unparryable` if the visual language is clear enough

M0 rules:

- only include if it improves readability testing
- must not overload M0
- must have a distinct telegraph from `Basic Attack A`
- should create a clear punish window on whiff or recovery

This attack exists to deepen learning, not to add spectacle.

### 8.5 Recovery / Punish Exposure

`Recovery / Punish Exposure` is the enemy-side action of visibly carrying consequence after a committed attack. Its purpose is to communicate that the enemy made a meaningful mistake and that the player may have earned a punish or counter opportunity.

M0 rules:

- should follow committed attacks
- must be debug-visible
- should become readable through animation or presentation support later
- can open or support `CounterWindow` depending on Combat Core rules

This action is one of the core payoffs of correct reading. Without readable punish exposure, the duel will feel flat even if telegraphs are good.

### 8.6 Stagger / Reaction

`Stagger / Reaction` is the enemy’s short success-response action when the player lands a meaningful hit, parry-based answer, or counter. Its purpose is to communicate player success clearly and to support reveal-related outcomes.

M0 rules:

- should be short and readable
- should feel stronger for counter than for normal hit
- should not become a long stun-lock foundation
- may lead into `EnemyRevealBeat` or reset

This action should make the enemy feel affected, not merely paused.

### 8.7 Reveal Beat / Memory Disruption

`Reveal Beat / Memory Disruption` is the enemy-side expression of a valid reveal outcome. Its purpose is to connect enemy response to the memory identity of `Glass Refrain`, showing that meaningful combat success has disturbed something deeper than health.

M0 rules:

- triggered only by valid reveal request
- short, restrained, and readable
- may be visual, audio, or debug-placeholder heavy in M0
- should not hide the next enemy read

This action should hint at fracture, not become a narrative cutscene.

### 8.8 Reset / Re-Engage

`Reset / Re-Engage` returns the enemy to readable duel rhythm after recovery, stagger, reveal, or a player failure exchange. Its purpose is to prevent endless pressure and preserve the calm-to-threat cadence of the fight.

M0 rules:

- after recovery, stagger, reveal, or player hit reaction, the enemy returns to presence or spacing behavior
- reset timing should preserve tension without feeling random
- enemy should not immediately loop into constant pressure forever

This action keeps the fight interpretable over repeated exchanges.

### 8.9 Recommended M0 Enemy Configuration

Two candidate configurations make sense for M0:

`Option 1`

- one attack only
- `Basic Attack A`: `ParryEligible` + `CounterOnParry` + optional `CounterOnWhiff`

`Option 2`

- two attacks
- `Basic Attack A`: `ParryEligible` + `CounterOnParry`
- `Basic Attack B`: `DodgePunishable` / `SpacingCheck` + `CounterOnWhiff`

Recommended first implementation:

Use `Option 1` first.

Reason:

- it keeps the first implementation focused on one clearly teachable threat
- it makes telegraph quality easier to tune before move contrast is added
- it reduces noise while validating whether parry, counter timing, and punish readability already work
- it makes failure reasons easier to diagnose

`Option 2` should be added only after `Basic Attack A` already feels good and readable. The second attack should deepen the test, not rescue an unclear first one.

### 8.10 Enemy Action Table

| Enemy Action | Purpose | Related State(s) | Player Lesson | Suggested Tags | M0 Priority |
|------|---------|------------------|---------------|----------------|-------------|
| `Idle / Threat Presence` | Establish tension and observation time | `EnemyIdle / Presence` | The enemy is dangerous before it swings | None | Required |
| `Approach / Spacing Step` | Create readable range pressure | `EnemyApproach / Spacing` | Distance matters and can be read | Optional `SpacingCheck` support | Required |
| `Basic Attack A — Readable Slash` | Teach the primary readable threat | `EnemyTelegraph`, `EnemyCommit / AttackStartup`, `EnemyAttackActive`, `EnemyAttackRecovery` | Learn telegraph, answer, and punish | `ParryEligible`, `CounterOnParry`, optional `DodgePunishable`, optional `CounterOnWhiff` | Required |
| `Basic Attack B — Optional Spacing / Heavy Threat` | Add a second readable threat contrast | Same core attack states | Learn that not every threat is answered the same way | `DodgePunishable`, `SpacingCheck`, optional `Unparryable`, `CounterOnWhiff` | Optional |
| `Recovery / Punish Exposure` | Communicate enemy consequence | `EnemyAttackRecovery`, `EnemyPunishWindow` | Openings appear after commitment | `CounterOnWhiff`, `CounterOnParry` as authored | Required |
| `Stagger / Reaction` | Communicate meaningful player success | `EnemyStagger` | Correct answers change the enemy | Reaction-driven, not tag-driven | Recommended |
| `Reveal Beat / Memory Disruption` | Support reveal identity | `EnemyRevealBeat` | Combat exposes memory instability | Reveal-trigger context only | Recommended |
| `Reset / Re-Engage` | Return duel to readable rhythm | `EnemyIdle / Presence`, `EnemyApproach / Spacing` | The fight resets into another read | None | Required |

### 8.11 Relationship To Combat Core

Enemy actions expose readable intent, readable timing windows, and readable eligibility context. They tell the player what kind of danger is happening and whether a punish opportunity may exist, but they do not decide player combat truth.

`Combat Core` remains responsible for:

- validating player response
- validating hit resolution
- deciding dodge or parry success
- deciding whether `CounterWindow` opens
- deciding whether reveal request is valid

Enemy action data should therefore provide:

- attack tags
- telegraph windows
- commitment and recovery windows
- vulnerability and punish context

Those signals are inputs to Combat Core, not replacements for it.

### 8.12 Anti-Patterns

The following would weaken the first enemy action set:

- giving the first enemy too many attacks
- adding boss-like patterns
- adding fake-out attacks before basic readability works
- making both attacks look too similar
- making every action punishable in the same way
- enemy action directly opening counter without Combat Core validation
- adding `Basic Attack B` before `Basic Attack A` feels good
- reveal triggering from enemy action alone

The first enemy should teach, not overwhelm.

### 8.13 Open Questions

The following action-set questions remain unresolved:

- does M0 start with one attack or two?
- should `Basic Attack B` be included in the first playable prototype?
- should `Basic Attack B` be `Unparryable` or only `DodgePunishable`?
- does the first enemy need a distinct idle threat animation?
- is approach a real enemy action or just locomotion behavior?
- is punish exposure part of recovery or a separate action or state?
- is reveal beat an enemy action, a memory response, or a presentation overlay?

## 9. Telegraph Rules

This section defines how the M0 enemy communicates intent before an attack becomes active. Telegraph is the enemy’s fairness layer. It exists to support the player’s `read` phase in `read → evade/parry → counter → reveal` by making incoming threat visible, learnable, and emotionally coherent.

The goal of telegraphing is not to make combat trivial. The goal is to make failure understandable. If the player is hit, they should feel that the danger was visible and that their response failed for a reason they can explain.

### 9.1 Telegraph Purpose

Telegraph should allow the player to understand:

- that an attack is coming
- roughly when danger will arrive
- whether the attack is likely answered by dodge, parry, or spacing discipline
- when the enemy has meaningfully committed
- when the player should prepare a response

This means the telegraph must do more than announce motion. It must make the enemy legible. The player should feel that the enemy is declaring intent before striking, even if the exact answer still has to be learned through a few attempts.

### 9.2 M0 Telegraph Requirements

For M0, every enemy attack must have:

- a clear pre-impact cue
- readable duration
- a consistent timing relationship to the active hit
- distinct visual or motion language
- debug-visible telegraph state
- no instant hit from idle
- no hidden attack startup

For `Basic Attack A — Readable Slash`, the telegraph should be obvious enough for early tuning. It should teach the player the timing of parry or dodge without depending on subtle animation nuance. A tester should be able to learn its rhythm after only a few attempts.

The first implementation should favor clarity over style. If the telegraph is beautiful but unclear, it is not yet successful for M0.

### 9.3 Telegraph Channels

Telegraph can be communicated through several channels:

- body pose or stance shift
- weapon draw-back or windup
- forward lean or foot placement
- short pause before attack release
- eye or head focus if useful
- VFX accent, glow, shimmer, or outline
- audio cue
- debug label

For M0, body and weapon motion should be the primary telegraph channel. VFX, audio, and debug support may help reinforce readability, but the core read should still be understandable from enemy motion. The debug label is acceptable during tuning, but it should not become the only readable source of truth.

### 9.4 Telegraph Timing Rules

Telegraph must begin before the attack’s active hit window. That sounds obvious, but it is the central fairness rule of the system. The player must be given a readable pre-impact phase before actual danger is live.

Timing rules for M0:

- telegraph must begin before active frames
- telegraph duration should start generous, then tighten later if needed
- telegraph should not be so long that it loses tension
- telegraph-to-hit timing should remain consistent for a given attack
- active hit should match the expected release implied by the telegraph
- tuning should prioritize readability before difficulty

The player does not need to know numeric timing. They need to feel that the attack arrives when the enemy’s motion said it would.

### 9.5 Telegraph And Attack Tags

Telegraph should communicate attack eligibility when possible. The enemy should not merely have hidden tags; its presentation should support what those tags mean.

- `ParryEligible` attacks should look precise, direct, and deflectable
- `DodgePunishable` attacks should look committed and avoidable
- `Unparryable` attacks, if introduced later, need distinct visual language
- `SpacingCheck` attacks should clearly communicate range, sweep, or area pressure
- `CounterOnWhiff` attacks should show visible overcommitment or recovery consequence

For M0, `Basic Attack A` should prioritize `ParryEligible` clarity above everything else. If optional `CounterOnWhiff` support is used, it should only appear when the enemy’s recovery and overcommitment are clearly readable.

### 9.6 Telegraph And Commitment

Telegraph should lead cleanly into commitment. The player should feel that once they have seen the enemy preparing a specific attack, their read matters. In M0, this means the enemy should not freely cancel telegraphed commitment into something else just to surprise the player.

Rules:

- telegraph leads into commitment
- once commitment starts, the enemy should not freely cancel in M0
- the player should trust that a read has meaning
- fake-outs are deferred until basic readability works

This trust is essential. If telegraphs are unreliable, the whole duel loses fairness.

### 9.7 Telegraph Failure Cases

If the player fails during a telegraphed attack, the system should make that failure understandable. The player should be able to identify causes such as:

- reacted too early
- reacted too late
- chose the wrong answer
- stood at bad spacing
- attacked during visible threat
- ignored visible commitment

The system should avoid failures that feel random, invisible, or disconnected from the visible enemy behavior. A player getting hit is acceptable. A player feeling cheated by unreadable telegraphing is not.

### 9.8 Debug Requirements

The debug overlay should expose:

- telegraph active?
- telegraph time elapsed
- telegraph time remaining if available
- current attack id or name
- attack eligibility tags
- predicted active window if available
- commitment state
- whether the attack is parry-eligible
- whether the attack is dodge-punishable
- whether the attack is spacing-check-oriented
- last player response during telegraph

These tools are important because telegraph quality is often where combat “feels wrong” before the cause is obvious.

### 9.9 Telegraph Test Checklist

During testing, the team should check:

- can a fresh tester notice the enemy preparing an attack?
- can the tester learn the timing after a few attempts?
- does the active hit match what the telegraph promised?
- does parry or dodge failure feel explainable?
- do camera, VFX, and audio support the read rather than obscure it?
- does the enemy reset clearly after the threat?
- does debug data explain timing confusion?

If the answer to these questions is mostly no, the telegraph is not yet strong enough for M0.

### 9.10 Anti-Patterns

The following would undermine telegraph fairness in M0:

- instant attacks from idle
- hidden startup
- telegraph that only exists in debug
- telegraph that does not match active hit timing
- every attack having identical telegraph language
- overly subtle telegraph before M0 readability is proven
- VFX hiding weapon or body motion
- audio cue contradicting visual timing
- fake-outs before basic attack readability works
- camera angle hiding telegraph
- attack tags not being reflected in presentation at all

Telegraph should make the enemy more understandable, not more decorative.

### 9.11 Open Questions

The following telegraph-specific questions remain unresolved:

- how long should `Basic Attack A` telegraph be?
- is telegraph timing authored in data from day one?
- are VFX and audio support required for M0 telegraph readability, or only optional reinforcement?
- do attack eligibility tags need unique visual language immediately?
- is `Unparryable` telegraph language deferred?
- should debug gizmos show predicted hit range?
- can the first playable prototype rely on placeholder animations?

## 10. Attack Commitment Rules

This section defines when an enemy attack becomes committed, what commitment means for M0, and why it matters to fair `read → evade/parry → counter` play. Commitment is the trust boundary of the enemy system. It is the point where the player should believe that their read matters and that the enemy is now meaningfully following through on a chosen threat.

For M0, commitment should stay simple, visible, and trustworthy. The first enemy does not need advanced fake-outs, boss-style cancels, or deceptive complexity. It needs reliable follow-through so the player can learn.

### 10.1 Commitment Purpose

Attack commitment exists so that:

- player reads are meaningful
- telegraphs lead to predictable threat timing
- enemy mistakes can create punish opportunities
- dodge, parry, and counter outcomes feel fair
- enemy pressure does not feel random

Commitment should make the enemy feel deliberate rather than robotic or unfair. The goal is not to freeze the enemy into stiffness, but to give the player a reliable cause-and-effect relationship between reading intent and answering it.

### 10.2 When Commitment Begins

For M0, commitment begins when:

- the enemy has selected a specific attack
- the telegraph has clearly reached the point where the player can trust what is coming
- the enemy enters `EnemyCommit / EnemyAttackStartup`
- the attack’s path toward active frames is now locked enough for the player’s read to matter

This establishes four readable phases:

- `telegraph` is the warning phase
- `commit / startup` is the trust phase
- `active` is the danger phase
- `recovery / punish` is the consequence phase

The exact boundary between late telegraph and early commitment may still be tuned, but M0 should make that transition legible rather than ambiguous.

### 10.3 M0 Commitment Rules

For `Basic Attack A`:

- once committed, the enemy should not freely cancel into another attack
- the enemy should not instantly change direction unfairly
- the enemy should not skip active or recovery
- the enemy should proceed through `startup → active → recovery` unless interrupted by a valid combat result
- parry, counter, stagger, or defeat may interrupt commitment only if validated by Combat Core and enemy-side state rules

For optional `Basic Attack B`:

- commitment should be even more obvious if the move is slower or heavier
- if `Unparryable` is introduced later, both commitment and visual language must be very clear

The purpose of these rules is to keep the first enemy honest. The player should lose because they misread or mistimed their answer, not because the enemy changed its mind invisibly.

### 10.4 Allowed Interruptions

Commitment may be interrupted by:

- successful parry
- successful counter
- valid stagger result
- defeat or disabled result
- explicit debug reset or testing command

Commitment should not be interrupted by:

- random AI decision change
- presentation event alone
- VFX or audio timing
- camera event
- hidden difficulty adjustment
- unvalidated animation event

If the enemy exits commitment early, the reason must be mechanically real and debuggable.

### 10.5 Direction / Tracking Rules

Enemy direction and tracking should remain readable during commitment. In M0, the enemy may face or align toward the player before commitment begins, but once the attack is committed, tracking should be limited enough that the player’s dodge or spacing decision remains meaningful.

Provisional M0 rules:

- enemy may align toward the player before commitment
- once committed, tracking should be limited
- no unfair snap-turn during active hit
- if tracking exists, it must be readable and tuned carefully
- committed attacks should remain dodgeable or parryable according to their tags

This is especially important for the first attack. Over-tracking can make a readable telegraph feel dishonest, even if the timing itself is technically fair.

### 10.6 Recovery Commitment

Commitment does not end at the first active frame. After active frames resolve, the enemy should still carry consequence through recovery unless a valid interruption changes the result.

Rules:

- enemy should enter recovery after active frames unless interrupted
- recovery should not be skipped
- recovery creates readability and possible punish
- enemy should not instantly chain another attack in M0
- recovery length can be tuned, but it must remain debug-visible

This is what turns commitment into consequence. Without recovery, enemy mistakes are hard to read and punish.

### 10.7 Relationship To Attack Tags

Commitment should reinforce what attack tags mean:

- `ParryEligible`: committed timing should be reliable enough that the player can parry with trust
- `DodgePunishable`: commitment should create an avoidable line or timing path
- `CounterOnWhiff`: commitment and recovery should make whiff punish understandable
- `SpacingCheck`: commitment should clearly expose range, sweep, or area pressure
- `Unparryable`: if introduced later, commitment must be visually distinct and very readable

Tags should not only exist in data. Commitment behavior should help teach what those tags actually mean.

### 10.8 Player Trust Rules

The player should be able to trust the following sequence:

- telegraph means danger is coming
- commitment means the enemy will follow through
- active means the attack can hit
- recovery or punish means the player has earned a response opportunity
- failure came from timing, spacing, or choice rather than enemy cheating

This trust is the foundation of readable duel design. Without it, every successful answer feels uncertain and every failure feels suspect.

### 10.9 Debug Requirements

The debug overlay should expose:

- committed attack id or name
- commitment active?
- time since commitment began
- can the enemy cancel?
- tracking active?
- attack active?
- recovery active?
- punish window active?
- interruption source if commitment was interrupted
- reason if commitment was canceled or reset

These values are especially important during early feel tuning, because commitment bugs often present as “this enemy feels unfair” before the actual cause is obvious.

### 10.10 Anti-Patterns

The following patterns would break commitment trust in M0:

- enemy canceling attacks randomly
- enemy snapping to the player during active hit
- enemy skipping recovery
- telegraph leading into a different attack without clear rule
- fake-outs before baseline readability works
- difficulty systems shortening commitment invisibly
- presentation events changing commitment without validation
- every attack tracking perfectly
- commitment so long that combat loses tension
- commitment so short that the player cannot trust the read

Commitment should create confidence, not suspicion.

### 10.11 Open Questions

The following commitment questions remain unresolved:

- does commitment begin at telegraph start or after telegraph completes?
- can the enemy rotate during commitment?
- how much tracking should `Basic Attack A` have?
- are whiff recovery and normal recovery different?
- can successful light attacks interrupt commitment?
- can the enemy be staggered during telegraph?
- should optional `Basic Attack B` have stricter commitment rules than `Basic Attack A`?

## 11. Attack Eligibility Tags

This section defines the provisional enemy attack eligibility tags used by M0. These tags describe how an enemy attack can be answered and what kinds of punish or counter opportunities it may expose. They exist to keep the first duel readable, not to build a large generic ability-tag framework.

Tags are especially important because they help align enemy-side authored behavior with Combat Core’s resolution rules. They should be reflected in telegraph, commitment, recovery, debug visibility, and later presentation language so the player can eventually learn them through play rather than through hidden data.

### 11.1 `ParryEligible`

`ParryEligible` means an attack can be answered by a valid parry during `ParryActive`. If the player times the answer correctly, the attack can be interrupted, deflected, or otherwise resolved as a successful parry result, and that success can open `CounterWindow`.

Design purpose:

- teaches timing-based defense
- supports the precise duel fantasy of `Glass Refrain`
- creates a clean `read → parry → counter` path

M0 notes:

- `Basic Attack A` should likely be `ParryEligible`
- parry timing should start generous enough for early tuning
- the tag must be debug-visible

This is the most important first teaching tag for the M0 enemy.

### 11.2 `DodgePunishable`

`DodgePunishable` means the attack can be meaningfully avoided through dodge timing or spacing, and that if the enemy misses while committed, the player may gain punish or counter opportunity.

Design purpose:

- teaches spatial defense
- rewards positioning and timing
- prevents parry from becoming the only valid defensive answer

M0 notes:

- this can be optional on `Basic Attack A`
- it may be more appropriate for optional `Basic Attack B`
- it must not make dodge solve every attack by default

This tag is important for making the duel feel spatial instead of purely timing-based.

### 11.3 `CounterOnWhiff`

`CounterOnWhiff` means that if the attack misses because of player dodge or spacing and the enemy enters readable recovery, Combat Core may open or support `CounterWindow`.

Design purpose:

- makes enemy overcommitment readable
- rewards clean dodge or spacing answers
- connects whiff punish to the counter loop

M0 notes:

- should require clear recovery and punish visibility
- should not trigger from every minor miss unless explicitly authored

This tag makes the enemy’s mistakes feel meaningful rather than cosmetic.

### 11.4 `CounterOnParry`

`CounterOnParry` means that a successful parry against the attack can open `CounterWindow`.

Design purpose:

- makes parry success immediately rewarding
- creates a clean parry-to-counter teaching path
- turns precise defense into a readable offensive payoff

M0 notes:

- `Basic Attack A` should likely use this tag
- parry success feedback must be clear

This is the clearest reward tag for the first duel prototype.

### 11.5 `SpacingCheck`

`SpacingCheck` means the attack tests the player’s position, range, or angle more than pure timing. The best answer may be staying out of range, moving laterally, or dodging early enough to avoid the line or area of danger.

Design purpose:

- prevents combat from becoming only reaction timing
- makes spacing part of reading
- gives the enemy another readable kind of threat without adding complexity for its own sake

M0 notes:

- optional for `Basic Attack B`
- only include if range and readability can be communicated clearly
- should not be required for the first implementation if it adds noise

This tag should only appear when the enemy’s spatial threat can actually be read.

### 11.6 `Unparryable`

`Unparryable` means the attack cannot be parried even if the player uses `ParryActive`. The player must answer with dodge, spacing, or another future defensive rule.

Design purpose:

- creates defensive variety later
- prevents parry from solving everything
- encourages the player to read more than one kind of answer pattern

M0 notes:

- optional and likely deferred unless visual language is very clear
- must have distinct telegraph and presentation support
- should not be introduced before baseline parry readability already works

This tag is powerful and easy to misuse. It should be deferred unless it helps readability rather than hurting it.

### 11.7 Tag Combination Rules

For M0, tag combinations should remain simple. One attack should not attempt to teach every defensive lesson at once.

Allowed or useful simple combinations:

- `ParryEligible + CounterOnParry`
- `DodgePunishable + CounterOnWhiff`
- `ParryEligible + CounterOnParry + optional CounterOnWhiff`
- optional `SpacingCheck + DodgePunishable`

Combination restriction:

- `Unparryable` should not combine with `ParryEligible`

M0 rule:

- `Basic Attack A` should prioritize one clear lesson first
- tags should stay small and legible
- contrast between attacks is more useful than density on one attack

### 11.8 Recommended Tag Setup For M0

Recommended setup:

`Basic Attack A`

- `ParryEligible`
- `CounterOnParry`
- optional `CounterOnWhiff` only if recovery is already clearly readable

Optional `Basic Attack B`

- `DodgePunishable`
- `CounterOnWhiff`
- optional `SpacingCheck`
- `Unparryable` only if distinct visual language is available

This recommendation keeps the first attack focused on teaching parry confidence, while a second optional attack, if added later, teaches dodge or spacing without overloading the first playable version.

### 11.9 Relationship To Combat Core

Attack tags do not apply damage, do not directly open `CounterWindow`, and do not decide outcomes by themselves. They inform Combat Core resolution.

Combat Core should still validate:

- player state
- timing window
- vulnerability
- enemy attack tags
- whether a hit, dodge, parry, punish, or counter result is valid

Tags are therefore inputs into authoritative combat resolution, not replacements for it.

### 11.10 Relationship To Presentation

Attack tags should eventually be readable through animation, VFX, audio, camera support, or some combination of those channels. During M0 tuning, debug labels are acceptable and useful, but the final player understanding should not rely only on debug overlays.

`Unparryable` especially requires strong visual language if it is ever used. A move that is mechanically unparryable but visually appears parryable would damage player trust immediately.

Presentation should reinforce tags. It should not contradict them.

### 11.11 Debug Requirements

The debug overlay should expose:

- current attack tags
- parry eligible?
- dodge punishable?
- counter on whiff?
- counter on parry?
- spacing check?
- unparryable?
- tag-based reason for accepted or rejected player answer

This visibility helps distinguish “the player answered badly” from “the attack was not authored for that answer.”

### 11.12 Tag Table

| Tag | Meaning | Player Lesson | Can Open Counter? | M0 Priority | Presentation Requirement |
|------|---------|---------------|-------------------|-------------|--------------------------|
| `ParryEligible` | Attack can be answered by valid parry timing | Some threats are best answered precisely | Indirectly, usually with `CounterOnParry` | Required | Should look precise and deflectable |
| `DodgePunishable` | Attack can be avoided and punished through spatial answer | Some threats are best answered by movement and spacing | Indirectly, often with `CounterOnWhiff` | Recommended | Should look committed and avoidable |
| `CounterOnWhiff` | Missed committed attack may support counter opportunity | Enemy overcommitment creates offense | Yes | Recommended | Requires readable whiff and recovery |
| `CounterOnParry` | Successful parry may support counter opportunity | Clean parry creates immediate reward | Yes | Required | Needs clear parry-success feedback |
| `SpacingCheck` | Attack tests position, range, or angle | Spacing is part of reading | Sometimes | Optional | Must communicate area or line threat clearly |
| `Unparryable` | Attack cannot be answered by parry | Not every threat is solved by timing alone | Usually via other tags and conditions | Deferred | Must have strong distinct visual language |

### 11.13 Anti-Patterns

The following would undermine tag clarity in M0:

- every attack having every tag
- tags contradicting telegraph language
- `Unparryable` attacks looking parryable
- `CounterOnWhiff` triggering without visible recovery
- `DodgePunishable` making dodge solve everything
- `ParryEligible` making parry solve everything
- tags being hidden from debug
- tags directly deciding results without Combat Core validation
- changing tags dynamically without readable presentation

The point of tags is to simplify and clarify authored intent, not to create invisible rule soup.

### 11.14 Open Questions

The following tag questions remain unresolved:

- should `Basic Attack A` also be `CounterOnWhiff`?
- is `Basic Attack B` needed in the first playable prototype?
- is `Unparryable` deferred entirely until after M0?
- does `SpacingCheck` need range gizmos or other debug visualization?
- are tags authored data from day one?
- is tag presentation language required before the first real playtest?
- should tag combinations be validated by future tooling?

## 12. Dodge / Parry / Counter Interaction Rules

This section defines how M0 enemy attacks interact with the player’s dodge, parry, and counter responses. `Enemy Intent & Telegraph` does not validate combat outcomes by itself. Instead, it exposes readable intent, readable attack tags, readable punish conditions, and readable opportunity states so that `Combat Core` can validate results in a trustworthy way.

The design goal is simple: when the player answers correctly, enemy-side behavior should make that success visible; when the player answers incorrectly, enemy-side behavior should make failure understandable.

### 12.1 Interaction Purpose

Dodge, parry, and counter interactions exist to make the enemy readable and answerable. They should support:

- `read → evade/parry → counter → reveal`
- fair failure
- clear success feedback
- meaningful enemy commitment
- readable punish windows

The enemy should not simply exist to be hit. It should create a structured conversation of threat, answer, and consequence.

### 12.2 Dodge Interaction

Dodge is the player’s spatial answer. From the enemy side, this means the attack must present a readable trajectory, readable range, and readable timing path that can be meaningfully avoided when the attack is authored to allow it.

Enemy-side requirements:

- the attack must have readable trajectory, range, or timing
- a committed attack must be avoidable if tagged `DodgePunishable` or `CounterOnWhiff`
- the enemy should not snap-turn unfairly during active frames
- whiff and recovery must be visible if dodge can lead to punish or counter
- `DodgePunishable` attacks should expose clear overcommitment

Dodge success may lead to:

- enemy whiff
- enemy recovery
- `EnemyPunishWindow`
- possible `CounterWindow` if Combat Core validates `CounterOnWhiff`

Dodge failure may happen if:

- the player dodges too early
- the player dodges too late
- the player dodges into attack range
- the attack was not intended to be dodge-punishable
- the enemy active hit still connects

The important enemy-side rule is that correct dodge should produce visible enemy consequence when authored to do so.

### 12.3 Parry Interaction

Parry is the player’s timing answer. From the enemy side, the attack must be learnable enough that the player can trust parry timing and know when they were correct.

Enemy-side requirements:

- the attack must be tagged `ParryEligible`
- attack timing must be consistent enough to learn
- telegraph must clearly support parry timing
- parry success should visibly affect the enemy
- parry failure should be explainable

Parry success may lead to:

- enemy deflect, stagger, or hesitation
- `EnemyStagger` or `EnemyPunishWindow`
- `CounterWindow` if Combat Core validates `CounterOnParry`
- possible reveal request after successful counter

Parry failure may happen if:

- the player parries too early
- the player parries too late
- the attack is not `ParryEligible`
- the attack is `Unparryable`
- the player is in the wrong state
- the enemy active hit connects after failed parry

Parry should feel like the cleanest read path in M0, which means the enemy must react clearly when that read succeeds.

### 12.4 Counter Interaction

Counter is the player’s reward answer after correct defensive play. From the enemy side, counter only makes sense if the enemy has visibly exposed a punishable state, vulnerable recovery, stagger, or other valid opening.

Enemy-side requirements:

- the enemy must expose a valid punish, stagger, or recovery condition
- the counter target should remain readable and reachable where possible
- the enemy should provide a clear reaction on counter hit
- counter success may support reveal request
- counter should never trigger from enemy-side state alone without Combat Core validation

Counter success may lead to:

- `EnemyStagger`
- optional `EnemyRevealBeat`
- temporary rhythm disruption
- reveal request context
- reset or re-engage after feedback

Counter failure may happen if:

- the player misses `CounterWindow`
- counter whiffs because of spacing
- the enemy is no longer vulnerable
- Combat Core rejects the counter input
- the player attempted counter without a valid opening

From the enemy side, the key job is to make valid openings readable and to react strongly enough that counter feels earned.

### 12.5 Enemy Reaction To Player Answers

When the player dodges correctly:

- the enemy may whiff
- the enemy may enter recovery or punish window
- the enemy should not instantly cancel its mistake

When the player parries correctly:

- the enemy should show deflect, stagger, or hesitation
- the attack should be interrupted or neutralized if Combat Core validates it
- the counter opportunity should be clear

When the player counters successfully:

- the enemy should react more strongly than on a normal hit
- the enemy may briefly show memory disruption
- the reveal hook may be requested
- the enemy should return to readable reset after the reaction

When the player fails:

- the enemy attack should resolve clearly
- player failure should feel caused by timing, spacing, or wrong answer
- the enemy should still reset enough for re-reading

These reactions are what make interaction outcomes emotionally legible.

### 12.6 Interaction Table

| Player Response | Enemy Requirement | Success Result | Failure Result | CounterWindow? | Reveal Support? |
|------|-------------------|----------------|----------------|----------------|-----------------|
| Dodge vs `DodgePunishable` attack | Readable commitment, whiffable line/timing, visible recovery | Enemy whiff or recovery exposes punish | Player is still clipped or dodges poorly | Sometimes, if `CounterOnWhiff` and Combat Core validate | Indirect, through later counter |
| Dodge vs non-`DodgePunishable` attack | Attack remains readable but is not authored as clean dodge punish | Survival may occur, but punish not guaranteed | Player may still be hit or gain no punish | Usually no | No direct support |
| Parry vs `ParryEligible` attack | Clear telegraph, reliable timing, readable enemy reaction | Deflect, stagger, or punish exposure | Failed timing results in hit or lost opportunity | Yes, if `CounterOnParry` and Combat Core validate | Indirect, through later counter |
| Parry vs `Unparryable` / non-`ParryEligible` attack | Distinct authored restriction and readable presentation | Usually no parry success; player must use another answer | Player is punished or loses opportunity | No | No direct support |
| Counter during valid `EnemyPunishWindow` | Enemy is visibly vulnerable and reachable | Strong enemy reaction, possible stagger, possible reveal support | Counter misses or is rejected if spacing/timing is wrong | Already open or supported | Yes, if counter success is meaningful |
| Counter outside valid opening | No valid enemy vulnerability state | No valid result; Combat Core rejects or counter whiffs | Player loses timing and may be exposed | No | No |
| Light attack during enemy telegraph | Telegraph is still readable and commitment not yet protected beyond authored rules | Possibly interrupts only if later allowed and authored | Usually loses to commitment if mistimed | Usually no | No |
| Light attack during enemy active threat | Enemy is already in real hit window | Usually not a valid answer | Player gets hit or loses trade | No | No |

### 12.7 Relationship To Attack Tags

Attack tags define what kinds of responses are valid or emphasized:

- `ParryEligible` enables parry success checks
- `CounterOnParry` allows `CounterWindow` after valid parry
- `DodgePunishable` supports spatial answer and readable avoidance
- `CounterOnWhiff` allows `CounterWindow` after valid whiff or punish exposure
- `SpacingCheck` tests player range and positioning
- `Unparryable` rejects parry but must be readable

Tags tell Combat Core what kind of interaction is potentially valid. They do not decide success by themselves.

### 12.8 Relationship To Combat Core

Combat Core remains the authority on:

- player state validation
- dodge, parry, and hit success
- vulnerability checks
- hit resolution
- `CounterWindow`
- reveal request validity

`Enemy Intent & Telegraph` provides:

- readable threat
- readable windows
- readable tags
- readable punish conditions
- readable enemy-side reaction opportunities

This boundary must stay clear. Enemy-side rules support Combat Core, but do not replace it.

### 12.9 Debug Requirements

The debug overlay should expose:

- player response attempted
- enemy current state
- current attack tags
- dodge success or failure reason
- parry success or failure reason
- counter success or failure reason
- enemy whiff detected?
- enemy punish window active?
- `CounterWindow` opened?
- reveal request triggered?
- last interaction result

This data is critical because interaction bugs often feel like “combat is unfair” until the actual reason becomes visible.

### 12.10 Anti-Patterns

The following patterns would break M0 interaction clarity:

- dodge success with no visible enemy whiff or recovery
- parry success with no enemy feedback
- counter opening with no readable cause
- enemy instantly canceling after being correctly dodged
- `Unparryable` attack punishing parry without clear presentation
- every attack supporting every answer
- counter triggering from enemy state without Combat Core validation
- player failure feeling random instead of explainable
- reveal triggering before counter success is confirmed

Each answer should feel grounded in enemy-side truth, not hidden exceptions.

### 12.11 Open Questions

The following interaction questions remain unresolved:

- does dodge success open `CounterWindow` directly, or only through enemy whiff and punish state?
- does parry always interrupt `EnemyAttackActive`, or only specific attacks?
- does parry success enter `EnemyStagger` or `EnemyPunishWindow`?
- does counter target auto-align, or does it require spacing discipline?
- can light attacks interrupt `EnemyTelegraph`?
- does failed parry always lead to punish vulnerability?
- should successful dodge have a distinct enemy hesitation animation?

## 13. Punish Window Rules

This section defines when and how the M0 enemy becomes punishable after a committed action, whiff, parry, stagger, or recovery. `Enemy Intent & Telegraph` exposes punish opportunity by making enemy vulnerability readable. `Combat Core` still decides whether the player’s answer becomes a valid `CounterWindow`, a valid hit, or a failed punish.

The main design goal is that punish windows feel earned. The player should understand that the enemy is open because of commitment, mistake, or successful defensive read, not because of arbitrary hidden generosity.

### 13.1 Punish Window Purpose

Punish windows exist to:

- reward correct reading
- make enemy commitment meaningful
- create fair counter opportunities
- teach the player when an enemy has made a mistake
- support `read → evade/parry → counter → reveal`

Punish should feel earned rather than random. The player should understand why the enemy became vulnerable and why the opportunity exists only for a limited time.

### 13.2 What Can Create A Punish Window In M0

Punish windows may be created by several simple sources in M0.

#### Committed Attack Recovery

The enemy finishes active frames and enters recovery. That recovery may expose vulnerability if the attack was committed enough to create consequence.

#### Whiffed Attack

The enemy attack misses because of player dodge or spacing. This is especially important if the attack is authored with `CounterOnWhiff` or `DodgePunishable`, because those tags imply readable overcommitment and follow-through.

#### Successful Parry

The enemy attack is interrupted, deflected, or destabilized by a valid parry. This may place the enemy into `EnemyStagger` or a more explicit `EnemyPunishWindow`.

#### Successful Counter Hit

The enemy is struck by a meaningful counter and enters a stronger reaction state. This may support reveal-related feedback and enemy-side disruption.

#### Enemy Overcommitment

The enemy uses an authored committed action with visible recovery or vulnerability consequence, even if the result is not a full stagger.

Punish windows should not be created by:

- random idle state
- generic VFX event
- hidden AI state
- unvalidated animation event
- passive time passing

If the enemy becomes open, there should be a readable reason.

### 13.3 Punish Window Visibility Rules

A punish window should be visible through one or more of the following:

- enemy pose or recovery animation
- brief hesitation
- stagger reaction
- readable overcommitment
- VFX or audio support if useful
- debug label during M0

The player should understand three things:

- the enemy is temporarily open
- the opening was caused by correct reading or enemy commitment
- the opening will expire

If the punish window exists only mechanically and not readably, the duel becomes harder to learn.

### 13.4 Relationship To `CounterWindow`

`EnemyPunishWindow` and player `CounterWindow` are related, but they are not identical.

- `EnemyPunishWindow` means the enemy is exposed
- `CounterWindow` means Combat Core allows the player’s counter response

This distinction matters because not every enemy vulnerability must become a special counter opportunity. An enemy may be open to a normal punish without always granting the stronger counter path.

Combat Core should validate:

- player state
- timing
- spacing
- attack tags
- enemy punish context

before opening or accepting `CounterWindow`.

### 13.5 M0 Punish Window Types

For M0, the following provisional punish types are enough:

#### `RecoveryPunish`

The enemy is recovering after a committed attack. This may allow a normal punish and may or may not open `CounterWindow` depending on the authored interaction.

#### `WhiffPunish`

The enemy missed because of dodge or spacing. This may open `CounterWindow` if `CounterOnWhiff` is present and the recovery is visibly punishable.

#### `ParryPunish`

The enemy has been deflected or staggered after successful parry. This should usually support `CounterWindow` if `CounterOnParry` is present.

#### `CounterStagger`

The enemy is staggered after a successful counter. This may support `RevealBeat` or memory response and should feel like a stronger success state than normal punish.

#### `DefeatPunish / Disabled`

The enemy is defeated or disabled. This may trigger reveal if accepted by `Memory State`, but it is an encounter endpoint rather than a recurring punish loop.

### 13.6 Punish Duration Philosophy

For M0, punish windows should start generous enough to teach the loop. They should become stricter only after readability is already proven.

Rules:

- start generous enough for learning
- shorten only after the player can reliably read the enemy
- punish window should not be so long that counter feels automatic
- punish window should not be so short that testers miss the lesson
- duration should be debug-visible
- different punish sources may later have different durations, but M0 should stay simple

The goal is to teach the player that correct defense creates opportunity, not to create free damage phases with no timing tension.

### 13.7 Punish Expiration Rules

When punish expires:

- the enemy should return to readable reset, idle, or approach behavior
- the player should lose special counter opportunity if `CounterWindow` expires
- the enemy should not instantly chain into unfair pressure
- expiration should be debuggable
- if the player misses the window, failure should still be explainable

Missed punish should feel like “I was too slow” or “I was too far,” not “the game took the opening away invisibly.”

### 13.8 Punish Window Table

| Punish Source | Enemy State | Visibility Cue | Can Open `CounterWindow`? | Reveal Support? | M0 Notes |
|------|-------------|----------------|---------------------------|-----------------|----------|
| normal attack recovery | `EnemyAttackRecovery` | committed follow-through, visible recovery | Sometimes | No direct support | Basic readable consequence |
| whiffed `DodgePunishable` attack | `EnemyAttackRecovery` or `EnemyPunishWindow` | visible miss and overcommitment | Sometimes | Indirect, through later counter | Good for teaching dodge reward |
| whiffed `CounterOnWhiff` attack | `EnemyPunishWindow` | clear whiff plus exposed recovery | Yes | Indirect, through later counter | Strongest whiff-punish teaching case |
| successful parry | `EnemyStagger` or `EnemyPunishWindow` | deflect, hesitation, stagger | Yes, if `CounterOnParry` | Indirect, through later counter | Primary parry teaching case |
| successful counter hit | `EnemyStagger` | strong enemy reaction | Already resolving or no new window needed | Yes | May support `EnemyRevealBeat` |
| enemy defeat / disabled | `EnemyDefeated / Disabled` | collapse, disable, or endpoint state | No further counter expected | Yes, if Memory State accepts | Encounter-ending case |

### 13.9 Debug Requirements

The debug overlay should expose:

- punish window active?
- punish source
- punish type
- time in punish window
- time remaining if available
- related attack id or name
- related attack tags
- can open `CounterWindow`?
- did `CounterWindow` open?
- why punish window expired
- last punish or counter result

These values make it easier to tell whether the problem is enemy readability, timing leniency, or Combat Core acceptance.

### 13.10 Anti-Patterns

The following patterns would weaken punish readability in M0:

- punish window existing only in code or debug but not readably
- recovery being too short to punish
- every recovery granting special counter
- punish window opening without clear cause
- enemy instantly attacking again after a whiff
- parry success with no visible enemy vulnerability
- `CounterWindow` and `EnemyPunishWindow` being treated as the same thing without validation
- punish windows so long that they remove tension
- punish windows so short that they cannot teach the loop
- reveal triggering from punish state before counter success

Punish should be readable consequence, not invisible generosity.

### 13.11 Open Questions

The following punish-specific questions remain unresolved:

- should `EnemyPunishWindow` be a separate state or part of recovery?
- can normal recovery be punished with light or heavy but not counter?
- does `CounterWindow` open automatically on `ParryPunish`?
- does `WhiffPunish` require `CounterOnWhiff`?
- is punish duration fixed or data-authored?
- should punish window be visually indicated in M0?
- can the enemy transition from punish directly to stagger if hit late?

## 14. Enemy Hit Reaction / Stagger Contract

This section defines how the M0 enemy reacts to light hits, heavy hits, parries, counters, stagger, defeat, and reveal-supporting disruption. The purpose is not to build a full poise or stagger architecture. The purpose is to make player success visible and emotionally legible in the first duel prototype.

Enemy reaction should support the rhythm `calm → threat → answer → punish/reveal → reset`. Reactions must be strong enough to communicate success, but restrained enough that the duel does not collapse into stun-lock loops or spectacle spam.

### 14.1 Contract Purpose

Enemy hit reaction and stagger exist to:

- communicate player success
- make parry and counter feel meaningful
- support punish readability
- support reveal feedback
- preserve the `calm → threat → answer → punish/reveal → reset` rhythm

The enemy should visibly acknowledge that something meaningful happened. If the player answers correctly and the enemy feels unchanged, the loop loses emotional clarity.

### 14.2 Reaction Categories

For M0, the following provisional reaction categories are enough:

- `NoReaction`
- `LightHitReact`
- `HeavyHitReact`
- `ParryStagger`
- `CounterStagger`
- `Defeat / Disabled`
- optional `RevealDisruption`

These categories are intentionally small. M0 does not need a rich layered poise model to prove feel.

### 14.3 Light Hit Reaction

`LightHitReact` exists to communicate contact and modest player success. It should make hits feel real without overpowering enemy commitment or becoming the basis of stun-lock behavior.

M0 rules:

- light attack may cause small reaction if the enemy is vulnerable
- light attack should not always interrupt committed attacks
- light reaction should not become the basis of repeated control-lock loops

This reaction should tell the player “you connected,” not “you solved the encounter.”

### 14.4 Heavy Hit Reaction

`HeavyHitReact` exists to communicate stronger commitment and reward. It should feel heavier and more consequential than light hit reaction, while still staying within the readable pace of M0.

M0 rules:

- heavy hit reaction should feel stronger than light hit reaction
- it may interrupt vulnerable enemy states more clearly
- it should still preserve player-side risk if the heavy attack was badly timed or whiffed

This reaction should signal meaningful impact without becoming a full stagger system.

### 14.5 Parry Stagger

`ParryStagger` communicates successful timing defense. It is the enemy-side proof that the player did not merely survive the attack, but answered it precisely.

M0 rules:

- parry stagger should be clear and immediate
- it should usually support `CounterWindow` if the attack has `CounterOnParry`
- it should not last so long that counter becomes automatic

This reaction is one of the most important teaching tools in the prototype. If parry success does not visibly change the enemy, the player will struggle to trust the mechanic.

### 14.6 Counter Stagger

`CounterStagger` is the strongest enemy-side success reaction in M0. It exists to communicate that the player earned a meaningful offensive payoff after correct reading and defense.

M0 rules:

- counter stagger should feel stronger than normal hit reaction
- it may support reveal request context
- it should stay short, readable, and emotionally restrained
- it should transition into reset or reveal-supporting feedback rather than into long helplessness

This is the emotional high point of the M0 duel loop and should feel distinct from ordinary contact.

### 14.7 Defeat / Disabled

`Defeat / Disabled` is the endpoint reaction where the enemy is no longer an active threat in the M0 encounter.

M0 rules:

- a placeholder defeat or disable result is acceptable
- it may support reveal if `Memory State` accepts it
- no full death consequence or narrative-state system is required yet

This category only needs to make the encounter endpoint readable.

### 14.8 Reveal Disruption

`RevealDisruption` is an optional reaction category used to show memory or emotional fracture after meaningful counter success or defeat. It exists to bridge enemy reaction with the reveal identity of `Glass Refrain`.

M0 rules:

- optional
- should not become a cutscene
- should not hide the next enemy read
- may be handled as presentation overlay or explicit enemy state; the final choice remains open

This reaction should hint at instability rather than replace combat with narrative interruption.

### 14.9 Stagger Duration Philosophy

For M0, stagger and reaction duration should begin readable and generous enough to teach the loop, then tighten only after the intended interaction is already understood.

Rules:

- start readable and generous
- avoid long stun-locks
- keep counter timing clear
- tune with debug overlay active
- reaction duration may be fixed at first and become data-authored later

The goal is to make reaction teachable, not to maximize control denial.

### 14.10 Debug Requirements

Debug should expose:

- current reaction category
- stagger active?
- stagger source
- time in stagger
- interruption source
- can the enemy be hit again?
- can the enemy recover?
- did the reaction support `CounterWindow`?
- did the reaction support reveal request?

These values help the team distinguish between “the enemy reacted weakly,” “the enemy was not supposed to react,” and “the reaction happened but the follow-up rule failed.”

### 14.11 Anti-Patterns

The following patterns would weaken enemy-side reaction clarity in M0:

- every light hit staggering the enemy
- long stun-lock loops
- parry success with weak or invisible feedback
- counter reaction feeling like a normal hit
- reveal disruption hiding combat readability
- physics or ragdoll deciding combat truth
- reaction duration being impossible to debug
- boss-style poise complexity in M0

Reactions should clarify the duel, not drown it in systems.

### 14.12 Open Questions

The following reaction questions remain unresolved:

- can light attacks interrupt telegraph?
- can heavy attacks interrupt commitment?
- are `ParryStagger` and `EnemyPunishWindow` separate or overlapping concepts?
- does `CounterStagger` always request reveal?
- are reaction durations fixed or data-authored?
- can the enemy be hit repeatedly during stagger?
- does defeat always trigger reveal response?

## 15. Emotional Intent Placeholder

This section defines the minimum emotional tone and rhythm the M0 enemy should express without becoming a full emotional AI system. The goal is not to build advanced memory-driven behavior yet. The goal is to make the first enemy feel appropriate to `Glass Refrain` rather than like a generic combat dummy.

For M0, emotional intent should remain simple and mostly expressed through rhythm, hesitation, pose, and reaction. It should support readability, not compete with it.

### 15.1 Placeholder Purpose

The emotional intent placeholder exists to:

- give the first enemy a restrained emotional identity
- support the sad and mysterious tone of `Glass Refrain`
- make enemy rhythm feel deliberate rather than random
- connect combat readability to memory or emotional presence
- prepare space for future `Memory State` integration

Even in a prototype, the enemy should feel like a presence trapped inside a distorted memory rather than a mechanically neutral dummy.

### 15.2 M0 Emotional Direction

The first enemy should feel:

- deliberate
- haunted
- restrained
- readable
- tense
- slightly hesitant
- emotionally fractured, but not chaotic

It should not feel:

- like a generic punching bag
- like a berserker
- like a comedy enemy
- like a complex boss
- like a fully narrative character yet

The emotional goal is melancholy under pressure, not explosive personality.

### 15.3 Emotional Rhythm

The M0 enemy rhythm should follow this shape:

- calm presence
- measured approach
- visible hesitation or pause before attack
- committed burst of threat
- brief vulnerability after mistake
- restrained stagger or reveal disruption
- readable reset

This supports the larger project rhythm:

`calm → threat → answer → punish/reveal → reset`

Emotion in M0 should therefore feel like a pacing quality, not a separate behavior system.

### 15.4 How Emotion Affects Intent In M0

For M0, emotional intent may affect:

- idle pose
- hesitation before telegraph
- attack pacing
- recovery posture
- stagger reaction
- reveal disruption
- reset timing

It should not yet affect:

- complex attack selection
- dynamic difficulty
- multi-phase behavior
- full memory-state branching
- narrative dialogue
- district reinterpretation

This keeps emotion present in the duel without allowing it to become an uncontrolled source of rules complexity.

### 15.5 Default Emotional State

M0 should use one default placeholder emotional state:

`Default / Haunted Restraint`

Meaning:

- the enemy is not fully aggressive
- the enemy seems bound to repeat a remembered action
- attacks feel ritual-like or memory-like
- hesitation suggests emotional residue
- the enemy still remains readable and testable

This is not a full emotional state machine. It is a single tonal baseline that helps the first duel feel appropriate for the project.

### 15.6 Relationship To Memory Reveal

Emotional intent should support reveal by making successful counter feel like it disrupted something more fragile than ordinary combat posture. The enemy should seem momentarily disturbed, fractured, or exposed in a way that hints at memory instability.

For M0:

- reveal response can briefly intensify hesitation, shimmer, or disruption
- enemy rhythm may reset slightly differently after reveal, but this is optional
- no full memory progression is required yet

The key point is that reveal should feel connected to the enemy’s emotional presence, not bolted on after the fact.

### 15.7 Presentation Suggestions

Possible placeholder expressions include:

- slight idle sway
- weapon lowered before sudden commitment
- pause before slash
- brief head or shoulder twitch
- short shimmer on counter stagger
- quiet audio sting on reveal
- restrained VFX pulse
- slow reset back to presence

These are suggestions only. Presentation does not own combat truth. It only helps communicate emotional tone.

### 15.8 Debug Requirements

The debug overlay should expose:

- current emotional placeholder state
- emotional rhythm active?
- hesitation active?
- reveal disruption active?
- rhythm modifier if any
- last reveal influence if used

For M0, this can remain minimal. The point is to help the team verify that emotional placeholder behavior is not accidentally making the enemy unreadable.

### 15.9 Anti-Patterns

The following patterns would push emotional placeholder work beyond M0 or weaken readability:

- building full emotional AI in M0
- adding random attack behavior just to seem emotional
- making hesitation so long that combat loses tension
- making emotion obscure telegraph clarity
- changing attack timing invisibly for mood
- using reveal disruption to hide the next read
- making the enemy too passive
- making the enemy too chaotic
- tying emotion to narrative progression too early

Emotion should enrich the duel, not destabilize it.

### 15.10 Open Questions

The following emotional-placeholder questions remain unresolved:

- should the first enemy visibly hesitate before every attack?
- should emotional rhythm affect timing values in M0?
- does reveal change enemy rhythm after success?
- is emotional state debug-only or authored data?
- should the default state be called `Haunted Restraint` or something else?
- is emotional expression mostly animation, VFX, audio, or timing?
- does `Memory State` own emotional rhythm later?

## 16. Debug / Readability Requirements

This section defines what `Enemy Intent & Telegraph` must expose so M0 enemy behavior can be tested, tuned, and understood. Debug visibility is required for M0. Enemy readability cannot be tuned blind, because many failures that feel like “combat is unfair” are actually telegraph, commitment, punish, or tag-clarity issues.

Debug systems may observe enemy state and interaction data, but they must not become the owner of combat truth.

### 16.1 Debug Purpose

Debug should help designers and testers answer:

- what is the enemy currently trying to do?
- is the enemy telegraphing?
- has the enemy committed?
- when is the attack active?
- when is the enemy recovering?
- when is the enemy punishable?
- what tags does the current attack have?
- why did dodge, parry, or counter work or fail?
- did stagger or reveal disruption happen?

If the team cannot answer these questions quickly during tuning, the enemy system is not observable enough for M0.

### 16.2 Required Enemy State Debug Data

The system should expose:

- current enemy state
- previous enemy state
- time in current state
- current loop phase
- current attack id or name
- target actor if any
- enemy vulnerable?
- enemy can be interrupted?
- enemy can recover?
- enemy defeated or disabled?

This gives the team a stable baseline for understanding what the enemy believes it is doing at any moment.

### 16.3 Required Telegraph Debug Data

The system should expose:

- telegraph active?
- telegraph elapsed time
- telegraph remaining time if available
- telegraph source attack
- telegraph channel used if useful
- predicted active window if available
- last player response during telegraph

These values are especially important during early readability tuning, where the difference between “too subtle” and “too short” may not be obvious from feel alone.

### 16.4 Required Commitment Debug Data

The system should expose:

- commitment active?
- committed attack id or name
- time since commitment began
- can enemy cancel?
- tracking active?
- tracking limit if available
- interruption source if interrupted
- cancel or reset reason if any

This helps the team verify that commitment is trustworthy and that the enemy is not escaping consequence invisibly.

### 16.5 Required Attack Window Debug Data

The system should expose:

- startup active?
- attack active?
- recovery active?
- active hit window elapsed
- recovery elapsed
- related attack tags
- hit resolved?
- whiff detected?
- player response result if any

These values make it possible to correlate the enemy’s action timeline with Combat Core’s resolution timeline.

### 16.6 Required Attack Tag Debug Data

The system should expose the current attack tags:

- `ParryEligible`
- `DodgePunishable`
- `CounterOnWhiff`
- `CounterOnParry`
- `SpacingCheck`
- `Unparryable`

It should also expose:

- tag-based reason for accepted or rejected player answer
- invalid tag combinations if detected later by tooling or validation

Tags are too important to remain hidden during M0 tuning.

### 16.7 Required Punish / Counter Debug Data

The system should expose:

- `EnemyPunishWindow` active?
- punish source
- punish type
- punish elapsed time
- punish remaining time if available
- can support `CounterWindow`?
- did Combat Core open `CounterWindow`?
- why punish expired
- last punish or counter result

This is critical because “enemy is open” and “player can special-counter now” are related but not identical concepts.

### 16.8 Required Stagger / Reveal Debug Data

The system should expose:

- current reaction category
- stagger active?
- stagger source
- stagger elapsed time
- can enemy be hit again?
- reaction supports `CounterWindow`?
- reveal disruption active?
- reveal request supported?
- reveal request accepted or rejected if known
- last reveal influence if used

These values help separate ordinary hit feedback from the stronger success states that matter for reveal.

### 16.9 Required Emotional Placeholder Debug Data

The system should expose:

- current emotional placeholder state
- hesitation active?
- emotional rhythm active?
- rhythm modifier if any
- reveal influence on rhythm if any

For M0, this can remain simple. The point is only to ensure that emotional placeholder behavior is not silently changing readability.

### 16.10 Debug Presentation Modes

For M0, debug can be presented through:

- on-screen text overlay
- state labels
- timing labels
- simple tag list
- optional gizmos for attack range or hit area later
- console logs only as secondary support

This does not need polished UI. The debug overlay should not be treated as part of the final HUD design.

### 16.11 Readability Test Checklist

During testing, the team should check:

- can the tester identify when the enemy is about to attack?
- can the tester tell when the enemy has committed?
- can the tester tell when danger is active?
- can the tester tell when the enemy is punishable?
- can the tester understand why dodge, parry, or counter worked or failed?
- does telegraph match hit timing?
- do recovery and punish feel readable?
- does the enemy reset clearly after the exchange?
- does emotional hesitation support readability or obscure it?
- does reveal disruption preserve the next read?

If these questions cannot be answered with confidence, the enemy-side readability layer is not yet proven.

### 16.12 Ownership Boundary

`Enemy Intent & Telegraph` owns:

- enemy state data
- telegraph state
- commitment state
- attack window state
- attack tags
- punish window state
- enemy-side reaction or stagger state
- emotional placeholder state

`Combat Core` owns:

- player response validation
- hit resolution
- `CounterWindow` validation
- reveal request validity

`Debug Overlay` owns:

- displaying, filtering, and visualizing debug data only

`Debug Overlay` must not:

- change enemy state
- force punish windows
- open `CounterWindow`
- decide hit, parry, or dodge outcomes
- trigger reveal except through an explicit manual debug command if allowed

This boundary protects debug from becoming a hidden gameplay authority.

### 16.13 Anti-Patterns

The following patterns would weaken M0 enemy debugging:

- enemy readability tuned without debug
- telegraph timing hidden from overlay
- attack tags invisible during testing
- punish window only visible in code
- stagger or reveal disruption with no debug source
- debug overlay changing enemy behavior
- console logs replacing readable in-game state display
- only testing successful parry or counter, not failure cases
- emotional rhythm changing timing invisibly

Readable combat requires readable tooling.

### 16.14 Open Questions

The following debug questions remain unresolved:

- is Enemy Intent debug part of the same M0 combat debug overlay?
- are attack range or hit area gizmos required in M0?
- should telegraph show predicted active timing?
- should punish window show remaining time?
- should attack tag combinations be validated by future tooling?
- should emotional placeholder debug be visible by default?
- is debug editor-only or available in development builds?

## 17. Data Authoring Needs

This section defines the minimum enemy intent and telegraph data that should be authored or tuned for M0. The goal is not to create a full enemy ability framework. The goal is to identify the smallest set of readable, tuneable values needed to make the first enemy fair, legible, and iteration-friendly.

For M0, enemy data should help designers adjust timing, commitment, tags, punish windows, reactions, and emotional placeholder behavior without burying those rules in opaque implementation details.

### 17.1 Data Authoring Purpose

`Enemy Intent & Telegraph` needs authored or tuneable data so designers can adjust:

- enemy action timing
- telegraph duration
- attack commitment
- active and recovery windows
- attack eligibility tags
- punish window behavior
- stagger and reaction behavior
- emotional hesitation and rhythm
- debug readability labels

The purpose is fast M0 tuning, not full enemy-system scalability.

### 17.2 Minimum M0 Data Categories

#### Enemy Profile Data

Used for:

- the first simple M0 enemy

Should include:

- enemy id or name
- default emotional placeholder state
- basic movement or approach notes
- available attacks
- debug label

This category defines the overall authored identity of the prototype enemy.

#### Enemy Attack Data

Used for:

- `Basic Attack A`
- optional `Basic Attack B` later

Should include:

- attack id or name
- telegraph duration
- startup or commitment duration
- active duration
- recovery duration
- attack range or reach placeholder
- attack eligibility tags
- tracking or rotation allowance
- punish behavior
- reaction on parry or counter
- debug label

This is the most important data category for the first implementation.

#### Telegraph Data

Used for:

- communicating enemy intent

Should include:

- telegraph duration
- primary telegraph channel
- secondary telegraph channel if used
- timing relationship to active hit
- distinctiveness notes
- debug label

This category exists to make fairness tuneable instead of accidental.

#### Commitment Data

Used for:

- defining when the enemy can or cannot cancel or track

Should include:

- commitment start point
- can cancel?
- allowed interruption sources
- rotation or tracking rules
- recovery requirement
- debug label

This category helps keep commitment trustworthy and inspectable.

#### Attack Tag Data

Used for:

- `ParryEligible`
- `DodgePunishable`
- `CounterOnWhiff`
- `CounterOnParry`
- `SpacingCheck`
- `Unparryable`

Should include:

- tag list per attack
- tag combination notes
- debug label
- presentation or readability requirement

This category keeps attack-answer relationships explicit.

#### Punish Window Data

Used for:

- `RecoveryPunish`
- `WhiffPunish`
- `ParryPunish`
- `CounterStagger`
- `Defeat / Disabled` if needed

Should include:

- punish type
- duration
- source condition
- can support `CounterWindow`?
- visibility cue
- expiration behavior
- debug label

This category makes “enemy is open” understandable and tuneable.

#### Enemy Reaction / Stagger Data

Used for:

- `LightHitReact`
- `HeavyHitReact`
- `ParryStagger`
- `CounterStagger`
- `RevealDisruption`
- `Defeat / Disabled`

Should include:

- reaction category
- approximate duration
- interruption behavior
- can be hit again?
- supports reveal?
- return state
- debug label

This category keeps enemy success feedback readable without building a full poise model.

#### Emotional Placeholder Data

Used for:

- `Default / Haunted Restraint`

Should include:

- state name
- hesitation notes
- rhythm notes
- reveal influence if used
- presentation notes
- debug label

This category is intentionally lightweight and tone-oriented.

#### Debug Display Data

Used for:

- making enemy tuning readable

Should include:

- state labels
- attack labels
- tag labels
- timing labels
- window labels
- visibility toggles

This category supports iteration speed rather than player-facing content.

### 17.3 Recommended M0 Authoring Strategy

Recommended strategy:

- start with one `Enemy Profile`
- start with one `Basic Attack A`
- author and tune telegraph, startup, active, recovery, and punish timing first
- include tags:
  - `ParryEligible`
  - `CounterOnParry`
  - optional `CounterOnWhiff` only after recovery is readable
- defer `Basic Attack B` until `Attack A` already feels good
- keep emotional placeholder simple
- keep debug labels human-readable

This sequence keeps the first enemy legible and reduces the risk of using extra data complexity to compensate for unclear fundamentals.

### 17.4 What Can Be Hardcoded Temporarily

For M0, it is acceptable to temporarily hardcode:

- one enemy profile
- one attack
- one emotional placeholder state
- one reveal disruption behavior
- simple stagger categories
- simple punish duration

However, timing values and attack tags should remain easy to inspect and tune once implementation starts. Hardcoded values are acceptable only if they do not become buried or difficult to adjust.

### 17.5 What Should Not Be Authored Yet

Do not author full data for:

- large enemy roster
- boss phases
- advanced emotional AI
- procedural attack selection
- complex combo chains
- group tactics
- ranged enemies
- difficulty scaling
- full memory-state branching
- narrative memory graph
- production VFX or audio libraries
- RPG progression modifiers

M0 only needs enough authored data to make one duel readable.

### 17.6 Data Ownership Boundary

`Enemy Intent & Telegraph` owns or consumes:

- enemy profile data
- enemy attack timing
- telegraph data
- commitment data
- attack tags
- punish window data
- emotional placeholder data

`Combat Core` owns or consumes:

- player response validation
- hit resolution
- `CounterWindow` validation
- reveal request validity

`Health / Damage / Hit Reaction` owns or consumes:

- health values
- damage or reaction categories
- defeat or disabled result

`Memory State` owns or consumes:

- reveal request acceptance
- memory response consequence

Presentation owns or consumes:

- animation clips
- VFX cues
- audio cues
- camera impulse references
- UI or debug display styling

This boundary keeps enemy authored truth separate from combat resolution and presentation response.

### 17.7 Provisional Data Table

| Data Category | Used By | Minimum Fields | Why It Matters For M0 | Can Be Hardcoded Temporarily? |
|------|---------|----------------|------------------------|-------------------------------|
| `Enemy Profile Data` | first M0 enemy | id, emotional state, approach notes, attacks, debug label | Defines the prototype enemy as a readable unit | Yes |
| `Enemy Attack Data` | `Basic Attack A`, optional `Attack B` | id, telegraph, startup, active, recovery, range, tags, tracking, punish, reactions, debug label | Core readable threat behavior lives here | Partially |
| `Telegraph Data` | intent readability | duration, channels, timing relation, distinctiveness, debug label | Fairness and learnability depend on it | Partially |
| `Commitment Data` | trusted follow-through | commitment start, cancel rules, interruptions, tracking, recovery requirement, debug label | Prevents enemy-side cheating | Partially |
| `Attack Tag Data` | attack-answer rules | tag list, combination notes, readability requirement, debug label | Aligns enemy attacks with Combat Core answer logic | Partially |
| `Punish Window Data` | punish and counter support | type, duration, source, counter support, cue, expiration, debug label | Makes enemy openings readable | Yes at first |
| `Enemy Reaction / Stagger Data` | hit, parry, counter, defeat reactions | category, duration, interruption, re-hit rule, reveal support, return state, debug label | Communicates player success clearly | Yes at first |
| `Emotional Placeholder Data` | tonal rhythm | state name, hesitation, rhythm, reveal influence, notes, debug label | Keeps enemy tone appropriate to `Glass Refrain` | Yes |
| `Debug Display Data` | overlay readability | labels, timing names, window names, visibility toggles | Makes tuning practical | Yes |

### 17.8 Tuning Notes

For M0 tuning:

- tune `Attack A` before adding `Attack B`
- tune telegraph before difficulty
- tune recovery and punish visibility before counter strictness
- keep tag setup simple
- keep debug labels clear
- avoid too many hidden modifiers
- prefer fewer readable values over many complex parameters

This reduces the chance of solving readability problems with parameter clutter instead of better authored intent.

### 17.9 Anti-Patterns

The following patterns would weaken the M0 authoring strategy:

- building a full enemy database before one enemy works
- adding `Attack B` before `Attack A` is readable
- hardcoding all telegraph and timing values deep in code
- hiding attack tags from designers
- mixing presentation references with enemy truth data
- adding emotional AI parameters before basic rhythm works
- creating many attack variants before one loop is proven
- allowing VFX or audio data to decide combat result

M0 data should stay small, visible, and tuneable.

### 17.10 Open Questions

The following data-authoring questions remain unresolved:

- should M0 enemy data become `ScriptableObject`s immediately or begin as simpler constants?
- are attack tags authored from day one?
- is telegraph duration data-authored from day one?
- is punish duration fixed or data-authored?
- is emotional placeholder state authored data or debug-only?
- should `Basic Attack B` data exist but remain disabled?
- should presentation references be separated from intent and timing data immediately?

## 18. Presentation Boundaries

This section defines the boundary between `Enemy Intent & Telegraph` and presentation systems for M0. The enemy-side system owns intent, telegraph state, commitment, attack windows, tags, punish windows, reaction state, and emotional placeholder state. Presentation systems exist to communicate those states clearly and tonally.

Animation, VFX, audio, camera, and UI must not decide hit results, attack tags, punish validity, `CounterWindow`, or reveal validity. Their job is to help the player read the enemy, not to secretly own the rules.

### 18.1 Boundary Purpose

Presentation should make enemy intent:

- readable
- fair
- learnable
- emotionally restrained
- aligned with `Glass Refrain`’s sad and mysterious tone
- supportive of `read → evade/parry → counter → reveal`

Presentation must not own:

- enemy intent state
- attack eligibility tags
- attack active windows
- punish window validity
- hit resolution
- player response validation
- `CounterWindow`
- reveal request validity

This boundary matters because a beautifully presented enemy can still be unfair if the presentation is not aligned with authoritative state.

### 18.2 Enemy Intent & Telegraph Owns

`Enemy Intent & Telegraph` owns:

- enemy state
- loop phase
- telegraph state
- commitment state
- attack startup, active, and recovery windows
- attack tags
- punish window state
- stagger or reaction state
- emotional placeholder state
- enemy-side debug data

These are the authoritative enemy-side truths that presentation should follow.

### 18.3 Animation Owns

Animation owns:

- enemy pose
- idle or threat presence animation
- approach animation
- telegraph animation
- attack animation
- recovery animation
- stagger or reaction animation
- reveal disruption animation support

Animation must not:

- secretly change attack timing
- apply damage directly
- decide whether an attack is `ParryEligible` or `DodgePunishable`
- open punish window by itself
- skip recovery without `Enemy Intent & Telegraph` approval
- create hidden fake-outs in M0
- hide the real telegraph timing

Animation events may be used later as presentation sync points or validated timing requests, but not as final gameplay authority.

### 18.4 VFX / Shader Owns

VFX owns:

- telegraph accent
- parry or counter feedback support
- enemy shimmer or distortion
- reveal disruption visual
- hit or stagger accent
- optional tag readability support

VFX must not:

- decide attack tags
- trigger hit resolution
- open `CounterWindow`
- trigger reveal validity
- hide body or weapon telegraph
- obscure the next enemy read
- make an attack look parryable or unparryable if tags say otherwise

VFX should reinforce readability, not compete with it.

### 18.5 Audio Owns

Audio owns:

- telegraph cue
- attack cue
- hit or whiff cue
- stagger cue
- parry or counter cue support
- reveal sting support
- emotional ambience support

Audio must not:

- be the only indicator of attack timing
- contradict visual telegraph
- trigger gameplay results
- mask important telegraph cues
- suggest success when Combat Core rejects the response

Audio should support timing clarity, not replace it.

### 18.6 Camera Owns

Camera owns:

- framing enemy intent
- keeping telegraph readable
- supporting lock-on readability
- mild impulse on hit, counter, or reveal if useful

Camera must not:

- hide telegraph or active-hit cues
- decide whether the enemy is punishable
- decide target validity
- overuse shake during timing-critical moments
- make dodge or parry timing unreadable

Even in a dramatic duel, readability comes first.

### 18.7 UI / Debug Owns

UI / Debug owns:

- showing enemy state
- showing telegraph, commitment, and attack windows
- showing attack tags
- showing punish window state
- showing stagger and reveal debug
- filtering and formatting debug data

UI / Debug must not:

- change enemy state
- force attack tags
- force punish windows
- decide hit, parry, dodge, or counter results
- trigger reveal except through an explicit manual debug command if allowed

UI is a visibility layer, not a behavior authority.

### 18.8 Presentation Sync Philosophy

Presentation should follow enemy-side truth. It may request sync points, but enemy and combat systems validate whether those requests are actually meaningful. M0 should prioritize clarity over polish.

Rules:

- presentation follows authoritative enemy-side state
- presentation can request sync points, but validation remains elsewhere
- early M0 should prioritize clarity over polish
- placeholder animation is acceptable if timing and debug are clear
- body and weapon motion should remain the primary telegraph channel where possible
- VFX and audio should support, not replace, readable motion
- beautiful presentation is only valuable if it preserves fairness

This keeps tone in service of readability.

### 18.9 M0 Presentation Minimum

For M0, presentation only needs:

- readable idle or threat presence
- readable approach or spacing
- clear `Basic Attack A` telegraph
- clear active hit moment
- clear recovery or punish posture
- clear parry or stagger response
- clear counter or stagger response
- minimal reveal disruption feedback
- debug overlay

M0 does not require:

- final animation quality
- final VFX quality
- final audio mix
- cinematic camera
- polished HUD
- advanced emotional acting
- production enemy presentation pipeline

The first enemy only needs to be clear enough to judge the duel honestly.

### 18.10 Presentation Boundary Table

| Presentation Area | Allowed To Own | Must Not Own | M0 Requirement | Risk If Boundary Is Violated |
|------|----------------|---------------|----------------|------------------------------|
| Animation | poses, telegraph motion, attack motion, recovery, reaction playback | attack timing truth, tags, damage, punish validity | Required | enemy timing becomes hidden or misleading |
| VFX / Shader | telegraph accents, hit accents, reveal disruption visuals | tags, hit resolution, `CounterWindow`, reveal validity | Recommended | readability is obscured or contradicted |
| Audio | attack cues, telegraph support, stagger/reveal support | gameplay timing truth, hit validation, success authority | Recommended | player learns wrong timing from sound |
| Camera | framing, readability support, light impact emphasis | punish validity, target validity, combat truth | Recommended | telegraphs and active windows become unreadable |
| UI / Debug | state display, tags, window visibility, debug formatting | state changes, punish forcing, hit validation, reveal validity | Required | debug becomes a hidden gameplay controller |

### 18.11 Anti-Patterns

The following patterns would weaken enemy presentation boundaries in M0:

- animation timing secretly defining attack windows
- VFX making telegraph unreadable
- audio being the only parry timing cue
- camera hiding the windup
- UI becoming the only way to understand enemy intent
- presentation contradicting attack tags
- reveal VFX triggering without valid combat context
- recovery animation not matching punish window
- placeholder assets being used as an excuse for unreadable rules
- polished presentation masking unfair enemy behavior

Presentation should clarify truth, not disguise it.

### 18.12 Open Questions

The following presentation-boundary questions remain unresolved:

- are animation events allowed as validated timing requests?
- are placeholder animations enough for the first real playtest?
- does `Basic Attack A` need VFX or audio support immediately?
- do attack tags need presentation language before playtesting?
- does recovery or punish need a distinct animation pose?
- is reveal disruption mainly animation, VFX, audio, or shader-driven?
- do camera framing requirements belong here or only in `Lock-On & Combat Camera` GDD?

## 19. Technical Boundaries

This section defines the technical guardrails `Enemy Intent & Telegraph` should follow when implemented later. It is still a design-document section, not a detailed architecture spec. The goal is to keep the future implementation small, readable, testable, and aligned with Combat Core rather than over-engineered for hypothetical future enemy systems.

### 19.1 Boundary Purpose

Technical boundaries should ensure:

- `Enemy Intent & Telegraph` remains responsible for enemy-side readability only
- `Combat Core` remains authoritative for player response validation and hit resolution
- enemy states, tags, timing, and punish windows stay debug-visible
- presentation observes and communicates enemy intent but does not own gameplay truth
- M0 remains small, testable, and tuneable

These boundaries exist to keep the first duel honest. If enemy-side behavior becomes tangled with presentation, global state, or hidden reactive logic, readability will become harder to trust.

### 19.2 Enemy Intent Technical Principles

`Enemy Intent & Telegraph` should be:

- explicit
- readable
- debug-visible
- data-tuneable where timing matters
- small enough for one M0 enemy
- separated from presentation
- aligned with Combat Core contracts
- not dependent on final animation, VFX, camera, or UI to decide rules

The system should describe what the enemy is doing in a way that the team can inspect directly during M0 tuning.

### 19.3 Assembly / Dependency Direction

`Enemy Intent & Telegraph` may depend on:

- Core primitives or contracts
- Combat Core contracts or read-only interaction contracts if required
- minimal Unity types only where unavoidable
- `R3` only for observation or debug streams if useful

`Enemy Intent & Telegraph` should not depend on:

- UI
- Camera
- VFX
- Audio
- Bootstrap
- Editor-only code
- `DOTween`
- `Cinemachine`
- full Memory implementation
- full RPG progression
- boss framework

Presentation systems may observe enemy intent through:

- read-only state
- events or signals
- debug snapshots
- presentation DTOs
- explicit interfaces or contracts

This keeps enemy-side truth local and prevents presentation assemblies from becoming structural dependencies.

### 19.4 Combat Core Boundary

`Enemy Intent & Telegraph` should expose:

- enemy state
- telegraph
- attack windows
- attack tags
- punish state
- vulnerability hints

`Combat Core` should validate:

- player dodge success
- player parry success
- player counter success
- hit outcomes
- `CounterWindow`

`Enemy Intent & Telegraph` must not:

- directly decide player hit results
- directly decide parry or dodge success
- directly decide counter success
- directly trigger reveal validity

This boundary is one of the most important in the project. Enemy behavior creates readable opportunity, but Combat Core remains the authority on what actually resolves.

### 19.5 VContainer / Lifetime Boundary

Enemy runtime state should live in gameplay, combat, or encounter scene scope, not in project root scope. The root scope must not own active enemy runtime truth.

For M0:

- one enemy can be explicitly composed
- generic enemy factories are not required yet
- generated DI later should be used carefully only for pure C# enemy-intent services
- `MonoBehaviour`s, scene references, hitboxes, animation components, and VFX presenters should remain explicitly composed

This keeps the first enemy implementation concrete and understandable before generalization.

### 19.6 R3 / Reactive Boundary

`R3` may expose read-only observations of enemy state. It may help debug overlay, UI, VFX, and camera observe what the enemy is doing.

However:

- `R3` should not hide the enemy state machine
- `R3` should not own attack timing logic
- hot timing decisions should remain explicit and traceable
- reactive chains that make enemy timing difficult to debug should be avoided

If the team cannot explain why the enemy changed state without following a chain of reactive side effects, the boundary has failed.

### 19.7 DOTween Boundary

`DOTween` may be useful later for presentation polish, but it must not drive enemy truth.

Rules:

- `DOTween` must not drive enemy attack timing
- `DOTween` must not drive telegraph timing
- `DOTween` must not drive active windows
- `DOTween` must not drive punish windows
- `DOTween` must not define stagger authority
- `DOTween` may support VFX, UI, or camera presentation only if it does not alter enemy truth

Enemy timing should remain authored and inspectable, not embedded inside tween behavior.

### 19.8 Animation / Root Motion Boundary

Animation may visually support:

- telegraph
- attack
- recovery
- stagger
- reveal disruption

Animation events may request sync points only if enemy or combat systems validate them.

If root motion is used:

- it must be coordinated with `Enemy Intent & Telegraph`
- it must be coordinated with `Combat Core`
- it must be coordinated with locomotion or movement logic

Animation must not secretly own:

- attack tags
- hit frames
- vulnerability
- punish windows
- recovery duration

Animation should communicate enemy truth, not replace it.

### 19.9 Physics / Hit Detection Boundary

Provisional M0 options include:

- hitboxes or hurtboxes
- distance or angle checks
- hybrid checks

The final method remains open.

Rules:

- physics may assist detection but should not alone decide combat outcome
- `Combat Core` validates final hit, parry, dodge, and counter results using current state, timing, vulnerability, and tags
- `Enemy Intent & Telegraph` should expose intended attack range and timing clearly enough for validation and debug

This keeps enemy-side authored intent compatible with whichever detection strategy M0 ultimately uses.

### 19.10 Memory Boundary

`Enemy Intent & Telegraph` may support reveal through stagger or reveal-disruption state, but it must not become a memory progression system.

Rules:

- Combat Core requests reveal after meaningful combat success
- `Memory State` decides memory consequence
- `Enemy Intent & Telegraph` may contribute enemy-side disruption or hesitation
- emotional placeholder should remain lightweight until the `Memory State` GDD defines fuller ownership

This keeps tone connected while preventing enemy behavior from absorbing narrative systems too early.

### 19.11 Testing Boundary

`Enemy Intent & Telegraph` should be testable without final animation, VFX, audio, or camera.

The following should be testable:

- telegraph timing
- attack tags
- punish windows
- readable commitment
- controlled player-response interactions

Rules:

- one M0 enemy should be enough to validate the loop
- placeholder presentation is acceptable if timing and debug are clear
- tests should focus on learnability and explainable failure, not final polish

This allows the enemy system to be validated on design truth first.

### 19.12 Technical Anti-Patterns

The following patterns would weaken M0 enemy implementation:

- `Enemy Intent & Telegraph` depending directly on UI, Camera, or VFX
- enemy runtime state registered globally in project root
- reactive streams hiding timing decisions
- `DOTween` driving gameplay windows
- animation events applying hit results directly
- physics collisions alone deciding outcomes
- enemy AI deciding player parry, dodge, or counter success
- service locator use for enemy runtime state
- building generic enemy framework before one enemy works
- implementing boss or multi-enemy logic before M0
- hardcoding timing so deeply that it cannot be tuned

These are exactly the kinds of shortcuts that make early combat feel harder to diagnose later.

### 19.13 Open Questions

The following technical questions remain unresolved:

- is the `Enemy Intent & Telegraph` state machine pure C# or partly `MonoBehaviour`-driven?
- is enemy timing data `ScriptableObject`-based from the start?
- is `R3` used immediately or only after the state model stabilizes?
- is root motion used for enemy attacks?
- does hit detection use hitboxes, distance checks, or hybrid checks?
- do debug snapshots later become DTOs, events, logs, or direct overlay reads?
- does `Enemy Intent & Telegraph` live in Combat scope, AI scope, or Encounter scope for M0?

## 20. Dependencies

This section defines what `Enemy Intent & Telegraph` depends on, what depends on it, and which dependencies remain provisional for M0. The purpose is to keep the system focused on enemy-side readability, telegraph, commitment, attack windows, tags, punish windows, and enemy-side reactions without letting it quietly expand into full AI, combat resolution, or memory progression.

### 20.1 Dependency Purpose

This section clarifies:

- which systems `Enemy Intent & Telegraph` needs to function
- which systems consume enemy intent output
- which systems are provisional contracts in M0
- which systems are deferred until after M0
- which boundaries must remain protected

The goal is not to remove collaboration between systems. The goal is to keep ownership clear enough that future implementation does not drift.

### 20.2 Upstream Dependencies

`Enemy Intent & Telegraph` depends on several systems or contracts, but only for narrow needs.

#### Combat Core

Enemy Intent needs:

- player response validation results
- hit resolution results
- `CounterWindow` validation result
- reveal request validity result
- current combat interaction context if needed

`Combat Core` owns player-facing combat truth. `Enemy Intent & Telegraph` exposes enemy-side windows, tags, and state only.

#### Player / Target Context

Enemy Intent needs:

- player position
- target availability
- distance or range context
- facing or angle context if needed

`Enemy Intent & Telegraph` should not absorb full player locomotion or targeting ownership. It only needs enough target context to make enemy spacing and telegraph meaningful.

#### Health / Damage / Hit Reaction

Enemy Intent needs:

- enemy reaction category result
- defeat or disabled result
- stagger or recovery result

`Health / Damage / Hit Reaction` owns health and defeat consequences. Enemy Intent uses those results to choose readable enemy-side reaction flow.

#### Memory State

Enemy Intent needs:

- reveal accepted or rejected status if reveal disruption is used
- memory response state if it later affects enemy rhythm

`Memory State` owns memory consequence. Enemy Intent may only express a lightweight visible reaction.

#### Encounter Framework

Enemy Intent may need:

- encounter start or end context
- active or inactive enemy state
- reset or testing flow

`Encounter Framework` should own spawning and encounter composition later, not individual attack truth.

#### Debug Overlay

Enemy Intent needs:

- a way to expose state, timing, tag, and debug snapshots

`Debug Overlay` owns display only.

### 20.3 Downstream Consumers

Several other systems consume enemy intent output.

#### Combat Core

Consumes:

- enemy state
- telegraph active
- attack active or recovery windows
- attack tags
- punish window state
- vulnerability hints
- stagger or reaction state

#### Debug Overlay

Consumes:

- enemy state
- attack id or name
- telegraph, commitment, and attack timing
- tags
- punish window
- stagger or reveal disruption
- emotional placeholder state

#### Camera / Lock-On

Consumes:

- enemy target focus context
- telegraph or readability cues
- attack, recovery, or reveal events for framing if needed

#### VFX / Shader

Consumes:

- telegraph cue
- hit, stagger, counter, or reveal-support events
- emotional or reveal disruption hints

#### Audio

Consumes:

- telegraph cue
- attack cue
- hit, whiff, or stagger cue
- reveal disruption cue

#### Animation / Enemy Presentation

Consumes:

- enemy state
- current action
- telegraph, recovery, stagger, and reveal presentation cues

#### Memory State

Consumes:

- reveal-supporting enemy reaction context if needed
- enemy reveal disruption request context if routed that way

These consumers should observe or present enemy-side truth, not rewrite it.

### 20.4 Provisional M0 Contracts

The following should be treated as provisional M0 contracts rather than fully designed systems:

- `Combat Core` interaction interface
- `Player / Target Context`
- `Health / Damage / Hit Reaction`
- `Memory State`
- `Encounter Framework`
- `Debug Overlay`
- `Lock-On & Combat Camera`
- `Animation / VFX / Audio` presentation support

For each of these:

- `Enemy Intent & Telegraph` may define minimum needs
- the dedicated GDD or architecture later owns the full design
- temporary M0 assumptions must be revisited before vertical slice

This lets M0 move forward without pretending every adjacent system is already fully solved.

### 20.5 Systems That Should Not Be Dependencies For M0

`Enemy Intent & Telegraph` should not depend on:

- full boss framework
- large enemy roster
- RPG progression
- skill tree
- equipment or loot
- save/load
- full narrative memory graph
- full district reinterpretation
- stealth or investigation AI
- group tactics
- ranged enemy framework
- final cinematic camera
- final HUD
- final audio mix
- multiplayer or networking
- analytics or telemetry

These are outside the scope of proving the first enemy’s readable duel loop.

### 20.6 Dependency Table

| System | Relationship To Enemy Intent & Telegraph | Enemy Intent Needs | System Owns | M0 Status |
|------|-------------------------------------------|--------------------|-------------|-----------|
| `Combat Core` | Upstream validator and downstream consumer | response results, hit resolution results, `CounterWindow`, reveal validity | player-facing combat truth | Provisional contract |
| `Player / Target Context` | Upstream context provider | position, target availability, range, angle | player or target spatial context | Provisional contract |
| `Health / Damage / Hit Reaction` | Upstream consequence provider | reaction result, defeat state, stagger result | health, damage, defeat consequences | Provisional contract |
| `Memory State` | Upstream/downstream reveal consequence partner | reveal accepted/rejected, memory response context | memory consequence | Provisional contract |
| `Encounter Framework` | Upstream encounter lifecycle provider | encounter active state, reset context | spawn, lifecycle, composition later | Provisional contract |
| `Debug Overlay` | Downstream display consumer | presentation of state, timing, tags, punish, reactions | debug visualization | Provisional contract |
| `Lock-On & Combat Camera` | Downstream readability consumer | telegraph and focus cues | camera framing and lock-on presentation | Provisional contract |
| `Animation / Enemy Presentation` | Downstream presentation consumer | state and cue observation | visual playback and presentation | Provisional contract |
| `VFX / Shader` | Downstream presentation consumer | telegraph, hit, stagger, reveal cues | visual effects support | Provisional contract |
| `Audio` | Downstream presentation consumer | telegraph, attack, whiff, stagger, reveal cues | audio support | Provisional contract |
| `Progression / RPG Systems` | Should not be a dependency | none | progression and scaling | Deferred / excluded |
| `Boss Framework` | Should not be a dependency | none | phase logic and boss design | Deferred / excluded |
| `District Reinterpretation` | Should not be a dependency | none for M0 enemy truth | world-state reinterpretation | Deferred / excluded |

### 20.7 Dependency Risk Notes

The following dependency risks should be watched closely:

- `Enemy Intent & Telegraph` can become too large if it starts owning combat resolution
- `Combat Core` and `Enemy Intent & Telegraph` can conflict if boundaries are unclear
- Camera, VFX, and Animation can accidentally become readability crutches instead of supports
- `Memory State` can pull enemy behavior into narrative progression too early
- `Encounter Framework` can over-expand into AI orchestration before one enemy works
- debug can become stale if it is not tied to authoritative state and timing data
- presentation can contradict tags if tag language is not eventually aligned

Most of these risks come from unclear ownership rather than from lack of features.

### 20.8 Anti-Patterns

The following patterns would weaken dependency boundaries in M0:

- `Enemy Intent & Telegraph` directly deciding player hit, parry, dodge, or counter results
- `Combat Core` secretly overriding enemy timing without a clear contract
- Animation owning attack timing truth
- VFX or audio deciding tag meaning
- camera requirements forcing enemy attack design
- `Memory State` changing enemy rhythm invisibly
- `Encounter Framework` adding multi-enemy behavior before one enemy works
- progression stats modifying enemy readability before M0 feel is proven
- debug overlay reading stale or non-authoritative data

These are the kinds of coupling mistakes that make later tuning much harder.

### 20.9 Open Questions

The following dependency questions remain unresolved:

- should `Enemy Intent & Telegraph` be finalized before the full `Health / Damage / Hit Reaction` GDD?
- does `Encounter Framework` own enemy activation and reset for M0?
- does `Player / Target Context` need its own small contract section later?
- does `Lock-On & Combat Camera` need enemy-intent hooks before implementation?
- should `Memory State` consume reveal-support context from Combat Core only, or also from Enemy Intent?
- should `Debug Overlay` become its own GDD before implementation?
- does `Animation / Enemy Presentation` need a separate presentation contract before prototyping?

## 21. Risks

This section identifies the main design, tuning, presentation, and implementation risks that could derail `M0 — Katana Combat Feel Prototype` from the enemy-side perspective. These risks are specific to the first readable duel enemy, not to the project as a whole.

Each risk matters because `Enemy Intent & Telegraph` succeeds or fails on fairness, learnability, and readability rather than on content volume or sophistication.

### 21.1 Enemy Readability Risk

**Risk:** The player may not understand what the enemy is about to do.

**Why it matters:** The entire combat loop depends on `read → evade/parry → counter → reveal`.

**What could go wrong:**

- weak telegraph
- unclear body or weapon motion
- attack timing not matching animation
- camera hiding the enemy
- VFX or audio noise
- enemy attacking too quickly from idle

**Mitigation direction:**

- tune telegraph before difficulty
- keep `Basic Attack A` simple
- make telegraph debug-visible
- use placeholder presentation only if timing remains readable

### 21.2 Telegraph Timing Risk

**Risk:** Telegraph timing may not line up with the actual active hit.

**Why it matters:** If the telegraph lies, dodge and parry failure feel unfair.

**What could go wrong:**

- active window starts too early
- animation release does not match hit timing
- telegraph duration changes invisibly
- timing is hardcoded or hidden
- VFX or audio cue contradicts body motion

**Mitigation direction:**

- make telegraph, startup, active, and recovery debug-visible
- keep one attack first
- prioritize consistent timing over challenge
- validate timing with repeated playtests

### 21.3 Attack Commitment Risk

**Risk:** Enemy commitment may feel untrustworthy.

**Why it matters:** The player must believe that a read has meaning.

**What could go wrong:**

- enemy cancels attacks randomly
- enemy snap-turns during active hit
- recovery is skipped
- fake-outs are added too early
- tracking is too strong

**Mitigation direction:**

- no fake-outs in M0
- limited tracking after commitment
- committed attacks must resolve into active and recovery unless valid interruption occurs
- debug commitment and cancel reasons

### 21.4 Punish Window Readability Risk

**Risk:** The player may not recognize when the enemy is punishable.

**Why it matters:** Counter and punish are the reward side of the loop.

**What could go wrong:**

- recovery pose is unclear
- punish window is too short
- punish window is only visible in debug
- `EnemyPunishWindow` and `CounterWindow` are confused
- enemy resets too quickly

**Mitigation direction:**

- make punish source and duration debug-visible
- start generous
- use clear recovery or stagger posture
- distinguish enemy exposure from player `CounterWindow`

### 21.5 Tag Clarity Risk

**Risk:** Attack tags may exist in data but not be readable to the player.

**Why it matters:** `ParryEligible`, `DodgePunishable`, `CounterOnWhiff`, and `Unparryable` only work if players can learn them.

**What could go wrong:**

- tags are hidden in data
- all attacks look similar
- `Unparryable` looks parryable
- `DodgePunishable` has no visible overcommitment
- `CounterOnWhiff` has no clear recovery

**Mitigation direction:**

- start with simple tag setup
- `Basic Attack A` should prioritize `ParryEligible + CounterOnParry`
- defer `Unparryable` unless visual language is very clear
- expose tags in debug

### 21.6 Attack B Scope Risk

**Risk:** Adding `Basic Attack B` too early may create tuning noise.

**Why it matters:** M0 should first prove one readable enemy attack.

**What could go wrong:**

- trying to teach dodge, parry, spacing, and counter at once
- two attacks have unclear differences
- extra tag combinations arrive before `Attack A` works
- presentation burden doubles too early

**Mitigation direction:**

- implement and tune `Attack A` first
- add `Attack B` only after `Attack A` is readable and fun
- keep `Attack B` optional or deferred
- avoid `Unparryable` until tag language is proven

### 21.7 Presentation Masking Risk

**Risk:** Animation, VFX, audio, or camera may make enemy intent less readable.

**Why it matters:** Enemy presentation should support fairness, not hide rules.

**What could go wrong:**

- camera angle hides the windup
- VFX covers weapon motion
- audio cue contradicts timing
- placeholder animation is too ambiguous
- polished effects mask unfair timing

**Mitigation direction:**

- clarity before polish
- body and weapon motion as the primary telegraph channel
- debug timing independent of presentation
- test readability with minimal VFX first

### 21.8 Combat Core Boundary Risk

**Risk:** `Enemy Intent & Telegraph` may accidentally own player-facing combat truth.

**Why it matters:** `Combat Core` must validate hit, parry, dodge, counter, and reveal outcomes.

**What could go wrong:**

- enemy attack directly opens `CounterWindow`
- enemy state decides parry success
- enemy reaction triggers reveal directly
- tags directly apply gameplay result
- AI logic overrides Combat Core resolution

**Mitigation direction:**

- enemy exposes state, tags, and windows only
- Combat Core validates outcomes
- reveal validity remains routed through Combat Core and `Memory State`
- keep debug reasons clear

### 21.9 Emotional Placeholder Risk

**Risk:** The `Haunted Restraint` emotional rhythm may be too subtle or may interfere with readability.

**Why it matters:** The enemy should feel like `Glass Refrain`, but still remain testable.

**What could go wrong:**

- hesitation is too long
- emotional timing changes invisibly
- enemy becomes too passive
- reveal disruption hides the next read
- emotion becomes advanced AI too early

**Mitigation direction:**

- keep one default emotional rhythm
- make hesitation debug-visible
- emotion should support telegraph, not replace it
- defer advanced emotional AI

### 21.10 Technical / Tuning Risk

**Risk:** Enemy timing and tags may become difficult to tune.

**Why it matters:** M0 needs fast iteration.

**What could go wrong:**

- timing is hardcoded
- tag combinations are hidden
- no debug overlay exists
- reactive streams hide state
- animation events own windows
- data is split across too many places

**Mitigation direction:**

- keep timing and tag data inspectable
- start with one attack
- debug state, timing, tag, and punish data
- avoid a generic enemy framework too early

### 21.11 Risk Table

| Risk | Why It Matters | Failure Mode | Mitigation | M0 Severity |
|------|----------------|--------------|------------|-------------|
| Enemy readability | Read is the first step of the whole loop | Player cannot tell what the enemy is doing | Simple `Attack A`, telegraph-first tuning, debug visibility | High |
| Telegraph timing mismatch | Fairness depends on honest timing | Dodge/parry failure feels unfair | Debug-visible timing, repeated timing validation | High |
| Attack commitment | Read only matters if commitment is trustworthy | Enemy feels like it cheats or changes its mind | No fake-outs, limited tracking, clear cancel rules | High |
| Punish window clarity | Reward side of the loop depends on visible openings | Player misses or mistrusts punish opportunities | Visible recovery/stagger, generous early punish, debug timers | High |
| Tag clarity | Tags only matter if players can learn them | Attacks feel inconsistent or unreadable | Simple tags, clear telegraph language, debug tag visibility | Medium |
| `Attack B` scope creep | Too many lessons too early create noise | Harder to isolate whether readability works | Tune `Attack A` first, defer `Attack B` | High |
| Presentation masking | Presentation can hide rather than help readability | Rules feel unfair even if authored correctly | Minimal VFX first, body-motion-first telegraphing | Medium |
| Combat Core boundary blur | Ownership confusion breaks authoritative combat flow | Enemy system starts deciding player outcomes | Clear contract and debug reason visibility | High |
| Emotional placeholder | Tone can either help or hurt readability | Enemy feels generic, too passive, or too chaotic | One restrained default rhythm, visible hesitation state | Medium |
| Technical / tuning friction | M0 depends on quick iteration | Timing and tags become hard to inspect | Keep data visible, avoid framework bloat | High |

### 21.12 Highest Priority Risks

The top M0 risks are:

- enemy readability
- telegraph timing mismatch
- punish window clarity
- Combat Core boundary blur
- `Attack B` scope creep
- debug visibility

If these risks are not controlled, the first enemy will not be reliable enough to judge the duel loop fairly.

### 21.13 Anti-Patterns

The following patterns would create or worsen risk in M0:

- adding a second attack before the first is readable
- tuning difficulty before readability
- hiding attack tags from debug
- relying on final animation polish to fix unclear intent
- making enemy rhythm random to feel emotional
- allowing presentation to contradict tags
- letting enemy state directly open `CounterWindow`
- adding `Unparryable` before parry readability works
- making punish windows visible only in code
- testing only successful parry and counter cases

These are strong signals that the system has drifted away from M0’s real proof target.

### 21.14 Open Questions

The following risk-management questions remain unresolved:

- which enemy risk should be validated first in the prototype?
- is `Attack A` alone enough to pass M0 enemy readability?
- when should `Attack B` be introduced?
- how many failed-defense tests are needed to prove fairness?
- are placeholder animations sufficient for early readability testing?
- is the debug overlay required before tuning telegraph timing?
- when should enemy-intent tuning stop and hand off to `Lock-On / Camera` or `Player Locomotion` design work?

## 22. Open Questions

This section consolidates the unresolved `Enemy Intent & Telegraph` questions and organizes them by decision priority. The goal is not to answer everything immediately. The goal is to make implementation blockers visible, separate tuning decisions from planning decisions, and prevent deferred complexity from leaking into M0.

### 22.1 Must Answer Before M0 Implementation

The following questions should be answered before implementation planning begins, or explicitly accepted as prototype assumptions:

- does M0 start with one enemy attack or two?
- is `Basic Attack B` deferred until after `Basic Attack A` feels good?
- are attack tags authored data from day one?
- is `Basic Attack A` also `CounterOnWhiff`, or only `ParryEligible + CounterOnParry`?
- does commitment begin at telegraph start or after telegraph completes?
- is `EnemyCommit` separate from `EnemyAttackStartup`?
- is `EnemyPunishWindow` separate from `EnemyAttackRecovery`?
- is `EnemyRevealBeat` a real enemy state or a presentation overlay?
- is enemy timing data `ScriptableObject`-based from the start or simple constants first?
- is the `Enemy Intent & Telegraph` state machine pure C# or partly `MonoBehaviour`-driven?
- where does `Enemy Intent & Telegraph` live for M0: Combat scope, AI scope, or Encounter scope?
- is the debug overlay required before telegraph tuning?

These questions matter because they directly affect implementation shape, authoring workflow, state clarity, and whether the first enemy can be tuned confidently.

### 22.2 Can Answer During M0 Tuning

The following questions are better answered through playtesting and iteration:

- how long should `Basic Attack A` telegraph be?
- how long should presence or idle last before attacking?
- should the enemy start already in range or approach first?
- how much tracking should `Basic Attack A` have?
- can the enemy rotate during commitment?
- should whiff recovery and normal recovery differ?
- how generous should punish windows be?
- should punish duration be fixed or data-authored?
- can light attacks interrupt telegraph?
- can heavy attacks interrupt commitment?
- should successful dodge have a distinct enemy hesitation reaction?
- how visible does punish posture need to be?
- are placeholder animations sufficient for early readability testing?
- how many failed-defense tests are enough to prove fairness?

These are valid questions, but they do not need final answers before the first prototype pass starts.

### 22.3 Defer Until After M0

The following questions should not block M0 and should remain deferred:

- full boss duel framework
- large enemy roster
- advanced emotional AI
- procedural attack selection
- group tactics
- ranged enemy framework
- stealth or investigation AI
- multi-phase enemy behavior
- full memory-state branching
- district reinterpretation
- production animation, VFX, and audio pipeline
- difficulty scaling
- RPG progression modifiers
- `Unparryable` attack language if not needed for `Attack A`
- complex tag validation tooling

These are real future concerns, but none of them are required to prove one readable M0 duel enemy.

### 22.4 Cross-System Questions

The following questions should be answered in other GDDs or cross-system contracts rather than being solved entirely inside `Enemy Intent & Telegraph`.

#### Combat Core

- does dodge success open `CounterWindow` directly or only through enemy whiff and punish state?
- does parry always interrupt `EnemyAttackActive`?
- does parry success enter `EnemyStagger` or `EnemyPunishWindow`?
- does counter target auto-align or require spacing discipline?
- does `CounterStagger` always request reveal?

#### Player Locomotion

- is enemy or player spacing tested through controller movement, root motion, or code-driven movement?
- does dodge direction depend on input, camera, or target?
- does player counter movement auto-align to enemy?

#### Lock-On & Combat Camera

- can camera keep `Basic Attack A` telegraph readable?
- does lock-on need enemy-intent hooks before implementation?
- do camera framing requirements belong partly here or fully in the camera GDD?

#### Health / Damage / Hit Reaction

- are enemy reaction durations fixed or data-authored?
- can the enemy be hit repeatedly during stagger?
- does defeat always trigger reveal?
- is defeat a health result or an encounter result?

#### Memory State

- does `Memory State` consume reveal-support context from Combat Core only or also Enemy Intent?
- does reveal change enemy rhythm after success?
- does emotional rhythm belong to `Memory State` later?
- is `RevealDisruption` mostly enemy-side, memory-side, or presentation-side?

#### Debug Overlay

- is enemy debug part of the same M0 combat overlay?
- are hitbox or range gizmos required?
- should telegraph show predicted active timing?
- should punish show remaining time?
- is debug editor-only or available in development builds?

#### Animation / Presentation

- are animation events allowed as validated timing requests?
- does `Basic Attack A` need VFX or audio support immediately?
- do attack tags need presentation language before playtesting?
- does recovery or punish need a distinct pose?

These questions are real, but they should be routed to their owning systems once the minimum enemy-side contract is locked.

### 22.5 Recommended Decision Order

Recommended decision order before implementation:

1. one attack vs two attacks
2. `Basic Attack A` tag setup
3. enemy timing data approach
4. telegraph and commitment boundary
5. `EnemyPunishWindow` vs recovery separation
6. debug overlay requirement
7. state machine implementation style
8. scope ownership for `Enemy Intent & Telegraph`
9. placeholder animation acceptance
10. reveal beat ownership

This order resolves the questions that most strongly shape the first implementation pass before moving into polishing or edge-case decisions.

### 22.6 Non-Blocking Notes

- not every question needs to be answered immediately
- the goal is to prevent hidden blockers
- unresolved tuning questions can become explicit prototype assumptions
- deferred questions should not leak into M0 implementation
- `Attack A` should be proven before `Attack B` adds complexity

The document does not need total certainty. It needs visible assumptions and disciplined scope.

### 22.7 Open Question Table

| Question | Category | Blocks M0 Implementation? | Owner System | Recommended Timing |
|------|----------|---------------------------|--------------|--------------------|
| Does M0 use one attack or two? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph | Before implementation |
| Is `Basic Attack B` deferred until `Attack A` feels good? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph | Before implementation |
| Are attack tags authored from day one? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph | Before implementation |
| Is `Basic Attack A` also `CounterOnWhiff`? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph / Combat Core contract | Before implementation |
| Does commitment begin at telegraph start or after telegraph completes? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph | Before implementation |
| Is `EnemyCommit` separate from `EnemyAttackStartup`? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph | Before implementation |
| Is `EnemyPunishWindow` separate from `EnemyAttackRecovery`? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph | Before implementation |
| Is `EnemyRevealBeat` a state or overlay? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph / Memory / Presentation | Before implementation |
| Is timing data `ScriptableObject`-based or simpler first? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph / technical foundation | Before implementation |
| Is the state machine pure C# or partly `MonoBehaviour`-driven? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph / architecture | Before implementation |
| Where does Enemy Intent live for M0? | Must Answer Before M0 Implementation | Yes | Architecture / DI ownership | Before implementation |
| Is debug overlay required before telegraph tuning? | Must Answer Before M0 Implementation | Yes | Enemy Intent & Telegraph / Debug Overlay | Before implementation |
| How long should `Basic Attack A` telegraph be? | Can Answer During M0 Tuning | No | Enemy Intent & Telegraph | During tuning |
| How long should idle/presence last? | Can Answer During M0 Tuning | No | Enemy Intent & Telegraph | During tuning |
| Should the enemy start in range or approach first? | Can Answer During M0 Tuning | No | Enemy Intent & Telegraph / Encounter context | During tuning |
| How much tracking should `Basic Attack A` have? | Can Answer During M0 Tuning | No | Enemy Intent & Telegraph | During tuning |
| Can the enemy rotate during commitment? | Can Answer During M0 Tuning | No | Enemy Intent & Telegraph | During tuning |
| Should whiff recovery and normal recovery differ? | Can Answer During M0 Tuning | No | Enemy Intent & Telegraph | During tuning |
| How generous should punish windows be? | Can Answer During M0 Tuning | No | Enemy Intent & Telegraph / Combat Core feel | During tuning |
| Is punish duration fixed or data-authored? | Can Answer During M0 Tuning | No | Enemy Intent & Telegraph / Hit Reaction | During tuning |
| Can light attacks interrupt telegraph? | Can Answer During M0 Tuning | No | Combat Core / Enemy Intent contract | During tuning |
| Can heavy attacks interrupt commitment? | Can Answer During M0 Tuning | No | Combat Core / Enemy Intent contract | During tuning |
| Should successful dodge have hesitation feedback? | Can Answer During M0 Tuning | No | Enemy Intent & Telegraph / Presentation | During tuning |
| Are placeholder animations sufficient? | Can Answer During M0 Tuning | No | Presentation / Enemy Intent | During tuning |
| How many failed-defense tests prove fairness? | Can Answer During M0 Tuning | No | QA / Enemy Intent / Combat Core | During tuning |
| Boss framework questions | Defer Until After M0 | No | Boss Framework | After M0 |
| Advanced emotional AI questions | Defer Until After M0 | No | Memory / AI systems | After M0 |
| Large roster questions | Defer Until After M0 | No | Enemy roster systems | After M0 |
| Production pipeline questions | Defer Until After M0 | No | Animation / VFX / Audio pipeline | After M0 |

### 22.8 Final Summary

`Enemy Intent & Telegraph` is ready for M0 implementation planning once the must-answer questions are reviewed and either decided or explicitly accepted as prototype assumptions.

## 23. Acceptance Criteria For M0

This section defines the practical conditions under which `Enemy Intent & Telegraph` is considered successful enough at the M0 stage to move forward. The goal is not final polish. The goal is to know when the first enemy is readable, fair, and useful for proving `Combat Core`.

### 23.1 M0 Acceptance Purpose

Acceptance criteria for M0 should answer:

- can the player read enemy intent before impact?
- does the enemy attack feel committed and trustworthy?
- does the enemy expose fair dodge, parry, and counter opportunities?
- are attack tags clear enough for tuning?
- do punish and recovery feel understandable?
- does the enemy support reveal without becoming a memory system?
- can designers debug and tune the enemy behavior?
- is the scope still contained to one simple enemy?

If these questions cannot be answered positively in a repeatable one-enemy duel, the system is not yet ready to anchor downstream work.

### 23.2 Core Enemy Loop Acceptance

M0 `Enemy Intent & Telegraph` passes the core loop requirement if one simple enemy can repeatedly demonstrate:

`presence → approach/space → telegraph → commit → active threat → recovery/punish → stagger/reveal → reset`

Required:

- enemy presence gives the player time to read
- approach or spacing is understandable
- telegraph is visible before active hit
- commitment is trustworthy
- active threat timing matches telegraph expectation
- recovery or punish is readable
- stagger, counter, and reveal support are understandable
- reset returns the duel to readable tension

This is the basic proof that the enemy can participate honestly in the combat loop.

### 23.3 Telegraph Acceptance

Telegraph is acceptable if:

- a fresh tester can notice the enemy preparing an attack
- the tester can learn the timing after a few attempts
- telegraph begins before active hit
- active hit timing matches the telegraph
- telegraph does not rely only on debug
- camera, VFX, and audio do not obscure the read
- `Basic Attack A` clearly communicates its intended defensive lesson

If telegraph is not trustworthy, the rest of the enemy system cannot be judged fairly.

### 23.4 Commitment Acceptance

Commitment is acceptable if:

- once committed, the enemy follows through predictably
- the enemy does not randomly cancel
- the enemy does not unfairly snap-turn during active hit
- recovery is not skipped
- the player can trust that their read has meaning
- allowed interruptions are clear and validated through `Combat Core`

This ensures the player is learning from real enemy behavior instead of hidden exceptions.

### 23.5 Attack Tag Acceptance

Attack tags are acceptable if:

- `Basic Attack A` has a simple readable tag setup
- `ParryEligible` and `CounterOnParry` behavior is testable
- optional `CounterOnWhiff` is only used if recovery is already readable
- tags are visible in debug
- tags do not directly decide outcome without `Combat Core` validation
- presentation does not contradict tags

For M0, clarity matters more than variety.

### 23.6 Dodge / Parry / Counter Interaction Acceptance

Interactions are acceptable if:

- correct parry produces a clear enemy response
- correct dodge or spacing can produce visible whiff or recovery when authored
- punish or counter opportunity has a readable cause
- player failure feels caused by timing, spacing, or wrong answer
- counter success creates stronger enemy reaction than a normal hit
- reveal support only follows meaningful combat success

This confirms that the enemy is not only readable, but answerable.

### 23.7 Punish Window Acceptance

Punish windows are acceptable if:

- the player can tell when the enemy is exposed
- punish source is explainable
- punish duration is long enough to teach the loop
- punish duration is not so long that counter feels automatic
- `EnemyPunishWindow` and player `CounterWindow` remain conceptually distinct
- punish state is visible in debug

The player should feel that punish is earned and temporary.

### 23.8 Stagger / Reveal Support Acceptance

Stagger and reveal support are acceptable if:

- light hit reaction communicates contact without breaking everything
- parry stagger communicates timing success
- counter stagger feels stronger than normal hit
- reveal disruption is short and restrained
- reveal disruption does not hide the next read
- the enemy returns to readable reset afterward

This protects the enemy from feeling either unresponsive or theatrically overbuilt.

### 23.9 Debug Acceptance

Debug and readability tooling are acceptable if they can show:

- current enemy state
- current loop phase
- current attack
- telegraph active and timing
- commitment active and timing
- attack active and recovery timing
- attack tags
- punish window active, source, and timing
- stagger or reaction category
- reveal disruption or support state
- last player response result

Debug does not need polished UI. It only needs to make enemy behavior explainable.

### 23.10 Scope Acceptance

M0 remains acceptable only if it does not expand into:

- full enemy AI framework
- boss framework
- multiple enemy roster
- advanced emotional AI
- procedural attack selection
- group tactics
- ranged enemy framework
- full memory branching
- district reinterpretation
- production animation, VFX, or audio pipeline
- difficulty scaling
- RPG progression modifiers

If the enemy GDD begins solving those systems, M0 has lost focus.

### 23.11 Playtest Acceptance Checklist

A tester should be able to answer `yes` to the following:

- I could tell when the enemy was about to attack.
- I could tell when the enemy had committed.
- I could tell when the attack became dangerous.
- I understood why my dodge or parry worked or failed.
- I could tell when the enemy was punishable.
- Counter opportunity felt earned.
- Enemy reaction made my success clear.
- Reveal disruption felt connected but did not interrupt readability.
- The enemy reset clearly after exchanges.
- Debug information explained unclear moments.

This checklist is intended as a practical M0 test gate.

### 23.12 Failure Conditions

`Enemy Intent & Telegraph` M0 should not pass if:

- enemy attacks feel random
- telegraph does not match hit timing
- enemy cancels commitment unfairly
- punish window is invisible
- tags are only data or debug and not learnable at all
- `Attack B` adds noise before `Attack A` works
- presentation hides enemy intent
- enemy state directly owns player combat outcome
- debug cannot explain enemy timing
- final assets are required to judge basic readability

Any one of these is enough reason to keep tuning before moving on.

### 23.13 Acceptance Table

| Area | Acceptance Criteria | How To Verify | Pass/Fail Signal | M0 Priority |
|------|---------------------|---------------|------------------|-------------|
| Core Enemy Loop | One simple enemy repeatedly demonstrates readable loop phases | Repeated one-enemy duel playtest with debug visible | Pass if loop is understandable and repeatable | Must Pass |
| Telegraph | Telegraph is visible, learnable, and honest | Fresh tester observation and repeated timing attempts | Pass if testers can learn timing after a few tries | Must Pass |
| Commitment | Enemy follows through predictably once committed | Observe cancel, turn, and recovery behavior during playtest | Pass if player trust is preserved | Must Pass |
| Attack Tags | `Basic Attack A` tags are simple, visible, and testable | Debug inspection plus player response testing | Pass if tags support readable answers | Must Pass |
| Dodge / Parry Interaction | Defensive answers produce readable enemy-side consequence | Run dodge/parry success and failure cases | Pass if success/failure feels explainable | Must Pass |
| Counter / Punish | Enemy exposes readable punish and counter support | Test whiff, recovery, parry, and counter cases | Pass if openings feel earned and visible | Must Pass |
| Stagger / Reveal Support | Reactions communicate success without obscuring next read | Trigger hit, parry, counter, and reveal-support cases | Pass if reactions stay readable and restrained | Should Pass |
| Debug Visibility | Designers can explain enemy timing and state | Tuning session using overlay only | Pass if unclear moments become diagnosable | Must Pass |
| Scope Control | System remains limited to one readable M0 enemy | Review feature set against exclusions | Pass if no major out-of-scope behavior leaked in | Must Pass |
| Combat Core Boundary | Enemy system does not own player-facing outcome truth | Review behavior against Combat Core contract | Pass if enemy system exposes state but not outcomes | Must Pass |

### 23.14 Minimum “Good Enough” Definition

`Enemy Intent & Telegraph` M0 is good enough when one simple enemy, using `Basic Attack A`, repeatedly demonstrates readable telegraph, trustworthy commitment, fair active and recovery timing, visible punish opportunity, clear parry and counter interaction, and debug-visible state, timing, and tag data without relying on final presentation polish or expanding into boss or enemy-roster systems.

### 23.15 Deferred Acceptance

The following are explicitly not required for `Enemy Intent & Telegraph` M0:

- `Basic Attack B` unless `Attack A` is already readable
- `Unparryable` attack language
- final animation quality
- production VFX or audio
- full boss behavior
- full emotional AI
- full memory-state branching
- multi-enemy behavior
- difficulty scaling
- final lock-on or camera polish
- final enemy roster

These belong to later milestones and should not block the first enemy from being judged honestly.

### 23.16 Open Questions

The following acceptance questions remain unresolved:

- how many playtest runs are enough to pass enemy readability?
- is `Attack A` alone enough for M0 pass?
- must the debug overlay exist before the first real telegraph tuning session?
- are placeholder animations enough for first validation?
- who approves enemy readability as good enough?
- when is `Attack B` allowed to enter the prototype?
- what exact threshold ends enemy tuning and moves to the next dependency GDD?
