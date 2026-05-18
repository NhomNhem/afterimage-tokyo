# Testing Rules — Glass Refrain

## Purpose

These rules define testing expectations for M0 and future gameplay systems. Prioritize pure gameplay rule tests before broad PlayMode coverage.

## What Must Be Tested

Test pure gameplay rules first.

Priority:

1. Combat state transitions
2. Damage request/result
3. Target acquisition/release
4. Memory reveal acceptance/rejection
5. Input request routing
6. Encounter lifecycle
7. Debug snapshot shape

## EditMode Tests

Use EditMode tests for pure C# logic.

Good targets:

```txt
CombatCoreServiceTests
DamageResolverTests
TargetContextTests
MemoryRevealServiceTests
EncounterLifecycleTests
```

## PlayMode Tests

Use PlayMode tests for Unity integration.

Good targets:

```txt
GameplayLifetimeScope resolves services
Player prefab has required components
Input adapter emits intent
Debug overlay can read snapshots
Camera presenter receives target context
```

## Test Naming

Use this style:

```csharp
MethodName_WhenCondition_ShouldExpectedResult()
```

Examples:

```csharp
RequestParry_WhenPlayerIsRecovering_ShouldReject()
ApplyDamage_WhenAmountIsPositive_ShouldReduceHealth()
AcquireTarget_WhenEnemyIsDefeated_ShouldReject()
```

## Test Structure

Use Arrange / Act / Assert.

```csharp
[Test]
public void RequestDodge_WhenInNeutral_ShouldEnterDodge()
{
    // Arrange
    var service = CreateService();

    // Act
    var result = service.RequestDodge();

    // Assert
    Assert.That(result.IsAccepted, Is.True);
    Assert.That(service.CurrentState, Is.EqualTo(CombatState.DodgeStartup));
}
```

## Test Data

Prefer named test fixtures over magic values.

Good:

```csharp
private static DamageRequest CreateLightAttackDamage()
{
    return new DamageRequest(Amount: 10, Source: DamageSource.PlayerLightAttack);
}
```

Bad:

```csharp
service.ApplyDamage(new DamageRequest(10, 2, true));
```

## M0 Completion Rule

Do not mark an M0 system complete unless:

- core behavior is implemented
- debug visibility exists
- key rejection reasons are testable
- ownership boundaries are respected
- no unrelated full-game systems were added

## PlayMode Caution

Do not overuse PlayMode tests for pure logic.

If a rule can be tested without Unity scene objects, test it in EditMode.

## Regression Rule

Every bug fix should add a focused test when practical.

Test the behavior, not the implementation detail.
