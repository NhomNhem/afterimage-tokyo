## 1. Baseline And Scope Guard

- [x] 1.1 Confirm the working tree only contains approved pre-existing changes before implementation.
- [x] 1.2 Capture current `GameplayLifetimeScope` memory runtime hardcoded values and registration order.
- [x] 1.3 Run focused baseline SceneComposition and memory/runtime-log EditMode tests.
- [x] 1.4 Confirm the custom `GameplayLifetimeScope` inspector currently exposes config and memory reference fields.

## 2. Memory Runtime Tuning Config

- [x] 2.1 Add `M0MemoryRuntimeTuningConfig` ScriptableObject with authored static tuning fields.
- [x] 2.2 Provide behavior-preserving defaults: `M0RevealCandidate`, `0.25f` reveal duration, `0f` cooldown, and `standard` intensity label.
- [x] 2.3 Add validation or conversion methods that keep runtime service construction explicit and testable.
- [x] 2.4 Create the default config asset under the project data/content hierarchy.
- [x] 2.5 Ensure the config stores no runtime collected/revealed/accepted/rejected/duplicate/playback state.

## 3. Gameplay Scope Composition

- [x] 3.1 Add an explicit serialized memory runtime tuning config reference to `GameplayLifetimeScope`.
- [x] 3.2 Replace inline `M0MemoryState("M0RevealCandidate")` construction with config-derived composition.
- [x] 3.3 Replace inline `M0MemoryVFXResponse(0.25f, 0f, "standard")` construction with config-derived composition.
- [x] 3.4 Fail clearly when the config is missing, without broad lookup or fallback loading.
- [x] 3.5 Preserve generated NhemDI gameplay-scope registration and the existing scene composition registrar boundary.

## 4. Inspector And Scene Assignment

- [x] 4.1 Preserve the `GameplayLifetimeScope` UI Toolkit inspector layout and serialized binding.
- [x] 4.2 Ensure the new memory runtime tuning config field is visible and assignable.
- [x] 4.3 Assign the default config asset in the gameplay scene if implementation requires scene serialization.
- [x] 4.4 Record any scene or asset changes explicitly in evidence.

## 5. Tests And Guardrails

- [x] 5.1 Add or update tests proving the config exposes current default tuning values.
- [x] 5.2 Add or update tests proving `GameplayLifetimeScope` composes memory services from the config.
- [x] 5.3 Add or update guardrails proving no `FindObject*`, broad `FindObjectsByType`, `Resources.Load`, Service Locator, or direct Unity debug logging is introduced.
- [x] 5.4 Run focused SceneComposition EditMode tests.
- [x] 5.5 Run focused memory interaction and runtime memory log EditMode tests.
- [x] 5.6 Run focused M0/S4 PlayMode or manual smoke checks for eligible prompt, accepted Interact, reveal feedback once, runtime log append once, and duplicate/spam safety.

## 6. Evidence And Closure

- [x] 6.1 Run Unity compile smoke and classify console output.
- [x] 6.2 Record PASS/PARTIAL/FAIL evidence for automated tests, smoke/manual checks, inspector binding, and dirty asset classification.
- [x] 6.3 Run `openspec validate externalize-m0-memory-runtime-tuning-to-scriptableobject --strict`.
- [x] 6.4 Archive only after behavior-preserving evidence is complete and approved.

## 7. Deferred Follow-ups

- [x] 7.1 Defer MemoryState behavior refactor to a separate approved change.
- [x] 7.2 Defer prompt/log/VFX tuning expansion until there is a concrete duplicated tuning need.
- [x] 7.3 Defer R3/MessagePipe integration and broader NhemDI migration.
- [x] 7.4 Defer CombatCore, PlayerLocomotion, EnemyIntent, TargetContext, and input architecture changes.
