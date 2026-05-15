## Why

M0 needs a dedicated enemy-side readability owner so duel threat, telegraph commitment, attack-phase timing, and punishability are represented by one authoritative source before Combat Core, Health, Target, and Debug Overlay consume enemy context. This change creates a minimal Enemy Intent & Telegraph skeleton that proves ownership boundaries without implementing full AI, movement, or damage behavior.

## What Changes

- Introduce a minimal M0 Enemy Intent & Telegraph capability.
- Define a pure C# enemy intent state model for idle/telegraph/commit/active/recovery flow.
- Define an enemy telegraph snapshot placeholder for read/observe behavior.
- Define a basic attack intent placeholder contract.
- Define `EnemyPunishWindow` context placeholder (open/closed, source, remaining duration).
- Define enemy attack tag representation for M0 readability and rule handoff.
- Expose read-only enemy intent snapshot for Debug Overlay and downstream observers.
- Add edit-mode tests for idle/telegraph/commit/recovery/punish-window snapshot behavior.
- Keep ownership boundaries explicit so Combat Core, Locomotion, Target, Health, and Memory ownership are not blurred.

## Capabilities

### New Capabilities
- `m0-enemy-intent-skeleton`: Minimal enemy intent truth state model, telegraph snapshot, basic attack intent placeholder, enemy attack tags, `EnemyPunishWindow` placeholder, and read-only enemy intent snapshot for debug/observation.

### Modified Capabilities
- None. (Combat Core, Player Locomotion, Target Context, Health/Damage, and Memory State remain unchanged as authorities.)

## Impact

- `Assets/_Project/Code/Core` (new or refined contracts for enemy intent snapshots, tags, and punish window placeholders only)
- `Assets/_Project/Code/Enemy` (new pure C# enemy intent state owner skeleton)
- `Assets/_Project/Tests/EditMode` (new enemy intent skeleton behavior coverage)
- M0 ownership boundaries between Enemy Intent, Combat Core, Health, Locomotion, Target, and Debug systems
