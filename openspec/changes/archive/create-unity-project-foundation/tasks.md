## 1. Project Structure

- [x] 1.1 Create the authored `Assets/_Project` root structure for code, content, data, and tests
- [x] 1.2 Create the M0-specific code folder layout for bootstrap, input, locomotion, combat, enemy, targeting, camera, health, memory, encounter, VFX, and UI
- [x] 1.3 Create the content/data/test folder layout needed by the approved M0 architecture

## 2. Assembly Boundaries

- [x] 2.1 Create the minimal M0 asmdef set defined by the architecture
- [x] 2.2 Configure asmdef references to enforce the approved dependency direction
- [x] 2.3 Add test asmdefs for EditMode and PlayMode architecture verification

## 3. Scene Foundation

- [x] 3.1 Create or reserve the additive M0 scene set for Bootstrap, Systems, Gameplay_CombatPrototype, Camera_CombatPrototype, UI_DebugOverlay, and Level_TokyoStreet_Blockout
- [x] 3.2 Represent scene ownership boundaries so level, gameplay, camera, and UI responsibilities stay separated
- [x] 3.3 Represent the minimal additive composition path used by the M0 prototype

## 4. Dependency Injection Foundation

- [x] 4.1 Scaffold `ProjectRootLifetimeScope` for app-level composition only
- [x] 4.2 Scaffold gameplay-scoped composition for duel-state systems
- [x] 4.3 Scaffold camera and UI/debug scope boundaries so they remain downstream of gameplay truth

## 5. Input Foundation

- [x] 5.1 Create the Unity New Input System asset structure for M0 gameplay actions
- [x] 5.2 Represent generated input-code flow and input-routing boundaries for the `Input Mapping` system
- [x] 5.3 Verify no legacy Unity Input Manager path is introduced

## 6. Core Contracts

- [x] 6.1 Create the shared core contract/DTO layer for cross-system communication
- [x] 6.2 Define the action lock / recovery exchange contracts between `Combat Core` and `Player Locomotion`
- [x] 6.3 Define the read-only camera-relative movement basis contract
- [x] 6.4 Define target, health, memory, encounter, and debug snapshot contracts required by M0

## 7. Debug And Test Foundation

- [x] 7.1 Represent the read-only `Debug Overlay` snapshot/event structure
- [x] 7.2 Create EditMode test scaffolding for Pure C# contracts and architecture boundary checks
- [x] 7.3 Create PlayMode test scaffolding for additive scene composition and DI smoke checks

## 8. Guardrails And Verification

- [x] 8.1 Encode guardrails that keep gameplay truth out of Animator, camera, UI, and VFX layers
- [x] 8.2 Verify the foundation matches the approved M0 architecture and GDD ownership boundaries
- [x] 8.3 Verify the change satisfies the OpenSpec acceptance requirements for Unity project foundation
