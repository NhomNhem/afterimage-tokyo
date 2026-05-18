# Gameplay Scope Rules — Glass Refrain M0

## Purpose

These rules protect `Glass Refrain` from scope creep during M0. The first goal is not a full RPG. The first goal is to prove a readable katana duel.

## M0 Identity

M0 is:

```txt
Katana Combat Feel Prototype
```

M0 should prove:

```txt
read → evade/parry → counter → reveal
```

The prototype should support:

- one player
- one simple enemy
- one Tokyo Street duel space
- movement
- lock-on / target focus
- dodge
- parry
- light attack
- heavy attack
- counter
- basic hit reaction
- readable enemy intent
- restrained memory VFX response
- debug overlay

## Scope Protection Rule

If a feature does not improve the one-player / one-enemy / one-arena duel loop, defer it.

## Explicitly Deferred After M0

Do not implement unless explicitly approved:

- full RPG stat framework
- loot
- equipment rarity
- skill tree
- save/persistence
- full narrative memory graph
- district reinterpretation
- multiple enemy types
- boss phase framework
- multi-enemy combat
- full HUD
- final UI flow
- economy
- open world systems
- multiplayer/network code

## Combat Feel First

Combat feel has priority over system breadth.

Before adding any combat feature, ask:

- Does it improve readability?
- Does it make defensive choice clearer?
- Does it make counter timing more satisfying?
- Does it preserve restrained elegance?
- Does it help the reveal feel earned?

If not, defer it.

## Debug Visibility Required

Every M0 gameplay system must expose enough debug truth to explain success/failure.

Minimum expectations:

- current state
- previous state if useful
- accepted/rejected request reason
- timing window if applicable
- owner system clearly identified

## Ownership Rule

M0 systems must not steal each other's truth.

- Combat Core owns combat validity and results.
- Player Locomotion owns movement truth.
- Enemy Intent & Telegraph owns enemy telegraph and enemy attack timing truth.
- Health / Damage / Hit Reaction owns consequence after confirmed result.
- Lock-On / Target Context owns target truth.
- Lock-On & Combat Camera owns framing/readability only.
- Memory State owns reveal acceptance/rejection.
- Memory VFX Response owns visual response only after accepted reveal.
- Debug Overlay owns read-only presentation of debug truth.

## Prototype Naming Rule

Temporary M0 classes may use `M0` only when they are clearly prototype-only.

Examples:

```txt
M0SimpleEnemyBrain
M0PrototypeEncounterBootstrap
```

Before moving past prove-feel, rename M0 classes to production names or delete them.

## No Fake Completion Rule

Do not mark a gameplay system done if:

- it only works through debug buttons
- it has no rejection reasons
- its state cannot be inspected
- it hides truth in Animator
- it depends on unexplained scene object search
- it adds full-game scope before the duel works
