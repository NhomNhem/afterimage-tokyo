## Context

S3-2 established the Memory Fragment interaction truth path and evidence:

`eligible fragment context -> Interact intent -> MemoryInteractionService -> MemoryState accepted/rejected outcome`

S3-3 adds a minimal UI affordance on top of that path. The prompt must improve player readability without becoming interaction authority. UI observes a read-only interaction eligibility/context surface and displays or hides placeholder text.

Key constraints:
- Presentation/UI must not own gameplay truth.
- Input remains raw intent only.
- `MemoryInteractionService` remains interaction orchestration owner.
- `MemoryState` remains reveal/collect truth owner.
- No `FindObjectOfType`, `Resources.Load`, service locator, or direct Unity debug logging.
- No full HUD, runtime memory log, reveal VFX/audio, inventory, save/profile, quest, dialogue, or progression scope.

## Goals / Non-Goals

**Goals:**
- Show a minimal prompt when a Memory Fragment is eligible for interaction.
- Hide the prompt when the fragment is no longer eligible.
- Keep prompt visibility downstream of S3-2 interaction eligibility/context.
- Preserve S3-2 interaction behavior and M0 combat behavior.
- Produce manual evidence for prompt appear/disappear behavior and ownership boundaries.

**Non-Goals:**
- Runtime memory log UI; S3-5 owns that.
- Reveal VFX/audio placeholder; S3-4 owns that.
- Interaction validity, duplicate handling, or MemoryState behavior changes.
- Input architecture refactor or Unity InputAction callback ownership changes.
- Broad UI Toolkit architecture refactor, final UI art, localization, or accessibility pass.

## Decisions

1. The prompt SHALL observe read-only interaction context rather than query or mutate gameplay services.
   - Rationale: keeps UI presentation-only and avoids truth drift into UI.
   - Alternative considered: prompt directly queries `MemoryInteractionService` or `MemoryState`; rejected because UI would become coupled to interaction/reveal authority.

2. Prompt text SHALL remain placeholder-level.
   - Rationale: Sprint 3 needs readability, not final UX polish.
   - Suggested text: `Interact` or `Press F to Interact`.
   - Alternative considered: authored localization-ready prompt copy; deferred to later UI polish/localization work.

3. The implementation MAY add a small UI-facing read model if existing context is not suitable.
   - Rationale: a read model can keep UI consumption stable without exposing command APIs.
   - Constraint: any read model must be downstream of S3-2 interaction eligibility and must not own eligibility truth.

4. Prompt evidence SHALL be manual-first.
   - Rationale: S3-3 is a UI placeholder story; Sprint 3 QA plan requires prompt visibility/behavior capture, not automated UI tests.
   - Evidence should include PASS/PARTIAL/FAIL classification for prompt visible, prompt hidden, ownership boundaries, console output, and dirty asset state.

## Risks / Trade-offs

- [Risk] UI starts deciding whether a fragment is interactable.
  - Mitigation: require read-only context and forbid UI calls into mutation/acceptance paths.

- [Risk] Prompt expands into full HUD or runtime log work.
  - Mitigation: keep runtime memory log in S3-5 and limit S3-3 to one placeholder affordance.

- [Risk] Prompt becomes misleading because S3-2 debug raycast follow-up is not aligned.
  - Mitigation: consume the same gameplay eligibility/read model used by the interaction path, not `MemoryRaycastProProbe` debug-only output.

- [Risk] Scene/UI wiring creates unintended dirty assets.
  - Mitigation: explicitly classify any intentional scene/prefab/UI asset edits in evidence.

## Migration Plan

1. Define the prompt visibility contract in spec.
2. Implement a minimal UI/presentation adapter or read-only prompt presenter.
3. Wire it to approved S3-2 interaction eligibility/context.
4. Capture prompt appear/disappear evidence and console classification.
5. Rollback by removing the prompt presenter/UI asset wiring; S3-2 interaction truth path remains unchanged.

## Open Questions

- Which existing UI surface should host the placeholder prompt: current debug/UI scene, a small UI Toolkit document, or an existing presentation adapter?
- Is an existing S3-2 eligibility snapshot sufficient, or should this change add a tiny UI-facing read model?
