## Why

Sprint 3 needs the Memory Fragment interaction loop to be readable before adding broader UI or presentation polish. S3-2 proves the interaction truth path, but the player still needs a minimal prompt that communicates when a fragment can be interacted with.

## What Changes

- Add a placeholder interaction prompt that appears when the player has an eligible Memory Fragment interaction context.
- Hide the prompt when no eligible fragment is available.
- Keep the prompt strictly presentation-only:
  - no reveal/collect truth ownership,
  - no direct interaction mutation,
  - no input callback ownership,
  - no inventory/journal/progression behavior.
- Use an approved read-only interaction context or UI-facing read model derived from the S3-2 interaction path.
- Add evidence expectations for prompt appear/disappear behavior, ownership boundaries, console classification, and dirty asset classification.

## Non-goals

- No runtime memory log UI; that remains S3-5.
- No reveal VFX/audio placeholder; that remains S3-4.
- No changes to S3-2 interaction validity, duplicate handling, or MemoryState truth.
- No full HUD, final UI art, localization, accessibility pass, dialogue, quest, inventory, save/profile, or progression systems.
- No broad UI Toolkit architecture refactor.
- No CombatCore, EnemyIntent, TargetContext, Camera, or input architecture refactor.

## Capabilities

### New Capabilities
- `interaction-prompt-placeholder`: Player sees a minimal prompt when a Memory Fragment is eligible for interaction, while UI remains downstream of gameplay truth.

### Modified Capabilities
- None.

## Impact

- Affected systems:
  - UI / Presentation placeholder surface
  - Read-only interaction eligibility/context consumption
  - Debug/evidence capture for prompt visibility
- Dependencies:
  - S3-2 Memory Fragment interaction path and evidence
  - Existing UI/presentation conventions in the Unity project
- M0/M1 loop impact:
  - Improves readability for `approach -> interact` without changing interaction truth.
  - Does not change M0 combat loop behavior.
- Ownership boundary affected:
  - Presentation/UI observes interaction eligibility but must not own or mutate `MemoryState`, `MemoryInteractionService`, input callbacks, or fragment runtime truth.
