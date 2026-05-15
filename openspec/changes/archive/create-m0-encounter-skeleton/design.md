## Context

M0 already splits ownership across dedicated systems: Combat Core owns combat validation and result truth, Enemy Intent owns telegraph and punish truth, Health owns damage and defeat consequence truth, Target Context owns target truth, Memory State owns reveal acceptance, Memory VFX Response is downstream presentation only, and Debug Overlay is read-only. Encounter Framework needs to sit above those systems as a lifecycle shell only.

The encounter layer should make one duel repeatable and inspectable. It should not decide combat results, target truth, reveal truth, or presentation behavior.

## Goals / Non-Goals

**Goals:**
- Model the encounter lifecycle explicitly: uninitialized, preparing, ready, starting, active, completing, completed, failed, aborted, resetting
- Track one player and one enemy as registered duel participants
- Surface readiness blockers and end/reset reasons in read-only debug data
- Observe player defeat, enemy defeat, reveal acceptance, and manual abort/reset without owning them
- Keep the system small enough to prove the first duel without creating a god system

**Non-Goals:**
- No wave spawning
- No boss framework
- No quest or narrative system
- No save/persistence
- No loot/reward logic
- No scene loading or prefab spawning
- No combat result validation
- No enemy AI behavior
- No health mutation
- No target switching system
- No camera/UI/VFX behavior

## Decisions

### 1. Explicit lifecycle state machine
Use a small enum-driven state model instead of event-driven or hierarchical lifecycle objects.

Rationale: M0 needs clarity and testability more than extensibility. An explicit lifecycle makes readiness, start, active, and end states easy to inspect and assert.

Alternatives considered: event-driven encounter orchestration, nested state objects.

### 2. One player / one enemy registration only
The encounter registers exactly one player and one enemy for M0.

Rationale: The prototype only proves a single duel. Avoiding roster logic keeps ownership boundaries clean and prevents mission/wave scope creep.

Alternatives considered: generic multi-participant roster, spawn-managed participant lists.

### 3. Observation-only integration with other systems
Encounter may observe combat, health, target, memory, and manual reset/abort signals, but never becomes authoritative for them.

Rationale: This preserves the architecture contract that each gameplay truth remains in its owning system.

Alternatives considered: encounter as a coordinator that issues combat or target commands (rejected).

### 4. Read-only snapshots for debug and tooling
Expose read-only snapshots that summarize lifecycle state, participants, blockers, and observed reasons.

Rationale: Debug Overlay needs clear visibility without mutating encounter truth. This mirrors the broader M0 contract style.

Alternatives considered: direct mutable fields, debug-only mirror objects.

## Risks / Trade-offs

- [Risk] Encounter becomes a god system ➔ Mitigation: keep the model lifecycle-only and observe adjacent systems instead of owning them.
- [Risk] Readiness becomes ambiguous ➔ Mitigation: expose explicit blockers and a simple prepare/ready transition.
- [Risk] Reset gets complicated ➔ Mitigation: keep reset local, explicit, and debug-visible.
- [Risk] Runtime target ownership blurs ➔ Mitigation: allow only initial seeding; hand off runtime target truth to Lock-On / Target Context.
