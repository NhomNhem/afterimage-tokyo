## Context

M0 memory reveals are downstream presentation responses to accepted Memory State context. The architecture requires strict separation of concerns:

- **Combat Core** owns combat validity, reveal request context, and CounterWindow
- **Memory State** owns reveal acceptance/rejection, memory-side consequence, and reveal state truth
- **Memory VFX Response** owns only the visual presentation timeline after Memory State acceptance
- **Debug Overlay** reads VFX state for observation-only
- **Lock-On & Combat Camera** owns framing; VFX response complements but does not drive framing
- **Enemy Intent & Telegraph** owns enemy readability and punish windows; VFX must not obscure these
- **Health / Damage / Hit Reaction** owns damage and stagger; VFX must not imply either

The hard rule: Memory VFX Response must not infer reveal validity. It only plays after Memory State has already accepted the context. Rejected or ignored contexts must not produce VFX playback.

## Goals / Non-Goals

**Goals:**
- Build a pure C# state model that manages VFX response lifecycle (idle → requested → playing → cooldown or reset)
- Enforce that VFX only plays after accepted Memory State context through observer-friendly API
- Provide read-only snapshots for Debug Overlay and other downstream systems
- Track rejected/ignored responses for debug visibility
- Maintain explicit state transitions that are frame-readable and testable
- Support simple tuning (duration, intensity labels, cooldown if needed)

**Non-Goals:**
- No shader implementation, Shader Graph asset, or custom HLSL
- No post-processing renderer features or particle/VFX Graph assets
- No camera control or animator manipulation
- No audio playback or cutscene sequencing
- No damage, stagger, or reveal validity inference
- No scene/prefab wiring (contracts only, composition happens upstream)
- No narrative progression or full district interpretation
- No complex VFX pipeline or per-enemy reveal sets

## Decisions

### 1. Pure C# State Model with Manual Composition (not DI-generated)
**Decision**: Implement M0MemoryVFXResponse as a pure C# state model (no Nhem DI generation). Composition happens in scene-scoped gameplay scope, not project-root.

**Rationale**: The architecture restricts M0Contracts to contracts-only. VContainer scopes remain manual. Nhem-generated DI is explicitly forbidden. Memory VFX Response is a gameplay-layer system that should be composed with Memory State at the scene/duel level, not at project root.

**Alternative**: Generate via DI at project root (rejected: violates architecture rule for manual scopes and contracts-only M0Contracts).

### 2. State Machine: Five Explicit States, Not Hierarchical
**Decision**: Implement five distinct states (Idle, Requested, Playing, CoolingDown, RejectedOrIgnored) as separate enum values, not a hierarchical state machine.

**Rationale**: M0 scope is small and linear. An explicit enum is more frame-readable, easier to test, and requires less boilerplate than a full state-pattern hierarchy. State transitions are deterministic and can be tested with simple assertions.

**Alternative**: Hierarchical state machine with base states and substates (rejected: overkill for M0 linear flow, harder to debug, requires more composition).

### 3. Observer Pattern: Read-Only Snapshot API
**Decision**: Expose a read-only snapshot interface (IMemoryVFXResponseSnapshot) that Debug Overlay and other systems consume, not direct state mutation.

**Rationale**: Prevents accidental state mutation from presentation systems. Clear separation between authoritative state (owned by M0MemoryVFXResponse) and observable state (consumed via snapshot). Aligns with architecture rule that presentation is read-only.

**Alternative**: Expose mutable state directly (rejected: violates boundary rule, allows hidden state changes).

### 4. Owned by Memory State, Triggered by Memory State Acceptance
**Decision**: Memory VFX Response does not subscribe to Memory State events. Instead, Memory State calls a OnAcceptedReveal() method after acceptance is confirmed.

**Rationale**: Explicit method calls are clearer than event subscription and prevent races or missed state updates. Keeps causality explicit: Memory State decides, then Memory VFX Response responds. No hidden cross-system dependencies.

**Alternative**: Subscribe to Memory State events (rejected: harder to test, less explicit about ownership).

### 5. Cooldown as Optional Tuned Behavior, Not Required
**Decision**: Cooldown state is supported but optional. M0 may use it for gating rapid-fire replays, but the core state machine works without it.

**Rationale**: Keeps implementation simple. Tuning can decide whether to use cooldown later. State tracking is still complete if cooldown duration is zero.

**Alternative**: Require cooldown always (rejected: unnecessary complexity if M0 doesn't need it).

### 6. No Damage / Stagger Inference
**Decision**: VFX Response does not read Health, does not call stagger methods, does not modify any combat state. It is pure presentation state only.

**Rationale**: Health / Damage / Hit Reaction owns those systems. VFX Response must not imply damage. Keeps ownership boundary clear.

**Alternative**: Allow VFX to trigger stagger feedback (rejected: violates architecture, hides combat authority).

### 7. Snapshot Contains: Current State, Source Context, Intensity, Cooldown Remaining
**Decision**: IMemoryVFXResponseSnapshot exposes only: current state enum, source memory context (if available), intensity label, whether playback was skipped/rejected/ignored, and cooldown progress if used.

**Rationale**: Minimal set of data needed for Debug Overlay to explain why an effect did or did not play. Avoids exposing internal timing details.

**Alternative**: Expose internal frame counters and frame-based timing (rejected: unnecessary, harder to reason about).

## Risks / Trade-offs

**[Risk] VFX plays without accepted Memory State context.**
- Mitigation: API does not expose OnAcceptedReveal() to arbitrary callers. Composition root is responsible for only calling it after Memory State has confirmed acceptance. Test verifies that Idle state alone does not produce playback.

**[Risk] Cooldown allows accepted reveals to be silently dropped.**
- Mitigation: Rejected/Ignored state is explicitly logged to snapshot. Debug Overlay shows whether a request was skipped due to cooldown, acceptance gate, or other reason.

**[Risk] Snapshot stale by the time it's read.**
- Mitigation: Snapshot is immutable copy, not a live reference. Consumers get a consistent view of state at snapshot time. Debug can update snapshot every frame if needed.

**[Risk] State transitions not frame-atomic (multiple transitions in one frame).**
- Mitigation: Transitions are gated through explicit method calls (OnAcceptedReveal, OnPlaybackComplete, OnEnterCooldown). Frame atomicity is ensured by composition root timing these calls correctly.

**Trade-off: Pure C# model means no Animator/VFX Graph integration yet.**
- Acceptance: M0 does not require shader or VFX Graph implementation. State model is ready for wiring later. Composition root or a separate adapter can translate state to VFX Graph properties in future phases.

**Trade-off: Manual composition instead of DI-generated.**
- Acceptance: Architecture explicitly forbids Nhem DI generation and requires manual VContainer scopes. This is the agreed constraint.
