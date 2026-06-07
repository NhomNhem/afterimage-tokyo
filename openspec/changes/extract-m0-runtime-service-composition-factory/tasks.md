## 1. Baseline And Scope Guard

- [x] 1.1 Confirm the working tree is clean before implementation.
- [x] 1.2 Capture current `GameplayLifetimeScope` runtime service registration block and lifetimes.
- [x] 1.3 Run focused baseline SceneComposition EditMode tests.
- [x] 1.4 Run focused baseline M0 combat/locomotion/input/enemy intent and memory/runtime-log EditMode tests.

## 2. Runtime Service Composition Collaborator

- [x] 2.1 Add a Bootstrap-owned runtime service composition registrar/collaborator.
- [x] 2.2 Move `M0CombatCore` manual factory registration into the collaborator without changing lifetime or exposed service types.
- [x] 2.3 Move `M0PlayerLocomotion` manual factory registration into the collaborator without changing lifetime or exposed service types.
- [x] 2.4 Move `M0MemoryState` manual factory registration into the collaborator without changing lifetime or exposed service types.
- [x] 2.5 Move `M0MemoryVFXResponse` manual factory registration into the collaborator without changing lifetime or exposed service types.
- [x] 2.6 Keep logger registration and generated NhemDI gameplay-scope registration in `GameplayLifetimeScope`.

## 3. Config Validation And Composition Order

- [x] 3.1 Preserve explicit validation for `M0CombatTimingConfig`.
- [x] 3.2 Preserve explicit validation for `M0LocomotionConfig`.
- [x] 3.3 Preserve explicit validation for `M0MemoryRuntimeTuningConfig`.
- [x] 3.4 Ensure `GameplayLifetimeScope.Configure` reads as high-level composition order.
- [x] 3.5 Keep scene component registration/wiring delegated to `M0SceneCompositionRegistrar`.

## 4. Tests And Guardrails

- [x] 4.1 Add or update source composition tests proving runtime service registrations moved to the collaborator.
- [x] 4.2 Add or update tests proving lifetimes and `.As<T>()` registration intent remain equivalent.
- [x] 4.3 Add or update guardrails proving no `FindObject*`, broad `FindObjectsByType`, `Resources.Load`, Service Locator, or direct Unity debug logging is introduced.
- [x] 4.4 Add or update guardrails proving the collaborator does not call gameplay command APIs such as combat request, locomotion input consumption, memory interaction commands, or presentation playback authority.
- [x] 4.5 Run focused SceneComposition EditMode tests.

## 5. Regression And Evidence

- [x] 5.1 Run Unity compile smoke and classify console output.
- [x] 5.2 Run focused M0 input/combat/locomotion/enemy intent EditMode tests.
- [x] 5.3 Run focused memory interaction, memory VFX response, and runtime memory log EditMode tests.
- [x] 5.4 Run PlayMode or manual smoke for eligible prompt, accepted Interact, reveal feedback once, runtime log append once, and duplicate/spam safety.
- [x] 5.5 Record evidence with PASS/PARTIAL/FAIL summary and dirty asset classification.
- [x] 5.6 Run `openspec validate extract-m0-runtime-service-composition-factory --strict`.

## 6. Deferred Follow-ups

- [x] 6.1 Defer CombatCore state-machine decomposition to a separate approved change.
- [x] 6.2 Defer generated NhemDI migration for config-backed special-case factories.
- [x] 6.3 Defer R3/MessagePipe composition events until there is a concrete consumer.
- [x] 6.4 Defer further `GameplayLifetimeScope` inspector redesign.
