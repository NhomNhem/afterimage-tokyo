# Tasks: Complete M0 Playable Combat Prototype Verification

> **Change**: complete-m0-playable-combat-prototype-verification  
> **Source Context**: archived `create-m0-playable-combat-prototype-scene` left PlayMode verification gaps

## Closure Snapshot (Documentation Hygiene)

- Story-done outcome: **COMPLETE WITH NOTES** (2026-05-21)
- Blocking status: **No FAIL items / No remaining blockers**
- Canonical verification result: `production/qa/evidence/complete-m0-playable-combat-prototype-verification-evidence.md`
- Non-blocking follow-ups remain tracked separately:
  - Parry visual feedback capture/polish
  - Counter visual feedback capture/polish
  - LockOn second-press behavior decision (acquire-only/maintain focus vs toggle acquire/release)

Note:
- Checklist items below are retained as historical execution checklist for the change.
- Closure/readiness is determined by the evidence file and story-done record, not by re-opening this checklist.

---

## 1) Runtime Camera and Visibility Verification

- [x] 1.1 Open `Assets/_Project/Content/Scenes/Gameplay/Gameplay_CombatPrototype.unity`
- [ ] 1.2 Enter PlayMode and verify Main Camera renders Game View (no runtime camera error)
- [ ] 1.3 Verify PlayerMesh is visible in Game View
- [ ] 1.4 Verify EnemyMesh is visible in Game View
- [ ] 1.5 Verify PlayerMesh follows Player transform during movement/actions
- [ ] 1.6 Verify EnemyMesh follows Enemy presentation state/transform
- [ ] 1.7 If any reference is broken, apply minimal scene/reference fix only (no gameplay behavior changes)

## 2) Camera Movement Basis and Movement Visibility

- [x] 2.1 Verify `CameraMovementBasisProvider` references runtime Main Camera
- [ ] 2.2 Verify WASD visibly moves Player in Game View
- [ ] 2.3 Capture proof logs/screenshots/notes for movement visibility

## 3) Visual Feedback PlayMode Verification

- [ ] 3.1 Verify LightAttack visual feedback
- [ ] 3.2 Verify HeavyAttack visual feedback
- [ ] 3.3 Verify Parry visual feedback
- [ ] 3.4 Verify Dodge visual feedback
- [ ] 3.5 Verify Counter visual feedback inside valid counter window
- [ ] 3.6 Verify enemy visual cycle for Telegraph -> Active -> Recovery

## 4) Debug Overlay Runtime Verification

- [ ] 4.1 Verify Debug Overlay is visible in Game View
- [ ] 4.2 Verify Combat label updates
- [ ] 4.3 Verify Enemy state label updates
- [ ] 4.4 Verify CounterWindow label updates
- [ ] 4.5 Verify Last Input label updates
- [ ] 4.6 Verify LockOn target label updates
- [ ] 4.7 Verify overlay toggle behavior works as currently wired

## 5) Gameplay Preservation Verification

- [ ] 5.1 Re-run Story 1-6 defensive loop smoke (`F6 -> Q -> wait Neutral -> E`) and confirm expected logs
- [ ] 5.2 Verify no CombatCore behavior drift
- [ ] 5.3 Verify no Locomotion behavior drift
- [ ] 5.4 Verify no EnemyIntentModel behavior drift
- [ ] 5.5 Verify no input architecture drift

## 6) Scope Exclusion Sweep

- [x] 6.1 Confirm no health/damage/hit-reaction scope added
- [x] 6.2 Confirm no memory reveal/VFX scope added
- [x] 6.3 Confirm no Animancer/root motion authority added
- [x] 6.4 Confirm no KCC/NavMesh scope added
- [x] 6.5 Confirm no generated DI and no forbidden API regressions

## 7) Verification Checklist and Evidence Artifact

- [x] 7.1 Produce a verification checklist artifact under `production/qa/evidence/`
- [x] 7.2 Include pass/fail per required check from sections 1-6
- [x] 7.3 Include notable logs and any non-blocking tooling noise
- [x] 7.4 Include explicit statement: "verification/testability cleanup only; no new gameplay"
- [x] 7.5 Include archive-readiness recommendation for this follow-up change

---

## Verification Checklist (must be explicit in evidence)

- [ ] Main Camera renders Game View
- [ ] PlayerMesh visible and follows Player
- [ ] EnemyMesh visible and follows Enemy
- [ ] CameraMovementBasisProvider bound to runtime Main Camera
- [ ] WASD movement visible
- [ ] LightAttack visual feedback
- [ ] HeavyAttack visual feedback
- [ ] Parry visual feedback
- [ ] Dodge visual feedback
- [ ] Counter visual feedback in valid window
- [ ] Enemy Telegraph/Active/Recovery visual cycle
- [ ] Debug overlay labels visible and updating
- [ ] Gameplay preservation block passes
- [ ] Scope exclusion sweep passes

---

## Expected Evidence

- PlayMode verification notes with pass/fail for each checklist item
- Captured logs proving combat/input/debug overlay transitions
- Any minimal scene/reference fixes listed with file paths
- Explicit confirmation that hard exclusions were respected
