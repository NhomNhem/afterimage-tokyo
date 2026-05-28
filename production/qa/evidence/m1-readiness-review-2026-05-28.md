# M1 Readiness Review — 2026-05-28

## Verdict

APPROVED WITH NOTES

M0 foundation is sufficient to begin M1 slice implementation, with explicit boundaries and scoped additions.

## Scope

Review-only evidence for Sprint 3 Story S3-1:
- No gameplay code changes
- No Unity submodule changes
- No implementation claims

## Reusable M0 Systems

| System | Reuse Level | Notes |
|---|---|---|
| Player Locomotion | High | Movement/facing pipeline can support exploration movement baseline |
| Input Mapping / Router | Medium-High | Existing input path is reusable; Interact intent needs explicit mapping/story implementation |
| Memory State | Medium | Existing reveal acceptance/state ownership model is reusable for reveal/collect truth |
| Memory VFX Response | Medium | Placeholder presentation response path reusable for feedback once triggered |
| Debug Overlay | Medium | Read-only snapshot verification pattern reusable for M1 evidence |
| VContainer/Nhem DI composition style | High | Existing explicit/manual registration pattern is compatible with M1 service additions |

## New M1 Boundaries Required

| Boundary | Responsibility | Ownership |
|---|---|---|
| MemoryFragment | Fragment identity and interaction target concept | Domain/config boundary |
| MemoryInteractionService | Interaction orchestration use-case | Application/use-case boundary |
| InteractionSensor | Proximity/candidate detection for interactable fragment | Presentation/adapter boundary feeding use-case |
| RuntimeMemoryLogStore | Runtime read-model for collected/revealed entries | Application/read-model boundary |

## Ownership Boundaries (M1)

- Input owns raw Interact intent only.
- MemoryInteractionService owns interaction orchestration.
- MemoryState owns reveal/collect truth transitions.
- ScriptableObject owns static fragment definition/config only.
- UI/VFX/Audio/Animancer remain presentation-only.
- Debug Overlay remains read-only.
- Camera does not own interaction truth.
- CombatCore is unchanged.

## System Readiness Assessment

| Area | Result | Notes |
|---|---:|---|
| Player Locomotion readiness | PASS | Exploration baseline is already available from M0 locomotion |
| Input Mapping readiness for Interact | PARTIAL | Interaction action path should be formalized in S3-2 scope |
| Memory State readiness | PASS WITH NOTES | Reveal model exists; collect semantics need explicit contract in M1 |
| Memory VFX response readiness | PASS WITH NOTES | Presentation path reusable; trigger contract must be defined by S3-2 |
| Debug Overlay usefulness | PASS WITH NOTES | Useful for verification; additional M1 fields likely needed later |
| Scene/map readiness | PARTIAL | Tokyo street exploration area is conceptually ready; exact interaction placement is implementation work |
| UI readiness (prompt/log) | PARTIAL | Placeholder UI stories needed (S3-3/S3-5) |
| Nhem DI/VContainer readiness | PASS | Explicit registration pattern is ready for incremental M1 services |
| ScriptableObject config readiness | PASS WITH NOTES | Good fit for static fragment definitions; runtime state must stay outside SO |
| Animancer presentation boundary | PASS | Should remain deferred to S3-4 and presentation-only |
| Save/Profile out-of-scope control | PASS | Explicitly excluded for Sprint 3 slice |

## Nhem DI Adoption Recommendation

Use current Nhem DI + VContainer explicit/manual registration conventions for new M1 services (same style as M0).

Rationale:
- Consistent with existing runtime composition.
- Low integration risk for a small slice.
- Avoids introducing new DI patterns during feature slicing.

## ScriptableObject Data Recommendation

Store in ScriptableObject (static only):
- Fragment ID
- Display name/label
- Static description/placeholder text
- Optional static reveal metadata tags
- Optional authored visual/audio placeholder references

Do not store in ScriptableObject (runtime truth):
- Collected state
- Reveal completion runtime flags
- Session/player progression state

## OpenSpec Recommendation for S3-2

YES — S3-2 should use a small OpenSpec change before implementation.

Reason:
- Introduces new behavior contracts across interaction orchestration/state/UI boundaries.
- Needs explicit acceptance criteria and guardrails to prevent scope drift.

## Animancer Recommendation

Defer Animancer behavior work to S3-4.

S3-2 should remain interaction/use-case truth wiring only, with presentation hooks/events prepared but not expanded into animation ownership.

## Non-Goals (Confirmed)

- Full inventory
- Save/load/profile
- Quest/dialogue systems
- RPG progression
- Boss/multi-enemy systems
- Large map/cinematic systems
- CombatCore changes

## Risks Before S3-2

| Risk | Impact | Mitigation |
|---|---|---|
| Interaction scope drifts into inventory/save | High | Keep strict S3-2 ACs and OpenSpec guardrails |
| Runtime truth drifts into UI/presentation | High | Enforce MemoryState/interaction-service ownership |
| Ambiguous fragment data/runtime split | Medium | Lock SO static vs runtime-store split early |
| Prompt/log UX expands beyond placeholder | Medium | Keep S3-3/S3-5 as placeholder-only scope |

## Final Recommendation

Proceed to S3-2 with a small OpenSpec change focused on:
- MemoryFragment interaction contract
- MemoryInteractionService orchestration
- InteractionSensor feed path
- RuntimeMemoryLogStore read-model boundary

No implementation is performed in this review artifact.
