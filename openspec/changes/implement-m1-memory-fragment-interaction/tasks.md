## 1. Scope Lock and Ownership Guardrails

- [ ] 1.1 Confirm S3-2 scope remains a minimal interaction slice (no inventory/save/quest/dialogue/progression expansion).
- [ ] 1.2 Confirm ownership map is explicit: Input intent -> InteractionSensor/Fragment eligibility -> MemoryInteractionService -> MemoryState truth -> presentation response.
- [ ] 1.3 Confirm CombatCore, enemy lifecycle, and camera truth ownership remain unchanged.

## 2. Fragment Definition and Runtime Identity

- [ ] 2.1 Add `MemoryFragmentDefinition` ScriptableObject with static-only fields (id/title/text/icon/presentation refs).
- [ ] 2.2 Add/define runtime fragment identity component/model (`MemoryFragment`) that references static definition and scene identity.
- [ ] 2.3 Ensure ScriptableObject does not carry runtime collected/revealed state.

## 3. Interaction Detection and Input Route

- [ ] 3.1 Implement/extend interaction sensor/query boundary for nearby eligible fragment detection.
- [ ] 3.2 Wire Interact raw intent through existing New Input System path without introducing direct gameplay truth in input layer.
- [ ] 3.3 Ensure interact requests are ignored safely when no eligible fragment exists.

## 4. Use-Case Orchestration and MemoryState Integration

- [ ] 4.1 Implement `MemoryInteractionService` using Nhem DI/VContainer conventions.
- [ ] 4.2 Route eligible interaction requests through service into MemoryState reveal/collect request flow.
- [ ] 4.3 Handle accepted/rejected outcomes explicitly and expose duplicate handling behavior safely.
- [ ] 4.4 Register new M1 services in scene LifetimeScope with explicit factory/config for primitive constructor parameters if needed.

## 5. Presentation and Debug Hooks

- [ ] 5.1 Emit downstream accepted/rejected signals for UI/VFX/Audio/Animancer presentation without ownership drift.
- [ ] 5.2 Keep Animancer optional in S3-2 and presentation-only if used.
- [ ] 5.3 Add/extend debug/evidence observability for nearby fragment, interact pressed, accepted/rejected, duplicate handling.

## 6. Verification and Evidence

- [ ] 6.1 Add focused tests where feasible for interaction eligibility, service route, MemoryState acceptance/rejection, and duplicate handling.
- [ ] 6.2 Run compile/domain and classify console output (S2/S3-scope vs external warnings).
- [ ] 6.3 Execute manual PlayMode checklist for approach -> interact -> accepted/rejected -> duplicate safety.
- [ ] 6.4 Record PASS/PARTIAL/FAIL evidence table, known limitations, and follow-up rules.
- [ ] 6.5 Explicitly list and justify any scene/prefab changes; classify dirty scene/prefab status.
