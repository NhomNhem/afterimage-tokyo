## 1. Baseline and Scope Guard

- [x] 1.1 Record current `GameplayLifetimeScope` hard-coded M0 combat timing values.
- [x] 1.2 Confirm current focused M0 combat regression baseline before implementation.
- [x] 1.3 Confirm no unrelated scene, prefab, or runtime changes are mixed into this slice.

## 2. ScriptableObject Config

- [x] 2.1 Add `M0CombatTimingConfig` ScriptableObject type with serialized authored timing values.
- [x] 2.2 Add conversion from `M0CombatTimingConfig` to immutable `M0CombatTimingSettings`.
- [x] 2.3 Ensure authored values validate through existing `M0CombatTimingSettings` positive-value rules.
- [x] 2.4 Create the default M0 combat timing asset with current verified values.

## 3. Runtime Composition

- [x] 3.1 Add an explicit required `M0CombatTimingConfig` reference to `GameplayLifetimeScope`.
- [x] 3.2 Replace inline `M0CombatTimingSettings` construction in `GameplayLifetimeScope` with `combatTimingConfig.ToSettings()`.
- [x] 3.3 Assign the default combat timing asset in `Gameplay_CombatPrototype`.
- [x] 3.4 Keep `M0CombatCore` independent from ScriptableObject and Unity asset types.

## 4. Tests and Guardrails

- [x] 4.1 Add focused EditMode test proving default config values match the current inline M0 timing values.
- [x] 4.2 Add or update composition guardrail test proving `GameplayLifetimeScope` no longer inlines M0 combat timing literals in the `M0CombatCore` registration.
- [x] 4.3 Add or update scene composition test proving `Gameplay_CombatPrototype` assigns the combat timing config reference.
- [x] 4.4 Run focused M0 combat regression tests.

## 5. Evidence and Closure

- [x] 5.1 Run compile smoke.
- [x] 5.2 Run focused EditMode config/composition tests.
- [x] 5.3 Run PlayMode smoke or manual M0 checklist for `read -> evade/parry -> counter -> reveal` parity.
- [x] 5.4 Run source guardrail checks for no direct `UnityEngine.Debug`, no `Resources.Load`, no `FindObject*`, and no Service Locator fallback in owned runtime composition.
- [x] 5.5 Record console classification and PASS/PARTIAL/FAIL evidence under `production/qa/evidence/`.
- [x] 5.6 Run `openspec validate externalize-m0-combat-tuning-to-scriptableobject --strict`.
- [x] 5.7 Commit only after explicit user instruction.

## Deferred Follow-Up Slices

- [x] [DEFERRED] Externalize M0 locomotion tuning to ScriptableObject.
- [x] [DEFERRED] Extract M0 scene component registration out of `GameplayLifetimeScope`.
- [x] [DEFERRED] Add R3 read-only tuning/debug observation where UI/debug read models need it.
- [x] [DEFERRED] Add MessagePipe events only for confirmed cross-system domain events.
