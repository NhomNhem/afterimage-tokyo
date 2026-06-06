## 1. Baseline and boundary confirmation

- [x] 1.1 Inventory owned runtime composition search/fallback calls.
  - Files: `afterimage-tokyo/Assets/_Project/Code/**/*.cs`
  - Why: establish the exact blast radius before editing.
  - Risk: Low.
  - Verify: `rg -n "FindObject|FindFirstObject|FindAnyObject|FindObjectsByType|Resources\\.Load|ServiceLocator" afterimage-tokyo/Assets/_Project/Code -g "*.cs"`.

- [x] 1.2 Confirm current memory loop baseline evidence before implementation.
  - Files: evidence doc under `production/qa/evidence/`.
  - Why: this is a behavior-preserving refactor and needs parity evidence.
  - Risk: Low.
  - Verify: reference latest S4-2/S4-6 evidence and current manual PlayMode checklist.

- [x] 1.3 Confirm no active implementation changes are mixed into proposal/apply branch.
  - Files: parent repo and Unity submodule git status.
  - Why: avoid refactor contamination from docs closure or other stories.
  - Risk: Low.
  - Verify: `git status --short` in `J:\afterimage-tokyo` and `J:\afterimage-tokyo\afterimage-tokyo`.

## 2. Bootstrap/DI composition hardening

- [x] 2.1 Design the narrow explicit scene composition boundary for memory probe/fragments.
  - Files: likely `Assets/_Project/Code/Bootstrap/*` or memory-owned adapter files.
  - Why: remove broad scene discovery while keeping scene objects as explicit dependencies.
  - Risk: Medium.
  - Verify: design notes identify owner, serialized/reference source, and failure behavior.

- [x] 2.2 Replace broad search fallback in `GameplayLifetimeScope`.
  - Files: `afterimage-tokyo/Assets/_Project/Code/Bootstrap/GameplayLifetimeScope.cs` plus new/updated adapter/provider type if needed.
  - Why: `GameplayLifetimeScope` should compose scope dependencies, not discover arbitrary scene inventory.
  - Risk: Medium.
  - Verify: no owned runtime `FindFirstObjectByType`, `FindAnyObjectByType`, broad `FindObjectsByType`, `FindObjectOfType`, `Resources.Load`, or Service Locator usage remains in the hardened path.

- [x] 2.3 Preserve NhemDI registration for pure/runtime gameplay services.
  - Files: affected service files only if registration attributes need alignment.
  - Why: avoid replacing NhemDI with broad manual registration.
  - Risk: Medium.
  - Verify: compile and NhemDI generated registration errors are clean; manual registration is limited to explicit Unity scene instances or documented special cases.

- [x] 2.4 Add setup diagnostics through project logger only.
  - Files: affected bootstrap/adapter files.
  - Why: missing composition should be diagnosable without direct `UnityEngine.Debug`.
  - Risk: Low.
  - Verify: source search shows no direct `Debug.Log*` in owned code; console classification records setup messages.

## 3. Guardrail and parity tests

- [x] 3.1 Add or update focused EditMode guardrail tests for runtime composition.
  - Files: `afterimage-tokyo/Assets/_Project/Tests/EditMode/*`.
  - Why: prevent reintroducing service locator/search fallback APIs in owned composition code.
  - Risk: Low.
  - Verify: focused tests fail if `FindObject*`, `Resources.Load`, or direct `Debug.Log*` return to hardened runtime composition files.

- [x] 3.2 Run memory path parity tests.
  - Files: no production code files expected.
  - Why: prove S3-2/S3-3/S3-4/S4-2 behavior remains unchanged.
  - Risk: Low.
  - Verify: focused memory suite passes for prompt, reveal feedback, runtime memory log, and duplicate/spam parity.

- [x] 3.3 Run M0 regression checks.
  - Files: no production code files expected.
  - Why: composition refactor must not affect combat loop behavior.
  - Risk: Medium.
  - Verify: M0 defensive regression and compile smoke pass.

## 4. Manual evidence and closure

- [x] 4.1 Run manual PlayMode checklist.
  - Files: evidence doc under `production/qa/evidence/`.
  - Why: Unity scene composition cannot be fully proven by EditMode tests.
  - Risk: Medium.
  - Verify: eligible fragment prompt visible; Interact accepted; reveal feedback once; runtime memory log one entry; spam Interact parity.

- [x] 4.2 Record console classification and PASS/PARTIAL/FAIL table.
  - Files: evidence doc under `production/qa/evidence/`.
  - Why: closure should be evidence-driven.
  - Risk: Low.
  - Verify: evidence includes compile/test/manual/console rows and any warnings are classified.

- [x] 4.3 Validate OpenSpec before archive.
  - Files: OpenSpec docs only.
  - Why: ensure proposal/spec/tasks remain consistent.
  - Risk: Low.
  - Verify: `openspec validate harden-m0-runtime-composition-nhemdi --strict`.

- [x] 4.4 Commit only after explicit user instruction.
  - Files: scoped implementation, tests, OpenSpec, and evidence.
  - Why: project workflow forbids autonomous commits.
  - Risk: Low.
  - Verify: staged files match the approved slice only.

## Deferred follow-up slices

- [x] [DEFERRED] Split `M0Contracts.cs` by bounded context.
- [x] [DEFERRED] Introduce ScriptableObject authored configs for M0 tuning data.
- [x] [DEFERRED] Introduce R3 read-only runtime snapshot streams where UI/debug observation needs them.
- [x] [DEFERRED] Introduce MessagePipe events only for confirmed domain events with clear ownership.
