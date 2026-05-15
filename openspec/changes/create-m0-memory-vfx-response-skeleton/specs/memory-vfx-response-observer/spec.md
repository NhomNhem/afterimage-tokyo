## ADDED Requirements

### Requirement: Read-Only Snapshot Interface
The Memory VFX Response observer API SHALL expose a read-only snapshot interface (IMemoryVFXResponseSnapshot) that Debug Overlay and other presentation systems can consume without mutation risk. The snapshot interface SHALL NOT allow state changes; it SHALL only provide inspection of current state. Snapshots SHALL be immutable copies, not live references, so modifications do not affect the underlying state.

#### Scenario: Snapshot provides current state enum
- **WHEN** IMemoryVFXResponseSnapshot.State is accessed
- **THEN** returns the current MemoryVFXResponseState enum value (Idle, Requested, Playing, CoolingDown, Rejected, Ignored)

#### Scenario: Snapshot is immutable
- **WHEN** snapshot is obtained via GetSnapshot()
- **THEN** the snapshot object cannot be modified; attempting to set properties raises an error or is impossible

#### Scenario: Snapshot can be stored without affecting VFX Response state
- **WHEN** GetSnapshot() is called, stored, then state changes via OnAcceptedReveal, then stored snapshot is queried
- **THEN** stored snapshot reflects previous state; current snapshot reflects new state

#### Scenario: Multiple snapshots can be taken sequentially
- **WHEN** GetSnapshot() is called multiple times
- **THEN** each snapshot reflects the state at the time of the call; earlier snapshots are independent of later state changes

### Requirement: Snapshot Exposes Source Memory Context
When Memory VFX Response is in Requested or Playing state (i.e., processing an accepted reveal), the snapshot SHALL expose the source accepted memory context. When not in those states, the context SHALL be null or explicitly unavailable. This allows Debug Overlay to trace which memory state triggered the VFX response.

#### Scenario: Snapshot includes context after OnAcceptedReveal
- **WHEN** OnAcceptedReveal(acceptedContext) is called and GetSnapshot() is called
- **THEN** snapshot.SourceAcceptedContext returns the same acceptedContext reference

#### Scenario: Snapshot context is null in Idle state
- **WHEN** state is Idle
- **THEN** snapshot.SourceAcceptedContext is null

#### Scenario: Snapshot context is cleared after Reset
- **WHEN** OnReset() is called after OnAcceptedReveal
- **THEN** snapshot.SourceAcceptedContext is null

#### Scenario: Snapshot context clears after playback completes
- **WHEN** state transitions from Requested to Playing to CoolingDown
- **THEN** snapshot.SourceAcceptedContext is available only while state is Requested or Playing

### Requirement: Snapshot Exposes Rejection or Ignore Reason
When Memory VFX Response is in Rejected or Ignored state, the snapshot SHALL expose the rejection reason (e.g., "generic_hit", "failed_dodge", "already_playing", "in_cooldown"). This allows Debug Overlay to explain why an expected VFX response did not occur.

#### Scenario: Snapshot includes rejection reason in Rejected or Ignored state
- **WHEN** OnRejectRequest("failed_dodge") is called and GetSnapshot() is called
- **THEN** snapshot.RejectionReason returns "failed_dodge"

#### Scenario: Snapshot rejection reason is null when not rejected
- **WHEN** state is Idle
- **THEN** snapshot.RejectionReason is null

#### Scenario: Snapshot reason persists until state changes
- **WHEN** in Rejected or Ignored state
- **THEN** querying snapshot.RejectionReason multiple times returns the same reason

#### Scenario: Reset clears rejection reason from snapshot
- **WHEN** OnReset() is called while in Rejected or Ignored state and GetSnapshot() is called
- **THEN** snapshot.RejectionReason is null and state is Idle

### Requirement: Snapshot Exposes Cooldown Progress
When Memory VFX Response is in CoolingDown state, the snapshot SHALL expose the remaining cooldown time as a normalized value (0.0-1.0), where 0.0 = just entered cooldown, 1.0 = cooldown complete. This allows Debug Overlay to visualize cooldown progress and understand gating behavior.

#### Scenario: Snapshot provides cooldown progress
- **WHEN** in CoolingDown state and GetSnapshot() is called
- **THEN** snapshot.CooldownProgress returns a value between 0.0 and 1.0

#### Scenario: Cooldown progress increases monotonically toward 1.0
- **WHEN** GetSnapshot() is called multiple times while in CoolingDown state
- **THEN** each subsequent call returns equal or higher progress value, approaching 1.0

#### Scenario: Cooldown progress is 0.0 when not in CoolingDown
- **WHEN** state is Idle
- **THEN** snapshot.CooldownProgress is 0.0

#### Scenario: Cooldown progress reaches 1.0 just before state transition to Idle
- **WHEN** in CoolingDown state and GetSnapshot() is called with elapsed time = cooldown duration
- **THEN** snapshot.CooldownProgress is 1.0 or very close to 1.0

### Requirement: Snapshot Exposes Intensity Label (Optional)
If Memory VFX Response is configured with an intensity label (e.g., "subtle", "standard", "intense"), the snapshot SHALL expose this label for debug visibility. If no intensity is configured, the label SHALL default to a neutral value (e.g., "standard").

#### Scenario: Snapshot includes configured intensity label
- **WHEN** Memory VFX Response is constructed with intensityLabel = "subtle" and GetSnapshot() is called
- **THEN** snapshot.IntensityLabel returns "subtle"

#### Scenario: Snapshot intensity label defaults to standard when not configured
- **WHEN** Memory VFX Response is constructed without intensity parameter and GetSnapshot() is called
- **THEN** snapshot.IntensityLabel returns a default value (e.g., "standard")

#### Scenario: Intensity label is consistent across snapshot calls
- **WHEN** GetSnapshot() is called multiple times
- **THEN** snapshot.IntensityLabel returns the same value each time

### Requirement: Observer-Friendly Access for Debug Overlay
The snapshot API SHALL be designed to allow Debug Overlay to safely read and display VFX state without importing or depending on Memory VFX Response implementation details. The interface SHALL use common types (enums, strings, floats, null) to remain stable across refactorings.

#### Scenario: Debug Overlay can import IMemoryVFXResponseSnapshot without internal dependencies
- **WHEN** Debug Overlay code imports IMemoryVFXResponseSnapshot
- **THEN** no internal types or private classes are required; only public interface types are needed

#### Scenario: Snapshot fields use common types
- **WHEN** snapshot interface is inspected
- **THEN** all exposed properties are of stable types (MemoryVFXResponseState enum, string, float, null references)

#### Scenario: GetSnapshot is available without special cast or import
- **WHEN** Memory VFX Response is injected into Debug Overlay
- **THEN** Debug Overlay can call GetSnapshot() on the public interface

#### Scenario: Snapshot remains usable after VFX Response is updated
- **WHEN** Memory VFX Response is updated with new internal state
- **THEN** snapshot interface contract remains unchanged; Debug Overlay code does not need updates

### Requirement: Snapshot Does Not Expose Implementation Details
The snapshot interface SHALL NOT expose internal timing counters, frame numbers, internal state machine details, or any implementation-specific data. Only user-facing information (current state, context, reason, progress, label) SHALL be exposed.

#### Scenario: Snapshot does not expose internal frame counters
- **WHEN** GetSnapshot() is called
- **THEN** snapshot does not expose _currentFrame or _startFrame or similar internal fields

#### Scenario: Snapshot does not expose internal playback timer
- **WHEN** GetSnapshot() is called
- **THEN** snapshot exposes only normalized cooldown progress (0.0-1.0), not raw millisecond timestamps

#### Scenario: Snapshot does not expose internal callbacks or event delegates
- **WHEN** GetSnapshot() is called
- **THEN** returned snapshot contains no event subscriptions, delegates, or callback references

### Requirement: Snapshot Supports Safe Multi-System Observation
Multiple systems (Debug Overlay, Editor tooling, telemetry) can observe the same Memory VFX Response via snapshots simultaneously without contention or state corruption. Each system receives its own snapshot copy.

#### Scenario: Debug Overlay and editor tooling can both read snapshots
- **WHEN** Debug Overlay and editor tooling both call GetSnapshot() on the same Memory VFX Response
- **THEN** each receives its own independent snapshot; no conflicts occur

#### Scenario: Snapshot copies are independent even if taken from same VFX Response
- **WHEN** GetSnapshot() is called, snapshot A is stored, then state changes, then GetSnapshot() is called again to get snapshot B
- **THEN** snapshot A retains its original data; snapshot B reflects new state

### Requirement: Snapshot Readability For Player-Facing Information
The snapshot interface structure SHALL be designed to make common diagnostic queries intuitive and efficient. Debug Overlay should be able to determine "why didn't the effect play?" with a single GetSnapshot() call.

#### Scenario: Single snapshot call provides complete diagnostic picture
- **WHEN** GetSnapshot() is called once
- **THEN** the returned snapshot allows determination of: current state, whether rejected, rejection reason, cooldown progress, and source context if applicable

#### Scenario: Snapshot state is human-readable
- **WHEN** snapshot.State is displayed to a tester
- **THEN** the state name is clear and meaningful (not enum values like "3" or "State_4")

#### Scenario: Rejection reasons are human-readable
- **WHEN** snapshot.RejectionReason is displayed
- **THEN** the reason is a clear string like "failed_dodge", not an opaque code

#### Scenario: Cooldown progress is normalized for intuitive display
- **WHEN** snapshot.CooldownProgress is used in a progress bar UI
- **THEN** a value of 0.5 clearly represents 50% complete; no formula or conversion is needed
