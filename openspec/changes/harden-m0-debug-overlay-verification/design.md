## Context

Debug Overlay exists as a presentation adapter, but Story 1-9 verification is partial because evidence has not consistently proven all required overlay fields in one focused PlayMode pass.  
Sprint 1 Must Have is now closed, so this change should stay small and evidence-driven, improving verification confidence without gameplay-side behavior changes.

## Goals / Non-Goals

**Goals:**
- Prove Debug Overlay visibility in PlayMode.
- Prove overlay reads and displays existing snapshot fields:
  - CombatState (CombatCore)
  - EnemyIntent (EnemyIntent)
  - LastInput (InputRouter/input snapshot)
  - CounterWindow (CombatCore snapshot, if present)
  - LockOnTarget (TargetContext snapshot)
- Keep overlay strictly read-only.
- Produce explicit evidence artifacts for closure review.

**Non-Goals:**
- Any gameplay logic ownership move to UI/debug
- Combat, targeting, enemy, or encounter behavior changes
- Input binding changes
- New debug console, HUD system, or visual polish
- Camera/animation/VFX changes

## Decisions

### 1) Verify via snapshot-path integrity, not new gameplay signals
We will harden only the presentation read path from already-owned domain snapshots.  
Rationale: prevents accidental ownership leakage into Debug Overlay and keeps change low-risk.

### 2) Minimal binding patch allowed only when snapshot data already exists
If a field is missing on overlay, only bind existing snapshot data in current adapters/forwarders.  
Rationale: keeps scope constrained to presentation wiring and avoids domain mutation.

### 3) Evidence-first closure
Closure requires concrete artifacts (overlay screenshot/log/manual table) showing before/after and state updates for required fields.  
Rationale: this story is verification hardening, so evidence quality is the primary deliverable.

### 4) Keep logging compliant and quiet
Any diagnostic logging remains via NhemLogger and define-gated where appropriate.  
Rationale: avoid log spam and preserve project logging policy.

### 5) Input path remains snapshot-driven only
Debug Overlay verification will use existing InputRouter/InputIntentSnapshot flow for LastInput evidence and MUST NOT add direct `Keyboard.current`, `Mouse.current`, or `Gamepad.current` polling.
Rationale: preserves input architecture boundaries and prevents presentation-owned input truth.

## Risks / Trade-offs

- **[Risk] Overlay appears correct but data source is stale**  
  → **Mitigation:** verify transitions across multiple actions (attack, dodge/parry window, lock-on) and cross-check with domain logs.

- **[Risk] Missing field is interpreted as gameplay bug**  
  → **Mitigation:** classify failures as binding/evidence gap vs gameplay truth gap; avoid domain-side changes in this story.

- **[Risk] External console noise blocks strict zero-error gate**  
  → **Mitigation:** classify unrelated external errors separately and track in tech debt; keep story verdict scoped to overlay verification.

## Allowed Implementation Files

- `Assets/_Project/Code/Presentation/M0CombatDebugOverlayAdapter.cs`
- `Assets/_Project/Code/Bootstrap/M0GameplayTickHandler.cs`
- `Assets/_Project/Tests/EditMode/M0DebugOverlaySnapshotIntegrationTests.cs` (or nearest existing debug overlay tests)
- `production/qa/evidence/*debug-overlay*`
- `openspec/changes/harden-m0-debug-overlay-verification/*`

## Forbidden Implementation Files

- Combat Core/domain logic files (e.g., `Assets/_Project/Code/Combat/*`)
- Enemy intent domain logic files (e.g., `Assets/_Project/Code/Enemy/*`)
- Target acquisition behavior files (except read-only display binding touch points)
- Encounter lifecycle behavior files
- Input binding assets/maps
- Scene/prefab/material assets
- Camera/animation/VFX files
