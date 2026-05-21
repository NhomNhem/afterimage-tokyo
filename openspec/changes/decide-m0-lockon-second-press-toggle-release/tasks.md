# Tasks: [Targeting] LockOn Second-Press Toggle Release Decision & Wiring

## 1) Decision Baseline

- [x] 1.1 Confirm M0 decision is Option B: toggle acquire/release.
- [x] 1.2 Confirm scope is limited to LockOn target-state behavior (no combat/memory/camera expansion).
- [x] 1.3 Confirm archived verification changes remain closed and are not reopened.

## 2) LockOn Intent Handling (Target Context Owns Truth)

- [x] 2.1 Keep existing LockOn input binding unchanged.
- [x] 2.2 Keep input layer as intent emitter only (no target ownership in input mapping/routing).
- [x] 2.3 Update target-context handling:
  - [x] 2.3.1 When `LockOn Target == None`, attempt acquire valid target.
  - [x] 2.3.2 When `LockOn Target != None`, release target to `None`.
  - [x] 2.3.3 Next press after release reacquires valid target when available.
- [x] 2.4 If no valid target exists, reject acquire with clear debug/log reason via NhemLogger/NhemLogging.

## 3) Debug/Overlay Expectations (Read-only)

- [x] 3.1 Preserve debug overlay as read-only.
- [ ] 3.2 Ensure `LockOn Target` reflects transitions:
  - [ ] `None -> Enemy -> None -> Enemy`
- [x] 3.3 Ensure no gameplay truth moves into overlay/UI.

## 4) Regression Guardrails

- [x] 4.1 Confirm no Combat Core modifications.
- [x] 4.2 Confirm no Parry/Counter modifications.
- [x] 4.3 Confirm no Memory State / Memory VFX modifications.
- [x] 4.4 Confirm no camera feature additions.
- [x] 4.5 Confirm no input-binding changes.
- [x] 4.6 Confirm no Animancer/root motion/KCC/NavMesh additions.
- [x] 4.7 Confirm no targeting architecture refactor.

## 5) Acceptance Criteria

- [ ] 5.1 Press Tab when `LockOn Target == None` acquires valid enemy target.
- [ ] 5.2 Press Tab again while locked releases target and overlay returns to `None`.
- [ ] 5.3 Press Tab again reacquires valid target.
- [ ] 5.4 If no valid target exists, acquire is rejected with clear debug/log reason.
- [ ] 5.5 Debug overlay shows `LockOn Target: None -> Enemy -> None -> Enemy`.
- [ ] 5.6 No regression to locomotion/combat smoke flow.
- [ ] 5.7 No new gameplay console errors.

## 6) Evidence Required

- [ ] 6.1 Log excerpt proving acquire -> release -> acquire.
- [ ] 6.2 Overlay screenshot/video/log proving `LockOn Target: None -> Enemy -> None -> Enemy`.
- [ ] 6.3 Smoke PlayMode result confirms no new gameplay errors.

## 7) Implementation Rules

- [x] 7.1 Use NhemLogger/NhemLogging only; no direct UnityEngine.Debug.Log in project code.
- [x] 7.2 Keep target truth in Target Context.
- [x] 7.3 Keep debug overlay read-only.
- [x] 7.4 Keep input mapping intent-only.
- [x] 7.5 Do not modify Combat Core for this change.

---

### Definition of Ready to Implement

Implementation may proceed once:

- Decision Option B is explicitly accepted.
- This task list is approved as the execution boundary.
- Acceptance/evidence criteria above are accepted without expansion.
