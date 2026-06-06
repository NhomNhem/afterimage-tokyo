## 1. Baseline And Scope Guard

- [x] 1.1 Confirm the working tree is clean or only contains approved pre-existing fixes before implementation.
- [x] 1.2 Capture the current `GameplayLifetimeScope` scene reference fields, service registration order, and post-build wiring responsibilities.
- [x] 1.3 Run focused baseline scene composition tests before extraction.
- [x] 1.4 Confirm the custom `GameplayLifetimeScope` inspector displays and binds serialized scene references before extraction.

## 2. Registrar Extraction

- [x] 2.1 Add a Bootstrap-owned M0 scene composition registrar/collaborator.
- [x] 2.2 Move explicit scene component registration from `GameplayLifetimeScope` into the registrar.
- [x] 2.3 Move post-build scene wiring for presentation adapters, enemy loop debug harness, and memory scene participant injection into the registrar.
- [x] 2.4 Keep generated NhemDI gameplay-scope registration and authored combat/locomotion config conversion in `GameplayLifetimeScope`.
- [x] 2.5 Keep all scene references explicit and avoid broad scene discovery or resource fallback.

## 3. Inspector And Composition UX

- [x] 3.1 Preserve the `GameplayLifetimeScope` UI Toolkit inspector layout.
- [x] 3.2 Verify all required core adapter, animation driver, config, and memory fields remain visible and assignable.
- [x] 3.3 Ensure the custom editor uses proper serialized binding and does not use direct Unity debug logging.

## 4. Tests And Guardrails

- [x] 4.1 Add or update source/scene composition tests proving registrar extraction keeps explicit references and generated gameplay-scope registration.
- [x] 4.2 Add or update guardrails proving no `FindObject*`, broad `FindObjectsByType`, `Resources.Load`, Service Locator, or direct Unity debug logging is introduced.
- [x] 4.3 Run focused SceneComposition EditMode tests.
- [x] 4.4 Run focused M0/S4 smoke checks for input routing, combat loop, locomotion, enemy loop, memory prompt, accepted Interact, reveal feedback, runtime memory log, and duplicate Interact behavior.

## 5. Evidence And Closure

- [x] 5.1 Run Unity compile smoke and classify console output.
- [x] 5.2 Run focused EditMode tests and record results.
- [x] 5.3 Record inspector binding/manual assignment evidence.
- [x] 5.4 Record PlayMode or manual smoke evidence with PASS/PARTIAL/FAIL summary.
- [x] 5.5 Run `openspec validate extract-m0-scene-composition-registrar --strict`.
- [x] 5.6 Archive only after behavior-preserving evidence is complete.

## 6. Deferred Follow-ups

- [x] 6.1 Defer any gameplay truth refactor to separate approved changes.
- [x] 6.2 Defer R3/MessagePipe composition events until there is a concrete consumer.
- [x] 6.3 Defer scene/prefab hierarchy redesign.
- [x] 6.4 Defer broader LifetimeScope decomposition beyond this registrar slice.
