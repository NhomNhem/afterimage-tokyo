## 1. Scope Lock and Baseline

- [x] 1.1 Confirm S3-3 remains UI prompt placeholder only, with no runtime memory log, reveal VFX/audio, inventory, quest, save/profile, progression, or full HUD expansion.
- [x] 1.2 Confirm S3-2 interaction behavior remains unchanged before implementing prompt UI.
- [x] 1.3 Identify the approved read-only interaction context or UI-facing read model the prompt will observe.

## 2. Prompt Presentation Implementation

- [x] 2.1 Implement a minimal prompt presenter or UI adapter that can show/hide placeholder text.
- [x] 2.2 Wire prompt visibility to the approved read-only interaction eligibility/context.
- [x] 2.3 Ensure prompt text remains concise and placeholder-safe.
- [x] 2.4 Ensure prompt hidden state is stable when no eligible fragment exists.

## 3. Ownership Guardrails

- [x] 3.1 Verify prompt code does not call MemoryState mutation/acceptance APIs.
- [x] 3.2 Verify prompt code does not call MemoryInteractionService command paths or fragment mutation paths.
- [x] 3.3 Verify prompt code does not own Unity InputAction callbacks or Interact execution.
- [x] 3.4 Verify no service locator, FindObjectOfType, Resources.Load, or direct Unity debug logging is introduced.

## 4. Scene/UI Wiring

- [x] 4.1 Add only the minimal UI scene/prefab/asset wiring required to display the placeholder prompt.
- [x] 4.2 Explicitly classify any scene/prefab/UI asset edits as intentional or unintentional in evidence.
- [x] 4.3 Preserve S3-2 Memory Fragment placement and interaction truth wiring.

## 5. Verification and Evidence

- [x] 5.1 Capture manual evidence that prompt appears when a Memory Fragment is eligible.
- [x] 5.2 Capture manual evidence that prompt disappears when no eligible fragment is available.
- [x] 5.3 Capture evidence that pressing Interact still routes through S3-2 input/orchestration, not UI.
- [x] 5.4 Classify console output as S3-scope vs external/non-scope warnings.
- [x] 5.5 Record PASS/PARTIAL/FAIL table at `production/qa/evidence/s3-3-interaction-prompt-placeholder-verification-2026-06-04.md`.
