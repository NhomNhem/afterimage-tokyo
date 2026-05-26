## ADDED Requirements

### Requirement: Target Context SHALL release active target during encounter reset
The Target Context system SHALL clear active target truth when encounter reset completes so post-reset duel state is deterministic.

#### Scenario: Encounter reset clears active target
- **GIVEN** `M0TargetContext` has an active target before reset
- **WHEN** encounter reset is executed
- **THEN** `CurrentTarget` is cleared
- **AND** `Active` becomes `false`
- **AND** reset-driven release reason is available for debug/read-only snapshot
