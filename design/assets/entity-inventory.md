# Entity Inventory (M0 Duel Scope)

Date: 2026-05-28
Scope: M0 first playable duel and Sprint 2 readability stabilization

## Runtime Entities

| ID | Name | Type | Owner System | Status | Notes |
|---|---|---|---|---|---|
| E-PLAYER-M0 | M0 Player | Character | Player Locomotion / Combat Core | active | Single controllable protagonist for duel loop |
| E-ENEMY-M0 | M0 Duel Enemy | Enemy | Enemy Intent & Telegraph / Combat Core | active | Single prototype enemy for telegraph/readability validation |
| E-TARGET-M0 | Target Context Current Target | Runtime Context | Lock-On / Target Context | active | Source-of-truth for lock-on target |

## Encounter and Scene Entities

| ID | Name | Type | Owner System | Status | Notes |
|---|---|---|---|---|---|
| ENCOUNTER-M0-01 | M0 Duel Encounter | Encounter | Encounter Framework | active | Reset/start lifecycle validated in S1-8 |
| SCENE-GAMEPLAY-COMBAT | Gameplay_CombatPrototype | Scene | Scene Composition | active | Main M0 duel verification scene |

## Memory and Presentation Entities

| ID | Name | Type | Owner System | Status | Notes |
|---|---|---|---|---|---|
| MEM-STATE-M0 | Memory Reveal State | Runtime State | Memory State | active | Accept/reject reveal requests |
| MEM-VFX-M0 | Memory VFX Response | Presentation | Memory VFX Response | active | Downstream-only placeholder VFX |
| DBG-OVERLAY-M0 | M0 Debug Overlay | Debug UI | Debug Overlay | active | Read-only state visualization |

## Ownership Guardrails

- Combat truth remains in CombatCore (timing/results/counter window/reveal request emission).
- Target truth remains in TargetContext.
- Enemy lifecycle truth remains in EnemyIntent.
- Camera, VFX, animation, and debug overlay remain presentation/read-only.

## Out of Scope Entities (Not Included in M0/S2)

- Multi-enemy roster entries
- Boss entity sets
- Inventory/item economy entities
- Save/load world-state entities
