# Proposal: Wire M0 Health & Hit Reactions

> **Change ID**: wire-m0-health-hit-reactions
> **Schema**: spec-driven
> **Status**: Proposed
> **Date**: 2026-05-16
> **Author**: User + Codex

## Problem Statement

Story 1-7 (Health & Hit Reactions) requires wiring health, damage, and hit reaction consequences so damage is applied only after confirmed CombatCore hit/counter results, Health owns health mutation, HitReaction owns reaction/suppression context, enemy stagger is triggered from player hit/counter success, and health/reaction state is visible in debug. Currently, health/damage/hit reaction runtime consequence is not implemented, though the M0HealthDamageReactionModel skeleton exists.

## Proposed Solution

Wire the existing M0HealthDamageReactionModel skeleton (or enhance if needed) to:
- Apply damage only after confirmed CombatCore hit/counter results
- Health system owns health mutation
- HitReaction system owns reaction classification and suppression context
- Enemy stagger triggered by player LightAttack/HeavyAttack hit or Counter success
- Debug overlay exposes current/max health, hit reaction state, suppression reason, defeated state

## Success Criteria

- Damage is applied to Health only after a confirmed CombatCore hit result
- Hit Reaction state triggers movement/control suppression in M0PlayerLocomotion
- Stagger state in enemy is triggered by player hits or counter success
- Health state (current/max) is visible in debug
- EnemyIntent does not apply damage
- Input does not apply damage
- TargetContext does not apply damage
- No MemoryState or MemoryVFX trigger occurs
- No animation/root motion authority
- No KCC/NavMesh usage

## Out of Scope

- RPG stat system
- Armor/resistance
- Status effects
- Loot/XP
- Memory Reveal
- Memory VFX
- Camera shake/VFX polish
- Animation/root motion authority
- Animancer integration
- KCC
- NavMesh
- Enemy AI navigation
- Multi-enemy damage system
- Full damage formula framework
- UI polish
- Asset Store package modifications
- Generated DI
- Story/sprint status updates during implementation

## Risks

- **Risk**: Damage might be applied before confirmed CombatCore result
  - **Mitigation**: Enforce strict ownership: CombatCore emits confirmed hit result only; Health processes result only after confirmation

- **Risk**: Health might be mutated by wrong system (Input, EnemyIntent, TargetContext)
  - **Mitigation**: Code review and EditMode tests to verify only Health system mutates health

- **Risk**: Hit reaction might become animation-owned
  - **Mitigation**: Enforce ADR-0002: Health owns reaction truth; Animator presents only

- **Risk**: MemoryState might be triggered prematurely
  - **Mitigation**: Hard exclusion: no MemoryState or MemoryVFX in this story

## Dependencies

- Story 1-1: Foundation Scene & VContainer Wiring (Complete)
- Story 1-2: Camera-Relative Movement (Complete)
- Story 1-3: Lock-On Wiring (Complete)
- Story 1-4: Player Attack Resolution (Complete)
- Story 1-5: Enemy Intent & Telegraph Loop (Complete)
- Story 1-6: Parry & Dodge Integration (Complete)
- Optional: create-m0-playable-combat-prototype-scene (if complete for visual verification)

## Timeline Estimate

1.0d (one day) - Health/damage/hit reaction wiring with debug visibility and EditMode tests.
