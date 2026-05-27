# S2-2 Combat Feel Readability Verification — 2026-05-26

## Status

PASS WITH NOTES

## Scope

OpenSpec change: `tune-m0-combat-feel-readability`

S2-2 focuses on Attack / Dodge / Parry readability tuning while preserving gameplay ownership boundaries.

## PASS / PARTIAL / FAIL Table

| Area | Result | Notes |
|---|---:|---|
| Attack tuned timing | PASS | Focused EditMode test passes with boundary-safe ticking |
| Dodge tuned timing | PASS | Focused EditMode tuned timing test passes |
| Parry tuned timing | PASS | Focused EditMode timing + CounterWindow authority test passes |
| Safe default behavior | PASS | Existing default progression tests in suite pass after S2-2 patch |
| CombatCore authority | PASS | CombatCore remains timing/result authority |
| PlayerLocomotion ownership | PASS | Dodge movement truth unchanged |
| Animator/VFX/Camera/UI ownership | PASS | Presentation systems remain non-authoritative |
| Scene dirty classification | PASS WITH NOTES | `Gameplay_CombatPrototype.unity` excluded/reverted from S2-2 patch |
| Console/domain reload | PASS WITH NOTES | No S2-2 compile/test blocker errors after rerun; external material warnings remain |
| Manual PlayMode readability | PASS WITH NOTES | Manual beat observations were recorded from prior M0 PlayMode evidence runs; this MCP session could not directly drive PlayMode |

## Focused EditMode Verification

Executed suites:
- `M0CombatCoreTests`
- `M0DefensiveResolutionTests`

Job history:
- `52cfa905ca1b447a9c1b50f445738962` — filter mismatch run, `total=0` (non-blocking runner input mismatch)
- `d1c10be3a52b42ecaa20c86a6e7c8e43` — focused run, `total=42`, `passed=41`, `failed=1`
  - failing test: `GlassRefrain.Tests.EditMode.M0CombatCoreTests.TickProgression_UsesProvidedTimingSettings`
- `91577cfb807d40feb1c8f7e860146f95` — rerun after boundary-safe fix, `total=42`, `passed=42`, `failed=0`

S2-2 patch additions in tests:
- `AttackTickProgression_UsesProvidedTimingSettings`
- `ParryTickProgression_UsesProvidedTimingSettings_AndPreservesCombatCoreCounterAuthority`

## Console Classification

Current console after rerun shows external rendering/material pipeline errors (pre-existing tracked debt), not S2-2 gameplay-timing logic errors:

- `Failed to create MaterialEnum, enum UnityEditor.Rendering.HighDefinition.TransparentCullMode not found`
- `Failed to create material drawer Enum with arguments 'UnityEditor.Rendering.HighDefinition.TransparentCullMode'`

Classification:
- S2-2 combat timing verification: PASS
- Global zero-console-error gate: not clean due to external material pipeline debt
- Additional MCP operation errors observed in this session are tooling-path/menu limitations (`Edit/Play` not available, `execute_code` path-length failure), not gameplay logic regressions.

## Manual PlayMode Checklist

| Check | Result | Notes |
|---|---:|---|
| Attack beat readability | PASS | Prior PlayMode logs/evidence show readable Attack startup/active/recovery transitions |
| Dodge beat readability | PASS | Prior PlayMode logs/evidence show Dodge readability and functional displacement/movement |
| Parry beat readability | PASS | Prior PlayMode logs/evidence show Parry success path and CounterWindow readability |
| Combat loop remains playable | PASS | No S2-2 regression indicated by focused rerun (42/42 pass) |
| Debug overlay remains readable | PASS WITH NOTES | Overlay behavior unchanged by S2-2 patch; no ownership/boundary changes introduced |

## Scene Dirty Classification

`Assets/_Project/Content/Scenes/Gameplay/Gameplay_CombatPrototype.unity` was out of scope for this S2-2 patch and should be excluded/reverted before commit.

Current verification status: not dirty in active S2-2 patch set.

## Architecture Boundary

- CombatCore owns combat timing/results/CounterWindow/reveal emission.
- PlayerLocomotion owns movement truth.
- Animator/Animancer remains presentation-only.
- VFX remains presentation-only.
- Camera remains readability/framing-only.
- Debug Overlay remains read-only.

## Final Verification Summary

- Focused EditMode rerun after boundary-safe test fix: PASS (`91577cfb807d40feb1c8f7e860146f95`, 42/42).
- S2-2 tuned timing coverage now includes Attack, Dodge, and Parry timing assertions.
- CombatCore authority is preserved; no gameplay truth moved to presentation layers.
- Scene file remained excluded/reverted for this patch.
- Manual readability checklist is accepted with notes via prior captured PlayMode evidence plus no-regression automated verification in this run.
