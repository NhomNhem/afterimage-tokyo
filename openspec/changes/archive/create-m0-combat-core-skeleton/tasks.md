## 1. Foundation Review

- [x] 1.1 Inspect the existing M0 contracts (M0Contracts.cs) and architecture boundaries for combat truth ownership
- [x] 1.2 Confirm the architecture and GDD constraints for combat validation, action lock/recovery, CounterWindow, reveal request context, and read-only combat snapshots
- [x] 1.3 Check whether M0Contracts.cs needs new combat-specific contract types or existing contracts can be extended

## 2. Core Contract Setup

- [x] 2.1 Define or refine CombatActionType enum (LightAttack, HeavyAttack, Dodge, Parry, Counter)
- [x] 2.2 Define CombatActionRequest struct (action type, timestamp, source context)
- [x] 2.3 Define CombatActionResult enum (Accepted, Rejected, Ignored) with rejection/ignore reason
- [x] 2.4 Define CombatResolutionResult (action type, success/failure, hit confirmation flag, counter window trigger flag)
- [x] 2.5 Define ActionLockContext (lock active, lock source, requesting state)
- [x] 2.6 Define RecoveryContext (recovery active, recovery source label, requesting state)
- [x] 2.7 Define CounterWindowState (open/closed, source tag, elapsed/duration)
- [x] 2.8 Define RevealRequestContext (request source type, combat result source label)
- [x] 2.9 Define M0CombatSnapshot (current state, last action result, last resolution result, CounterWindow state, active lock/recovery context)

## 3. Combat Skeleton

- [x] 3.1 Implement a lightweight pure C# Combat Core FSM/service skeleton with all M0 states
- [x] 3.2 Implement Neutral state as default idle baseline
- [x] 3.3 Implement AttackStartup / AttackActive / AttackRecovery state path
- [x] 3.4 Implement DodgeStartup / DodgeActive / DodgeRecovery state path
- [x] 3.5 Implement ParryStartup / ParryActive / ParryRecovery state path
- [x] 3.6 Implement CounterWindow placeholder state (open/closed, source, duration)
- [x] 3.7 Implement CounterActive state
- [x] 3.8 Implement HitReact state
- [x] 3.9 Implement RevealBeat state or event placeholder
- [x] 3.10 Implement Disabled state
- [x] 3.11 Wire action request intake and result emission (validation shape only — basic state-gating, not full timing/window validation)
- [x] 3.12 Wire ActionLockContext and RecoveryContext emission on entering committed/recovery states
- [x] 3.13 Wire CounterWindowState emission (placeholder — CounterWindow open/closed based on parry success or dodge-success placeholder triggers)
- [x] 3.14 Wire RevealRequestContext emission placeholder (emitted on CounterActive → RevealBeat transition)
- [x] 3.15 Implement read-only M0CombatSnapshot exposure for downstream consumers

## 4. Verification

- [x] 4.1 Add edit-mode tests for request intake: LightAttack, HeavyAttack, Dodge, Parry, Counter produce Accepted in Neutral
- [x] 4.2 Add edit-mode tests for request rejection: action requests rejected during committed states
- [x] 4.3 Add edit-mode tests for state transitions through a full attack cycle
- [x] 4.4 Add edit-mode tests for state transitions through a full dodge cycle
- [x] 4.5 Add edit-mode tests for state transitions through a full parry cycle
- [x] 4.6 Add edit-mode tests for CounterWindow open/close via placeholder trigger
- [x] 4.7 Add edit-mode tests for RevealRequestContext emission after counter path
- [x] 4.8 Add edit-mode tests for read-only snapshot consistency with internal state
- [x] 4.9 Add edit-mode tests for action lock/recovery context emission during committed states
- [x] 4.10 Run no-legacy-input and no-generated-DI checks
- [x] 4.11 Update the task checklist only after each task is complete and verified
