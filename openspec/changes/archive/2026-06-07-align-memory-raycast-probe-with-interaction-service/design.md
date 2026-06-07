## Context

`MemoryInteractionService` already owns the S3/S4 memory interaction route. It tracks registered `MemoryFragment` instances, finds the nearest eligible fragment by fragment radius and player position, and emits a read-only snapshot.

`MemoryRaycastProProbe` is a MonoBehaviour debug probe that currently performs its own RaycastPro `RangeDetector` pass and logs collider-derived debug output. Evidence shows this can diverge from the actual service path: gameplay interaction can pass while the probe reports no hit.

The goal is not to make the probe authoritative. The goal is to make debug evidence less misleading by aligning its reported state with the service-owned eligibility path, or by explicitly marking it as non-truth debug if alignment is not practical.

## Goals / Non-Goals

**Goals:**

- Keep `MemoryInteractionService` as interaction orchestration truth.
- Make `MemoryRaycastProProbe` debug output comparable to service eligibility.
- Avoid duplicate gameplay decision logic inside the probe where possible.
- Preserve current memory interaction behavior.
- Improve S4 smoke evidence so debug probe output no longer contradicts accepted interaction evidence.

**Non-Goals:**

- No change to MemoryState acceptance/rejection truth.
- No change to duplicate/spam interaction behavior.
- No change to prompt, reveal feedback, runtime memory log, or input routing behavior.
- No broad scene lookup or fallback resource loading.
- No conversion of debug probe into gameplay authority.

## Decisions

### Decision: Prefer observing service snapshot over reimplementing eligibility

The preferred implementation should inject or receive `MemoryInteractionService` read-only context and log that service-owned eligibility state. RaycastPro collider details may remain supplemental, but service eligibility must be clearly identified as the authoritative debug comparison.

Rationale: this avoids two competing eligibility algorithms.

Alternative considered: tune RaycastPro detector until it matches fragment distance checks. This may still drift because physics/collider setup and fragment service registration are different evidence paths.

### Decision: Keep probe optional and debug-only

If probe references are missing, the memory loop must still run through `MemoryInteractionService`. Missing probe setup should be diagnosable through project logger output, not gameplay blocking.

Rationale: the probe is evidence/debug tooling, not interaction runtime authority.

### Decision: Evidence must classify both service and probe state

Manual smoke should record service snapshot and probe debug output together for eligible, no-eligible, accepted, and duplicate/spam cases.

Rationale: the old blocker was evidence ambiguity, not core interaction failure.

## Risks / Trade-offs

- [Risk] Injecting service into a debug MonoBehaviour could tempt future gameplay calls.
  - Mitigation: expose/read only snapshot context and add tests that forbid command-path calls from the probe.

- [Risk] RaycastPro collider output remains different from service eligibility.
  - Mitigation: label collider output as supplemental and service snapshot as truth.

- [Risk] Probe logs become noisy.
  - Mitigation: log only on Interact/debug trigger or state changes, consistent with current low-noise behavior.

## Migration Plan

1. Baseline current probe/service evidence.
2. Add read-only service snapshot observation or a narrow read model for the probe.
3. Update probe log format to include service eligibility and optional collider hit data.
4. Add focused tests/guardrails.
5. Run memory interaction regressions and manual smoke.
6. Record S4-7 evidence and close the story.
