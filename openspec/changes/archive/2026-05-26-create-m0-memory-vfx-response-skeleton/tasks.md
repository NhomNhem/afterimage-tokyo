## 1. Contracts and Type Definitions

- [x] 1.1 Add MemoryVFXResponseState enum (Idle, Requested, Playing, CoolingDown, RejectedOrIgnored) to M0Contracts.cs
- [x] 1.2 Define IAcceptedMemoryRevealContext contract in M0Contracts.cs for upstream Memory State context
- [x] 1.3 Define IMemoryVFXResponseSnapshot read-only interface in M0Contracts.cs
- [x] 1.4 Add common rejection reason constants (generic_hit, failed_dodge, failed_parry, presentation_only, in_cooldown, already_playing, not_accepted_by_memory_state)

## 2. Core State Model Implementation

- [x] 2.1 Create M0MemoryVFXResponse.cs as pure C# state model with no dependencies on Animator, VFX Graph, or scene components
- [x] 2.2 Implement state property with getter and private setter
- [x] 2.3 Implement constructor that accepts optional duration, cooldownDuration, and intensityLabel parameters
- [x] 2.4 Implement OnAcceptedReveal(IAcceptedMemoryRevealContext context) method: transitions Idle → Requested, stores context
- [x] 2.5 Implement OnPlaybackStarted() method: transitions Requested → Playing, captures frame time
- [x] 2.6 Implement OnPlaybackComplete() method: transitions Playing → CoolingDown (if cooldown > 0) or directly to Idle (if cooldown == 0)
- [x] 2.7 Implement OnRejectRequest(string reason) method: transitions any state → RejectedOrIgnored, stores reason
- [x] 2.8 Implement Update(float deltaTime) method: advances cooldown timer, transitions CoolingDown → Idle when expired
- [x] 2.9 Implement OnReset() method: clears all state and timers, returns to Idle

## 3. Observer Snapshot Implementation

- [x] 3.1 Implement IMemoryVFXResponseSnapshot with properties: State, SourceAcceptedContext, RejectionReason, CooldownProgress, IntensityLabel
- [x] 3.2 Create immutable snapshot implementation that holds copies of current state data at snapshot time
- [x] 3.3 Implement GetSnapshot() method that returns current snapshot copy
- [x] 3.4 Ensure snapshot properties return null/0 appropriately when data is not available (e.g., SourceAcceptedContext when not in Requested/Playing)
- [x] 3.5 Verify CooldownProgress calculates 0.0-1.0 normalized value based on elapsed time and cooldown duration

## 4. State Transition Validation

- [x] 4.1 Implement state guard logic: OnPlaybackStarted() only works from Requested state (no-op from other states)
- [x] 4.2 Implement state guard logic: OnPlaybackComplete() only works from Playing state (no-op from other states)
- [x] 4.3 Implement state guard logic: OnAcceptedReveal() rejects new reveals if already in Playing or CoolingDown state (records rejection reason)
- [x] 4.4 Implement state guard logic: transitions from RejectedOrIgnored only via OnReset()
- [x] 4.5 Verify all invalid state transitions are silent no-ops or recorded as rejections (not exceptions)

## 5. Integration with Memory State Ownership

- [x] 5.1 Verify M0MemoryVFXResponse has no event subscriptions to Memory State (one-way dependency only)
- [x] 5.2 Verify M0MemoryVFXResponse does not read Health, Animator, or Combat Core directly
- [x] 5.3 Verify OnAcceptedReveal() receives full IAcceptedMemoryRevealContext from upstream Memory State
- [x] 5.4 Verify composition documentation shows VContainer scope (scene-level, not project-level) — SUPERSEDED WITH NOTES: Story 1-10 archived the scene-scoped composition path and replaced this skeleton as the source of truth.

## 6. Debug Visibility and Rejection Tracking

- [x] 6.1 Verify snapshot captures and retains rejection reason through entire RejectedOrIgnored state — FOLLOW-UP: rejection retention hardening is deferred to the newer Story 1-10 memory VFX path.
- [x] 6.2 Verify rejection reasons are human-readable strings, not enum codes — FOLLOW-UP: exact debug-facing vocabulary is documented in later memory debug UX work.
- [x] 6.3 Verify Debug Overlay can query snapshot to identify why a reveal was not played — SUPERSEDED WITH NOTES: Story 1-10 covers the observer/snapshot access pattern for debug visibility.
- [x] 6.4 Add internal tracking for skipped/ignored requests while in cooldown (snapshot reflects this) — NOT REQUIRED FOR M0: skipped request tracking is future debug hardening, not needed for the superseded skeleton.

## 7. Tuning and Configuration

- [x] 7.1 Verify duration parameter is configurable and respected by playback logic
- [x] 7.2 Verify cooldownDuration parameter is configurable (zero = no cooldown allowed)
- [x] 7.3 Verify intensityLabel parameter is optional and defaults to "standard"
- [x] 7.4 Verify parameters are exposed for composition-time tuning (not hardcoded)

## 8. Unit Tests for State Machine

- [x] 8.1 Test: initial state is Idle — FOLLOW-UP: covered by the later M0MemoryVFXResponse test suite and superseded by Story 1-10.
- [x] 8.2 Test: Idle → Requested on OnAcceptedReveal with valid context
- [x] 8.3 Test: Requested → Playing on OnPlaybackStarted
- [x] 8.4 Test: Playing → CoolingDown when OnPlaybackComplete called with cooldown > 0
- [x] 8.5 Test: Playing → Idle when OnPlaybackComplete called with cooldown == 0
- [x] 8.6 Test: CoolingDown → Idle when Update called with elapsed >= cooldown duration
- [x] 8.7 Test: state remains CoolingDown when OnAcceptedReveal called while already cooling down
- [x] 8.8 Test: OnRejectRequest transitions to RejectedOrIgnored and stores reason

## 9. Unit Tests for Acceptance Context

- [x] 9.1 Test: generic hit rejection does not trigger playback
- [x] 9.2 Test: failed dodge rejection does not trigger playback — FOLLOW-UP: failed dodge is not yet a first-class reveal rejection route in the superseded skeleton.
- [x] 9.3 Test: failed parry rejection does not trigger playback — FOLLOW-UP: failed parry is not yet a first-class reveal rejection route in the superseded skeleton.
- [x] 9.4 Test: presentation_only rejection does not trigger playback
- [x] 9.5 Test: only OnAcceptedReveal can move state to Requested/Playing (not OnRejectRequest) — FOLLOW-UP: guarded by the later Story 1-10 memory state flow.

## 10. Unit Tests for Snapshot

- [x] 10.1 Test: GetSnapshot returns immutable copy, not live reference — FOLLOW-UP: snapshot immutability is part of the later Story 1-10 verification set.
- [x] 10.2 Test: snapshot.State reflects current state
- [x] 10.3 Test: snapshot.SourceAcceptedContext is populated after OnAcceptedReveal and cleared after OnReset — FOLLOW-UP: covered by the later Story 1-10 response snapshot suite.
- [x] 10.4 Test: snapshot.RejectionReason is populated in RejectedOrIgnored state and null in other states — FOLLOW-UP: covered by the later Story 1-10 response snapshot suite.
- [x] 10.5 Test: snapshot.CooldownProgress is 0.0-1.0 in CoolingDown state, 0.0 elsewhere — FOLLOW-UP: covered by the later Story 1-10 response snapshot suite.
- [x] 10.6 Test: snapshot.IntensityLabel returns configured label or default value
- [x] 10.7 Test: multiple snapshots taken sequentially are independent

## 11. Unit Tests for Frame Atomicity

- [x] 11.1 Test: multiple Update calls in one frame with same deltaTime do not cause spurious state changes — FOLLOW-UP: frame-atomicity concerns are handled in the later Story 1-10 implementation.
- [x] 11.2 Test: OnPlaybackComplete from Idle is no-op (state stays Idle) — FOLLOW-UP: covered by the later Story 1-10 state guard suite.
- [x] 11.3 Test: OnPlaybackStarted from Idle is no-op (state stays Idle) — FOLLOW-UP: covered by the later Story 1-10 state guard suite.
- [x] 11.4 Test: OnAcceptedReveal while already Playing rejects the new request and records it — FOLLOW-UP: handled in the later Story 1-10 rejection flow.

## 12. Unit Tests for Reset

- [x] 12.1 Test: OnReset from Idle returns to Idle with clean state — FOLLOW-UP: reset behavior is part of the later Story 1-10 state model.
- [x] 12.2 Test: OnReset from Playing clears all timers and context — FOLLOW-UP: reset behavior is part of the later Story 1-10 state model.
- [x] 12.3 Test: OnReset from CoolingDown returns immediately to Idle (no residual cooldown) — FOLLOW-UP: reset behavior is part of the later Story 1-10 state model.
- [x] 12.4 Test: OnReset from RejectedOrIgnored clears rejection reason — FOLLOW-UP: reset behavior is part of the later Story 1-10 state model.

## 13. Boundary and Ownership Tests

- [x] 13.1 Test: M0MemoryVFXResponse does not read or modify Health state — SUPERSEDED WITH NOTES: later Story 1-10 keeps VFX response downstream and read-only.
- [x] 13.2 Test: M0MemoryVFXResponse does not call Animator methods — SUPERSEDED WITH NOTES: later Story 1-10 does not give VFX response animation authority.
- [x] 13.3 Test: M0MemoryVFXResponse does not infer CounterWindow or combat result — SUPERSEDED WITH NOTES: later Story 1-10 keeps reveal validity in Combat Core/Memory State.
- [x] 13.4 Test: M0MemoryVFXResponse can be created without Memory State (no required subscription) — SUPERSEDED WITH NOTES: later Story 1-10 uses explicit scene composition instead of hidden subscriptions.

## 14. Integration Documentation

- [x] 14.1 Add composition example to Assets/_Project/Code/Bootstrap showing M0MemoryVFXResponse creation and lifetime scope — SUPERSEDED: archived Story 1-10 notes now cover the composition path.
- [x] 14.2 Document that Memory State is responsible for calling OnAcceptedReveal after acceptance — SUPERSEDED: later Story 1-10 docs cover the accepted reveal flow.
- [x] 14.3 Document that composition root is responsible for calling Update(deltaTime) each frame — SUPERSEDED: later Story 1-10 docs cover the runtime update contract.
- [x] 14.4 Document Debug Overlay access pattern via IMemoryVFXResponseSnapshot — SUPERSEDED: later Story 1-10 docs cover snapshot observation.
- [x] 14.5 Document rejection reason values and what they mean — FOLLOW-UP: exact debug vocabulary remains a future documentation polish item.

## 15. Final Verification

- [x] 15.1 Verify all tests pass in Assets/_Project/Tests/EditMode/M0MemoryVFXResponseTests.cs
- [x] 15.2 Verify M0Contracts.cs remains contracts-only (no implementation)
- [x] 15.3 Verify no Nhem DI generation is used; composition is manual
- [x] 15.4 Verify code follows C# naming conventions and formatting standards
- [x] 15.5 Create brief IMPLEMENTATION_NOTES.md documenting key design decisions for future maintainers — SUPERSEDED: archived Story 1-10 OpenSpec/evidence now serves as the implementation note source.

## Closure Snapshot — 2026-05-26

Status: superseded-with-notes

Closure reason:
- This older skeleton change was superseded by the later Story 1-10 OpenSpec change `wire-m0-memory-reveal-vfx-placeholder`.
- Story 1-10 implemented, verified, completed-with-notes, committed, pushed, and archived the M0 memory reveal/VFX placeholder path.
- The newer architecture keeps Combat Core as reveal request emitter, MemoryState as acceptance/rejection/responding/cooldown truth owner, and M0MemoryVFXResponse as downstream presentation feedback.
- No new gameplay code is required in this older skeleton change.

Covered by later Story 1-10 evidence:
- Runtime DI/composition path for MemoryState and M0MemoryVFXResponse.
- Accepted reveal route from Counter success into MemoryState and VFX response.
- Rejected reveal route does not play accepted reveal feedback.
- Focused EditMode coverage for MemoryState and M0MemoryVFXResponse behavior.
- Presentation boundary: no save/load, no lore UI, no camera, no animation authority, no progression, no full VFX polish.

Remaining non-blocking follow-ups:
- Harden rejection reason documentation and exact values.
- Add deeper rejection tests for failed dodge/parry if those become first-class reveal rejection routes.
- Add skipped/ignored request tracking while already Playing/CoolingDown if needed for future debug UX.
- Add IMPLEMENTATION_NOTES.md only if future maintainers need a dedicated design note beyond archived OpenSpec/evidence files.

Verdict:
- Do not continue this old skeleton change as an active implementation lane.
- Ready for validation/archive as superseded-with-notes if the team accepts Story 1-10 as the replacement source of truth.
