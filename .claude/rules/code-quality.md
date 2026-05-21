# Code Quality Rules — Glass Refrain

## Purpose

These rules define practical code quality expectations for day-to-day implementation.

## Method Size

Keep methods small.

Target:

```txt
5–30 lines
```

If a method is longer than 50 lines, consider splitting it.

Allowed exceptions:

- simple mapping methods
- generated code
- editor UI code
- test setup code

## Class Size

Target:

```txt
under 300 lines for normal classes
under 500 lines for complex services
```

If a class grows beyond this, check responsibility boundaries.

## Early Return

Prefer early return to reduce nesting.

Good:

```csharp
public CombatRequestResult RequestDodge()
{
    if (!_inputEnabled)
    {
        return CombatRequestResult.Rejected(CombatRejectReason.InputDisabled);
    }

    if (_state.IsRecovering)
    {
        return CombatRequestResult.Rejected(CombatRejectReason.InRecovery);
    }

    EnterDodge();
    return CombatRequestResult.Accepted();
}
```

Bad:

```csharp
public CombatRequestResult RequestDodge()
{
    if (_inputEnabled)
    {
        if (!_state.IsRecovering)
        {
            EnterDodge();
            return CombatRequestResult.Accepted();
        }
        else
        {
            return CombatRequestResult.Rejected(...);
        }
    }
    else
    {
        return CombatRequestResult.Rejected(...);
    }
}
```

## Guard Clauses

Validate inputs at boundaries.

```csharp
public DamageResult ApplyDamage(DamageRequest request)
{
    if (request.Amount <= 0)
    {
        return DamageResult.Rejected(DamageRejectReason.InvalidAmount);
    }

    // apply damage
}
```

## Null Rule

Avoid unnecessary nulls.

Prefer:

- constructor-required dependencies
- `[Required]` serialized fields
- explicit validation
- nullable annotations where available

Serialized references should be validated in `OnValidate` or via Odin `[Required]`.

## Magic Number Rule

Avoid unexplained magic numbers.

Bad:

```csharp
if (_timer > 0.35f)
```

Good:

```csharp
private const float DefaultParryWindowSeconds = 0.35f;

if (_timer > DefaultParryWindowSeconds)
```

For tunable gameplay values, prefer serialized config.

```csharp
[SerializeField, MinValue(0f)]
private float parryWindowSeconds = 0.35f;
```

## Result Object Rule

For gameplay requests that can fail, return result objects.

Good:

```csharp
public CombatRequestResult RequestParry();
```

Bad if failure matters:

```csharp
public void RequestParry();
```

## Exception Rule

Do not use exceptions for normal gameplay flow.

Good:

```csharp
return CombatRequestResult.Rejected(CombatRejectReason.InRecovery);
```

Bad:

```csharp
throw new InvalidOperationException("Cannot parry during recovery");
```

Use exceptions for programmer errors and invalid setup.

## Update Loop Rule

Avoid putting heavy logic directly in `Update`.

Good:

```csharp
private void Update()
{
    _combatCore.Tick(Time.deltaTime);
}
```

Better for testability:

```csharp
public void Tick(float deltaTime)
{
    _stateMachine.Tick(deltaTime);
}
```

## Allocation Rule

Avoid unnecessary per-frame allocations in hot gameplay code.

Avoid in `Update` and hot ticks:

```txt
new List<T>()
LINQ-heavy chains
string interpolation for logs
capturing lambdas
boxing through non-generic APIs
```

Allowed in tools/debug/editor code.

Use ZLinq carefully if needed, but do not optimize prematurely.

## Logging Rule — NhemLogger Only

Use `NhemLogger` / `NhemLogging` (project logging wrapper on ZLogger).

Forbidden in all gameplay, application, presentation, and infrastructure code:

```csharp
Debug.Log("...");
Debug.LogWarning("...");
Debug.LogError("...");
UnityEngine.Debug.Log("...");
```

Prefer:

```csharp
NhemLogger.Combat("Counter window opened.");
```

Allowed exceptions:
- Inside the NhemLogger/NhemLogging implementation itself.
- Temporary local experiments removed before commit.
- Vendor/package code not owned by this project.
- Explicitly approved Unity editor diagnostics.

Debug logs must be removable by define symbols or log level.

## Async Rule

Use Unity Awaitable first for simple Unity async flows.

Use UniTask when:

- cancellation matters
- composition is complex
- async flow crosses systems
- performance/control is needed

Do not use async for simple deterministic state transitions.

## Region Rule

Use `#region` sparingly.

Allowed:

- long editor tooling classes
- generated-like registration grouping
- large test fixture helpers

Avoid using regions to hide classes that should be split.

## TODO Rule

Temporary code must be searchable and explicit.

Use project-prefixed TODOs:

```csharp
// TODO GR_M0: Replace with authored config after combat timing stabilizes.
// TODO GR_TECHDEBT: Split this presenter when debug overlay grows.
```

Avoid vague TODOs:

```csharp
// TODO fix later
```
