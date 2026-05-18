# VContainer Rules — Glass Refrain

## Purpose

These rules define how to use VContainer for clean dependency composition without turning DI into a service locator or global state container.

## General Rule

Use VContainer for dependency composition.

Do not use Service Locator for gameplay systems.

## Constructor Injection

Prefer constructor injection for pure C# services.

Good:

```csharp
public sealed class CombatCoreService : ICombatCoreService
{
    private readonly ITargetContextReader _targetContext;
    private readonly ITimeProvider _timeProvider;

    public CombatCoreService(
        ITargetContextReader targetContext,
        ITimeProvider timeProvider)
    {
        _targetContext = targetContext;
        _timeProvider = timeProvider;
    }
}
```

## MonoBehaviour Injection

Use method injection for MonoBehaviours.

Good:

```csharp
public sealed class CombatAnimatorPresenter : MonoBehaviour
{
    private ICombatStateReader _combatStateReader;

    [Inject]
    public void Construct(ICombatStateReader combatStateReader)
    {
        _combatStateReader = combatStateReader;
    }
}
```

Do not use constructor injection for MonoBehaviours.

## LifetimeScope Rule

LifetimeScope composes dependencies.

LifetimeScope must not contain gameplay logic.

Good:

```csharp
protected override void Configure(IContainerBuilder builder)
{
    builder.Register<ICombatCoreService, CombatCoreService>(Lifetime.Scoped);
    builder.Register<IPlayerLocomotionService, PlayerLocomotionService>(Lifetime.Scoped);
}
```

Bad:

```csharp
protected override void Configure(IContainerBuilder builder)
{
    var combat = new CombatCoreService();
    combat.StartDuel();
    combat.OpenCounterWindow();
}
```

## Lifetime Rules

Use `Singleton` only for project-wide services.

Allowed singleton examples:

```txt
logging
configuration
time provider if stateless
asset registry
global settings
```

Use `Scoped` for gameplay scene systems.

```txt
combat core
player locomotion
target context
encounter framework
memory state
combat camera state
debug overlay state
```

Do not register combat runtime truth globally.

## Scope Ownership

Project root scope owns:

```txt
global infrastructure
settings
logging
shared app services
```

Gameplay scene scope owns:

```txt
combat
locomotion
target context
encounter
memory
camera runtime
debug runtime
```

## Interface Registration

Register services by meaningful interfaces.

Good:

```csharp
builder.Register<CombatCoreService>(Lifetime.Scoped)
    .As<ICombatCoreService>()
    .As<ICombatStateReader>();
```

Avoid registering everything as self only unless needed.

## Source Generator Rule

Generated registration is preferred when stable.

Manual registration is allowed during M0.

Mark temporary manual registration clearly:

```csharp
// M0 Technical Skeleton: manual registration until source-generation guardrails stabilize.
builder.Register<ICombatCoreService, CombatCoreService>(Lifetime.Scoped);
```

## No Runtime Resolve Abuse

Avoid resolving services manually during gameplay.

Bad:

```csharp
var combat = container.Resolve<ICombatCoreService>();
```

Prefer injected dependencies.

Manual resolve is allowed only in composition/bootstrap or tooling.

## Circular Dependency Rule

Avoid circular dependencies.

Bad:

```txt
CombatCoreService → PlayerLocomotionService → CombatCoreService
```

Fix by splitting reader/command interfaces:

```txt
CombatCoreService → ILocomotionStateReader
PlayerLocomotionService → ICombatRestrictionReader
```

## Registration Naming Rule

Registration code should be grouped by system.

Example:

```csharp
private static void RegisterCombat(IContainerBuilder builder)
{
    builder.Register<CombatCoreService>(Lifetime.Scoped)
        .As<ICombatCoreService>()
        .As<ICombatStateReader>();
}
```

Avoid one long unstructured `Configure` method when registration grows.
