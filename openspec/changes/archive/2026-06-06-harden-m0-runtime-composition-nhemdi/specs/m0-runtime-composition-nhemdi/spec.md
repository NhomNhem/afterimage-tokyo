# m0-runtime-composition-nhemdi Specification

## Purpose

Harden M0 runtime dependency composition by making scene-provided participants explicit, keeping gameplay services registered through NhemDI where possible, and removing broad Unity scene discovery fallback behavior from owned runtime composition code.

## ADDED Requirements

### Requirement: Gameplay runtime services SHALL prefer NhemDI registration

Pure and runtime-scoped gameplay services that do not require Unity scene instance construction MUST use NhemDI registration in the gameplay lifetime scope.

#### Scenario: Pure gameplay service registration remains generated
- **WHEN** a pure/runtime gameplay service is part of the M0 gameplay scope
- **THEN** it is registered through NhemDI attributes or generated gameplay-scope registration
- **AND** it is not manually registered in `GameplayLifetimeScope` unless a documented special case requires it

### Requirement: GameplayLifetimeScope SHALL not perform broad scene discovery fallback

Owned runtime composition code MUST NOT use broad Unity scene discovery or resource lookup APIs to find gameplay participants during normal composition.

Forbidden owned runtime composition APIs include:

- `FindObjectOfType`
- `FindFirstObjectByType`
- `FindAnyObjectByType`
- broad `FindObjectsByType`
- `Resources.Load`
- Service Locator lookup patterns

#### Scenario: Runtime composition avoids broad search APIs
- **WHEN** gameplay scope composition runs
- **THEN** owned runtime composition code uses explicit references, generated registration, or narrow scene adapters/providers
- **AND** it does not call broad Unity object search or resource lookup APIs

### Requirement: Scene-provided memory participants SHALL use an explicit composition boundary

Memory scene participants such as memory probes and memory fragments MUST be supplied through an explicit scene composition boundary rather than discovered through broad bootstrap searches.

#### Scenario: Memory participants are explicitly composed
- **WHEN** the memory interaction path requires scene-provided participants
- **THEN** those participants are supplied by explicit scene references, a narrow scene adapter, or a narrow provider
- **AND** `GameplayLifetimeScope` does not discover them by broad scene search

### Requirement: Composition boundary SHALL not own gameplay truth

Scene composition adapters/providers MUST only bridge Unity scene references into runtime composition. They MUST NOT own gameplay truth or gameplay decisions.

#### Scenario: Memory truth ownership remains unchanged
- **WHEN** a memory scene participant is composed into runtime services
- **THEN** `MemoryState` remains reveal/collect truth owner
- **AND** `MemoryInteractionService` remains interaction orchestration owner
- **AND** the composition boundary does not decide prompt eligibility, reveal acceptance, collect state, duplicate interaction policy, or reveal feedback replay policy

### Requirement: Missing composition SHALL be diagnosable without direct Unity Debug logging

Missing or invalid scene composition MUST be surfaced through existing project logging or validation mechanisms, not direct `UnityEngine.Debug` calls in owned runtime code.

#### Scenario: Missing scene reference is visible
- **WHEN** a required scene participant is missing from explicit composition
- **THEN** the setup issue is diagnosable through project logger output, validation result, or a focused test
- **AND** owned runtime code does not add direct `UnityEngine.Debug.Log`, `Debug.LogWarning`, or `Debug.LogError` calls

### Requirement: M0/M1 memory loop behavior SHALL be preserved

The refactor MUST preserve verified M0/M1 memory loop behavior.

#### Scenario: Memory loop parity is preserved
- **WHEN** the player approaches an eligible memory fragment and presses Interact
- **THEN** the eligible prompt behavior remains equivalent
- **AND** `Interact -> MemoryInteractionService -> MemoryState` accepted path remains equivalent
- **AND** reveal feedback appears once
- **AND** runtime memory log appends the expected single entry
- **AND** duplicate/spam Interact behavior remains equivalent to baseline

### Requirement: Verification evidence SHALL cover compile, guardrails, regressions, and manual PlayMode

The change MUST include evidence proving the composition refactor is behavior-preserving and architecture-compliant.

#### Scenario: Evidence package is complete
- **WHEN** the change is ready for closure
- **THEN** compile evidence is recorded
- **AND** focused composition guardrail tests are recorded
- **AND** focused memory path parity tests are recorded
- **AND** M0 regression checks are recorded
- **AND** manual PlayMode memory checklist is recorded
- **AND** console classification and PASS/PARTIAL/FAIL summary are recorded

## Definition of Done

- No owned runtime composition search fallback remains in the hardened M0/M1 path.
- NhemDI remains the preferred registration path for pure/runtime gameplay services.
- Any manual registration is limited to explicit Unity scene instances or documented special cases.
- MemoryState, MemoryInteractionService, CombatCore, Input, Locomotion, TargetContext, UI/VFX/Animancer ownership boundaries remain unchanged.
- Compile, focused tests, M0 regression, manual PlayMode, console classification, and OpenSpec strict validation are all recorded.
