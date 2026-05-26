## ADDED Requirements

### Requirement: Duel lifecycle SHALL support deterministic reset to playable baseline
The system SHALL support an M0 duel lifecycle that includes start, active duel, reset request, and reset complete states for one-player/one-enemy replay in the same scene.

#### Scenario: Reset requested during active duel
- **WHEN** the duel is active and a reset trigger is issued
- **THEN** the encounter lifecycle enters reset flow and completes with a clean playable baseline

### Requirement: Combat Core SHALL return to Neutral on encounter reset
On encounter reset, Combat Core SHALL clear transient combat state and return to `Neutral` without requiring scene reload.

#### Scenario: Combat state is non-neutral before reset
- **WHEN** reset is executed while Combat Core is in any non-neutral state
- **THEN** Combat Core ends reset in `Neutral` and no stale combat action remains pending

### Requirement: Player Locomotion SHALL restore known start transform/state on reset
On encounter reset, Player Locomotion SHALL reset movement/transient locomotion state and restore the player to a known start transform for replay.

#### Scenario: Player moved before reset
- **WHEN** reset executes after player translation/displacement occurred
- **THEN** player transform and locomotion runtime state are restored to configured baseline values

### Requirement: Enemy Intent SHALL return to initial duel state on reset
On encounter reset, Enemy Intent model/loop SHALL return to its initial known start state so telegraph/commit/active/recovery cycle can replay deterministically.

#### Scenario: Enemy intent is mid-cycle before reset
- **WHEN** reset executes while enemy intent is not in initial state
- **THEN** enemy intent returns to initial duel-ready state

### Requirement: Target Context SHALL release active LockOn target on reset
On encounter reset, Target Context SHALL release/reset active target truth to `None` unless explicitly configured to reacquire an initial target.

#### Scenario: Target is locked before reset
- **WHEN** reset executes while a target is active
- **THEN** target context reports `None` (or configured initial target) after reset completion

### Requirement: Debug overlay SHALL reflect post-reset state as read-only evidence
Debug overlay SHALL display post-reset snapshots for combat state, target state, and relevant encounter fields, and SHALL NOT own reset truth or trigger logic.

#### Scenario: Reset completes
- **WHEN** reset flow completes
- **THEN** debug overlay fields update to show post-reset state values and remain read-only

### Requirement: Reset evidence SHALL include before/after proof and console health
Verification artifacts SHALL capture before/after reset observations for player transform and key state fields, and SHALL report whether new gameplay console errors occurred.

#### Scenario: Evidence capture run
- **WHEN** a reset verification run is performed
- **THEN** evidence includes before/after reset observations and explicit console error status
