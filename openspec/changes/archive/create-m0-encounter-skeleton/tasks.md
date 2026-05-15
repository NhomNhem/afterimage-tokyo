## 1. Contracts and Lifecycle Shapes

- [x] 1.1 Add encounter lifecycle enum and state identifiers to M0Contracts.cs
- [x] 1.2 Add one-player / one-enemy participant registration contract shape
- [x] 1.3 Add readiness blocker contract shape
- [x] 1.4 Add start/end/fail/abort/reset request and result shapes
- [x] 1.5 Add read-only encounter snapshot contract shape

## 2. Encounter Lifecycle Model

- [x] 2.1 Create the M0 encounter lifecycle model as a pure C# state machine
- [x] 2.2 Implement prepare and ready transitions
- [x] 2.3 Implement start and active transitions
- [x] 2.4 Implement complete, fail, abort, and reset transitions
- [x] 2.5 Track elapsed time and last observed lifecycle reason

## 3. Participant Registration and Readiness

- [x] 3.1 Implement explicit player registration
- [x] 3.2 Implement explicit enemy registration
- [x] 3.3 Implement readiness blocker collection for missing or invalid participant/config state
- [x] 3.4 Implement participant duplicate/missing validation

## 4. Observed Encounter Context

- [x] 4.1 Add read-only observation of player defeated state
- [x] 4.2 Add read-only observation of enemy defeated state
- [x] 4.3 Add read-only observation of accepted reveal context
- [x] 4.4 Add read-only observation of manual abort and reset requests

## 5. Snapshot and Debug Readability

- [x] 5.1 Implement immutable encounter snapshot generation
- [x] 5.2 Expose lifecycle state, elapsed time, participants, blockers, and observed reasons in snapshot
- [x] 5.3 Ensure snapshot is read-only from consumer perspective

## 6. Tests

- [x] 6.1 Test prepare to ready behavior
- [x] 6.2 Test ready to start to active behavior
- [x] 6.3 Test complete, fail, abort, and reset transitions
- [x] 6.4 Test readiness blockers for missing/invalid participants
- [x] 6.5 Test snapshot readability and immutability
- [x] 6.6 Test observed reveal/defeat context stays read-only
- [x] 6.7 Test elapsed time tracking and reset behavior

