# m0-lockon-camera-readability Specification

## Purpose
TBD - created by archiving change implement-m0-lockon-camera-readability. Update Purpose after archive.
## Requirements
### Requirement: Camera Readability Is Framing-Only

The M0 lock-on camera MUST improve duel readability while remaining presentation-only and MUST NOT become a gameplay truth owner.

#### Scenario: Camera consumes lock-on truth but does not author it

- **Given** lock-on is active with a valid target in `TargetContext`
- **When** camera framing updates
- **Then** camera uses target information for framing only
- **And** lock-on truth remains owned by `TargetContext`

#### Scenario: Camera does not drive combat outcomes

- **Given** attack/dodge/parry interactions occur during lock-on
- **When** camera readability tuning is applied
- **Then** combat timing/results still come from `CombatCore`
- **And** camera does not change combat acceptance/rejection logic

### Requirement: Duel Readability Under Lock-On

Lock-on framing SHALL keep both player and enemy readable across telegraph/commit/active/recovery and attack/dodge/parry beats.

#### Scenario: Enemy phase readability remains visible

- **Given** enemy loop transitions through `Telegraph -> Commit -> Active -> Recovery`
- **When** player remains in lock-on duel flow
- **Then** camera framing preserves enemy phase readability
- **And** phase truth still comes from `EnemyIntent`

#### Scenario: Player action readability remains visible

- **Given** player performs attack, dodge, and parry actions under lock-on
- **When** readability tuning is active
- **Then** action beats remain visually readable
- **And** movement/facing truth still comes from `PlayerLocomotion`

### Requirement: Evidence-First Closure

S2-4 implementation closure MUST include explicit PASS/PARTIAL/FAIL evidence and console classification.

#### Scenario: Evidence bundle is complete

- **Given** S2-4 tuning changes are implemented
- **When** verification is executed
- **Then** evidence includes focused verification results, manual checklist outcomes, and console/domain classification
- **And** unresolved limits are disclosed as notes instead of hidden

### Requirement: Ownership Boundaries Remain Unchanged

S2-4 camera readability tuning MUST preserve gameplay ownership boundaries and MUST NOT move gameplay truth into camera logic.

#### Scenario: TargetContext remains sole lock-on truth owner

- **Given** lock-on targeting is active in duel flow
- **When** camera readability tuning is applied
- **Then** `TargetContext` SHALL remain the sole owner of lock-on target truth
- **And** camera SHALL only consume target/camera-relevant snapshots or references for framing

#### Scenario: Combat and enemy lifecycle logic are not changed

- **Given** S2-4 implementation is scoped to camera readability
- **When** code and tuning changes are reviewed
- **Then** S2-4 SHALL NOT change combat timing or combat result logic in `CombatCore`
- **And** S2-4 SHALL NOT change `EnemyIntent` Telegraph/Commit/Active/Recovery lifecycle logic
- **And** Debug Overlay SHALL remain read-only and usable to verify camera-independent gameplay truth
