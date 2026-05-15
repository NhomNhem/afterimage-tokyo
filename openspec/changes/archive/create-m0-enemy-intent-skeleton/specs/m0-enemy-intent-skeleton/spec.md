## ADDED Requirements

### Requirement: Enemy Intent & Telegraph SHALL own enemy telegraph and commitment truth

The system MUST treat Enemy Intent & Telegraph as the authoritative owner of enemy-side telegraph, commitment, active/recovery timing, attack tags, and `EnemyPunishWindow` context for M0. Combat Core, Health/Damage, Player Locomotion, Target Context, and Debug Overlay MUST NOT own or override enemy telegraph truth.

#### Scenario: Enemy telegraph truth stays in Enemy Intent
- **WHEN** enemy intent transitions from idle to telegraph/commit/active/recovery during the M0 duel
- **THEN** the authoritative enemy-side state MUST be owned by Enemy Intent & Telegraph

#### Scenario: Other systems remain non-authoritative
- **WHEN** Combat Core, Locomotion, Target, Health, or Debug consume enemy intent state
- **THEN** those systems MUST treat enemy intent truth as read-only authority

### Requirement: Enemy Intent SHALL define a pure C# state model

The system MUST define a pure C# enemy intent state model sufficient for M0 skeleton readability phases (idle, telegraph, commit, active, recovery).

#### Scenario: Enemy state is inspectable
- **WHEN** enemy intent transitions occur
- **THEN** the current enemy intent state MUST be inspectable via a read-only enemy snapshot

#### Scenario: Enemy state is not owned by Animator
- **WHEN** presentation systems animate enemy behavior
- **THEN** Animator or animation events MUST NOT own authoritative enemy intent state

### Requirement: Enemy Telegraph snapshot SHALL be represented as a placeholder

The system MUST represent enemy telegraph state through a read-only placeholder snapshot suitable for M0 read-phase inspection.

#### Scenario: Telegraph phase is observable
- **WHEN** the enemy enters telegraph phase
- **THEN** the snapshot MUST expose telegraph-active state and relevant placeholder context

#### Scenario: Telegraph phase exits cleanly
- **WHEN** the enemy transitions from telegraph to commit or returns idle
- **THEN** the snapshot MUST reflect telegraph no longer active

### Requirement: Enemy basic attack intent placeholder SHALL be represented

The system MUST represent a basic enemy attack intent placeholder for M0 combat readability and downstream observation.

#### Scenario: Attack intent is emitted for commit path
- **WHEN** enemy transitions into commit/active path
- **THEN** the snapshot/context MUST expose a basic attack intent placeholder

#### Scenario: Attack intent does not apply damage by itself
- **WHEN** basic attack intent placeholder is exposed
- **THEN** it MUST NOT directly apply damage or hit reaction consequences

### Requirement: Enemy attack tag representation SHALL be owned by Enemy Intent

The system MUST represent enemy attack tags in enemy-side state/context for M0 readability and downstream rule interpretation.

#### Scenario: Tags are visible during enemy attack phases
- **WHEN** enemy attack placeholder is active
- **THEN** associated enemy attack tags MUST be inspectable from Enemy Intent outputs

#### Scenario: Tag ownership is not moved to Combat Core
- **WHEN** Combat Core processes player combat request/result
- **THEN** Combat Core MUST observe enemy tags as external context and MUST NOT become enemy-tag authority

### Requirement: EnemyPunishWindow context SHALL be represented as a placeholder

The system MUST represent `EnemyPunishWindow` as an inspectable placeholder context with open/closed state, source, and remaining time fields.

#### Scenario: Punish window opens on enemy-side punishable transition
- **WHEN** enemy transitions into a punishable placeholder condition (for example recovery/whiff placeholder)
- **THEN** `EnemyPunishWindow` MUST indicate open with source and remaining duration

#### Scenario: Punish window closes on timeout/exit
- **WHEN** punish window duration expires or enemy exits punishable state
- **THEN** `EnemyPunishWindow` MUST indicate closed

### Requirement: Enemy intent snapshot SHALL be read-only

The system MUST expose a read-only enemy intent snapshot for Debug Overlay and downstream observers.

#### Scenario: Snapshot reflects current enemy truth
- **WHEN** enemy intent state, telegraph state, tags, or punish window changes
- **THEN** the latest snapshot MUST reflect current enemy intent truth

#### Scenario: Consumers cannot mutate enemy authority
- **WHEN** a consumer reads enemy intent snapshot data
- **THEN** the consumer MUST NOT be able to mutate authoritative enemy intent state through the snapshot

### Requirement: System ownership boundaries SHALL remain explicit

The system MUST preserve M0 ownership boundaries while adding enemy intent skeleton contracts and behavior.

#### Scenario: Combat Core authority remains combat request/result only
- **WHEN** enemy intent skeleton is introduced
- **THEN** Combat Core MUST continue owning combat request/result and `CounterWindow`, not enemy telegraph truth

#### Scenario: Health/Damage authority remains unchanged
- **WHEN** enemy intent emits attack placeholders
- **THEN** damage, health mutation, hit reaction consequence, and defeat consequence MUST remain owned by Health/Damage systems

#### Scenario: Locomotion and Target ownership remain unchanged
- **WHEN** enemy intent state updates
- **THEN** Player Locomotion MUST remain movement-truth owner and Target Context MUST remain target-truth owner

#### Scenario: Debug Overlay remains observer-only
- **WHEN** debug overlay consumes enemy snapshot data
- **THEN** it MUST remain read-only and non-authoritative

### Requirement: Skeleton SHALL exclude non-goal implementation dependencies

The system MUST keep this change as a skeleton and exclude full behavior and integration dependencies.

#### Scenario: No full AI/navigation/hitbox/damage/presentation implementation
- **WHEN** the enemy intent skeleton is implemented
- **THEN** it MUST NOT include real enemy AI movement, NavMesh, animation controller dependency, hitbox logic, damage application, player tracking behavior, scene/prefab wiring, boss/multi-enemy behavior, or final telegraph VFX/audio logic

#### Scenario: No forbidden framework regressions
- **WHEN** files are added/updated for this change
- **THEN** there MUST be no legacy Input Manager references, no Nhem generated DI usage, and VContainer scopes MUST remain manual

#### Scenario: Contracts remain data-only
- **WHEN** `M0Contracts.cs` is updated for enemy intent types
- **THEN** it MUST contain contract shape only and MUST NOT include behavior logic
