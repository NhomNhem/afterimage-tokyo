## 1. Proposal and boundary confirmation

- [ ] 1.1 Confirm ADR-0001 Slice 1 boundary mapping to memory-only orchestration extraction.
- [ ] 1.2 Confirm non-goals are locked (no CombatCore timing/result changes, no input architecture refactor, no MemoryRaycastProProbe alignment, no scene/prefab changes).
- [ ] 1.3 Capture baseline S3-2 interact accepted path evidence references before implementation.

## 2. Implementation planning for memory bridge extraction

- [ ] 2.1 Define target bridge interface/responsibility text for `MemoryInteractionTickBridge` (or approved final name) as routing-only.
- [ ] 2.2 Map exact `M0GameplayTickHandler` memory-related orchestration segments to move, preserving execution order.
- [ ] 2.3 Define explicit ownership checks ensuring `MemoryState` and `MemoryInteractionService` remain truth owners.

## 3. Verification planning

- [ ] 3.1 Define focused tests for memory interaction orchestration path parity.
- [ ] 3.2 Define M0 regression checks required after extraction.
- [ ] 3.3 Define manual PlayMode checklist for `Interact -> MemoryInteractionService -> MemoryState`.
- [ ] 3.4 Define console classification format and PASS/PARTIAL/FAIL evidence table requirements.

## 4. Apply readiness and safety gates

- [ ] 4.1 Verify extraction plan does not modify Unity submodule, scene, or prefab assets.
- [ ] 4.2 Verify duplicate interaction behavior is preserved as parity requirement in acceptance checks.
- [ ] 4.3 Verify debug/evidence outputs are constrained to equivalent-or-better quality.
- [ ] 4.4 Approve change as implementation-ready only after all above planning artifacts are complete.
