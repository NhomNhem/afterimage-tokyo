## Context

M0 currently proves core duel mechanics but lacks a guaranteed lifecycle reset path that restores all runtime truth owners to a clean baseline in-place. Existing smoke/evidence runs rely on manual scene state conditions, which slows iteration and makes Sprint 1 closure fragile.

This change introduces the smallest practical encounter lifecycle wiring for one-player/one-enemy replay in Tokyo Street. It must preserve current ownership boundaries:

- Combat Core owns combat validity/state timing.
- Player Locomotion owns movement/transform expression reset.
- Enemy Intent owns enemy state loop reset.
- Target Context owns target truth and release/acquire validity.
- Debug Overlay is read-only reflection only.

## Goals / Non-Goals

**Goals:**
- Provide deterministic M0 reset flow: start duel -> active duel -> reset duel -> clean playable state.
- Reset core runtime systems without scene reload and without shifting truth into presentation.
- Expose one minimal reset trigger for smoke/evidence capture.
- Make post-reset state verifiable via logs + overlay snapshot.
- Keep implementation tightly scoped for Sprint 1 closure.

**Non-Goals:**
- Save/load, checkpoints, scene transitions, or global encounter manager platforming.
- Combat redesign, parry/counter redesign, lock-on redesign.
- Camera, VFX, memory, animation-authoritative reset behavior.
- UI restart menu or broader UX flows.
- Multi-enemy/boss lifecycle.

## Decisions

1. **Lifecycle expressed as a lightweight orchestrated reset path, not a new broad manager**
   - Rationale: We need closeable M0 scope and low regression risk.
   - Alternative considered: introducing a full `EncounterLifecycleService` abstraction now.
   - Why not now: larger refactor and ownership churn with limited Sprint 1 payoff.

2. **Reset remains distributed by ownership, coordinated by bootstrap/tick orchestration**
   - Combat Core: reset combat state/transients.
   - Player Locomotion: reset transform + locomotion transients.
   - Enemy Intent: reset intent model/loop to known start.
   - Target Context: release/reset current target state.
   - Rationale: matches current architecture and avoids truth drift.

3. **Reset trigger is minimal and test-oriented**
   - Keep existing input architecture; add/reset trigger only through approved M0 debug/smoke path.
   - Rationale: evidence-first goal without productizing restart UX.
   - Alternative considered: adding restart button/menu.
   - Why not now: out of scope and adds UI/system dependencies.

4. **Debug overlay remains read-only evidence surface**
   - Overlay displays post-reset snapshot fields; it does not issue reset commands or own state.
   - Rationale: preserves architecture contract and test reliability.

5. **Logging policy**
   - Use `INhemLogger`/NhemLogging wrapper only.
   - Keep noisy traces define-gated (`GR_M0_PROTOTYPE` / debug symbols); key warnings visible.

## Risks / Trade-offs

- **[Risk] Partial reset leaves stale transient flags (combat/input/locomotion).**
  - Mitigation: explicit reset checklist per owner + before/after evidence fields.

- **[Risk] Orchestrator accidentally becomes gameplay truth owner.**
  - Mitigation: orchestrator invokes existing owner APIs only; no duplicate state model.

- **[Risk] Reset order bugs (e.g., target release after overlay read).**
  - Mitigation: define deterministic reset order and capture ordered logs in evidence.

- **[Risk] Scope bleed into restart UX/camera/animation polish.**
  - Mitigation: enforce allowed/forbidden file list and spec non-goals.

## Migration Plan

1. Add/reset wiring in scoped runtime files only.
2. Add/update tests covering reset outcomes (state/transform/target).
3. Run compile + focused EditMode/PlayMode smoke.
4. Capture evidence before/after reset.
5. Mark tasks complete only with direct artifacts.

Rollback:
- Revert reset wiring change set; no data migration required because this is runtime-only behavior.

## Open Questions

- Should post-reset Target Context always be `None`, or optionally reacquire configured duel target by default in M0?
- Which reset trigger path is preferred for long-term (debug key vs. overlay button vs. test-only command)? For this change, keep one minimal approved trigger.

## Allowed Implementation Files

- `J:/afterimage-tokyo/afterimage-tokyo/Assets/_Project/Code/Bootstrap/M0GameplayTickHandler.cs`
- `J:/afterimage-tokyo/afterimage-tokyo/Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs`
- `J:/afterimage-tokyo/afterimage-tokyo/Assets/_Project/Code/Combat/M0CombatCore.cs` (reset API/wiring only)
- `J:/afterimage-tokyo/afterimage-tokyo/Assets/_Project/Code/Locomotion/M0PlayerLocomotion.cs` (reset API/wiring only)
- `J:/afterimage-tokyo/afterimage-tokyo/Assets/_Project/Code/Enemy/M0EnemyIntentModel.cs` (reset API/wiring only)
- `J:/afterimage-tokyo/afterimage-tokyo/Assets/_Project/Code/Bootstrap/M0EnemyIntentLoopDriver.cs` (reset orchestration only)
- `J:/afterimage-tokyo/afterimage-tokyo/Assets/_Project/Code/Targeting/M0TargetContext.cs` (reset/release hook only)
- `J:/afterimage-tokyo/afterimage-tokyo/Assets/_Project/Tests/EditMode/*` (targeted tests only)
- `J:/afterimage-tokyo/production/qa/evidence/*` (evidence only)

## Forbidden Implementation Files

- Any scene/prefab/material assets under `Assets/_Project/Content/**`
- Camera systems (`LockOn & Combat Camera`) except read-only observation
- Memory state/VFX systems
- Input binding asset/mapping architecture
- Animancer/root motion/KCC/NavMesh integrations
- Save/load/checkpoint or progression systems
