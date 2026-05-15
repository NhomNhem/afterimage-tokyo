## 1. Contracts and Channel Shapes

- [x] 1.1 Add debug overlay snapshot contract shapes to `M0Contracts.cs`
- [x] 1.2 Add required channel identifiers for all nine M0 debug channels
- [x] 1.3 Add read-only aggregate snapshot and per-channel snapshot shapes
- [x] 1.4 Add pass-through fields for last accepted/rejected reason data

## 2. Debug Snapshot Aggregation Model

- [x] 2.1 Create a pure C# debug snapshot aggregator
- [x] 2.2 Aggregate read-only snapshots from Input, Locomotion, Target Context, Combat Core, Enemy Intent, Health, Memory State, Memory VFX Response, and Encounter Framework
- [x] 2.3 Add simple channel visibility/toggle state
- [x] 2.4 Keep aggregation read-only and source-system neutral

## 3. Tests

- [x] 3.1 Test aggregate snapshot composition
- [x] 3.2 Test read-only snapshot pass-through
- [x] 3.3 Test channel toggle state behavior
- [x] 3.4 Test source snapshots are not mutated
