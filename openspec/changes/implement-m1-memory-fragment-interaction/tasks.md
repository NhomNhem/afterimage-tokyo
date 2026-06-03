## 1. Scope Lock and Ownership Guardrails

- [x] 1.1 Confirm S3-2 scope remains a minimal interaction slice (no inventory/save/quest/dialogue/progression expansion).
- [x] 1.2 Confirm ownership map is explicit: Input intent -> InteractionSensor/Fragment eligibility -> MemoryInteractionService -> MemoryState truth -> presentation response.
- [x] 1.3 Confirm CombatCore, enemy lifecycle, and camera truth ownership remain unchanged.

## 2. Fragment Definition and Runtime Identity

- [x] 2.1 Add `MemoryFragmentDefinition` ScriptableObject with static-only fields (id/title/text/icon/presentation refs).
- [x] 2.2 Add/define runtime fragment identity component/model (`MemoryFragment`) that references static definition and scene identity.
- [x] 2.3 Ensure ScriptableObject does not carry runtime collected/revealed state.

## 3. Interaction Detection and Input Route

- [x] 3.1 Implement/extend interaction sensor/query boundary for nearby eligible fragment detection.
- [x] 3.2 Wire Interact raw intent through existing New Input System path without introducing direct gameplay truth in input layer.
- [x] 3.3 Ensure interact requests are ignored safely when no eligible fragment exists.

## 4. Use-Case Orchestration and MemoryState Integration

- [x] 4.1 Implement `MemoryInteractionService` using Nhem DI/VContainer conventions.
- [x] 4.2 Route eligible interaction requests through service into MemoryState reveal/collect request flow.
- [x] 4.3 Handle accepted/rejected outcomes explicitly and expose duplicate handling behavior safely.
- [x] 4.4 Register new M1 services in scene LifetimeScope with explicit factory/config for primitive constructor parameters if needed.

## 5. Presentation and Debug Hooks

- [x] 5.1 Emit downstream accepted/rejected signals for UI/VFX/Audio/Animancer presentation without ownership drift.
- [x] 5.2 Keep Animancer optional in S3-2 and presentation-only if used.
- [x] 5.3 Add/extend debug/evidence observability for nearby fragment, interact pressed, accepted/rejected, duplicate handling.

## 6. Verification and Evidence

- [x] 6.1 Add focused tests where feasible for interaction eligibility, service route, MemoryState acceptance/rejection, and duplicate handling.
- [x] 6.2 Run compile/domain and classify console output (S2/S3-scope vs external warnings).
- [ ] 6.3 Execute manual PlayMode checklist for approach -> interact -> accepted/rejected -> duplicate safety.
- [x] 6.4 Record PASS/PARTIAL/FAIL evidence table, known limitations, and follow-up rules.
- [x] 6.5 Explicitly list and justify any scene/prefab changes; classify dirty scene/prefab status.
