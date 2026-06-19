# Next Feel Slice Decision
**Date**: 2026-06-16
**Story**: S6-7 (S7-1) — Select Next M0/M1 Feel Slice
**Source**: Sprint 6 smoke context (`production/qa/smoke-2026-06-16.md`)

## Primary Slice: Player Animation Polish

**Scope**: Improve player character animation quality, transitions, and visual
readability during the M0 combat loop — specifically attack animations, dodge
animation blending, hit reaction animation clarity, and parry/counter animation
transitions.

**Rationale**: Sprint 6 confirmed the combat loop (read → evade/parry → counter →
reveal) is functional, but the player's own animations lack the polish needed
for visual clarity during combat. Attack windups blend too quickly, dodge lacks
distinct visual phases, and parry/counter transitions are hard to read as
separate states. This directly impacts the "read" and "evade/parry" parts of the
loop — if the player can't read their own state from animations, they can't
predict when they can act next.

**Sprint 6 evidence cited**: Smoke report PASS WITH WARNINGS notes readability
as an ongoing area. S6-2 (parry/counter visual feedback) improved feedback
via VFX/animator triggers, but the underlying player animation transitions
remain unpolished.

## Deferred Alternatives

| Slice | Defer Reason |
|-------|-------------|
| Enemy telegraph clarity | Already improved in S5-1/S5-2; lower evidence gap than player animation |
| Lock-on readability | Functional in M0; polish can wait until target-switching scenarios are tested |
| Counter/reveal feedback | Already improved in S6-2; further polish can follow player animation pass |
| M1 memory feedback polish | M1 epic nearly complete; feedback polish can wait until Investigation/Contradiction GDD is written |

## Scope Boundary

Player animation polish is limited to:
- Owned animation controller and clip references
- Animator parameter tuning and transition timing
- Animation event alignment with Combat Core state
- Player-facing presentation only (Animator is presentation layer per ADR-0003)

Out of scope:
- Enemy animation changes
- Combat Core gameplay truth changes
- New animation assets (uses existing clips)
- Full HUD, UI, or camera changes
- Broad RPG or progression systems

## Next Step

Sprint 8 should include a story for player animation polish. The specific
animation systems to address:
1. Attack animation windup and recovery clarity
2. Dodge animation phase distinction (start → active → end)
3. Parry/counter animation transition readability
4. Hit reaction animation blending
