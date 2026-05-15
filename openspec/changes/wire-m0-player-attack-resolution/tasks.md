# Tasks: Wire M0 Player Attack Resolution

## 1. Contracts (M0Contracts)

- [x] 1.1 Add `LightAttackIntent` record to M0Contracts (raw attack intent DTO)
- [x] 1.2 Add `HeavyAttackIntent` record to M0Contracts (raw attack intent DTO)
- [x] 1.3 Add `CombatResultSnapshot` record to M0Contracts (read-only snapshot with init-only properties)
- [x] 1.4 Add `MovementRestrictionContext` record to M0Contracts (if skeleton requires)
- [x] 1.5 Add `RecoveryContext` record to M0Contracts (if skeleton requires)
- [x] 1.6 Verify contracts-only compliance (no behavior logic, ADR-0005)

## 2. Input Routing (Input Assembly)

- [x] 2.1 Extend `M0InputRouter` to handle LightAttack action from InputActionAsset
- [x] 2.2 Extend `M0InputRouter` to handle HeavyAttack action from InputActionAsset
- [x] 2.3 Emit `LightAttackIntent` to injected `M0CombatCore` on LightAttack trigger
- [x] 2.4 Emit `HeavyAttackIntent` to injected `M0CombatCore` on HeavyAttack trigger
- [x] 2.5 Verify no legacy Input Manager usage
- [x] 2.6 Verify no hardcoded device polling (Keyboard.current, Mouse.current, Gamepad.current)

## 3. Combat Core Validation (Combat Assembly)

- [x] 3.1 Implement attack request validation in `M0CombatCore` (check current state)
- [x] 3.2 Reject attack requests during AttackRecovery
- [x] 3.3 Reject attack requests during HitReact
- [x] 3.4 Reject attack requests during other committed states (AttackStartup, AttackActive, etc.)
- [x] 3.5 Accept attack requests from Neutral state
- [x] 3.6 Distinguish light attack vs heavy attack requests
- [x] 3.7 Track rejection reason for debug visibility

## 4. Combat Core Resolution (Combat Assembly)

- [x] 4.1 Implement placeholder hit resolution when valid target exists in Target Context
- [x] 4.2 Implement whiff resolution when no valid target exists
- [x] 4.3 Implement whiff resolution when target is out of range
- [x] 4.4 Read Target Context snapshot (read-only) for spacing/timing truth
- [x] 4.5 Verify no damage/health mutation occurs
- [x] 4.6 Verify no hit reaction mutation occurs
- [x] 4.7 Emit `MovementRestrictionContext` on attack if skeleton supports
- [x] 4.8 Emit `RecoveryContext` on attack completion if skeleton supports

## 5. Combat State Snapshot (Combat Assembly)

- [x] 5.1 Implement `CombatResultSnapshot` with init-only properties
- [x] 5.2 Include current combat state in snapshot
- [x] 5.3 Include attack type (light vs heavy) in snapshot
- [x] 5.4 Include result (hit, whiff, rejected) in snapshot
- [x] 5.5 Include reason string in snapshot
- [x] 5.6 Verify snapshot is read-only (no setters)
- [x] 5.7 Expose snapshot via `GetSnapshot()` method

## 6. DI Composition (Bootstrap/Gameplay)

- [x] 6.1 Update `GameplayLifetimeScope` to register `IM0CombatCore` → `M0CombatCore` (Lifetime.Scoped)
- [x] 6.2 Inject `ITargetContext` into `M0CombatCore` for read-only access
- [x] 6.3 Inject `M0CombatCore` into `M0InputRouter` for intent routing
- [x] 6.4 Verify manual registration only (no automatic scanning or generated DI)
- [x] 6.5 Verify no ProjectRoot registrations for combat services

## 7. Input Action Asset Setup

- [x] 7.1 Add LightAttack action to `M0InputActions.inputactions`
- [x] 7.2 Add HeavyAttack action to `M0InputActions.inputactions`
- [x] 7.3 Bind LightAttack to keyboard and gamepad
- [x] 7.4 Bind HeavyAttack to keyboard and gamepad
- [x] 7.5 Verify actions route through InputActionAsset only

## 8. EditMode Tests

- [x] 8.1 Create `CombatResolution_test.cs` with test methods
- [x] 8.2 Test LightAttack intent routes to Combat Core as light attack request
- [x] 8.3 Test HeavyAttack intent routes to Combat Core as heavy attack request
- [x] 8.4 Test Combat Core rejects attack when not allowed by current combat state
- [x] 8.5 Test Combat Core resolves placeholder hit when valid active target exists
- [x] 8.6 Test Combat Core resolves whiff/no-target result when no valid target exists
- [x] 8.7 Test combat result snapshot is read-only
- [x] 8.8 Test Target Context is read-only consumer data only and does not decide combat validity
- [x] 8.9 Test no damage/health mutation occurs
- [x] 8.10 Test manual VContainer registration resolves Combat Core wiring
- [x] 8.11 Test no legacy Input Manager usage
- [x] 8.12 Test no hardcoded device polling

## 9. Manual Verification

- [x] 9.1 Unity Editor play mode: Bootstrap → Systems → Level → Gameplay scenes load
- [x] 9.2 Press LightAttack key: intent routes to Combat Core
- [x] 9.3 Press HeavyAttack key: intent routes to Combat Core
- [x] 9.4 Debug Overlay shows combat state transitions and lock reasons
- [x] 9.5 Verify attack rejection during recovery state
- [x] 9.6 Verify hit/whiff resolution against target context

## 10. Scope Exclusions Verification

- [x] 10.1 Code review: No damage/health mutation present
- [x] 10.2 Code review: No hit reaction implementation
- [x] 10.3 Code review: No parry/dodge integration
- [x] 10.4 Code review: No counter window implementation beyond placeholder shape
- [x] 10.5 Code review: No enemy AI expansion
- [x] 10.6 Code review: No animation/root motion authority
- [x] 10.7 Code review: No combo system
- [x] 10.8 Code review: No stamina system
- [x] 10.9 Code review: No skill system
- [x] 10.10 Code review: No VFX/camera polish
- [x] 10.11 Code review: No target-relative movement rewrite
- [x] 10.12 Code review: No locomotion rewrite
- [x] 10.13 Code review: No camera-owned combat or target truth
- [x] 10.14 Code review: No generated DI
- [x] 10.15 Code review: No legacy Input Manager calls
- [x] 10.16 Code review: No hardcoded device polling via Keyboard.current, Mouse.current, Gamepad.current
- [x] 10.17 Code review: No FindObjectOfType, FindFirstObjectByType, GameObject.Find, Resources.Load

## 11. Documentation & Handoff

- [x] 11.1 Update `M0Contracts.cs` XML docs for new combat types
- [x] 11.2 Add combat section to Debug Overlay documentation
- [x] 11.3 Verify Story 1-4 acceptance criteria pass
- [x] 11.4 Mark Story 1-4 as Complete in story file
- [x] 11.5 Update sprint-1.md task status for S1-4
