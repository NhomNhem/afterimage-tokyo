---
paths:
  - "Assets/_Project/Code/Application/**"
  - "Assets/_Project/Code/Domain/**"
  - "Assets/_Project/Code/Infrastructure/**"
---

# Gameplay Code Rules

- ALL gameplay values MUST come from external config/data files, NEVER hardcoded.
- Use delta time for ALL time-dependent calculations (frame-rate independence).
- NO direct references to UI code — use interfaces, reader contracts, or R3/MessagePipe for cross-system observation.
- Every gameplay system must implement a clear interface.
- State machines must have explicit transition tables with documented states.
- Write unit tests for all gameplay logic (EditMode) — separate logic from presentation.
- Ownership boundaries must be respected — a system must not modify another system's truth.
- No static singletons for game state — use VContainer dependency injection.
- Gameplay truth lives in pure C# state/models, not in Animator, MonoBehaviour fields, or scene objects.

## Examples

**Correct** (data-driven, uses DI):

```csharp
private readonly CombatConfig _config;

public CombatCoreService(CombatConfig config, ITimeProvider timeProvider)
{
    _config = config;
    _timeProvider = timeProvider;
}

public DamageRequestResult EvaluateDamage()
{
    float baseDamage = _config.LightAttackDamage;
    float applyAfter = baseDamage * _timeProvider.DeltaTime;
    // ...
}
```

**Incorrect** (hardcoded, no delta time):

```csharp
private void Update()
{
    var damage = 25.0;                // VIOLATION: hardcoded
    transform.position += Vector3.forward * 5.0 * Time.deltaTime; // VIOLATION: hardcoded speed
}
```
