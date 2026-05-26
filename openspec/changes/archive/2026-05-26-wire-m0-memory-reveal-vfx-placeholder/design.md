## Context

M0 already has CombatCore, MemoryState skeleton, and Memory VFX presentation skeleton. Story 1-10 needs only the minimum integration to prove that a successful counter can produce a readable reveal response in the duel loop. Sprint pressure requires a narrow, closeable slice with evidence-first closure.

Current architectural constraints:
- Combat Core owns counter validity/result truth.
- MemoryState owns reveal acceptance and response lifecycle.
- Memory VFX is presentation-only and must never mutate gameplay state.
- Debug overlay remains read-only.

## Goals / Non-Goals

**Goals:**
- Provide a deterministic `successful counter -> RevealRequestContext` emission path.
- Ensure `MemoryState` transitions to `Responding` on accepted request and returns cleanly.
- Ensure `M0MemoryVFXResponse` reacts to accepted memory state (event/snapshot) with restrained placeholder VFX.
- Keep implementation minimal and verifiable via focused tests + PlayMode evidence.

**Non-Goals:**
- No reveal cinematic direction, animation polish, camera shake, or VFX polish.
- No new gameplay mechanics (stamina, buffs, progression, lore UI).
- No ownership shifts from domain to UI/presentation layers.

## Decisions

### 1) Combat emits reveal request context only on successful counter
**Decision:** Use existing CombatCore success path to emit/create `RevealRequestContext` only for accepted counter outcomes.
**Why:** Keeps reveal trigger aligned to combat truth and avoids speculative input/UI triggers.
**Alternative considered:** Overlay/input directly signaling reveal.
**Why rejected:** Violates ownership and creates false-positive reveal paths.

### 2) MemoryState remains single source of reveal acceptance truth
**Decision:** Memory acceptance/rejection and `Responding` timing remain inside MemoryState FSM.
**Why:** Domain state can be tested in EditMode and remains independent of presentation timing.
**Alternative considered:** VFX adapter deciding acceptance.
**Why rejected:** Presentation owning gameplay truth.

### 3) VFX response subscribes downstream to accepted memory signal
**Decision:** `M0MemoryVFXResponse` plays placeholder VFX from accepted memory state/event snapshot only.
**Why:** Maintains strict one-way data flow Domain -> Presentation.
**Alternative considered:** Combat directly triggering VFX object.
**Why rejected:** Tight coupling and bypass of MemoryState policy.

### 4) Evidence-first closure with readability classification
**Decision:** Require manual proof that reveal VFX is short/restrained and does not obscure enemy intent/readability.
**Why:** M0 outcome is player readability, not effect complexity.
**Alternative considered:** Test-only closure.
**Why rejected:** Visual readability cannot be proven by EditMode tests alone.

### 5) Define-gated evidence helper for unreliable manual counter timing
**Decision:** Allow a minimal `GR_M0_PROTOTYPE || GR_MEMORY_DEBUG` evidence helper to trigger the same reveal route when manual CounterWindow timing is not reliably reproducible.
**Why:** Story 1-10 is evidence-driven and manual counter timing in current M0 scene can be unstable for repeatable verification.
**Alternative considered:** Keep manual timing only.
**Why rejected:** High flake risk and non-repeatable evidence capture.
**Constraints:** Helper must route through CombatCore reveal emission and MemoryState acceptance; it must not directly start VFX or mutate gameplay truth.

## Risks / Trade-offs

- **[Risk] Counter opportunity is hard to reproduce consistently in manual runs**
  -> **Mitigation:** Keep evidence checklist explicit; allow repeated short smoke loops with logs and overlay snapshots.
- **[Risk] Placeholder VFX overdraw could obscure telegraph readability**
  -> **Mitigation:** Enforce restrained duration/intensity in acceptance criteria and evidence notes.
- **[Risk] Cross-system wiring leaks responsibility into GameplayTickHandler**
  -> **Mitigation:** TickHandler only forwards/coordinates signals; no new memory truth fields there.
- **[Risk] Existing animation warnings may appear during smoke**
  -> **Mitigation:** Classify known non-blocking warnings separately from hard gameplay errors.

## Migration Plan

1. Wire reveal request emission from successful counter path.
2. Wire memory acceptance path to responding lifecycle.
3. Wire VFX observer to accepted memory signal.
4. Add/update focused tests (Memory acceptance + response return).
5. Run manual PlayMode checklist and record evidence.
6. Close tasks by evidence status (PASS/PARTIAL/FAIL).

Rollback strategy:
- Revert wiring changes in combat-memory bridge and presentation observer files.
- Preserve existing combat and memory baseline behavior.

## Open Questions

- Should reveal cooldown use current MemoryState default timings or explicit authored M0 values in scene config?
- For M0 evidence, is LockOn required during counter->reveal capture or optional if counter proof is clear?
