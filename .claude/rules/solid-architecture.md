# SOLID / Architecture Rules — Glass Refrain

## Purpose

These rules protect code architecture, gameplay ownership, and long-term maintainability. Architecture must support M0 combat feel, not slow it down.

## Core Principle

Architecture must protect gameplay ownership.

Do not over-engineer before M0 combat feel is proven.

Prefer:

- small explicit services
- request/result APIs
- pure C# state machines
- debug-visible state
- boring architecture that is easy to test

Avoid:

- god classes
- hidden global state
- inheritance-heavy gameplay
- generic ability frameworks before needed
- event chains that hide cause and effect

## Single Responsibility Principle

Each class should have one clear reason to change.

Good:

```txt
CombatCoreService
DamageResolver
PlayerLocomotionMotor
LockOnTargetContext
MemoryRevealService
DebugSnapshotPresenter
```

Bad:

```txt
PlayerManager
CombatManager
GameManager
EverythingController
```

A class is probably too large if it owns many of these at once:

- input
- movement
- combat
- camera
- animation
- VFX
- health
- debug

Split responsibilities by system ownership.

## Open / Closed Principle

Prefer extension through small strategies/configs when variation is real.

Do not introduce abstractions before there is a second real use case.

Good later:

```csharp
public interface IDamageFormula
{
    DamageResult Resolve(DamageRequest request);
}
```

Good for M0 if there is only one formula:

```csharp
public sealed class SimpleM0DamageResolver
{
}
```

M0 rule:

> Do not abstract before the second real use case appears.

## Liskov Substitution Principle

Avoid inheritance-heavy gameplay architecture.

Prefer composition over inheritance.

Allowed:

```csharp
public interface IDamageable
{
    DamageResult ApplyDamage(DamageRequest request);
}
```

Avoid deep trees:

```txt
BaseCharacter
  BasePlayer
    KatanaPlayer
      M0KatanaPlayer
```

Use inheritance only when substitution is actually safe.

## Interface Segregation Principle

Prefer small interfaces.

Good:

```csharp
public interface ICombatStateReader
{
    CombatSnapshot CurrentSnapshot { get; }
}

public interface ICombatCommandService
{
    CombatRequestResult RequestLightAttack();
    CombatRequestResult RequestDodge();
}
```

Bad:

```csharp
public interface ICombatService
{
    void Attack();
    void Dodge();
    void Parry();
    void ApplyDamage();
    void PlayAnimation();
    void ShakeCamera();
    void TriggerVfx();
    void Save();
}
```

Separate readers and writers when useful.

Good:

```txt
ICombatStateReader
ICombatCommandService
ITargetContextReader
ITargetCommandService
```

## Dependency Inversion Principle

High-level gameplay rules should depend on abstractions, not concrete Unity components.

Good:

```csharp
public sealed class CombatCoreService
{
    private readonly ITimeProvider _timeProvider;
    private readonly ITargetContextReader _targetContext;

    public CombatCoreService(
        ITimeProvider timeProvider,
        ITargetContextReader targetContext)
    {
        _timeProvider = timeProvider;
        _targetContext = targetContext;
    }
}
```

Bad:

```csharp
public sealed class CombatCoreService
{
    private readonly Animator _animator;
    private readonly CinemachineCamera _camera;
}
```

Domain/Application code should not directly depend on Unity scene objects unless explicitly intended.

Avoid in Domain/Application:

- MonoBehaviour
- Animator
- Cinemachine
- GameObject
- Transform
- ParticleSystem
- VisualElement

## Layer Rules

Use these conceptual layers:

```txt
Domain
Application
Infrastructure
Presentation
```

### Domain

Pure rules and data.

Allowed:

```txt
CombatState
DamageRequest
DamageResult
CounterWindow
TargetContextSnapshot
```

Forbidden:

```txt
MonoBehaviour
GameObject
Transform
Animator
Cinemachine
SerializedMonoBehaviour
```

### Application

Coordinates gameplay use cases and state machines.

Allowed:

```txt
CombatCoreService
EncounterLifecycleService
MemoryRevealService
PlayerLocomotionService
```

Application may depend on Domain contracts.

### Infrastructure

Implements external/package-specific details.

Allowed:

```txt
UnityInputReader
UnityTimeProvider
VContainer LifetimeScopes
Addressables loaders
```

### Presentation

Displays state and adapts Unity scene objects.

Allowed:

```txt
CombatAnimatorPresenter
DebugOverlayView
CameraPresenter
VfxPresenter
```

Presentation observes truth. It does not own truth.

## Anti-God-Class Rule

If a class name includes `Manager`, challenge it.

Before accepting a `Manager`, ask:

- What exactly does it own?
- Can the name be more specific?
- Is it coordinating too many systems?
- Should it be split into service, presenter, resolver, context, registry, or router?

## Data Flow Rule

Prefer explicit request/result objects for gameplay operations.

Good:

```csharp
public readonly record struct DamageRequest(
    int Amount,
    DamageSource Source,
    HitReactionType ReactionType
);

public readonly record struct DamageResult(
    bool WasApplied,
    int NewHealth,
    DamageRejectReason RejectReason
);
```

Bad:

```csharp
public void Damage(int amount)
{
    // modifies hidden global state
}
```

## Mutation Rule

State-changing methods should be named clearly.

Good:

```txt
EnterState
ApplyDamage
RequestDodge
OpenCounterWindow
ResetEncounter
```

Read-only methods/properties should not mutate state.

## Event Rule

Use direct method calls when systems are tightly related.

Use events/R3/MessagePipe only when decoupling is useful.

Good direct call:

```csharp
_combatCore.RequestDodge();
```

Good message:

```csharp
_publisher.Publish(new CounterWindowOpenedMessage(...));
```

Bad:

```csharp
// Local direct logic hidden behind unnecessary global event.
_messageBus.Publish(new MoveInputChangedMessage(...));
```

## M0 Architecture Rule

For M0, prefer:

- explicit state machines
- simple request/result APIs
- small services
- debug-visible state
- narrow scope

Avoid:

- generic ability framework
- broad RPG stat framework
- deep inheritance
- hidden reflection magic
- over-abstracted event chains
