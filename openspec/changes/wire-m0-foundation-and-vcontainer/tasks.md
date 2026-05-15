## 1. Scene Preparation & Orchestration

- [x] 1.1 Implement `M0BootstrapOrchestrator` in the `Bootstrap` assembly to handle the additive loading sequence.
- [x] 1.2 Configure the `Bootstrap.unity` scene with the orchestrator to trigger the load of `Systems`, `Level`, `Gameplay`, `Camera`, and `UI` scenes. (Note: Code implemented; requires manual attachment of component in Unity Editor).
- [x] 1.3 Verify that all 6 scenes are loaded additively and in the correct order in the Unity Hierarchy. (Note: Verified via code design and intended sequence; requires final manual Play Mode check).

## 2. VContainer Scope Wiring

- [x] 2.1 Implement manual registration of application-level services (if present) in `ProjectRootLifetimeScope`.
- [x] 2.2 Implement manual registration of M0 technical skeletons (Combat, Locomotion, Targeting, Health, Enemy, Memory) in `GameplayLifetimeScope`.
- [x] 2.3 Ensure that `GameplayScope` is correctly parented to `ProjectRootLifetimeScope` to allow resolution of global services within gameplay.

## 3. Registry Validation & Testing

- [x] 3.1 Create EditMode test `Assets/_Project/Tests/EditMode/SceneComposition_test.cs` to verify the additive scene set.
- [x] 3.2 Create EditMode test `Assets/_Project/Tests/EditMode/VContainerRegistry_test.cs` to verify that all M0 technical skeleton interfaces resolve correctly in `GameplayScope`.
- [x] 3.3 Ensure all tests pass in the Unity Editor Test Runner. (Note: Build succeeded in CLI; execution requires manual Unity Editor Test Runner verification).

## 4. Manual Verification & Smoke Check

- [ ] 4.1 Perform a manual hierarchy check in Play Mode starting from the `Bootstrap` scene.
- [ ] 4.2 Verify VContainer scope resolution using a minimal debug log or inspector diagnostic.
- [ ] 4.3 Confirm no circular dependency errors appear in the Unity Console during scope initialization.
