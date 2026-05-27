## Why

Sprint 2 shifts from wiring-complete to feel/readability stabilization. Enemy-side readability is currently the biggest risk to the M0 loop `read -> evade/parry -> counter -> reveal`: players can mechanically act, but telegraph-to-impact clarity is not yet consistently readable under play pressure.

S2-3 exists to improve readability of `Telegraph -> Commit -> Active -> Recovery` cues without changing ownership boundaries or combat truth authorities.

## What Changes

- Define M0 telegraph readability targets and non-goals for Sprint 2.
- Plan a narrow tuning pass for enemy intent phase cue readability (timing/presentation-alignment only).
- Define required verification evidence (EditMode + PlayMode checklist + console classification).
- Lock explicit boundaries so EnemyIntent remains authority and presentation layers remain non-authoritative.

## Scope

### In Scope (Plan only)

- Readability criteria for enemy intent phase transitions.
- Safe tuning surface definition for M0 enemy telegraph readability.
- Verification requirements and PASS/PARTIAL/FAIL rubric.
- Allowed/forbidden implementation file boundaries for follow-up apply.

### Out of Scope

- New enemy types/roster.
- Boss lifecycle/phases.
- Behavior tree/GOAP expansion.
- Broad AI architecture refactor.
- CombatCore authority changes.
- Camera/Animator/VFX owning gameplay truth.

## Risks

- Over-tuning timing may accidentally alter gameplay difficulty rather than readability.
- Presentation cue adjustments may mask true intent timing if not anchored to EnemyIntent snapshot.
- Scope creep into broader AI/combat rework.

## Guardrail Summary

- EnemyIntent owns telegraph/commit/active/recovery/punish window truth.
- CombatCore owns combat timing/results.
- Animator/Animancer, VFX, Camera, Debug Overlay remain presentation/read-only layers.
- No tuning implementation in this change; planning artifacts only.
