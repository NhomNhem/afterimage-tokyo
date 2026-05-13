# Unity Version Decision

## Locked Engine Line

- **Project**: Glass Refrain
- **Engine Line**: Unity 6000.3.x
- **Language**: C#
- **Render Pipeline**: URP

## Current Phase

This is the documentation-only engine setup phase before OpenSpec `project-foundation`.

Not yet implemented:

- package installation changes
- asmdef creation
- scene creation
- prefab creation
- source code
- VContainer integration
- source-generator integration

## Foundation Decisions

- additive scene loading from day one
- `Bootstrap` / `Systems` / `Gameplay` / `Camera` / `UI` / `Level` scene separation
- M0 minimal additive scene set
- `ProjectRootLifetimeScope` via `VContainerSettings`
- root scope owns app lifetime only
- scene scopes own gameplay lifetime
- combat truth must never be registered globally

## DI Tooling Status

- `VContainer`: approved runtime DI container
- `NhemDangFugBixs.VContainer.SourceGenerator`: planned DI architecture guardrail
- official `VContainer.SourceGenerator`: optional later optimization only

## Knowledge Gap Warning

The LLM's training data likely covers Unity up to around 2022 LTS or early Unity 6-era material. Unity 6000.3.x and later package behavior should be validated against current docs before implementation-level guidance is treated as authoritative.

## Verified Sources

- Official docs: https://docs.unity3d.com/6000.0/Documentation/Manual/index.html
- Unity 6 support: https://unity.com/releases/unity-6/support
- Cinemachine manual: https://docs.unity3d.com/Packages/com.unity.cinemachine@3.1/manual/index.html
- Input System manual: https://docs.unity3d.com/Packages/com.unity.inputsystem@1.15/manual/index.html
