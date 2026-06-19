# S6-5 Retrospective Debt Marker Baseline

**Date**: 2026-06-16
**Story**: S6-5 — Standardize Retrospective Debt Marker Baseline
**Sprint**: Sprint 7 (S7-5)
**Run from**: repository root (`J:\afterimage-tokyo`)

---

## Repeatable Command

```powershell
rg "TODO|FIXME|HACK" -g "*.cs" afterimage-tokyo/Assets/_Project --stats
```

This is the canonical command for future retrospectives. Run from repository root.

---

## Included Paths

| Path | Reason |
|------|--------|
| `afterimage-tokyo/Assets/_Project` | All owned project C# source and test files |

---

## Excluded Paths

The search is scoped to `afterimage-tokyo/Assets/_Project`, which naturally excludes:

| Excluded | Reason |
|----------|--------|
| `afterimage-tokyo/Assets/_Project/../Library/` | Unity generated cache — not in `_Project` |
| `afterimage-tokyo/Assets/_Project/../Temp/` | Unity temp build output |
| `afterimage-tokyo/Assets/_Project/../Obj/` | Build intermediates |
| `afterimage-tokyo/Assets/_Project/../build/` | Build output |
| `Library/PackageCache/` | Vendor/package code — not owned |
| `.git/` | Version control metadata |

Production docs, design docs, and rule files (`.md`) are **not** included in the baseline. Mentions of `TODO/FIXME/HACK` in those files are documentation about the practice, not actionable source debt.

---

## Results — 2026-06-16

```
0 matches
0 files contained matches
102 files searched
```

**C# debt markers: 0**

No `TODO`, `FIXME`, or `HACK` markers exist in owned project source as of this baseline.

---

## Notes

- Future retrospectives should rerun this exact command and compare against 0.
- If the count increases, the new markers are candidates for the retro debt discussion.
- Doc/rule `.md` mentions are intentionally excluded — they are examples and references, not debt.
- If `.asmdef`, `.uxml`, or `.uss` files need tracking in the future, add `-g "*.asmdef" -g "*.uxml"` to the command.
