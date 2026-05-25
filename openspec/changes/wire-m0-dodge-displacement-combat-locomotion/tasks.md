## 1. Scope Guardrails

- [x] 1.1 Confirm change scope is limited to dodge displacement wiring and evidence closure for locomotion/combat integration.
- [x] 1.2 Confirm no changes to LockOn behavior, Parry/Counter logic, Memory systems, camera features, or input bindings.
- [x] 1.3 Confirm no scene/prefab/material authored changes are required for this implementation slice.

## 2. Locomotion Dodge Displacement Capability

- [x] 2.1 Add/define explicit dodge displacement profile fields in locomotion tuning/settings with validation guards.
- [x] 2.2 Add locomotion-side dodge displacement execution path that updates movement truth in world space.
- [x] 2.3 Ensure dodge displacement does not alter normal move-speed logic outside dodge windows.
- [x] 2.4 Ensure invalid profile values fail fast with clear setup diagnostics.

## 3. Combat-to-Locomotion Bridge Wiring

- [x] 3.1 Wire accepted dodge state flow from Combat Core snapshot transitions into locomotion displacement trigger.
- [x] 3.2 Prevent duplicate displacement application during repeated snapshot notifications in the same dodge cycle.
- [x] 3.3 Ensure rejected dodge requests do not trigger locomotion displacement.

## 4. Debug/Testability

- [x] 4.1 Keep logging on project logger wrapper only (no direct UnityEngine.Debug.Log in project code).
- [x] 4.2 Add transition-level evidence-friendly displacement log/snapshot outputs (before/after or equivalent) with define-gated noise control.
- [x] 4.3 Validate debug overlay remains read-only and does not become gameplay authority.

## 5. Verification & Evidence

- [x] 5.1 Run focused PlayMode verification: accepted dodge from Neutral produces visible displacement.
- [x] 5.2 Run negative verification: rejected dodge does not produce displacement.
- [x] 5.3 Verify dodge combat state chain remains: `Neutral -> DodgeStartup -> DodgeActive -> DodgeRecovery -> Neutral`.
- [x] 5.4 Verify no new gameplay console errors in smoke run.
- [x] 5.5 Update evidence artifacts with displacement proof and close the external follow-up reference (`m0-dodge-displacement-wiring`).

Verification note (2026-05-25):
- `5.1`/`5.2` closed by manual PlayMode logs showing Dodge state chain and position delta:
  `[M0Locomotion] Dodge displacement started: before=(-1.28,0.00,0.00)`
  and
  `[M0Locomotion] Move applied: before=(-1.28,0.00,0.00) after=(-1.36,0.00,0.02)`.
- `5.3` closed by both manual PlayMode logs and EditMode evidence (`GlassRefrain.Tests.EditMode.M0CombatCoreTests`).
- `5.4` closed by manual smoke (no new hard gameplay errors observed; only known non-blocking animation presentation warnings).
- `5.5` closed as PASS BY REFERENCE: WASD + LightAttack + EnemyIntent smoke proven in this run, and LockOn smoke is accepted by reference to prior completed LockOn evidence artifacts because this change does not touch LockOn scope.

## Closure Snapshot — 2026-05-25

Verdict: COMPLETED WITH NOTES

Evidence:
- `production/qa/evidence/wire-m0-dodge-displacement-combat-locomotion-verification-2026-05-25.md`

Summary:
- 5.1 PASS
- 5.2 PASS
- 5.3 PASS
- 5.4 PASS
- 5.5 PASS BY REFERENCE

Notes:
- LockOn smoke accepted by reference to prior completed LockOn evidence:
  - `production/qa/evidence/lockon-toggle-release-2026-05-24.md`
  - `production/qa/evidence/lockon-toggle-release-2026-05-24-artifacts.md`
  - `openspec/changes/archive/2026-05-25-decide-m0-lockon-second-press-toggle-release`

Archive readiness: YES after clean scoped commit.
