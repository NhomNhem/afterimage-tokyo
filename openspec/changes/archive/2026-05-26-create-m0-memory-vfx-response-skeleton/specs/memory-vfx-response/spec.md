## ADDED Requirements

### Requirement: Memory VFX Response State Machine
The Memory VFX Response system SHALL maintain an explicit, frame-readable state machine with six distinct states: Idle, Requested, Playing, CoolingDown, Rejected, and Ignored. State transitions SHALL occur only through explicit method calls from Memory State acceptance, playback completion, rejection, ignore handling, or cooldown expiration. The state machine SHALL be implemented as a pure C# model with no dependencies on Animator, VFX Graph, renderer features, or scene components.

#### Scenario: Initial state is Idle
- **WHEN** Memory VFX Response is constructed
- **THEN** current state is Idle

#### Scenario: Transition from Idle to Requested on accepted reveal
- **WHEN** OnAcceptedReveal(acceptedContext) is called while in Idle state
- **THEN** state transitions to Requested and stores the source accepted context

#### Scenario: Transition from Requested to Playing on playback start
- **WHEN** OnPlaybackStarted() is called while in Requested state
- **THEN** state transitions to Playing and captures current frame time

#### Scenario: Transition from Playing to CoolingDown on playback complete
- **WHEN** OnPlaybackComplete() is called while in Playing state AND cooldown duration > 0
- **THEN** state transitions to CoolingDown and initializes cooldown timer

#### Scenario: Transition from Playing to Idle if no cooldown
- **WHEN** OnPlaybackComplete() is called while in Playing state AND cooldown duration == 0
- **THEN** state transitions directly to Idle

#### Scenario: Transition from CoolingDown to Idle when cooldown expires
- **WHEN** Update() is called with elapsed time >= cooldown duration
- **THEN** state transitions to Idle and cooldown timer is reset

#### Scenario: Transition to Rejected from Requested when context is invalid
- **WHEN** OnRejectRequest(reason) is called while in Requested state
- **THEN** state transitions to Rejected and stores rejection reason

#### Scenario: Cannot transition from Rejected or Ignored except by Reset
- **WHEN** in Rejected or Ignored state
- **THEN** no state transition occurs until OnReset() is called

### Requirement: Accepted Reveal Context Ownership
Memory VFX Response SHALL only enter Requested or Playing states after receiving an OnAcceptedReveal call from Memory State. Rejected, ignored, or generic combat events SHALL NOT trigger VFX response playback. The system SHALL not infer reveal validity; it SHALL only react to explicit acceptance from upstream Memory State.

#### Scenario: Generic hit does not trigger VFX response
- **WHEN** OnRejectRequest("generic_hit") is called
- **THEN** state transitions to RejectedOrIgnored and playback does not occur

#### Scenario: Failed dodge does not trigger VFX response
- **WHEN** OnRejectRequest("failed_dodge") is called
- **THEN** state transitions to RejectedOrIgnored and playback does not occur

#### Scenario: Failed parry does not trigger VFX response
- **WHEN** OnRejectRequest("failed_parry") is called
- **THEN** state transitions to RejectedOrIgnored and playback does not occur

#### Scenario: Presentation-only event does not trigger VFX response
- **WHEN** OnRejectRequest("presentation_only") is called
- **THEN** state transitions to RejectedOrIgnored and playback does not occur

#### Scenario: Only accepted Memory State context can trigger playing state
- **WHEN** OnAcceptedReveal(acceptedContext) is called from Memory State
- **THEN** state can transition to Requested, then Playing when playback begins

### Requirement: Cooldown Behavior (Optional, Tunable)
If cooldown duration is configured > 0, Memory VFX Response SHALL prevent immediate replay of accepted reveals by gating the transition from CoolingDown back to Idle. Cooldown duration SHALL be externally tunable. If cooldown duration is 0, the system SHALL allow consecutive reveals without delay.

#### Scenario: Rapid successive reveals are gated by cooldown
- **WHEN** OnAcceptedReveal is called while in CoolingDown state
- **THEN** state remains CoolingDown; the new request is silently ignored and recorded in debug state

#### Scenario: Cooldown expiration allows next reveal
- **WHEN** Update() is called with elapsed time >= cooldown duration
- **THEN** state transitions to Idle and next OnAcceptedReveal can proceed

#### Scenario: Zero cooldown allows immediate replay
- **WHEN** cooldown duration is configured as 0 AND OnPlaybackComplete() is called
- **THEN** state transitions directly to Idle without blocking period

### Requirement: Snapshot for Observer Access
Memory VFX Response SHALL expose a read-only snapshot interface (IMemoryVFXResponseSnapshot) that returns immutable copies of relevant state. The snapshot SHALL include: current state enum, source memory context (if available), intensity label (if configured), whether the current state is a rejection/ignore with reason, and cooldown progress if applicable. Snapshots SHALL NOT expose mutable state or allow external modifications.

#### Scenario: Snapshot reflects current state
- **WHEN** GetSnapshot() is called
- **THEN** returned snapshot contains current state enum value

#### Scenario: Snapshot includes source context when available
- **WHEN** GetSnapshot() is called after OnAcceptedReveal(context)
- **THEN** snapshot contains reference to the accepted memory context

#### Scenario: Snapshot includes rejection reason when appropriate
- **WHEN** GetSnapshot() is called after OnRejectRequest("failed_dodge")
- **THEN** snapshot contains rejection reason "failed_dodge"

#### Scenario: Snapshot includes cooldown progress
- **WHEN** GetSnapshot() is called while in CoolingDown state
- **THEN** snapshot contains cooldown remaining time as 0.0-1.0 normalized value

#### Scenario: Multiple snapshots are independent
- **WHEN** GetSnapshot() is called, then state changes, then GetSnapshot() is called again
- **THEN** first snapshot retains previous state; second snapshot reflects new state

### Requirement: Debug Visibility for Rejected and Ignored States
Memory VFX Response SHALL track rejected and ignored requests for debug visibility. The Debug Overlay SHALL be able to query why a reveal request was not acted upon (accepted but already cooling down, rejected due to invalid context, or ignored due to current state gates). This traceability SHALL help diagnose whether missing VFX response is due to upstream acceptance failure, local VFX gating, or intentional cooldown.

#### Scenario: Debug can identify why a reveal was not played
- **WHEN** state is Rejected or Ignored
- **THEN** snapshot includes the reason (e.g., "in_cooldown", "not_accepted_by_memory_state", "already_playing")

#### Scenario: Rejection reason is recorded for the entire Rejected or Ignored duration
- **WHEN** in Rejected or Ignored state
- **THEN** querying rejection reason returns the same reason until state changes

#### Scenario: Reset clears rejection state
- **WHEN** OnReset() is called while in Rejected or Ignored state
- **THEN** state transitions to Idle and rejection reason is cleared

### Requirement: Frame-Atomic State Transitions
All state transitions SHALL be deterministic and testable. State changes SHALL occur only through explicit method calls (OnAcceptedReveal, OnPlaybackStarted, OnPlaybackComplete, OnRejectRequest, OnReset) and Update() for time-based transitions. No implicit state changes due to event subscriptions or hidden dependencies.

#### Scenario: Multiple Update calls in one frame do not cause spurious transitions
- **WHEN** Update(deltaTime) is called multiple times with same deltaTime
- **THEN** cooldown progress is monotonic; no unexpected state changes occur

#### Scenario: OnPlaybackComplete from wrong state has no effect
- **WHEN** OnPlaybackComplete() is called while in Idle state
- **THEN** state remains Idle; call is a no-op

#### Scenario: OnAcceptedReveal from wrong state has no effect
- **WHEN** OnAcceptedReveal(context) is called while already in Playing state
- **THEN** state remains Playing; new reveal is rejected and recorded

### Requirement: Integration with Memory State Ownership
Memory VFX Response SHALL NOT subscribe to Memory State events or attempt to infer reveal validity. Memory State SHALL explicitly call OnAcceptedReveal() only after confirming acceptance. This enforces clear causality: Memory State decides → Memory VFX Response responds.

#### Scenario: VFX Response does not subscribe to Memory State
- **WHEN** Memory VFX Response is constructed
- **THEN** it has no event subscription to Memory State; it is stateless until Memory State calls OnAcceptedReveal

#### Scenario: Only one-way dependency: VFX Response depends on Memory State call, not vice versa
- **WHEN** Memory State is destroyed
- **THEN** Memory VFX Response remains functional and can accept new OnAcceptedReveal calls from a different Memory State

### Requirement: No Damage, Stagger, or Combat Authority
Memory VFX Response SHALL NOT read or modify Health state, SHALL NOT call stagger methods, SHALL NOT change Animator state, and SHALL NOT infer CounterWindow or combat success. It is pure presentation state only. Ownership boundaries are strict: Combat Core owns reveal request context, Memory State owns acceptance, Health/Damage/Hit Reaction owns damage and stagger, Memory VFX Response owns only the visual timeline after acceptance.

#### Scenario: VFX Response does not apply damage
- **WHEN** OnAcceptedReveal is called
- **THEN** no Health modify operation occurs; no damage is applied

#### Scenario: VFX Response does not trigger stagger
- **WHEN** OnPlaybackStarted is called
- **THEN** no stagger or hit reaction method is called

#### Scenario: VFX Response does not read Animator state
- **WHEN** GetSnapshot is called
- **THEN** returned data does not include Animator information; no Animator is queried

### Requirement: Configurable Intensity and Duration (Tunable)
Memory VFX Response implementation SHALL support external configuration of effect duration, cooldown duration, and an optional intensity label for composition-time tuning. These tunables SHALL be optional; default behavior with zero cooldown and standard duration SHALL work out of the box.

#### Scenario: Duration is configurable
- **WHEN** constructed with duration = 2.0f
- **THEN** effects playing respect the 2.0f duration when calculating timing

#### Scenario: Cooldown is configurable
- **WHEN** constructed with cooldownDuration = 0.5f
- **THEN** CoolingDown state lasts for 0.5f before transitioning to Idle

#### Scenario: Intensity label is optional
- **WHEN** constructed without intensity parameter
- **THEN** snapshot has default intensity label (e.g., "standard") and system functions normally

#### Scenario: Zero duration is valid (instant complete)
- **WHEN** constructed with duration = 0.0f AND OnPlaybackStarted is called
- **THEN** state can immediately complete if supported by composition

### Requirement: Reset Capability
Memory VFX Response SHALL provide an OnReset() method that clears all state, sets state to Idle, and clears all timing counters, rejection reasons, and source contexts. Reset SHALL be used for encounter restart or debug purposes.

#### Scenario: Reset from any state returns to Idle
- **WHEN** OnReset() is called from Playing state
- **THEN** state transitions to Idle; all timers are cleared; all context is cleared

#### Scenario: Reset clears rejection reason
- **WHEN** OnReset() is called while in RejectedOrIgnored state
- **THEN** state is Idle; rejection reason is no longer available in snapshot

#### Scenario: Reset clears source context
- **WHEN** OnReset() is called after OnAcceptedReveal
- **THEN** source context is cleared; snapshot has no accepted context reference
