# Tasks — S2-4 Lock-On Camera Readability Implementation

## 1. Scope and Boundary Lock

- [x] 1.1 Confirm runtime edits are limited to camera readability/framing behavior.
- [x] 1.2 Confirm no gameplay truth ownership moves to camera.
- [x] 1.3 Confirm no scene/prefab/material/asset edits are introduced.

## 2. Small Camera Readability Pass

- [x] 2.1 Implement a minimal camera movement basis stabilization pass in existing camera provider code.
- [x] 2.2 Keep fallback behavior safe when camera basis is invalid.
- [x] 2.3 Preserve existing lock-on/target/combat ownership boundaries.

## 3. Focused Tests

- [x] 3.1 Add focused EditMode tests for camera basis readability behavior.
- [x] 3.2 Keep existing target/context/debug overlay tests passing.
- [x] 3.3 Ensure tests prove behavior without broadening architecture scope.

## 4. Focused Verification

- [x] 4.1 Run focused EditMode tests (camera + target/debug relevant suites).
- [x] 4.2 Classify console/domain results (errors/warnings and scope relevance).
- [x] 4.3 Record PASS/PARTIAL/FAIL evidence for S2-4.

## 5. Evidence and Closure Snapshot

- [x] 5.1 Update `production/qa/evidence/s2-4-lockon-camera-readability-verification-2026-05-28.md`.
- [x] 5.2 Include ownership-boundary confirmation and manual limitation disclosures (if any).
- [x] 5.3 Add closure snapshot in this tasks file when verification is complete.

## Implementation Snapshot — 2026-05-28

- Runtime change scope: camera readability only (`CameraMovementBasisProvider` basis stabilization).
- Focused EditMode verification (Unity MCP):
  - Job: `562b19e7c4524d6c8d29456bce96f1b0`
  - Total: 15, Passed: 15, Failed: 0
- Console classification:
  - Known external material-drawer warnings (non-S2-4).
  - Test-runner cleanup warning noted.
- Current closure state: verification pass with notes, pending manual PlayMode lock-on readability pass before full closure snapshot.

## Closure Snapshot — 2026-05-28

- Status: `completed-with-notes`
- Focused tests: PASS (`562b19e7c4524d6c8d29456bce96f1b0`, 15/15)
- Manual PlayMode readability: PASS WITH NOTES
  - LockOn acquire/release captured
  - Enemy loop readability captured across repeated intent phases
  - Attack + Dodge readability captured
  - Explicit Parry line not captured in this sample
- Console classification: PASS WITH NOTES
  - Known external HDRP material warnings
  - Placeholder animation-set warnings (non-S2-4 ownership)
