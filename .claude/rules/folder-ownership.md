# Folder Ownership Rules — Glass Refrain

## Purpose

These rules define what belongs in each folder and which dependencies are allowed. The goal is to prevent gameplay truth, presentation, Unity adapters, and bootstrap code from mixing into god scripts.

## Recommended Root Structure

```txt
Assets/_Project/Code/
├─ Domain/
├─ Application/
├─ Infrastructure/
├─ Presentation/
├─ Bootstrap/
└─ Editor/
```

## Domain Folder

Path:

```txt
Assets/_Project/Code/Domain/
```

Purpose:

- pure gameplay concepts
- state enums
- request/result structs
- value objects
- domain rules without Unity scene dependency

Allowed examples:

```txt
Domain/Combat/CombatState.cs
Domain/Combat/CombatRequest.cs
Domain/Combat/CombatResult.cs
Domain/Health/DamageRequest.cs
Domain/Targeting/TargetContextSnapshot.cs
```

Forbidden in Domain:

```txt
MonoBehaviour
GameObject
Transform
Animator
Cinemachine
SerializedMonoBehaviour
```

Domain code should be easy to unit test.

## Application Folder

Path:

```txt
Assets/_Project/Code/Application/
```

Purpose:

- use-case services
- gameplay orchestration
- state machines
- system coordination

Allowed examples:

```txt
Application/Combat/CombatCoreService.cs
Application/Locomotion/PlayerLocomotionService.cs
Application/Encounter/EncounterLifecycleService.cs
Application/Memory/MemoryRevealService.cs
```

Application can depend on Domain.

Application should not directly own Unity presentation.

Avoid direct dependency on:

```txt
Animator
CinemachineCamera
VisualElement
ParticleSystem
GameObject scene wiring
```

## Infrastructure Folder

Path:

```txt
Assets/_Project/Code/Infrastructure/
```

Purpose:

- external package implementations
- Unity package adapters
- input system adapter
- time provider
- persistence later
- Addressables later
- VContainer composition helpers if not in Bootstrap

Allowed examples:

```txt
Infrastructure/Input/UnityInputReader.cs
Infrastructure/Time/UnityTimeProvider.cs
Infrastructure/DI/GameplayInstaller.cs
```

Infrastructure can reference Unity APIs and packages.

Infrastructure should adapt external systems to project-owned interfaces.

## Presentation Folder

Path:

```txt
Assets/_Project/Code/Presentation/
```

Purpose:

- MonoBehaviour views
- Animator presenters
- Camera presenters
- VFX presenters
- UI Toolkit views
- Debug overlay views

Allowed examples:

```txt
Presentation/Combat/CombatAnimatorPresenter.cs
Presentation/Camera/CombatCameraPresenter.cs
Presentation/Debug/DebugOverlayView.cs
Presentation/VFX/MemoryVfxPresenter.cs
```

Presentation observes Application/Domain state.

Presentation must not own gameplay truth.

## Bootstrap Folder

Path:

```txt
Assets/_Project/Code/Bootstrap/
```

Purpose:

- LifetimeScope
- scene composition
- root setup
- composition entry points

Allowed examples:

```txt
Bootstrap/ProjectRootLifetimeScope.cs
Bootstrap/GameplayLifetimeScope.cs
Bootstrap/SceneCompositionRoot.cs
```

Bootstrap should not contain gameplay logic.

Bad:

```csharp
protected override void Configure(IContainerBuilder builder)
{
    // 200 lines of combat logic
}
```

Good:

```csharp
protected override void Configure(IContainerBuilder builder)
{
    builder.Register<ICombatCoreService, CombatCoreService>(Lifetime.Scoped);
}
```

## Editor Folder

Path:

```txt
Assets/_Project/Code/Editor/
```

Purpose:

- Unity editor tools
- custom inspectors
- validation tools
- editor-only test helpers

Editor code must not be included in runtime assemblies.

## Tests Folder

Recommended:

```txt
Assets/_Project/Tests/EditMode/
Assets/_Project/Tests/PlayMode/
```

or package-style:

```txt
Tests/Editor/
Tests/Runtime/
```

EditMode tests should cover:

- pure domain rules
- combat state transition rules
- damage resolver
- target context validation
- memory reveal acceptance/rejection

PlayMode tests should cover:

- Unity scene composition
- VContainer resolution
- MonoBehaviour adapters
- input/camera/debug integration

## Folder Dependency Direction

Recommended dependency direction:

```txt
Presentation → Application → Domain
Infrastructure → Application/Domain
Bootstrap → all composition targets
Domain → nothing project-external
```

Forbidden dependency direction:

```txt
Domain → Presentation
Domain → Infrastructure
Application → Presentation
Application → concrete scene MonoBehaviours
```

## Assembly Definition Rule

When assembly definitions are added, keep boundaries explicit.

Recommended assemblies:

```txt
GlassRefrain.Domain
GlassRefrain.Application
GlassRefrain.Infrastructure
GlassRefrain.Presentation
GlassRefrain.Bootstrap
GlassRefrain.Editor
GlassRefrain.Tests.EditMode
GlassRefrain.Tests.PlayMode
```

Domain should have the fewest dependencies.
