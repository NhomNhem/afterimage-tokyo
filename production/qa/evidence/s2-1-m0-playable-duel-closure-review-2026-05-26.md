# S2-1 Evidence Review — M0 Sprint 1 Playable Duel Closure

**Date**: 2026-05-26
**Story**: S2-1 `[Review] M0 Sprint 1 Playable Duel Closure Review`
**Scope**: Documentation and QA evidence only (no gameplay code changes)

## Source Artifacts Reviewed

- `production/qa/evidence/m0-sprint-1-final-review-2026-05-26.md`
- `production/qa/evidence/wire-m0-encounter-reset-duel-lifecycle-verification-2026-05-25.md`
- `production/qa/evidence/wire-m0-memory-reveal-vfx-placeholder-verification-2026-05-26.md`
- `production/qa/evidence/harden-m0-debug-overlay-verification-2026-05-26.md`
- `docs/tech-debt-register.md`
- `production/sprints/sprint-2.md`

## Sprint 1 Verified-With-Notes Summary

1. **Story 1-8 Encounter Reset Lifecycle**: Verified with notes, archived.
2. **Story 1-9 Debug Overlay Verification**: Evidence closed, archived.
3. **Story 1-10 Memory Reveal Placeholder**: Completed with notes.
   - Runtime/DI stabilized after explicit primitive factory registration.
   - Focused EditMode tests passed.
   - Manual counter window path proven.
   - Helper-route memory acceptance proven.
   - Memory phase completion/VFX completion logs remain partial evidence.
4. **External material/HDRP enum editor error** is tracked as tech debt and classified outside core duel gameplay scope.

## PASS / PARTIAL / FAIL Review Table

| Area | Result | Evidence Summary | Follow-up |
|---|---|---|---|
| Combat feel/readability | PARTIAL | Core loop works, but timing clarity is still prototype-level. | S2-2 |
| Attack/Dodge/Parry timing readability | PARTIAL | Defensive/counter path is proven but consistency/readability needs tuning pass. | S2-2 |
| Enemy telegraph readability | PARTIAL | Intent loop transitions are present; readability quality needs focused pass. | S2-3 |
| Lock-on camera readability | PARTIAL | Lock-on works functionally; readability/framing polish is pending. | S2-4 |
| Player movement readability | PARTIAL | Movement and dodge wiring verified; feel/readability refinement pending. | S2-2 |
| Memory reveal readability | PARTIAL | Acceptance route proven; full phase and VFX completion evidence remains partial. | S2-7 (Should) |
| Animation placeholder readability | PARTIAL | Known placeholder/missing presentation warnings in Sprint 1 notes. | S2-6 (Should) |
| Audio/VFX feedback gaps | PARTIAL | Placeholder level; feedback clarity not yet hardened. | S2-8 (Should) |
| Debug overlay usefulness | PASS | Overlay verification hardening archived; read-only boundary preserved. | S2-10 (Could) |
| Sprint 1 verified-with-notes carryover handling | PASS | Notes are explicit and traceable to evidence artifacts. | S2-5 |
| Tech debt visibility | PASS | Known debt items are documented and scoped. | S2-9 (Could) |

## Current M0 Playability Gaps (Pre-Tuning)

1. Timing readability for attack/dodge/parry is functionally correct but still hard for repeatable feel judgment.
2. Enemy telegraph readability needs clearer distinction across phases under active duel pressure.
3. Lock-on camera readability needs practical framing validation for sustained duel.
4. Memory reveal visualization is intentionally restrained but evidence for full response lifecycle is still partial.
5. Placeholder animation/audio/VFX layers can hide whether failures are design vs presentation noise.

## Prioritized Sprint 2 Recommendations

1. **S2-2 Combat Feel (Must Have)**
   Priority: P0
   Why: Highest impact on readable loop quality.

2. **S2-3 Enemy Telegraph (Must Have)**
   Priority: P0
   Why: Directly affects read -> respond confidence.

3. **S2-4 Camera Readability (Must Have)**
   Priority: P0
   Why: Duel readability collapses if framing is weak.

4. **S2-5 Smoke Checklist (Must Have)**
   Priority: P0
   Why: Locks a repeatable verification baseline after each tuning pass.

5. **S2-6/S2-7/S2-8 (Should Have)**
   Priority: P1
   Why: Lift readability quality once core feel/readability passes are stable.

6. **S2-9/S2-10 (Could Have)**
   Priority: P2
   Why: Good cleanup and visibility improvements, but not core duel blockers.

## OpenSpec Requirement Markers

- **Requires OpenSpec**:
  - S2-2 Combat Feel tuning
  - S2-3 Enemy Telegraph readability changes
  - S2-4 Camera readability tuning
  - S2-7 Memory reveal readability adjustments (if behavior/state timing changes)

- **Likely no new OpenSpec required** (docs/process-first):
  - S2-5 Smoke checklist hardening
  - S2-9 Tech debt classification-only pass
  - S2-10 Debug overlay presentation polish if strictly read-only UI wording/layout

## Conclusion

**Verdict**: PASS (Review Complete)
Sprint 1 closure is sufficiently evidenced to begin Sprint 2 stabilization.
Current duel is playable but readability remains PARTIAL in several key presentation/feel axes, matching Sprint 2 priorities.
