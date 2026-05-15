## ADDED Requirements

### Requirement: Health / Damage / Hit Reaction SHALL own consequence truth

The system MUST treat Health / Damage / Hit Reaction as the authoritative owner of health values, damage application, hit reaction classification, and defeat/disabled consequence for M0. Combat Core, Player Locomotion, Enemy Intent & Telegraph, Memory State, and Debug Overlay MUST NOT own or override this consequence truth.

#### Scenario: Consequence truth stays in Health
- **WHEN** a confirmed combat outcome requires consequence processing
- **THEN** health change, reaction classification, and defeat/disabled consequence MUST be owned by Health / Damage / Hit Reaction

#### Scenario: Other systems remain non-authoritative
- **WHEN** Combat Core, Locomotion, Enemy Intent, Memory, or Debug consume consequence data
- **THEN** they MUST treat health/reaction truth as read-only authority

### Requirement: Health skeleton SHALL define a pure C# state model

The system MUST define a pure C# health state model sufficient for M0 consequence phases (living, damaged, recovering, defeated or disabled).

#### Scenario: Health state is inspectable
- **WHEN** accepted damage or consequence transitions occur
- **THEN** the current health state MUST be inspectable via a read-only snapshot

#### Scenario: Health state is not owned by animation
- **WHEN** presentation systems play reaction visuals
- **THEN** animation systems MUST NOT own authoritative health/reaction state

### Requirement: Damage application SHALL use request/result contracts

The system MUST represent damage application through explicit request/result contracts.

#### Scenario: Confirmed consequence request is accepted
- **WHEN** a valid damage request derived from confirmed combat context is submitted
- **THEN** health system MUST return an accepted damage result and update health snapshot accordingly

#### Scenario: Invalid or out-of-scope request is rejected/ignored
- **WHEN** a damage request is invalid for the current health state
- **THEN** health system MUST return a rejected or ignored result with readable reason

### Requirement: Combat Core SHALL provide confirmed context only

Combat Core MUST provide confirmed combat result/context only and MUST NOT apply damage directly.

#### Scenario: Combat Core remains non-applicative for damage
- **WHEN** combat result is confirmed
- **THEN** Combat Core MUST hand off context and Health system MUST own damage application

#### Scenario: Combat Core ownership remains combat-only
- **WHEN** consequence processing is performed
- **THEN** Combat Core MUST continue owning combat validation/result and `CounterWindow` only

### Requirement: Hit reaction context SHALL be represented as placeholder

The system MUST represent hit reaction classification context as placeholder consequence data.

#### Scenario: Hit reaction context emitted after accepted damage
- **WHEN** accepted damage is applied
- **THEN** snapshot/context MUST expose a hit reaction placeholder classification

#### Scenario: Hit reaction context does not own movement expression
- **WHEN** hit reaction placeholder is emitted
- **THEN** Player Locomotion MUST remain owner of movement-side recovery/hit reaction expression

### Requirement: Defeat/disabled consequence SHALL be represented as placeholder

The system MUST represent defeated/disabled consequence context when health threshold conditions are met.

#### Scenario: Defeated state is observable
- **WHEN** health reaches defeated threshold
- **THEN** health system MUST expose defeated or disabled context in read-only consequence snapshot

#### Scenario: Defeat context does not imply full fail loop
- **WHEN** defeated/disabled context is emitted
- **THEN** no full respawn/checkpoint/failure-loop behavior is required in this skeleton

### Requirement: Health/reaction snapshot SHALL be read-only

The system MUST expose a read-only health/reaction snapshot for Debug Overlay and downstream observers.

#### Scenario: Snapshot reflects current consequence truth
- **WHEN** health value, damage result, hit reaction context, or defeated context changes
- **THEN** latest snapshot MUST reflect current consequence truth

#### Scenario: Consumers cannot mutate consequence authority
- **WHEN** consumers read health/reaction snapshot data
- **THEN** they MUST NOT be able to mutate authoritative health/reaction truth through that snapshot

### Requirement: Ownership boundaries with adjacent systems SHALL remain explicit

The system MUST preserve adjacent ownership boundaries when adding the health skeleton.

#### Scenario: Locomotion ownership remains movement-side only
- **WHEN** recovery/hit reaction movement expression is required
- **THEN** Player Locomotion MUST remain movement-truth owner while consuming health consequence context

#### Scenario: Enemy Intent ownership remains enemy rhythm only
- **WHEN** enemy-side telegraph/commit/recovery rhythm changes
- **THEN** Enemy Intent MUST remain owner of enemy-side rhythm and tags, not health truth

#### Scenario: Memory ownership remains reveal acceptance/rejection
- **WHEN** consequence context could feed reveal flow
- **THEN** Memory State MUST remain owner of reveal acceptance/rejection

#### Scenario: Debug Overlay remains observer-only
- **WHEN** debug overlay displays health/reaction state
- **THEN** it MUST remain read-only and non-authoritative

### Requirement: Skeleton SHALL exclude non-goal dependencies

The system MUST keep this change as a skeleton and exclude deferred implementation dependencies.

#### Scenario: No full collision/animation/physics/stats/UI/AI/scene dependencies
- **WHEN** health skeleton is implemented
- **THEN** it MUST NOT include actual hitbox collision, animation hit reactions, ragdoll/physics knockback, RPG stats/armor/resistance, damage numbers UI, enemy AI changes, Combat Core hit validation logic, Memory reveal acceptance logic, or scene/prefab wiring

#### Scenario: No forbidden framework regressions
- **WHEN** files are added/updated for this change
- **THEN** there MUST be no legacy Input Manager references, no Nhem generated DI usage, and VContainer scopes MUST remain manual

#### Scenario: Contracts remain data-only
- **WHEN** `M0Contracts.cs` is updated for health/damage/reaction types
- **THEN** it MUST contain contract shape only and MUST NOT include behavior logic
