# Story S5-4: [Feature] Wire M0 Dodge Displacement

> **Sprint**: Sprint 5
> **Status**: Complete
> **Layer**: Core / Integration
> **Type**: Integration
> **Estimate**: 2.0d
> **Priority**: Must Have
> **Owner**: gameplay-programmer
> **Dependencies**: None
> **Manifest Version**: 2026-05-15
> **Last Updated**: 2026-06-12

## Context

The high-priority M0 tech debt item `m0-dodge-displacement-wiring` says Dodge input and Combat Core Dodge state are present, but a visible player dodge lunge is not reliably expressed by Player Locomotion. Sprint 5 makes this the critical gameplay-feel story.

Relevant trace:
- `docs/tech-debt-register.md`
- `production/sprints/sprint-5.md`
- `production/qa/qa-plan-sprint-5-2026-06-09.md`
- `design/gdd/player-locomotion.md`: `Player Locomotion` owns dodge movement expression, displacement, movement restriction, recovery, and locomotion debug truth.
- `design/gdd/player-locomotion.md`: Dodge / Evade criteria require readable direction, displacement, and recovery.
- `design/gdd/combat-core.md`: `Combat Core` owns dodge action validity, timing, result, and recovery context; it does not own movement truth.
- `afterimage-tokyo/Assets/_Project/Code/Combat/M0CombatCore.cs`
- `afterimage-tokyo/Assets/_Project/Code/Locomotion/M0PlayerLocomotion.cs`
- `afterimage-tokyo/Assets/_Project/Code/Bootstrap/M0GameplayTickHandler.cs`

Technical requirement trace:
- `TR-M0-COMBAT-001`: Combat Core owns combat validation and result truth.
- `TR-M0-LOCOMOTION-001`: Player Locomotion owns movement truth and expression.

ADR / architecture reference:
- ADR source: `docs/architecture/control-manifest.md` ADR-0002 rules for Pure C# Authority, Ownership Separation, and Lock/Recovery Request Pattern.
- No standalone `docs/architecture/adr-0002*.md` file exists in this repo snapshot; use the accepted control manifest rules as the implementation authority for this sprint story.

## Goal

Wire Combat Core Dodge state into Player Locomotion dodge displacement so the player gets a visible, readable dodge lunge while preserving Combat Core as dodge validity/timing authority and Player Locomotion as movement truth owner.

## Acceptance Criteria

- [x] Combat Core Dodge state triggers a Player Locomotion dodge displacement request.
- [x] Dodge displacement has observable player movement in PlayMode.
- [x] Dodge displacement direction and magnitude follow existing M0 locomotion tuning unless a separate approved tuning change exists.
- [x] Dodge displacement does not trigger during non-Dodge combat states.
- [x] Player Locomotion remains the owner of movement truth and displacement expression.
- [x] Combat Core remains the owner of dodge action validity, timing, result, and recovery state.
- [x] Dodge request rejection or duplicate dodge behavior remains explicit and testable.
- [x] Attack, parry, counter, target context, health, memory, and runtime log flows do not regress.
- [x] No service locator, `FindObjectOfType`, `Resources.Load`, broad scene lookup, or direct Unity debug logging is introduced.
- [x] Automated integration evidence and manual PlayMode evidence are captured.

## Out of Scope

- New perfect dodge reward
- New i-frame or dodge success policy
- Enemy AI or telegraph changes
- Parry/counter visual polish
- LockOn policy changes
- Broad locomotion rewrite
- Root-motion-owned gameplay displacement
- New full RPG movement systems

## Implementation Notes

- Keep this as a narrow bridge between combat state and locomotion expression.
- Prefer existing contracts/snapshots over new broad service interfaces.
- If a new request object is needed, keep it small and place ownership where existing architecture expects movement/recovery request data.
- Do not let the Animator decide displacement or dodge success.
- Use `NhemLogger` / `NhemLogging` only if logging is needed.
- The Unity project root for implementation paths is `afterimage-tokyo/`.

## Engine Notes

- Engine: Unity 6000.3.x with URP.
- Verify dodge displacement in PlayMode because visible transform movement is the player-facing acceptance signal.
- Do not use legacy `Input.GetKey`, `Input.GetAxis`, or `Input.GetButton`.
- Do not let Animator or root motion own gameplay displacement.
- Keep the implementation compatible with the existing Unity Test Framework EditMode/PlayMode layout under `afterimage-tokyo/Assets/_Project/Tests`.

## Control Manifest Notes

- Required: Combat Core owns validity; Player Locomotion owns movement truth.
- Required: Lock/recovery request pattern between Combat Core and Locomotion.
- Forbidden: gameplay truth in MonoBehaviours.
- Forbidden: service locator, `GameObject.Find`, `Resources.Load`, direct Unity debug logging.
- Guardrail: presentation observes only; it must not own dodge outcomes.

## Performance Budget

- No per-frame allocations in the hot gameplay tick path.
- No new broad polling, scene lookup, `FindObjectOfType`, `GameObject.Find`, or `Resources.Load`.
- Dodge displacement should reuse existing tick/update flow and complete within the authored M0 locomotion dodge duration.
- Target remains 60 fps / 16.6 ms frame budget.

## QA Test Cases

- **AC-1**: Combat Core Dodge triggers locomotion displacement.
  - Given: the player is in a state where Dodge is valid.
  - When: Dodge input causes Combat Core to enter Dodge state.
  - Then: Player Locomotion receives or derives a dodge displacement request and applies movement.
  - Edge cases: already dodging, recovering, invalid dodge direction, zero move input.

- **AC-2**: Dodge does not displace outside Dodge state.
  - Given: the player is attacking, parrying, countering, neutral, or in recovery.
  - When: locomotion ticks without an active Dodge context.
  - Then: no dodge displacement impulse is applied.
  - Edge cases: stale dodge context, repeated input frames, recovery transition.

- **AC-3**: Authority boundaries remain intact.
  - Given: Combat Core and Player Locomotion snapshots are inspected after Dodge.
  - When: a dodge lunge occurs.
  - Then: Combat Core still owns action validity/result and Player Locomotion owns movement expression.
  - Edge cases: Animator/root motion tries to move gameplay truth, presentation code mutates state.

- **AC-4**: M0 and M1 regressions remain stable.
  - Given: S5-4 is implemented.
  - When: focused regression checks run.
  - Then: attack/parry/counter/health, target context, memory interaction, reveal feedback, and runtime memory log still pass.
  - Edge cases: dodge displacement changes combat spacing enough to break counter or target focus readability.

## Test Evidence

**Story Type**: Integration

Required evidence:
- Automated test path from QA plan: `afterimage-tokyo/Assets/_Project/Tests/PlayMode/M0DodgeDisplacementIntegrationTests.cs`
- Focused M0 combat/locomotion regression results
- Manual PlayMode evidence showing visible dodge lunge displacement
- Console classification with no new S5-scope blocker

Expected evidence location:
- `production/qa/evidence/s5-4-wire-m0-dodge-displacement-verification-2026-06-11.md`

**Status**: [x] Created — `production/qa/evidence/s5-4-wire-m0-dodge-displacement-verification-2026-06-11.md`

## Dependencies

- Depends on: None
- Unlocks: Sprint 5 must-have closure, S5 smoke, M0 feel polish follow-ups

## Completion Notes

**Completed**: 2026-06-12
**Criteria**: 10/10 passing
**Deviations**: None blocking. Valid closure fix added Odin serialization and scene references for existing M0 runtime config fields so `GameplayLifetimeScope` can compose config-backed services in PlayMode.
**Test Evidence**: `production/qa/evidence/s5-4-wire-m0-dodge-displacement-verification-2026-06-11.md`
**Code Review**: Complete with fixes applied. Initial review found missing runtime config serialization and secondary tick-handler NREs after failed DI; both were fixed and verified.
**Verification**:
- Unity MCP PlayMode smoke: PASS, no `M0RuntimeServiceCompositionRegistrar` config exception and no `M0GameplayTickHandler` `Update` / `OnDestroy` NRE.
- Unity MCP focused PlayMode test run: PASS 7/7, including all 5 `M0DodgeDisplacementIntegrationTests`.
- Manual dodge-lunge smoke: PASS, `Dodge pressed` drove `Neutral -> DodgeStartup -> DodgeActive -> DodgeRecovery -> Neutral`, and `[M0Locomotion] Dodge displacement started` was observed.
- Console classification: no new S5-scope blocker; optional missing animation set warnings remain non-blocking.
