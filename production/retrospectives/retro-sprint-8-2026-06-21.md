# Retrospective: Sprint 8 — Player Animation Polish

Period: 2026-08-04 -- 2026-08-15
Generated: 2026-06-21

---

## Metrics

| Metric | Planned | Actual | Delta |
|--------|--------:|-------:|------:|
| Stories | 9 | 8 done, 1 deferred | -1 should-have |
| Must-have stories | 6 | 7 (+S8-9 added) | +1 |
| Should-have stories | 2 | 1 | -1 (S8-6 not started) |
| Completion Rate | — | 100% must / 50% should | — |
| Effort Days | 7.0 planned | 7.0 delivered | 0 |
| Bugs Found | — | 0 S1/S2 | — |
| Unplanned Tasks Added | — | 1 (S8-9) | — |
| Unplanned Bug Fixes | — | 4 (dash/lock-on/locomotion) | — |
| Commits | — | 2 (uncommitted work remains) | — |
| Smoke Check | — | PASS WITH WARNINGS | — |
| QA Sign-off | — | APPROVED WITH CONDITIONS | — |

---

## Velocity Trend

| Sprint | Planned | Completed | Rate |
|--------|--------:|----------:|-----:|
| Sprint 5 | 9 | 7 | 100% must / 78% total |
| Sprint 6 | 7 | 7 | 100% total |
| Sprint 7 | 7 | 6 | 100% must / 86% total |
| Sprint 8 | 9 | 8 | 100% must / 89% total |

**Trend**: Stable. Four consecutive sprints with 100% must-have completion.

---

## What Went Well

- **All 4 animation areas readable**: Attack windup/recovery, dodge phases, parry/counter distinction, hit reaction blending — all confirmed PASS in smoke.
- **PlayerStateMachine decompose (S8-8) clean**: Zero API breakage. 281/281 EditMode throughout.
- **Playtest-driven bug discovery**: Testing lock-on and dash revealed 4 critical bugs — caught and fixed within the sprint.
- **School_Katana_Girl wired**: Character with URP materials integrated. M0 has a visually coherent protagonist.
- **No S1/S2 regressions**: EditMode 281/281, PlayMode 5/5.

---

## What Went Poorly

- **Significant uncommitted work**: Multiple bug fixes applied locally but not committed.
- **S8-6 M1 Epic Closure deferred**: Third sprint carryover.
- **Dash/locomotion bugs discovered late**: Four architecture-level fixes consumed unplanned effort.
- **Turn clips still unassigned**: `Sp_TurnL`, `Sp_TurnR`, `Turn180` remain at `fileID: 0`.

---

## Action Items for Sprint 9

| # | Action | Priority |
|---|--------|----------|
| 1 | Commit all uncommitted Sprint 8 work | High |
| 2 | Close S8-6 M1 Epic Closure or descope | Med |
| 3 | Assign turn clips in animation set | Low |
| 4 | Add EditMode tests for HasTargetFocus + SetStrafeMode | Med |

---

## Summary

Sprint 8 achieved its goal — all four animation polish areas are readable in the duel. Four pre-existing locomotion bugs were discovered and fixed. The only open item is S8-6 (M1 Epic Closure), deferred across two sprints.
