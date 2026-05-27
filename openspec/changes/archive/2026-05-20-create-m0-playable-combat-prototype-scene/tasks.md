# Tasks Reconciliation: Create M0 Playable Combat Prototype Scene

> **Change**: create-m0-playable-combat-prototype-scene
> **Archived at**: openspec/changes/archive/2026-05-20-create-m0-playable-combat-prototype-scene
> **Status note**: This archive reflects a **partial, evidence-driven defensive-loop visible slice**, not strict completion of every originally planned task.

---

## Evidence-backed Completed Tasks

### Scene/bootstrap foundations
- [x] Opened `Gameplay_CombatPrototype.unity` and worked in-scene
- [x] Main Camera object presence/configuration setup tasks completed (structural setup)
- [x] Player and enemy placeholder visibility setup tasks completed (structural setup)
- [x] Scene save steps performed during prior fix/verification passes

### Enemy loop / defensive deterministic path evidence
- [x] Enemy loop transitions evidenced: Idle -> Telegraph -> Commit -> Active -> Recovery -> Idle
- [x] Input logs and combat logs evidenced for deterministic defensive loop path
- [x] F6 debug harness route evidenced
- [x] F6 -> Q -> wait Neutral -> E path evidenced
- [x] CounterWindow open/consume/CounterActive evidence captured

### Architecture/compliance constraints evidenced
- [x] No fallback lookup retained
- [x] No direct `UnityEngine.Debug.Log/Warning/Error` retained
- [x] No CombatCore rule ownership change
- [x] No input binding architecture change
- [x] Animation refs treated as optional/deferred for smoke path

### Presentation implementation existence (not full runtime proof)
- [x] Visual feedback adapter code exists
- [x] Debug overlay adapter code exists
- [x] Core debug snapshot update path evidenced in logs/reports

---

## Deferred / Requires Fresh PlayMode Verification

> Keep these unchecked until fresh PlayMode verification is run and recorded.

- [ ] Main Camera conclusively renders Game View in current scene state (`No cameras rendering` absent)
- [ ] PlayerMesh is visibly rendered and follows Player transform during movement/actions
- [ ] EnemyMesh is visibly rendered and follows Enemy transform/state presentation
- [ ] `CameraMovementBasisProvider` is confirmed bound to runtime Main Camera
- [ ] WASD movement visibly moves Player in Game View
- [ ] LightAttack visual feedback verified in PlayMode
- [ ] HeavyAttack visual feedback verified in PlayMode
- [ ] Parry visual feedback verified in PlayMode
- [ ] Dodge visual feedback verified in PlayMode
- [ ] Counter visual feedback verified inside valid counter window
- [ ] Enemy Telegraph / Active / Recovery visual cycle verified in PlayMode
- [ ] Debug Overlay labels are visibly rendered in Game View
- [ ] Debug Overlay labels update live for combat/enemy/counter/input/lock-on fields
- [ ] Debug Overlay toggle behavior is verified at runtime
- [ ] Full gameplay-preservation PlayMode block re-run and recorded
- [ ] Scope exclusion sweep re-run and recorded
- [ ] Fresh EditMode/PlayMode verification artifact linked from this archived change

---

## Truthful Reconciliation Notes

- [x] Input logs and combat logs are evidenced.
- [x] Visual feedback is implemented, but not fully PlayMode-verified end-to-end.
- [x] Debug overlay is partially evidenced; runtime labels/toggle are not fully task-proven.
- [x] Main Camera runtime rendering is not conclusively task-proven in this archived checklist.

---

## Follow-up Change Candidate

- [ ] **complete-m0-playable-combat-prototype-verification**
      Verification/testability cleanup follow-up to finish deferred PlayMode checks and minimal scene/reference fixes only.
