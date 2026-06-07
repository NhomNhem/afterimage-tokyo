## 1. Baseline And Scope Guard

- [x] 1.1 Confirm working tree is clean before implementation.
- [x] 1.2 Capture current `MemoryRaycastProProbe` output and `MemoryInteractionService` snapshot behavior.
- [x] 1.3 Create or update S4-7 story doc if it does not exist.
- [x] 1.4 Run baseline focused memory interaction tests.

## 2. Probe Alignment

- [x] 2.1 Add a read-only service snapshot dependency or narrow read model for `MemoryRaycastProProbe`.
- [x] 2.2 Update probe debug output to report service-owned eligibility separately from RaycastPro collider data.
- [x] 2.3 Preserve optional RaycastPro detector output as supplemental debug evidence only.
- [x] 2.4 Ensure missing probe/detector setup does not block gameplay interaction.
- [x] 2.5 Keep logging through `INhemLogger` only.

## 3. Ownership Guardrails

- [x] 3.1 Add or update tests proving the probe does not execute Interact.
- [x] 3.2 Add or update tests proving the probe does not call MemoryState mutation APIs or MemoryInteractionService command paths.
- [x] 3.3 Add or update guardrails proving no broad lookup, Service Locator, `Resources.Load`, or direct Unity debug logging is introduced.
- [x] 3.4 Confirm prompt, reveal feedback, and runtime memory log remain downstream of service/memory truth.

## 4. Regression Tests

- [x] 4.1 Run `MemoryInteractionServiceTests`.
- [x] 4.2 Run prompt/reveal/runtime-log focused EditMode tests.
- [x] 4.3 Run SceneComposition or VContainer registry tests if injection/composition changes.
- [x] 4.4 Run PlayMode or manual smoke for eligible prompt, accepted Interact, reveal feedback once, runtime log append once, and duplicate/spam safety.

## 5. Evidence And Closure

- [x] 5.1 Record PASS/PARTIAL/FAIL evidence comparing service eligibility and probe output.
- [x] 5.2 Classify console output.
- [x] 5.3 Run `openspec validate align-memory-raycast-probe-with-interaction-service --strict`.
- [x] 5.4 Update Sprint 4/S4-7 status if story closure is requested.
- [x] 5.5 Archive only after evidence is complete and approved.

## 6. Deferred Follow-ups

- [x] 6.1 Defer MemoryInteractionService behavior changes.
- [x] 6.2 Defer input architecture refactor.
- [x] 6.3 Defer prompt/log/VFX feature expansion.
- [x] 6.4 Defer R3/MessagePipe migration.
