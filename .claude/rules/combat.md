# Combat Rules — Glass Refrain M0

## Scope

M0 is a katana combat feel prototype.

Only implement features that improve:

read → evade/parry → counter → reveal

## Combat Core Authority

Combat Core owns:

- combat action validity
- light/heavy attack request validation
- dodge result
- parry result
- counter opportunity
- CounterWindow
- hit resolution
- reveal request context

Combat Core must not own:

- player movement truth
- enemy telegraph truth
- camera framing
- memory reveal acceptance
- VFX/audio presentation
- Animator state truth

## M0 Allowed Features

Allowed:

- light attack
- heavy attack
- dodge
- parry
- counter
- basic recovery
- basic hit reaction integration
- one simple counter window
- debug visibility

Not allowed without explicit approval:

- full combo tree
- skill tree
- RPG stats
- weapon switching
- elemental damage
- loot scaling
- boss phase framework
- multi-enemy combat
- animation-driven combat truth

## Feel Rule

Combat must feel:

- readable
- fair
- restrained
- precise
- emotionally tense

If a feature makes combat noisier but not clearer, defer it.

## Debug Rule

Every combat state must be inspectable:

- current combat state
- previous state
- time in state
- active timing window
- can parry?
- can counter?
- last accepted/rejected request reason