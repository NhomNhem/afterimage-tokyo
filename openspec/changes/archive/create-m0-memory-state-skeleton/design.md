## Context

M0 now has separate skeleton authorities for combat requests/results, locomotion truth, enemy intent rhythm, and health consequence truth. Memory reveal acceptance/rejection is the next boundary that needs an explicit owner so reveal outcomes are not inferred ad hoc by Combat Core or Health.

This change defines only the Memory State skeleton: pure C# state model, reveal request/result placeholders, reveal response/cooldown shape, read-only snapshot, and tests for core phase transitions. Presentation and content systems remain downstream and read-only.

## Goals / Non-Goals

**Goals:**
- Establish Memory State as the sole owner for reveal acceptance/rejection decisions in M0.
- Define a pure C# memory state model with inspectable phases: dormant, requested, accepted, rejected, responding, cooldown.
- Define reveal request/result contract shapes with reason/context placeholders.
- Define reveal response/cooldown state shape and transitions.
- Expose read-only memory snapshot for Debug Overlay and observers.
- Add edit-mode tests for idle/requested/accepted/rejected/responding/cooldown behavior.
- Preserve strict boundaries: Combat Core may produce context but must not accept reveal.
- Keep `M0Contracts.cs` contract-only.

**Non-Goals:**
- Memory VFX playback.
- Narrative graph integration.
- Clue database lookup.
- Branching memory progression.
- District reinterpretation logic.
- Save/persistence.
- Cutscene system.
- Combat validation logic changes.
- Damage application logic changes.
- Scene/prefab wiring.
- Legacy Input Manager support or generated DI APIs.

## Decisions

### 1. Keep reveal authority in a pure C# memory owner

**Decision:** Implement Memory State as a small pure C# model/FSM that owns reveal acceptance/rejection and cooldown truth.

**Why:** Keeps reveal policy deterministic and testable without scene/runtime dependencies.

**Alternatives considered:**
- Accept reveal directly in Combat Core
  - rejected because Combat Core owns combat request/result and CounterWindow, not reveal acceptance authority
- Accept reveal in Health consequence model
  - rejected because Health owns damage/reaction/defeat consequence only

### 2. Represent reveal flow with explicit request/result contracts

**Decision:** Accept reveal inputs through explicit request context and return explicit result shapes (accepted/rejected + reason).

**Why:** Prevents hidden side effects and makes acceptance criteria test-first.

**Alternatives considered:**
- Boolean-only acceptance output
  - rejected because rejection/ignore reasons are needed for debugging and future tuning

### 3. Separate response state from presentation playback

**Decision:** Model responding/cooldown as state-only placeholders and keep Memory VFX response downstream.

**Why:** Enforces gameplay truth vs presentation separation.

**Alternatives considered:**
- Trigger VFX/audio directly in memory model
  - rejected because this introduces presentation dependency and scope creep

### 4. Explicitly gate invalid reveal triggers

**Decision:** Include classification guards in request/result behavior so generic hits, failed dodge/parry/counter, and presentation-only events cannot produce accepted reveal.

**Why:** Prevents early coupling where any combat event might incorrectly become reveal truth.

**Alternatives considered:**
- Defer invalid trigger gating to later phases
  - rejected because ownership leaks happen earliest at boundary interfaces

### 5. Keep snapshots immutable for observers

**Decision:** Provide read-only memory snapshot for Debug Overlay and observers.

**Why:** Debug remains read-only and cannot mutate memory authority.

**Alternatives considered:**
- Mutable debug-accessible memory data
  - rejected because it weakens authority boundaries

## Risks / Trade-offs

- [Reveal rules are too placeholder-heavy for early content tests] -> Include reason/context fields so policy can evolve without replacing interface shape.
- [Combat Core starts embedding reveal acceptance shortcuts] -> Keep acceptance APIs in Memory State only and test that Combat Core remains non-authoritative.
- [Health consequence and memory reveal become conflated] -> Restrict health role to consequence context provider only.
- [Presentation requests become accepted reveal by mistake] -> Enforce explicit rejection of presentation-only categories.
- [Future persistence pressure adds premature state serialization] -> Keep persistence out of scope in M0 skeleton.

## Migration Plan

1. Review architecture and GDD boundaries for Memory State, Combat Core, Health, and Debug ownership.
2. Define/refine reveal request/result, response/cooldown, and read-only snapshot contract shapes in `M0Contracts.cs` (contracts-only).
3. Implement pure C# `M0MemoryState` skeleton in Memory module.
4. Implement transition and result behavior for dormant/requested/accepted/rejected/responding/cooldown.
5. Add rejection guards for generic hit/failed dodge/failed parry/invalid counter/presentation-only request categories.
6. Expose read-only snapshot and optional change signal for observers.
7. Add edit-mode tests for required phase and result behavior.
8. Run static checks for forbidden scope/dependency regressions.
9. Update OpenSpec task status after each verified completion.

Rollback strategy:
- Revert Memory skeleton files and contract additions if ownership boundaries are violated or non-goal dependencies leak in.

## Open Questions

- Should cooldown be expressed as simple phase token only, or include a provisional duration field in M0 contracts?
- Should accepted reveal result include a minimal reveal reason enum now, or defer to broader memory content passes?
- Should rejected reveal reasons be normalized into fixed codes now for test strictness?
