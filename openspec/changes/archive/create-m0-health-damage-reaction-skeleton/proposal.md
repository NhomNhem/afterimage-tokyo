## Why

M0 needs a dedicated consequence-layer owner so confirmed combat outcomes can be translated into health change, hit reaction classification, and defeat/disabled consequences without leaking authority into Combat Core, Enemy Intent, Locomotion, or Memory systems. This change establishes the minimum Health / Damage / Hit Reaction skeleton before downstream systems rely on consequence context.

## What Changes

- Introduce a minimal M0 Health / Damage / Hit Reaction capability.
- Define pure C# health state model for living/damaged/recovering/defeated or disabled flow.
- Define damage application request/result contract shapes.
- Define hit reaction context placeholder shape.
- Define defeat/disabled context placeholder shape.
- Expose read-only health/reaction snapshot for Debug Overlay and downstream observers.
- Add edit-mode tests for damage request/result behavior, health snapshot behavior, hit reaction placeholder behavior, and defeated state behavior.
- Keep ownership boundaries explicit so Combat Core does not apply damage and adjacent systems remain non-authoritative for health truth.

## Capabilities

### New Capabilities
- `m0-health-damage-reaction-skeleton`: Minimal health truth state model, damage request/result contracts, hit reaction placeholder context, defeat/disabled placeholder context, and read-only health/reaction snapshot for M0.

### Modified Capabilities
- None. (Combat Core, Player Locomotion, Enemy Intent & Telegraph, Target Context, and Memory State remain unchanged as authorities.)

## Impact

- `Assets/_Project/Code/Core` (new or refined health/damage/reaction contract shapes only)
- `Assets/_Project/Code/Health` (new pure C# health/damage/hit reaction skeleton owner)
- `Assets/_Project/Tests/EditMode` (new health/damage/reaction skeleton behavior coverage)
- M0 consequence ownership boundaries between Health, Combat Core, Locomotion, Enemy Intent, Memory, and Debug systems
