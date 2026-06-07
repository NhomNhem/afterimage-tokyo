# memory-raycast-probe-alignment Specification

## Purpose
TBD - created by archiving change align-memory-raycast-probe-with-interaction-service. Update Purpose after archive.
## Requirements
### Requirement: Probe Reports Service-Owned Eligibility
`MemoryRaycastProProbe` SHALL report memory interaction eligibility using `MemoryInteractionService` read-only state as the authoritative debug comparison.

#### Scenario: Eligible fragment debug matches service snapshot
- **WHEN** `MemoryInteractionService` reports an eligible nearby fragment
- **THEN** probe debug output identifies the same service-owned eligible fragment context or explicitly labels any collider-only mismatch as supplemental

#### Scenario: No eligible fragment debug matches service snapshot
- **WHEN** `MemoryInteractionService` reports no eligible fragment
- **THEN** probe debug output reports no service-owned eligible fragment

### Requirement: Probe Remains Debug-Only
`MemoryRaycastProProbe` MUST remain debug/evidence tooling and MUST NOT own interaction truth, execute Interact, mutate memory state, or decide reveal acceptance.

#### Scenario: Probe does not execute interaction
- **WHEN** the player presses Interact
- **THEN** interaction execution still routes through the existing input intent to `MemoryInteractionService` path, not through the probe

#### Scenario: Probe does not mutate memory truth
- **WHEN** probe debug output is produced
- **THEN** it does not call `MemoryState` mutation APIs, `MemoryInteractionService` command paths, fragment mutation paths, or runtime log append commands

### Requirement: Probe Output Distinguishes Truth From Supplemental Collider Data
Probe debug output SHALL distinguish service-owned eligibility from optional RaycastPro collider information.

#### Scenario: Collider hit differs from service eligibility
- **WHEN** RaycastPro collider data differs from `MemoryInteractionService` eligibility
- **THEN** debug output identifies the mismatch without treating collider data as gameplay truth

#### Scenario: Collider data unavailable
- **WHEN** RaycastPro detector or collider data is unavailable
- **THEN** service-owned eligibility output remains available if the service snapshot is available

### Requirement: Existing Memory Interaction Behavior Is Preserved
Aligning probe debug output SHALL preserve existing S3/S4 memory behavior.

#### Scenario: Accepted interaction path remains unchanged
- **WHEN** the player interacts with an eligible fragment
- **THEN** the accepted path remains `Interact -> MemoryInteractionService -> MemoryState`

#### Scenario: Duplicate spam behavior remains unchanged
- **WHEN** the player repeats Interact on an already accepted fragment
- **THEN** duplicate/spam handling remains equivalent to baseline

#### Scenario: Presentation remains downstream
- **WHEN** prompt, reveal feedback, or runtime memory log responds to memory interaction state
- **THEN** those systems remain downstream of service/memory truth and do not depend on probe authority

### Requirement: Probe Alignment Avoids Forbidden APIs
The implementation SHALL avoid broad Unity lookup, resource fallback, service locator lookup, and direct Unity debug logging in owned memory probe code.

#### Scenario: No broad lookup introduced
- **WHEN** source guardrails scan owned probe alignment code
- **THEN** no `FindObject*`, broad `FindObjectsByType`, `Resources.Load`, or Service Locator pattern is introduced

#### Scenario: No direct Unity debug logging introduced
- **WHEN** source guardrails scan owned probe alignment code
- **THEN** no direct `UnityEngine.Debug.Log`, `Debug.LogWarning`, `Debug.LogError`, `Debug.Log`, `Debug.LogWarning`, or `Debug.LogError` call is introduced

### Requirement: Probe Alignment Evidence Is Captured
Closure evidence SHALL compare service eligibility and probe output for the memory interaction smoke path.

#### Scenario: Evidence records eligible and no-eligible cases
- **WHEN** S4-7 verification is recorded
- **THEN** evidence includes eligible fragment and no-eligible fragment classifications comparing service-owned eligibility against probe output

#### Scenario: Evidence records accepted and duplicate cases
- **WHEN** S4-7 verification is recorded
- **THEN** evidence includes accepted Interact and duplicate/spam Interact classifications showing behavior parity
