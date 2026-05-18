## Context

Story 1-1, 1-2, and 1-3 are complete, establishing:
- Foundation scene and VContainer wiring (Story 1-1)
- Camera-relative movement and Locomotion ownership of movement truth (Story 1-2)
- Lock-On wiring with Target Context ownership of target truth (Story 1-3)

Story 1-4 must now wire player attack resolution so that Combat Core owns combat validity and result truth per ADR-0002. Input already emits raw intents (Story 1-3), and Locomotion owns movement truth (Story 1-2). This story focuses exclusively on light/heavy attack intent routing, combat validation, and placeholder hit/whiff resolution using read-only Target Context data.

**Constraints:**
- ADR-0002: Combat Core owns combat validation and result truth
- ADR-0003: Combat Core exposes read-only snapshots; presentation systems must not own combat truth
- ADR-0004: Manual VContainer registration only; no generated DI
- ADR-0005: M0Contracts.cs changes must remain contracts-only
- Control Manifest: Pure C# Authority for combat truth, Lock/Recovery Request Pattern
- No damage/health mutation in this story
- No parry/dodge integration (deferred to Story 1-6)
- No animation/root motion authority
- No VFX/camera polish
- One player, one active target max (M0 duel scope)

**Stakeholders:**
- Combat Core system owner
- Input Mapping system owner
- Locomotion system owner
- Target Context system owner
- Debug Overlay system owner

## Goals / Non-Goals

**Goals:**
- Wire Input to emit raw LightAttack/HeavyAttack intents to Combat Core
- Implement Combat Core attack validation (reject if recovering, invalid state)
- Implement Combat Core placeholder hit/whiff resolution using read-only Target Context
- Expose read-only combat state/result snapshot for debug and presentation
- Manual VContainer registration for Combat Core in GameplayLifetimeScope
- Maintain Pure C# authority (no combat truth in MonoBehaviours)
- Support movement restriction/recovery request shape if skeleton allows

**Non-Goals:**
- Damage/health mutation (deferred to later stories)
- Hit reaction implementation (deferred)
- Parry/dodge validation (deferred to Story 1-6)
- Counter window implementation beyond placeholder shape
- Enemy AI expansion
- Animation/root motion authority
- Combo system
- Stamina system
- Skill system
- VFX/camera polish
- Target-relative movement rewrite
- Locomotion rewrite
- Camera-owned combat or target truth
- Generated DI
- Legacy Input Manager usage
- Hardcoded device polling (Keyboard.current, Mouse.current, Gamepad.current)
- Unity object finding APIs (FindObjectOfType, FindFirstObjectByType, GameObject.Find, Resources.Load)

## Decisions

### Decision 1: Combat Core State Model

**Choice:** Use existing M0CombatCore skeleton FSM with minimal state additions for attack resolution.

**Rationale:**
- Combat Core skeleton already exists with provisional state model (Neutral, AttackStartup, AttackActive, AttackRecovery, etc.)
- Avoids re-architecting before feel is proven
- M0 scope is narrow (light/heavy attacks only)
- Alternative: Full state machine redesign — rejected as over-engineering for M0

### Decision 2: Attack Intent Routing

**Choice:** Extend M0InputRouter to emit LightAttackIntent and HeavyAttackIntent to injected M0CombatCore.

**Rationale:**
- Input already has M0InputRouter skeleton from Story 1-3
- Maintains separation: Input emits intent only, Combat Core decides validity
- Consistent with Story 1-3 Lock-On pattern
- Alternative: Direct InputActionAsset → Combat Core coupling — rejected (violates ADR-0002)

### Decision 3: Placeholder Hit/Whiff Resolution

**Choice:** Resolve hit if active target exists and is in range, whiff otherwise. No complex scoring.

**Rationale:**
- M0 scope is proving attack resolution, not final combat balance
- Spacing/timing truth can be read from Target Context snapshot
- Avoids premature optimization or complex scoring frameworks
- Alternative: Full hit detection system with raycasts, hurtboxes, scoring — rejected as out of scope

### Decision 4: Read-Only Snapshot Exposure

**Choice:** CombatCore exposes CombatResultSnapshot with init-only properties (no setters).

**Rationale:**
- ADR-0003 requires read-only boundaries for presentation systems
- Prevents accidental mutation from debug, UI, or camera
- Consistent with Target Context snapshot pattern from Story 1-3
- Alternative: Mutable snapshot with warnings — rejected (violates ADR-0003)

### Decision 5: Movement Restriction/Recovery Requests

**Choice:** Emit MovementRestrictionContext and RecoveryContext shapes if M0CombatCore skeleton supports them.

**Rationale:**
- Combat Core should notify Locomotion when movement is restricted (ADR-0002)
- Locomotion owns movement expression, Combat Core owns combat truth
- If skeleton lacks these shapes, add minimal placeholder shapes
- Alternative: Combat Core directly modifies Locomotion state — rejected (violates ADR-0002)

### Decision 6: Manual VContainer Registration

**Choice:** Register Combat Core in GameplayLifetimeScope with manual builder.Register call.

**Rationale:**
- ADR-0004 requires manual DI only
- Consistent with Story 1-3 pattern for Target Context
- Prevents accidental global registrations
- Alternative: VContainer.SourceGenerator — rejected (violates ADR-0004)

## Risks / Trade-offs

**Risk:** Combat Core skeleton may lack movement restriction/recovery context shapes
**Mitigation:** Add minimal placeholder shapes (MovementRestrictionContext, RecoveryContext) if missing; document as provisional

**Risk:** Placeholder hit/whiff resolution may be too simple for meaningful testing
**Mitigation:** Accept as M0 limitation; focus on proving attack intent routing and validation, not final hit detection

**Risk:** Target Context snapshot may not provide all spacing/timing data needed for resolution
**Mitigation:** Use available data; note gaps as follow-up for later stories

**Trade-off:** Narrow scope (light/heavy only) vs. broader attack framework
**Decision:** Narrow scope — M0 is about proving duel loop, not building full RPG combat

**Trade-off:** Placeholder resolution vs. full hit detection
**Decision:** Placeholder resolution — M0 is about proving combat authority and intent flow, not final combat feel

## Migration Plan

No migration required — this is new functionality in M0 prototype. Combat Core skeleton exists but attack resolution is not yet wired.

**Rollback Strategy:**
- Delete attack intent routing code from M0InputRouter
- Remove Combat Core validation/resolution logic
- Remove Combat Core VContainer registration
- Restore M0Contracts.cs to pre-change state

## Open Questions

None — scope is narrow and well-defined by story acceptance criteria and exclusions.
