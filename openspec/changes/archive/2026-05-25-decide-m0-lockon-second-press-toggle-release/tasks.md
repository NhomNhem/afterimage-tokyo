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
- [x] 3.2 Ensure `LockOn Target` reflects transitions:
  - [x] `None -> Enemy -> None -> Enemy`
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

- [x] 5.1 Press Tab when `LockOn Target == None` acquires valid enemy target.
- [x] 5.2 Press Tab again while locked releases target and overlay returns to `None`.
- [x] 5.3 Press Tab again reacquires valid target.
- [x] 5.4 If no valid target exists, acquire is rejected with clear debug/log reason.
- [x] 5.5 Debug overlay shows `LockOn Target: None -> Enemy -> None -> Enemy`.
- [ ] 5.6 No regression to locomotion/combat smoke flow.
- [x] 5.7 No new gameplay console errors.

## 6) Evidence Required

- [x] 6.1 Log excerpt proving acquire -> release -> acquire.
- [x] 6.2 Overlay screenshot/video/log proving `LockOn Target: None -> Enemy -> None -> Enemy`.
- [x] 6.3 Smoke PlayMode result confirms no new gameplay errors.

### Evidence Audit — 2026-05-24

- Reviewed tracked evidence files:
  - `production/qa/evidence/complete-m0-playable-combat-prototype-verification-evidence.md`
  - `production/qa/evidence/story-1-6-defensive-wiring-evidence.md`
  - `production/qa/evidence/story-1-7-health-consequence-evidence.md`
- Result:
  - Existing evidence proves LockOn input/acquire in prior runs, but does **not** yet prove full toggle-release sequence for this change.
  - No tracked artifact currently contains:
    - `[M0Target] LockOn acquired`
    - `[M0Target] LockOn released`
    - `LockOn Target: None -> Enemy -> None -> Enemy`
- At that audit time, tasks 3.2 / 5.1-5.5 / 6.1-6.2 remained intentionally unchecked pending fresh manual PlayMode capture artifacts.

### Evidence Update — 2026-05-24 (Manual PlayMode)

- Added manual evidence file:
  - `production/qa/evidence/lockon-toggle-release-2026-05-24.md`
- Manual observation confirmed:
  - `LockOn Target: None -> Enemy -> None -> Enemy`
  - First Tab acquire, second Tab release, third Tab reacquire
  - No new gameplay console errors observed during LockOn run
- Checked as manual-evidence satisfied:
  - 3.2, 5.1, 5.2, 5.3, 5.5, 5.7, 6.3
- Still pending due to missing explicit artifact type:
  - 5.6 remains pending

### Evidence Update — 2026-05-25 (Dodge Displacement Triage)

- Regression smoke triage confirms:
  - Dodge input path and Combat Core Dodge state chain are working:
    `Neutral -> DodgeStartup -> DodgeActive -> DodgeRecovery -> Neutral`
  - Player dodge displacement/lunge is not observed in this pass.
- Determination:
  - This is not a LockOn toggle-release regression.
  - This is a separate locomotion/combat integration gap (dodge displacement gameplay expression).
- 5.6 status:
  - PARTIAL / external follow-up.
  - Evidence reference: `production/qa/evidence/lockon-toggle-release-2026-05-24.md` (Dodge Displacement Triage Note section).

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

## Closure Snapshot — 2026-05-25

Status: completed-with-notes

### Closed

- LockOn second-press toggle-release behavior verified.
- `None -> Enemy -> None -> Enemy` transition verified.
- No-valid-target rejection path verified.
- `6.1` acquire -> release -> acquire log excerpt artifact referenced.
- `6.2` Debug Overlay transition artifact referenced.

### Notes

- `5.6` remains PARTIAL as an external follow-up.
- Dodge input and Combat Core Dodge state chain are proven, but Dodge displacement/lunge movement is not implemented/wired in the current M0 locomotion path.
- Follow-up is tracked in `docs/tech-debt-register.md` as `m0-dodge-displacement-wiring`.
- This does not block LockOn target-context behavior closure.

### Evidence

- `production/qa/evidence/lockon-toggle-release-2026-05-24.md`
- `production/qa/evidence/lockon-toggle-release-2026-05-24-artifacts.md`

### Archive Readiness

Ready for archive hygiene: YES
