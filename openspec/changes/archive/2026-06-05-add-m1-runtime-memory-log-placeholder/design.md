## Context

S3-2 established the Memory Fragment interaction truth path:

`eligible fragment context -> Interact intent -> MemoryInteractionService -> MemoryState accepted/rejected outcome`

S3-3 added a read-only interaction prompt placeholder. S3-4 added restrained accepted reveal feedback. S4-2 adds a small runtime memory log placeholder after the same accepted reveal/collect path so testers can see one durable-but-placeholder entry for the revealed fragment.

This change should consume existing accepted interaction/reveal context or memory response state instead of introducing a second truth source. The runtime log is presentation/read-model state only. It can remember which accepted fragment outcomes it has already displayed so the UI does not duplicate entries, but it must not decide whether a fragment is valid, revealed, collected, or accepted.

Key constraints:
- `MemoryState` remains reveal/collect truth owner.
- `MemoryInteractionService` remains interaction orchestration owner.
- Input remains raw intent only.
- UI must not infer, repair, or mutate gameplay truth.
- Runtime log scope remains placeholder-only, not a full journal/progression system.
- No `FindObjectOfType`, `Resources.Load`, service locator, or direct Unity debug logging.

## Goals / Non-Goals

**Goals:**
- Append one visible runtime memory log entry after an accepted Memory Fragment reveal/collect outcome.
- Suppress duplicate entries for the same accepted fragment outcome.
- Keep runtime log state downstream of MemoryState-backed accepted context.
- Preserve S3-2 interaction behavior, S3-3 prompt behavior, and S3-4 reveal feedback behavior.
- Add focused EditMode tests for read-only log behavior, duplicate suppression, and ownership guardrails.
- Produce manual PlayMode evidence for `prompt -> Interact -> reveal feedback -> runtime log`.

**Non-Goals:**
- MemoryState behavior changes.
- MemoryInteractionService command-path changes.
- Input architecture changes.
- S3-3 prompt changes.
- S3-4 reveal feedback changes.
- Full journal, inventory, quest, lore, codex, save/profile, progression UI, dialogue, narrative memory graph, clue tracking, contradiction tracking, or district reinterpretation.
- MemoryInteractionTickBridge extraction.
- MemoryRaycastProProbe alignment.
- R3/MessagePipe migration.
- Broad Nhem DI migration.

## Decisions

1. Runtime log SHALL observe accepted memory interaction/reveal context only.
   - Rationale: accepted context is already downstream of `MemoryInteractionService` and `MemoryState`; the log should react to it instead of rechecking truth.
   - Alternative considered: the log directly queries fragments or MemoryState. Rejected because UI would risk becoming gameplay authority.

2. Runtime log SHALL own only presentation deduplication.
   - Rationale: the UI needs to avoid duplicate visible entries when snapshots repeat or Interact is spammed after collection. This is display deduplication, not interaction duplicate handling.
   - Alternative considered: rely on upstream systems only and append whenever an accepted snapshot is observed. Rejected because repeated observation could create duplicate UI entries without changing gameplay truth.

3. Log entries SHALL stay minimal and placeholder-safe.
   - Rationale: Sprint 4 needs readability, not final journal design.
   - Suggested entry shape: fragment label or fallback ID plus a short state such as `Revealed` or `Collected`.
   - Alternative considered: final lore text, journal grouping, timestamps, filters, persistence, or progression links. Deferred to later UI/narrative scope.

4. The implementation MAY use the existing debug overlay/runtime UI surface if it keeps scope smaller.
   - Rationale: S3-3/S3-4 already use placeholder UI surfaces and debug evidence patterns.
   - Constraint: whichever surface is used must remain presentation-only and all UI asset/scene edits must be classified in evidence.

5. Evidence SHALL include both automated guardrails and manual PlayMode confirmation.
   - Rationale: this is UI behavior with ownership risks. EditMode tests should cover model/bridge behavior and source guardrails; manual PlayMode should prove the visible loop.

## Risks / Trade-offs

- [Risk] Runtime log becomes a full journal/progression system.
  - Mitigation: keep entry content minimal and explicitly forbid save/profile, lore database, progression, quest, and inventory behavior.

- [Risk] UI starts deciding reveal acceptance.
  - Mitigation: require read-only accepted context and guardrail tests/source checks against MemoryState mutation and interaction command calls.

- [Risk] Duplicate suppression accidentally becomes gameplay duplicate handling.
  - Mitigation: define deduplication as presentation-only by accepted fragment/outcome identity; upstream systems still own duplicate/rejected behavior.

- [Risk] Log append timing diverges from reveal feedback timing.
  - Mitigation: drive from accepted interaction/reveal context and manually verify prompt -> Interact -> reveal feedback -> runtime log ordering.

- [Risk] UI Toolkit or scene wiring dirties unintended assets.
  - Mitigation: classify every scene/prefab/UI asset edit in the evidence file; keep implementation code-first where practical.

## Migration Plan

1. Define the runtime memory log placeholder contract in spec.
2. Identify the existing accepted interaction/reveal context or response snapshot to observe.
3. Implement a narrow read-model/log component that appends and deduplicates placeholder entries.
4. Wire the minimal UI presentation surface to the read-model/log snapshot.
5. Preserve S3-2/S3-3/S3-4 behavior and avoid changing truth owners.
6. Add focused EditMode tests and source guardrails.
7. Capture manual PlayMode evidence and console/dirty asset classification.
8. Roll back by disabling/removing the runtime log presenter/read-model; S3-2, S3-3, and S3-4 behavior should remain intact.

## Open Questions

- Which exact existing accepted context is smallest to observe: `MemoryInteractionSnapshot`, `M0MemoryVFXResponse` snapshot, or a new UI-facing read-only bridge?
- Should the placeholder live in the existing combat debug overlay surface or a separate lightweight runtime UI document?
- What fallback label should be used when fragment display data is missing?
