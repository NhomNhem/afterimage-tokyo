## 1. Proposal and boundary confirmation

- [x] 1.1 Confirm ADR-0001 Slice 1 boundary mapping to memory-only orchestration extraction.
- [x] 1.2 Confirm non-goals are locked (no CombatCore timing/result changes, no input architecture refactor, no MemoryRaycastProProbe alignment, no scene/prefab changes).
- [x] 1.3 Capture baseline S3-2/S3-3/S3-4/S4-2 evidence references before implementation, including runtime memory log output.

## 2. Implementation planning for memory bridge extraction

- [x] 2.1 Define target bridge interface/responsibility text for `MemoryInteractionTickBridge` as routing-only.
- [x] 2.2 Map exact `M0GameplayTickHandler` memory-related orchestration segments to move, preserving execution order for interaction tick, prompt update, reveal feedback, runtime memory log update, and evidence/debug publishing.
- [x] 2.3 Define explicit ownership checks ensuring `MemoryState` and `MemoryInteractionService` remain truth owners.

## 3. Verification planning

- [x] 3.1 Define focused tests for memory interaction orchestration path parity, including prompt/reveal feedback/runtime memory log parity.
- [x] 3.2 Define M0 regression checks required after extraction.
- [x] 3.3 Define manual PlayMode checklist for `Interact -> MemoryInteractionService -> MemoryState -> prompt/reveal feedback/runtime log`.
- [x] 3.4 Define console classification format and PASS/PARTIAL/FAIL evidence table requirements.

## 4. Apply readiness and safety gates

- [x] 4.1 Verify extraction plan does not modify Unity submodule, scene, or prefab assets.
- [x] 4.2 Verify duplicate interaction behavior is preserved as parity requirement in acceptance checks.
- [x] 4.3 Verify debug/evidence outputs are constrained to equivalent-or-better quality.
- [x] 4.4 Approve change as implementation-ready only after all above planning artifacts are complete.
