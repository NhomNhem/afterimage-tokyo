## 1. Baseline And Scope Guard

- [x] 1.1 Confirm the working tree is clean or only contains approved slice changes before implementation.
- [x] 1.2 Record the current inline `M0LocomotionSettings` values from `GameplayLifetimeScope`.
- [x] 1.3 Run or identify existing focused locomotion regression coverage before changing runtime composition.

## 2. ScriptableObject Config

- [x] 2.1 Add an M0 locomotion tuning ScriptableObject type under locomotion-owned project code.
- [x] 2.2 Add conversion from authored config values to `M0LocomotionSettings`.
- [x] 2.3 Create a default M0 locomotion tuning asset with the current values: `5.0`, `0.1`, `8.0`, `1.5`, `10.0`, `0.2`.
- [x] 2.4 Keep the ScriptableObject limited to authored tuning data with no movement truth or runtime state progression.

## 3. Runtime Composition

- [x] 3.1 Add an explicit required config reference to `GameplayLifetimeScope`.
- [x] 3.2 Replace inline `M0LocomotionSettings` construction in `GameplayLifetimeScope` with config conversion.
- [x] 3.3 Assign the default locomotion tuning asset in `Gameplay_CombatPrototype`.
- [x] 3.4 Keep `M0PlayerLocomotion` constructor and runtime logic independent from Unity asset types.

## 4. Tests And Guardrails

- [x] 4.1 Add or update EditMode coverage proving config-to-settings parity.
- [x] 4.2 Add or update scene composition coverage proving the gameplay scene has the locomotion tuning config assigned.
- [x] 4.3 Add or update guardrail coverage proving locomotion tuning literals are not reintroduced into the `M0PlayerLocomotion` registration.
- [x] 4.4 Run focused locomotion regression coverage and confirm movement/dodge behavior remains equivalent.

## 5. Evidence And Closure

- [x] 5.1 Run Unity compile smoke and classify console output.
- [x] 5.2 Run focused EditMode tests for config parity and locomotion composition.
- [x] 5.3 Run PlayMode smoke or manual M0 checklist covering move, dodge, defensive loop continuity, and memory reveal continuity.
- [x] 5.4 Run source guardrails for direct Unity debug logging and generated folder checks.
- [x] 5.5 Record PASS/PARTIAL/FAIL evidence in a QA evidence file.
- [x] 5.6 Run `openspec validate externalize-m0-locomotion-tuning-to-scriptableobject --strict`.

## 6. Deferred Follow-ups

- [x] 6.1 Defer scene component registration extraction from `GameplayLifetimeScope` to a separate approved change.
- [x] 6.2 Defer R3 read-model or MessagePipe notifications until there is a concrete consumer.
- [x] 6.3 Defer runtime movement feel changes to a separate tuning story/change.
