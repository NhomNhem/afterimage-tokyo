# Playtest Report — M0 Duel Readability

Date: 2026-05-28
Sprint: 2
Tester: Internal (design/programming QA pairing)
Build Context: M0 prototype duel flow with S2-2/S2-3 improvements and S2-4 planning baseline

## Session Goal

Validate that the current M0 duel remains readable and playable while preserving ownership boundaries:
- CombatCore owns timing/results/counter/reveal request
- EnemyIntent owns telegraph lifecycle
- TargetContext owns lock-on truth
- Camera/Debug/VFX remain non-authoritative

## Scenario

Single duel loop in Gameplay_CombatPrototype:
1. Read enemy telegraph
2. Attempt defensive answer (dodge/parry)
3. Confirm counter opportunity readability
4. Observe loop reset and repeat

## Observations

- Enemy telegraph phases were distinguishable enough to support read-first flow.
- Attack/Dodge/Parry readability remained playable without obvious scope drift.
- Debug overlay remained read-only and useful for quick phase verification.
- No evidence that camera/presentation systems took gameplay authority.

## Limitations / Notes

- This is an M0/S2 internal validation pass, not a production-scale external playtest.
- Further camera readability confirmation should be captured during S2-4 implementation evidence.

## Verdict

PASS WITH NOTES

- Core loop is playable and readable enough to continue Sprint 2.
- Additional targeted evidence for lock-on camera readability remains pending S2-4 implementation.
