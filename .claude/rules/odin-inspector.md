# Odin Inspector Rules — Glass Refrain

## Purpose

These rules define how to use Odin Inspector and Odin serialization without turning inspector convenience into runtime authority.

## General Rule

Prefer Odin Inspector when it improves designer-facing clarity, safety, or validation.

Do not use Odin just to decorate every field.

Use Odin to make configuration:

- clearer
- safer
- grouped
- validated
- easier to tune

## Preferred Odin Attributes

Recommended attributes:

```txt
Title
BoxGroup
FoldoutGroup
TabGroup
Required
MinValue
MaxValue
Range
ReadOnly
ShowInInspector
InfoBox
ValidateInput
Button
ShowIf
HideIf
EnableIf
DisableIf
InlineEditor
AssetSelector
```

Example:

```csharp
[Title("Movement")]
[SerializeField, MinValue(0f)]
private float moveSpeed = 5f;

[SerializeField, Required]
private Transform cameraRoot;

[SerializeField, Range(0f, 1f)]
private float parryWindow = 0.2f;

[ReadOnly, ShowInInspector]
private CombatState CurrentState => _combat.CurrentState;
```

## Inspector Grouping

Group serialized fields by intent.

Good:

```csharp
[Title("References")]
[SerializeField, Required]
private Animator animator;

[SerializeField, Required]
private CharacterController characterController;

[Title("Movement Tuning")]
[SerializeField, MinValue(0f)]
private float moveSpeed = 5f;

[SerializeField, MinValue(0f)]
private float dodgeDistance = 3f;

[Title("Debug")]
[SerializeField]
private bool showDebug;
```

Bad:

```csharp
[SerializeField] private float moveSpeed;
[SerializeField] private bool showDebug;
[SerializeField] private Animator animator;
[SerializeField] private float dodgeDistance;
[SerializeField] private CharacterController characterController;
```

## SerializedMonoBehaviour Rule

Use `SerializedMonoBehaviour` only when Odin serialization is actually needed.

Allowed reasons:

- serialize interfaces
- serialize dictionaries
- serialize polymorphic data
- serialize complex nested authored data
- improve inspector workflows for designer-authored config

Good:

```csharp
public sealed class AttackConfigAuthoring : SerializedMonoBehaviour
{
    [OdinSerialize]
    private Dictionary<AttackId, AttackTimingConfig> attackTimings;
}
```

Use normal `MonoBehaviour` when Unity serialization is enough.

Good:

```csharp
public sealed class PlayerLocomotionView : MonoBehaviour
{
    [SerializeField] private CharacterController characterController;
    [SerializeField] private Animator animator;
}
```

Bad:

```csharp
public sealed class SimpleView : SerializedMonoBehaviour
{
    [SerializeField] private Transform target;
}
```

## Odin Serialization Boundary

Do not put gameplay truth inside Odin-serialized MonoBehaviours.

Odin can author data.

Odin should not become runtime authority.

Good:

```csharp
[SerializeField] private AttackTimingConfig lightAttackTiming;
```

Then convert or inject into runtime services.

Bad:

```csharp
public sealed class CombatManager : SerializedMonoBehaviour
{
    [OdinSerialize]
    private Dictionary<string, object> everything;

    private void Update()
    {
        // all combat logic here
    }
}
```

## Debug Buttons

Odin `[Button]` is allowed for debug/prototype actions, but must be guarded.

Good:

```csharp
#if GR_COMBAT_DEBUG
[Button]
private void DebugForceCounterWindow()
{
    _combatCore.DebugForceCounterWindow();
}
#endif
```

Bad:

```csharp
[Button]
private void KillEnemy()
{
    enemy.Health = 0;
}
```

without debug guard or clear prototype intent.

## ReadOnly Runtime State

Use Odin to expose runtime state for debugging.

Good:

```csharp
[ShowInInspector, ReadOnly]
private CombatState CurrentCombatState => _combatStateReader.CurrentState;

[ShowInInspector, ReadOnly]
private bool IsCounterWindowOpen => _combatStateReader.IsCounterWindowOpen;
```

Do not make runtime state editable unless it is explicitly a debug tool.

## ValidateInput

Use `ValidateInput` for authoring constraints.

```csharp
[SerializeField, ValidateInput(nameof(HasPositiveDuration), "Duration must be greater than zero.")]
private float duration = 0.2f;

private bool HasPositiveDuration(float value)
{
    return value > 0f;
}
```

## InfoBox

Use `InfoBox` to explain temporary M0 decisions.

```csharp
[InfoBox("M0 only: this config is provisional until combat timing stabilizes.")]
[SerializeField]
private AttackTimingConfig lightAttack;
```

## Odin Anti-Patterns

Avoid:

- using Odin to hide messy architecture
- making every field `[ShowInInspector]`
- exposing too many mutable runtime fields
- replacing Debug Overlay with random inspector fields
- using `SerializedMonoBehaviour` everywhere by default
- storing service dependencies as serialized fields
