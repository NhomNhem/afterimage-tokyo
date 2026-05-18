# C# Naming Rules — Glass Refrain

## Purpose

These rules define naming conventions for C# code in `Glass Refrain`. The goal is readable, consistent, intention-revealing code that works well with Unity, Odin Inspector, VContainer, and long-term AI-assisted development.

## General Naming

Use clear, intention-revealing names.

Good:

```csharp
private float _currentHealth;
private bool _isCounterWindowOpen;
private ICombatCoreService _combatCore;
```

Bad:

```csharp
private float hp;
private bool flag;
private ICombatCoreService service;
```

Avoid vague names unless the scope is tiny and obvious:

- `data`
- `manager`
- `handler`
- `controller`
- `temp`
- `obj`
- `thing`

Allowed common abbreviations:

- UI
- HUD
- VFX
- SFX
- FSM
- DI
- ID
- CPU
- GPU

## Private Fields

Private runtime fields use `_camelCase`.

```csharp
private float _moveSpeed;
private bool _isDodging;
private IInputReader _inputReader;
private Vector3 _currentVelocity;
```

## Serialized Private Fields

`[SerializeField] private` fields do **not** use `_`.

Reason:

- They appear in Unity Inspector.
- Inspector-facing names should be clean.
- They are authored configuration or scene references, not purely internal runtime state.

Good:

```csharp
[SerializeField] private float moveSpeed = 5f;
[SerializeField] private Transform cameraRoot;
[SerializeField] private Animator animator;
```

Bad:

```csharp
[SerializeField] private float _moveSpeed = 5f;
[SerializeField] private Transform _cameraRoot;
[SerializeField] private Animator _animator;
```

## Odin Inspector Fields

Odin-inspected private fields also do not use `_` when they are designer-facing.

```csharp
[Title("Movement")]
[SerializeField, MinValue(0f)]
private float moveSpeed = 5f;

[SerializeField, Required]
private Transform cameraRoot;
```

Runtime-only Odin debug properties may use normal property naming.

```csharp
[ShowInInspector, ReadOnly]
private CombatState CurrentCombatState => _combatStateReader.CurrentState;
```

## Readonly Dependencies

Private readonly dependencies use `_camelCase`.

```csharp
private readonly ITargetContextReader _targetContext;
private readonly ITimeProvider _timeProvider;
```

## Constants

Constants use `PascalCase`.

```csharp
private const float DefaultMoveSpeed = 5f;
private const int MaxTargetCount = 1;
```

Avoid:

```csharp
private const float DEFAULT_MOVE_SPEED = 5f;
```

## Static Readonly Fields

Static readonly fields use `PascalCase`.

```csharp
private static readonly int SpeedHash = Animator.StringToHash("Speed");
```

## Properties

Properties use `PascalCase`.

```csharp
public bool IsDodging { get; private set; }
public CombatState CurrentState { get; private set; }
```

Boolean properties should usually begin with:

- `Is`
- `Has`
- `Can`
- `Should`
- `Requires`

Examples:

```csharp
public bool IsActive { get; }
public bool HasTarget { get; }
public bool CanCounter { get; }
public bool ShouldShowDebug { get; }
```

## Methods

Methods use `PascalCase` and should describe actions.

Good:

```csharp
public void EnterDodge();
public bool TryOpenCounterWindow();
public void ApplyDamage(DamageRequest request);
```

Bad:

```csharp
public void Process();
public void DoThing();
public void Handle();
```

Use `Try` when a method can fail without throwing.

```csharp
public bool TryAcquireTarget(out ITargetable target);
public bool TryRequestParry(ParryRequest request);
```

Use `Create` for factory methods.

```csharp
public static DamageRequest CreateLightAttackDamage(...);
```

Use `Handle` only for event/message handlers.

```csharp
private void HandleParrySucceeded(ParrySucceededMessage message);
```

## Interfaces

Interfaces use `I` prefix.

```csharp
public interface ICombatCoreService
public interface IPlayerLocomotionService
public interface ITargetContextReader
```

Interface names should describe capability or role, not implementation details.

Good:

```csharp
ICombatStateReader
ITargetProvider
IDamageResolver
IInputIntentReader
```

Bad:

```csharp
IManager
IHelper
IThing
```

## Classes

Classes use `PascalCase`.

Class names should describe responsibility.

Good:

```csharp
CombatCoreService
PlayerLocomotionMotor
LockOnTargetContext
MemoryRevealService
DebugOverlayPresenter
```

Avoid vague suffixes unless the role is truly justified:

- `Manager`
- `Handler`
- `Processor`
- `Helper`
- `Util`

Prefer specific names:

```txt
CombatCoreService
EncounterLifecycleService
TargetContextService
DamageResolver
DebugOverlayPresenter
InputIntentRouter
```

## Events

C# events should usually be past-tense or state-change based.

```csharp
public event Action<DamageResult> DamageApplied;
public event Action<CombatState> CombatStateChanged;
```

Handlers use `HandleX`.

```csharp
private void HandleDamageApplied(DamageResult result);
```

Unity lifecycle methods keep Unity names.

```csharp
private void OnEnable();
private void OnDisable();
```

## Message Types

MessagePipe/R3 message names should be immutable and event-like.

Good:

```csharp
public readonly record struct DamageAppliedMessage(...);
public readonly record struct CounterWindowOpenedMessage(...);
public readonly record struct TargetChangedMessage(...);
```

Bad:

```csharp
public readonly record struct CombatMessage(...);
public readonly record struct GameEvent(...);
public readonly record struct DataMessage(...);
```

## Enums

Enums use `PascalCase`.

```csharp
public enum CombatState
{
    Neutral,
    AttackStartup,
    AttackActive,
    AttackRecovery,
    DodgeStartup,
    DodgeActive,
    DodgeRecovery,
    ParryActive,
    CounterWindow,
    HitReact,
}
```

Do not prefix enum values with the enum name.

Bad:

```csharp
CombatStateNeutral,
CombatStateAttackStartup
```

## File Names

One main public type per file.

File name must match the main type.

Good:

```txt
CombatCoreService.cs
ICombatCoreService.cs
PlayerLocomotionMotor.cs
DamageRequest.cs
```

Bad:

```txt
CombatStuff.cs
GameplayHelpers.cs
NewBehaviourScript.cs
```

## Namespaces

Namespace should match project and layer.

Examples:

```csharp
namespace GlassRefrain.Domain.Combat;
namespace GlassRefrain.Application.Combat;
namespace GlassRefrain.Infrastructure.Input;
namespace GlassRefrain.Presentation.Debug;
```

Avoid generic namespaces:

```csharp
namespace Scripts;
namespace Game;
namespace Test;
```

## Summary Table

| Item | Rule |
|---|---|
| private runtime field | `_camelCase` |
| `[SerializeField] private` field | `camelCase`, no `_` |
| Odin designer-facing field | `camelCase`, no `_` |
| private readonly dependency | `_camelCase` |
| const | `PascalCase` |
| static readonly | `PascalCase` |
| property | `PascalCase` |
| method | `PascalCase` |
| interface | `IName` |
| class/struct/record | `PascalCase` |
| enum value | `PascalCase`, no enum prefix |
