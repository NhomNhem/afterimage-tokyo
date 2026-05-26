## ADDED Requirements

### Requirement: Successful Counter SHALL Emit Reveal Request Context
The system SHALL emit a `RevealRequestContext` only when `M0CombatCore` resolves a successful counter result.

#### Scenario: Counter success emits reveal request
- **WHEN** counter input is accepted and CombatCore resolves counter success
- **THEN** a `RevealRequestContext` is produced on the combat truth path for memory handling

#### Scenario: Non-successful counter does not emit reveal request
- **WHEN** counter input is rejected or no valid counter opportunity exists
- **THEN** no `RevealRequestContext` is emitted

### Requirement: MemoryState SHALL Own Reveal Acceptance and Responding Transition
`MemoryState` SHALL evaluate reveal requests, accept valid requests, enter `Responding`, and return to neutral rhythm after response completion/cooldown.

#### Scenario: Accepted reveal enters responding
- **WHEN** `MemoryState` receives a valid `RevealRequestContext`
- **THEN** `MemoryState` transitions to `Responding`

#### Scenario: Invalid reveal is rejected
- **WHEN** `MemoryState` receives an invalid or disallowed reveal request
- **THEN** `MemoryState` remains in or returns to non-responding state and records rejection reason

#### Scenario: Responding returns to neutral rhythm
- **WHEN** responding duration/cooldown completes
- **THEN** `MemoryState` returns to baseline non-responding state suitable for continuing duel loop

### Requirement: Memory VFX SHALL Be Downstream Read-Only Presentation
`M0MemoryVFXResponse` SHALL trigger placeholder reveal VFX from accepted memory response signal/snapshot and SHALL NOT mutate gameplay truth.

#### Scenario: Accepted memory signal triggers placeholder VFX
- **WHEN** `MemoryState` enters `Responding` from accepted reveal
- **THEN** `M0MemoryVFXResponse` starts short restrained placeholder VFX playback

#### Scenario: No accepted memory signal means no reveal VFX trigger
- **WHEN** no accepted reveal response exists
- **THEN** `M0MemoryVFXResponse` does not trigger reveal placeholder playback

#### Scenario: Overlay remains read-only during reveal
- **WHEN** reveal response occurs
- **THEN** debug overlay only displays snapshot state and does not issue gameplay mutation

### Requirement: Reveal Evidence SHALL Prove Readability and Non-Obscuring VFX
Verification artifacts SHALL prove the counter->reveal sequence and classify whether reveal VFX remains readable and non-obscuring for enemy intent.

#### Scenario: Evidence captures counter to reveal sequence
- **WHEN** manual PlayMode verification is executed
- **THEN** evidence includes logs/observations for counter success, reveal acceptance, and responding transition

#### Scenario: Evidence classifies visual readability
- **WHEN** reveal VFX is observed in PlayMode
- **THEN** evidence classifies PASS/PARTIAL/FAIL for whether VFX is short, restrained, and does not obscure enemy intent
