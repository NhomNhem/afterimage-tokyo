## Status

Status: completed-with-notes

Completion Note — 2026-05-25

Dodge displacement wiring is verified as PASS WITH NOTES.

Completed:
- Dodge accepted from Neutral enters `DodgeStartup -> DodgeActive -> DodgeRecovery -> Neutral`.
- Player locomotion applies visible displacement/lunge.
- Transform before/after delta is captured.
- Duplicate/invalid Dodge gating remains controlled by Combat Core.
- Compile/domain reload passed.
- EditMode and PlayMode foundation tests passed.
- WASD, LightAttack, EnemyIntent smoke passed.
- LockOn smoke accepted by reference to prior completed LockOn evidence artifacts.

Notes:
- LockOn was not re-captured directly in this artifact; accepted by reference because this change did not modify LockOn, TargetContext, input bindings, camera, or target overlay behavior.

## Why

Current M0 evidence proves Dodge input and Combat Core Dodge state transitions, but the player does not visibly dodge/lunge in world space. This creates a feel/readability gap in the M0 loop and leaves defensive response under-expressed.

## What Changes

- Add a dedicated dodge displacement capability owned by Player Locomotion.
- Wire Combat Core Dodge acceptance/state into a locomotion dodge displacement request path.
- Introduce explicit dodge movement profile tuning (distance/speed/duration/direction policy) for M0.
- Add debug-visible evidence outputs to confirm displacement before/after in PlayMode verification.
- Keep LockOn/Target behavior unchanged and non-authoritative for movement truth.

## Capabilities

### New Capabilities
- `dodge-displacement-locomotion`: Player locomotion applies a short, readable displacement when Dodge is accepted and active, with deterministic tuning and debug-verifiable movement results.

### Modified Capabilities
- None.

## Impact

- Affected systems: Player Locomotion ownership boundary, M0GameplayTickHandler bridge layer, locomotion settings/config, debug/evidence capture.
- Unaffected by scope: Combat Core validation semantics, Parry/Counter logic, LockOn input binding, camera feature set, memory systems.
- M0 loop impact: improves `evade/parry` leg readability by making Dodge a visible positional response rather than state-only progression.

## Non-goals

- No Combat Core redesign.
- No invulnerability frame system.
- No stamina/cost mechanics.
- No root-motion authority shift.
- No KCC/NavMesh integration.
- No camera shake/cinematic additions.
