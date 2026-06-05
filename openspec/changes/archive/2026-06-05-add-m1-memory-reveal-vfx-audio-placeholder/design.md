## Context

S3-2 established the Memory Fragment interaction truth path:

`eligible fragment context -> Interact intent -> MemoryInteractionService -> MemoryState accepted/rejected outcome`

S3-3 added a read-only interaction prompt placeholder on top of that path. S3-4 adds the next downstream readability layer: restrained placeholder feedback after an accepted reveal/collect outcome.

The project already has a memory VFX response model and snapshot surface:
- `M0MemoryVFXResponse`
- `IMemoryVFXResponseSnapshot`
- `MemoryVFXResponseState`
- accepted reveal context types

This change should consume that existing memory VFX response state/context instead of introducing a second truth source.

Key constraints:
- `MemoryState` remains reveal/collect truth owner.
- `MemoryInteractionService` remains S3-2 interaction orchestration owner.
- Presentation/VFX/Audio must not infer reveal validity or mutate memory state.
- No broad UI/VFX/audio framework or final asset pass.
- No `FindObjectOfType`, `Resources.Load`, service locator, or direct Unity debug logging.

## Goals / Non-Goals

**Goals:**
- Play a minimal placeholder visual and/or audio response after an accepted Memory Fragment reveal/collect outcome.
- Keep reveal feedback downstream of `MemoryState` acceptance and `M0MemoryVFXResponse` response state.
- Ensure rejected, duplicate, ignored, or unavailable interactions do not trigger reveal feedback.
- Preserve S3-2 interaction behavior and S3-3 prompt behavior.
- Produce evidence for accepted feedback, non-playback cases, ownership boundaries, console classification, and dirty asset classification.

**Non-Goals:**
- MemoryState behavior changes.
- MemoryInteractionService command-path changes.
- CombatCore timing/result changes.
- Input architecture changes.
- Runtime memory log UI; S3-5 owns that.
- Final authored VFX/audio polish, cinematic timing, mix/bus work, localization, or accessibility pass.
- Full inventory, quest, dialogue, save/profile, progression, or narrative memory graph.

## Decisions

1. Reveal feedback SHALL observe accepted reveal response state/context only.
   - Rationale: `MemoryState` and `M0MemoryVFXResponse` already encode accepted/rejected/ignored response state. Presentation should react to that state, not recreate acceptance logic.
   - Alternative considered: feedback component directly checks fragments or MemoryState request fields. Rejected because it risks presentation-owned gameplay truth.

2. Placeholder feedback SHALL be restrained and replaceable.
   - Rationale: Sprint 3 needs readability, not final mood polish. A small pulse, temporary tint, simple particle, or short placeholder audio cue is enough if it proves the loop.
   - Alternative considered: full authored reveal sequence. Deferred to later presentation polish.

3. Non-accepted interactions SHALL be evidence-visible but not play reveal feedback.
   - Rationale: Rejections, duplicate ignores, cooldown gates, and unavailable interactions should help debug the loop without misleading players.
   - Alternative considered: playing error feedback for every rejection. Deferred because S3-4 is accepted reveal feedback, not a full feedback taxonomy.

4. Scene/prefab changes MAY be used only for minimal placeholder wiring.
   - Rationale: Visual/audio playback may need references to a particle, renderer, AudioSource, or UI/VFX object.
   - Constraint: all scene/prefab/UI/audio/VFX asset edits must be classified in evidence as intentional or unintentional.

## Risks / Trade-offs

- [Risk] Presentation starts deciding reveal acceptance.
  - Mitigation: require read-only accepted response context and guardrail tests/source checks against MemoryState mutation or command-path calls.

- [Risk] Placeholder expands into final VFX/audio production.
  - Mitigation: keep scope to minimal visual/audio cue and evidence readability only.

- [Risk] Duplicate/rejected interactions accidentally retrigger feedback.
  - Mitigation: require scenarios and tests/evidence showing rejected/duplicate/ignored states do not play accepted feedback.

- [Risk] Audio/VFX wiring creates unintended dirty assets.
  - Mitigation: classify all scene/prefab/UI/VFX/audio asset edits in evidence before closure.

## Migration Plan

1. Define the reveal feedback placeholder contract in spec.
2. Identify the existing accepted reveal response snapshot/context to observe.
3. Implement a narrow presentation adapter or bridge that plays placeholder feedback from accepted response state.
4. Preserve S3-2/S3-3 behavior and avoid changing truth owners.
5. Capture automated/source guardrails and manual PlayMode evidence.
6. Rollback by disabling/removing the placeholder feedback adapter/wiring; S3-2 and S3-3 behavior should remain intact.

## Open Questions

- Should the first placeholder be visual-only, audio-only, or both if existing authoring references are missing?
- Which existing scene object should host the placeholder response: memory fragment object, debug overlay/presentation object, or a dedicated lightweight VFX response adapter?
- Should accepted reveal feedback be driven directly by `M0MemoryVFXResponse.Snapshot.State == Playing`, or by a higher-level presentation bridge to avoid duplicate playback?
