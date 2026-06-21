# ADR-0003: M0 Presentation and Debug Read-Only Boundaries

## Status
Accepted

## Date
2026-06-21

## Engine Compatibility

| Field | Value |
|-------|-------|
| **Engine** | Unity 6000.3.x + URP |
| **Domain** | Animation, Camera, UI, Debug |
| **Knowledge Risk** | MEDIUM — Animator Controller and Cinemachine behavior stable across Unity 6; URP renderer features changed (RenderGraph) but this ADR does not touch custom render passes. |
| **References Consulted** | `docs/engine-reference/unity/VERSION.md`; `docs/engine-reference/unity/breaking-changes.md`; `docs/engine-reference/unity/deprecated-apis.md`; `docs/engine-reference/unity/modules/animation.md` |
| **Post-Cutoff APIs Used** | None — this ADR constrains presentation systems to observe-only patterns using standard Unity APIs. |
| **Verification Required** | EditMode tests confirming presentation files do not mutate gameplay state; code review boundary checks on presentation layer. |

## ADR Dependencies

| Field | Value |
|-------|-------|
| **Depends On** | ADR-0002 (M0 Gameplay Truth Ownership Boundaries) — this ADR defines the read-only side of the ownership boundary ADR-0002 establishes. |
| **Enables** | S8-2 (Dodge Animation Phase Distinction); S8-3 (Parry & Counter Animation Transition Readability); S8-4 (Hit Reaction Animation Blending) — all Presentation layer animation polish stories. |
| **Blocks** | None. |
| **Ordering Note** | This ADR must be Accepted before any Presentation layer story is implemented, so that animator and debug systems know they may only observe, never mutate. |

## Context

### Problem Statement

M0 needs clear presentation-layer rules so that animation, camera, VFX, and debug systems never accidentally become gameplay truth owners. Without this boundary:
- Animator clip length could define recovery duration (gameplay truth).
- Camera framing could decide target validity (gameplay truth).
- Debug overlay could hide or override gameplay state (gameplay truth).
- VFX could gate reveal acceptance (gameplay truth).

These would create hidden authorities that make combat behavior unpredictable and unreadable.

### Constraints
- Animator is Unity's built-in animation system — it has state machines but they must not compete with Pure C# state machines.
- Debug overlay is read-only by design — no mutation of gameplay state from debug code.
- VFX is downstream of memory-state acceptance — VFX observes, does not decide.
- Camera owns framing only — does not own target truth or movement truth.

### Requirements
- Animator must be presentation-only: observes Pure C# combat/locomotion snapshots and triggers clips accordingly.
- Camera must provide framing/readability only — does not own target/movement truth.
- Debug Overlay must be a read-only observer of aggregated gameplay snapshots.
- VFX Response must be downstream presentation only — fires after accepted reveal, does not gate it.
- No presentation system may mutate gameplay state.
- Animation clip length must not define gameplay timing (dodge recovery, invincibility window, counter window).

## Decision

**All presentation systems (Animator, Camera, VFX, Debug Overlay) MUST observe gameplay truth as read-only snapshots or context. They must not create, mutate, repair, or override gameplay state.**

### Ownership Matrix

| System | Owns | Must NOT Own |
|--------|------|-------------|
| **Animator** | Clip selection, blend weights, parameter values, transition settings | Combat state, locomotion truth, dodge timing, parry timing, recovery duration, hit validity, counter window |
| **Camera** | Framing position, blend timing, field-of-field, readability framing | Target truth, movement truth, combat truth |
| **Debug Overlay** | Grouping, formatting, snapshot aggregation, read-only display | Gameplay state creation, inference, repair, override |
| **VFX Response** | Visual particle emission, timing, intensity, color | Memory reveal acceptance/rejection, combat results, damage outcomes |

### Architecture

```
Pure C# Truth (CombatCore, Locomotion, Memory, TargetContext)
    │
    ├──► Snapshot Reader ──► Animator Presenter ──► Animator Controller / clips
    ├──► Snapshot Reader ──► Camera Presenter ──► Cinemachine cameras
    ├──► Snapshot Reader ──► Debug Overlay ──► UI display
    └──► Snapshot Reader ──► VFX Presenter ──► Particle systems / VFX Graph
```

Flow:
1. Pure C# systems compute gameplay truth (state enums, timing, results).
2. Presentation presenters read snapshots or state readers (read-only interfaces).
3. Presenters map state to Unity presentation APIs (Animator parameters, Cinemachine blend, VFX emission, UI text).
4. No presentation system writes back to gameplay truth.

### Key Interfaces

```csharp
/// Read-only interface for combat state observation.
public interface ICombatStateReader
{
    CombatSnapshot CurrentSnapshot { get; }
}

/// Read-only interface for locomotion state observation.
public interface ILocomotionStateReader
{
    LocomotionSnapshot CurrentSnapshot { get; }
}

/// Read-only interface for memory state observation.
public interface IMemoryStateReader
{
    MemorySnapshot CurrentSnapshot { get; }
}
```

### Animator Implementation Rules

- Animator parameters are set by presenters, not read back for gameplay decisions.
- Animation events may trigger presentation effects (sound, particle) but must not call gameplay state changes.
- Animator Controller state machine mirrors Pure C# state machine state; it does not define timing.
- Dodge, attack, parry, and recovery clips are selected based on Pure C# state, not Animator state machine transitions.
- Blend tree weights are tuned for visual feel only — gameplay values (dodge distance, recovery time) come from Pure C# config.

### Camera Implementation Rules

- Camera presenter reads target context from Pure C# (position, forward, right).
- Cinemachine blend timing is presentation-only — does not gate combat input windows.
- Camera framing follows target truth; it does not decide which target is active.

### Debug Overlay Implementation Rules

- Debug Overlay aggregates read-only snapshots from gameplay systems.
- Debug display shows truth, does not create or modify truth.
- Debug buttons (if present) are behind `#if GR_DEBUG` defines and call explicit debug methods on gameplay services — they do not mutate state directly.

### VFX Response Implementation Rules

- VFX Response reads memory-state acceptance result; it fires after acceptance.
- VFX does not determine whether a reveal is accepted — MemoryState does.
- VFX parameters (intensity, duration, color) are tuned for visual feel; they do not affect gameplay outcomes.

## Alternatives Considered

### Alternative 1: Animator as primary state machine
- **Description**: Use Unity Animator Controller as the authoritative state machine for combat, with animation events driving gameplay logic.
- **Pros**: Visual state machine in Unity Editor, animation-driven timing feels natural, fewer C# state machines.
- **Cons**: Animator is not testable in EditMode, hard to unit-test timing windows, creates tight coupling between animation and gameplay truth, makes debugging opaque.
- **Rejection Reason**: Violates M0 principle of testable, frame-readable combat truth. Animator is a presentation system, not a gameplay authority.

### Alternative 2: Mixed ownership with cross-system communication
- **Description**: Allow presentation systems to read and write limited gameplay state (e.g., Animator sets "dodge complete" flag after animation finishes).
- **Pros**: Simpler code paths, fewer adapters, faster prototyping.
- **Cons**: Hidden ownership, race conditions between systems, unpredictable behavior, harder to debug and test.
- **Rejection Reason**: Creates exactly the hidden authority problem this ADR exists to prevent.

### Alternative 3: No formal boundary — rely on code review
- **Description**: Do not document this ADR; rely on code review and developer discipline to keep presentation separate.
- **Pros**: No documentation overhead, flexibility.
- **Cons**: Boundary drift over time, inconsistent enforcement, new developers may not know the rule.
- **Rejection Reason**: M0's small scope makes this tempting, but the boundary is fundamental to the entire architecture. Code review alone is insufficient guardrail.

## Consequences

### Positive
- Clear, testable ownership: gameplay truth is in Pure C#, presentation observes.
- EditMode tests can verify presentation did not mutate state.
- Combat behavior is deterministic and explainable from Pure C# alone.
- Debug overlay provides reliable explanation of what happened.
- New developers have an explicit rule, not an implicit convention.

### Negative
- Requires adapter code between Pure C# and Unity presentation APIs.
- Two state machines to maintain (Pure C# truth + Animator mirror).
- Presentation feels slightly more disconnected from gameplay timing during prototyping.

### Risks
- **Risk**: Animator state machine drifts out of sync with Pure C# state machine.
  - **Mitigation**: Animator parameters are set explicitly from Pure C# state; no Animator-to-gameplay feedback loop.
- **Risk**: Debug overlay accidentally becomes a mutation point (e.g., debug button changes state).
  - **Mitigation**: Debug-only mutation methods are explicit on gameplay services, not direct state writes. Guarded by `#if GR_DEBUG` defines.
- **Risk**: VFX Response fires before memory acceptance is confirmed.
  - **Mitigation**: VFX reads memory-state acceptance result explicitly, does not trigger on proximity or input alone.

## GDD Requirements Addressed

| GDD System | Requirement | How This ADR Addresses It |
|------------|-------------|--------------------------|
| m0-animator-presentation-only.md | Animator owns presentation only; does not affect gameplay truth | Defines Animator as observation-only system; Pure C# owns all timing and validity. |
| m0-camera-framing-readonly.md | Camera owns framing and readability only; does not own target/movement truth | Camera reads target context; does not decide target or movement. |
| m0-debug-overlay-read-only.md | Debug Overlay owns grouping and presentation only; does not own debug truth | Debug aggregates read-only snapshots; creates nothing, displays everything. |
| m0-memory-vfx-response-presentation.md | Memory VFX Response is downstream presentation only | VFX fires after acceptance; does not gate or decide reveal. |
| systems-index.md | Ownership boundaries remain explicit | This ADR codifies the presentation side of all ownership boundaries. |

## Performance Implications
- **CPU**: Neutral — snapshot reads are cheap; no additional per-frame computation.
- **Memory**: Minimal — snapshot structs are small value types; no heap allocation.
- **Load Time**: Neutral — no additional scene or asset loading.
- **Network**: Not applicable.

## Migration Plan

1. **Audit existing presentation code**: Verify no presentation system currently mutates gameplay state.
2. **Add reader interfaces**: Ensure `ICombatStateReader`, `ILocomotionStateReader`, `IMemoryStateReader` exist and are used by presenters.
3. **Remove gameplay writes from presenters**: Any presenter that sets gameplay state must be refactored to call the owning service instead.
4. **Add EditMode tests**: Test that presentation presenters read but do not write gameplay state.
5. **Update stories**: Reference this ADR in all Presentation layer stories so implementers know the boundary.

## Validation Criteria
- No presentation file modifies gameplay state (verified by code review + EditMode tests).
- Animator parameters are set exclusively from Pure C# state readers.
- Debug Overlay displays only read-only snapshot data.
- VFX Response fires only after confirmed memory-state acceptance.
- Camera presenter reads target context; does not mutate target state.

## Related Decisions
- ADR-0002 (M0 Gameplay Truth Ownership Boundaries) — the Pure C# side of this boundary.
- ADR-0001 (Decompose M0 Gameplay Tick Handler Orchestration) — orchestration layer that coordinates snapshot fan-out to presentation readers.
- Story 1-11 (Animator Observer Adapters) — implementation of this ADR's Animator rules.
- Story S8-2 (Dodge Animation Phase Distinction) — uses this ADR's Animator presentation-only rules.
