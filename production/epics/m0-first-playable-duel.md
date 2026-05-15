# Epic: M0 First Playable Duel

## Summary
Wire the M0 technical skeletons into a functional one-player / one-enemy duel loop within the Tokyo Street blockout.

## Success Criteria
- [ ] Additive scene composition loads successfully from Bootstrap.
- [ ] VContainer wiring connects Input → Core → Presentation.
- [ ] Player can move using camera-relative basis.
- [ ] Player can lock-on to enemy.
- [ ] Combat loop (Attack/Dodge/Parry) resolves in Pure C#.
- [ ] Enemy cycles through Intent (Telegraph/Active/Recovery).
- [ ] Health and Hit Reactions trigger from combat results.
- [ ] Reveal trigger activates Memory response on success.
- [ ] Debug Overlay displays system snapshots for verification.

## Stories
| # | Story | Type | Status | ADR |
|---|-------|------|--------|-----|
| 1-1 | [[Foundation] Scene & VContainer Wiring](m0-first-playable-duel/story-1-1-foundation-wiring.md) | Integration | Ready | ADR-0001 |
| 1-2 | [[Locomotion] Camera-Relative Movement](m0-first-playable-duel/story-1-2-camera-locomotion.md) | Logic/Int | Ready | ADR-0002 |
| 1-3 | [[Targeting] Lock-On Wiring](m0-first-playable-duel/story-1-3-targeting-wiring.md) | Logic/Int | Ready | ADR-0002 |
| 1-4 | [[Combat] Player Attack Resolution](m0-first-playable-duel/story-1-4-combat-resolution.md) | Logic | Ready | ADR-0002 |
| 1-5 | [[Enemy] Intent & Telegraph Loop](m0-first-playable-duel/story-1-5-enemy-intent.md) | Logic | Ready | ADR-0002 |
| 1-6 | [[Combat] Parry & Dodge Integration](m0-first-playable-duel/story-1-6-defensive-wiring.md) | Logic/Int | Ready | ADR-0002 |
| 1-7 | [[Consequence] Health & Hit Reactions](m0-first-playable-duel/story-1-7-health-consequence.md) | Logic/Int | Ready | ADR-0002 |
| 1-8 | [[Encounter] Reset & Duel Lifecycle](m0-first-playable-duel/story-1-8-encounter-lifecycle.md) | Logic/Int | Ready | ADR-0002 |
| 1-9 | [[Presentation] Debug Overlay Snapshots](m0-first-playable-duel/story-1-9-debug-overlay.md) | UI/Logic | Ready | ADR-0003 |
| 1-10 | [[Memory] Reveal & VFX Placeholder](m0-first-playable-duel/story-1-10-memory-reveal.md) | Visual/Feel | Ready | ADR-0002 |
| 1-11 | [[Presentation] Animator Observer Adapters](m0-first-playable-duel/story-1-11-animator-adapters.md) | Visual/Feel | Ready | ADR-0003 |
