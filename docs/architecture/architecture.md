# Glass Refrain — Master Architecture

## Document Status

- **Version**: 1.0 (Phase 7 Complete)
- **Last Updated**: 2025-01-15
- **Engine**: Unity 6000.3.x URP
- **GDDs Covered**: All 11 M0 systems
- **ADRs Referenced**: ADR-0001 through ADR-0005 (all Accepted); ADR-0006 through ADR-0010 (Recommended)
- **Technical Director Sign-Off**: [Awaiting Review]
- **Lead Programmer Feasibility**: [Awaiting Review]

This document translates all 11 M0 system GDDs into a concrete technical architecture blueprint. It defines system layer mapping, module ownership boundaries, data flows, API contracts, and architectural decisions. All 25 technical requirements from GDDs are traced to existing ADRs with zero coverage gaps.

---

## Engine Knowledge Gap Summary

**Engine**: Unity 6000.3.x with URP
**LLM Training Covers**: Up to approximately Unity 6 (2024 Q2)
**Post-Cutoff Risk Domains**:

### HIGH RISK (Verify Against Engine Docs)
- **Input System**: Unity 6 deprecated legacy `Input` class; New Input System is post-cutoff (verified as active in current API)
  - Impact: All gameplay input must route through New Input System via abstraction; legacy input forbidden
  - Mitigation: Input Mapping service abstracts away API details; verified against `docs/engine-reference/unity/deprecated-apis.md`

### MEDIUM RISK (Verify Key APIs)
- **Cinemachine 3.x**: Major rewrite from 2.x; API structure changed significantly
  - Impact: Virtual camera composition, priority blending, composer algorithms differ
  - Mitigation: Lock-On & Camera module uses contract-first approach; camera APIs isolated in presentation layer
- **VContainer**: Post-cutoff DI library
  - Impact: Manual vs source-generation trade-offs
  - Mitigation: ADR-0004 locks M0 to manual registration; deferred post-M0

### LOW RISK (In Training Data)
- Scene management (additive loading)
- Pure C# FSM patterns
- MonoBehaviour lifecycle
- Animator presentation-only patterns
- URP rendering pipeline basics

### Systems Touching HIGH/MEDIUM Risk Domains

| System | Domain | Risk | Mitigation |
|---|---|---|---|
| Input Mapping | New Input System | HIGH | Verified; contracts in place |
| Lock-On & Camera | Cinemachine 3 | MEDIUM | Presentation-only; read-only pattern |
| Player Locomotion | Physics (optional) | LOW | Direct Transform if no Rigidbody |
| Core Runtime | VContainer | MEDIUM | ADR-0004 manual pattern stable |

---

## System Layer Map

All 11 M0 systems organized into 5 architectural layers:

```
┌──────────────────────────────────────────────────────────────┐
│ PRESENTATION LAYER                                           │
│ • Lock-On & Combat Camera (Cinemachine framing)              │
│ • Memory VFX Response (distortion, particles)                │
│ • Debug Overlay (read-only snapshot display)                 │
├──────────────────────────────────────────────────────────────┤
│ CORE GAMEPLAY LAYER                                          │
│ • Combat Core (action validation, hit resolution)            │
│ • Player Locomotion (movement truth, recovery)               │
│ • Health / Damage / Hit Reaction (health application)        │
│ • Enemy Intent & Telegraph (state machine, timing)           │
│ • Lock-On / Target Context (target focus, validity)          │
│ • Memory State (reveal acceptance/rejection logic)           │
├──────────────────────────────────────────────────────────────┤
│ FOUNDATION LAYER                                             │
│ • Core Runtime Foundation (bootstrap, DI composition)        │
│ • Input Mapping (intent routing, New Input System abstraction) │
│ • Scene Composition (additive loading, scene roles)          │
│ • Encounter Framework (lifecycle, participant mgmt)          │
├──────────────────────────────────────────────────────────────┤
│ PLATFORM LAYER                                               │
│ • Unity 6000.3.x + URP                                       │
│ • VContainer DI                                              │
│ • New Input System                                           │
│ • Cinemachine 3.x                                            │
│ • Animator (presentation only)                               │
└──────────────────────────────────────────────────────────────┘
```

### Layer Assignment Summary

| Layer | Systems | Count | Rationale |
|---|---|---|---|
| **PRESENTATION** | Lock-On & Camera, Memory VFX, Debug Overlay | 3 | Observation-only; consume game state; never own truth |
| **CORE** | Combat Core, Locomotion, Health, Enemy Intent, Target Context, Memory State | 6 | All gameplay truth ownership; explicit state machines |
| **FOUNDATION** | Core Runtime, Input Mapping, Scene Composition, Encounter | 4 | Infrastructure and encounter lifecycle |
| **PLATFORM** | Unity 6, VContainer, Input System, Cinemachine | — | Engine and libraries |

---

## Module Ownership Map

### Core Gameplay Layer Modules

#### **Combat Core**
**Owns**:
- Combat state machine (Idle → Attack → Dodge → Parry → Counter → Recovery)
- Action validation rules
- Hit/miss/parry/counter result resolution
- CounterWindow timing and validation
- Reveal request context generation
- Action lock and recovery frame windows

**Exposes**:
```csharp
CombatRequestResult RequestLightAttack()
CombatRequestResult RequestHeavyAttack()
CombatRequestResult RequestDodge(Vector3 direction)
CombatRequestResult RequestParry()
HitResolutionResult ValidateHit(HitContext context)
CounterWindowState GetCounterWindow()
bool IsInCounterWindow()
CombatStateName GetCurrentState()
RevealRequestContext GetRevealContext()
void DebugDumpState()
```

**Consumes**: Input intent, Enemy telegraph (observes), Target context, Player locomotion (observes)
**Engine APIs**: None directly (pure C# state machine)

---

#### **Player Locomotion**
**Owns**:
- Position and velocity truth
- Facing direction and rotation
- Dodge displacement and animation timing
- Movement recovery state after actions
- Sprint/walk/stance transitions

**Exposes**:
```csharp
MovementRequestResult RequestMove(Vector2 direction, float speed)
MovementRequestResult RequestDodge(Vector2 direction)
Vector3 GetPosition()
Quaternion GetFacing()
Vector3 GetVelocity()
bool IsRecovering()
LocomotionStateName GetCurrentState()
void LockMovement(float frames)
void DebugDumpState()
```

**Consumes**: Input intent (movement/look), Combat recovery context, Encounter active state
**Engine APIs**: `Transform` (position, rotation), `Rigidbody.velocity` (if physics-based), `Animator.SetFloat()` (presentation only)

---

#### **Health / Damage / Hit Reaction**
**Owns**:
- Current health value
- Max health value
- Damage application after combat validation
- Hit reaction category (light/medium/heavy/knockdown)
- Defeat/disabled consequence

**Exposes**:
```csharp
DamageApplicationResult ApplyDamage(DamageContext damage)
float GetCurrentHealth()
float GetMaxHealth()
bool IsDefeated()
HitReactionType GetLastReactionType()
void Reset()
void DebugDumpState()
```

**Consumes**: Hit result from Combat Core (after validation), Defeat event context
**Engine APIs**: None directly (pure C# service)

---

#### **Enemy Intent & Telegraph**
**Owns**:
- Enemy attack telegraph state (windup, commitment, active, recovery)
- Enemy attack tags (light/heavy/grab/unblockable)
- Vulnerability windows
- Enemy attack timing and rhythm data

**Exposes**:
```csharp
TelegraphState GetTelegraphState()
bool IsVulnerable()
FrameRange GetVulnerabilityWindow()
IReadOnlySet<AttackTag> GetCurrentAttackTags()
int GetRecoveryFramesRemaining()
void Reset()
void DebugDumpState()
```

**Consumes**: Encounter active state, (observes player state for threat)
**Engine APIs**: Animator state machine (observes for telegraph timing)

---

#### **Lock-On / Target Context**
**Owns**:
- Target focus state (active/inactive)
- Current target identity
- Target validity (alive, in range)
- Target direction and distance

**Exposes**:
```csharp
TargetRequestResult RequestAcquireTarget(TargetEntity target)
TargetRequestResult RequestReleaseTarget()
TargetEntity GetCurrentTarget()
bool IsTargetValid()
Vector3 GetTargetDirection()
float GetTargetDistance()
bool IsLockedOn()
void Reset()
void DebugDumpState()
```

**Consumes**: Input intent (lock-on toggle), Player position, Enemy position/state, Health state
**Engine APIs**: `Transform` for distance calculation

---

#### **Memory State**
**Owns**:
- Reveal request acceptance/rejection logic
- Current memory distortion state
- Reveal cooldown or guard
- Memory state debug visibility

**Exposes**:
```csharp
RevealRequestResult ProcessRevealRequest(RevealRequestContext context)
MemoryStateValue GetCurrentMemoryState()
bool CanRevealAgain()
float GetTimeUntilNextReveal()
void Reset()
void DebugDumpState()
```

**Consumes**: Reveal request context from Combat Core (only after validation), Hit result, Encounter state
**Engine APIs**: None directly (pure C# service)

---

### Foundation Layer Modules

#### **Core Runtime Foundation**
**Owns**:
- Project root lifetime scope setup
- Application lifetime services (logger, config, save paths)
- VContainer root scope composition
- Scene loading orchestration

**Exposes**:
- Application bootstrap entry
- Scene load/unload interface
- Logger service
- Config/settings service

**Engine APIs**: `VContainer` DI, `SceneManager`

---

#### **Input Mapping**
**Owns**:
- Raw input state (keyboard, gamepad)
- Input action mappings
- Input intent routing
- Input enable/disable context

**Exposes**:
```csharp
Vector2 GetMovementIntent()
Vector2 GetLookIntent()
bool GetLightAttackPressed()
bool GetHeavyAttackPressed()
bool GetDodgePressed()
bool GetParryPressed()
bool GetLockOnToggled()
void EnableInput()
void DisableInput()
bool IsInputEnabled { get; }
void DebugDumpState()
```

**Consumes**: Unity New Input System, Encounter active state
**Engine APIs**: `UnityEngine.InputSystem.Keyboard`, `UnityEngine.InputSystem.Gamepad`, `UnityEngine.InputSystem.InputAction` ✓ (verified post-cutoff)

---

#### **Scene Composition**
**Owns**:
- Additive scene loading order and roles
- Scene persistence and lifecycle
- Scene separation (Bootstrap/Systems/Gameplay/Camera/UI/Level)

**Engine APIs**: `SceneManager.LoadSceneAsync()` with `LoadSceneMode.Additive`

---

#### **Encounter Framework**
**Owns**:
- Encounter lifecycle (Setup → Ready → Active → Ended)
- Participant registration and readiness
- Win/fail/reset conditions
- Encounter-level debug state

**Exposes**:
```csharp
EncounterSetupResult SetupEncounter()
EncounterStartResult StartEncounter()
void EndEncounter(EncounterEndReason reason)
void ResetEncounter()
EncounterState GetCurrentState()
bool IsEncounterActive()
bool RegisterParticipant(IEncounterParticipant participant)
void SignalParticipantReady(IEncounterParticipant participant)
void DebugDumpState()
```

**Consumes**: Combat Core state, Health state, Player/Enemy state, Memory State signals
**Engine APIs**: None directly (orchestration only)

---

### Presentation Layer Modules

#### **Lock-On & Combat Camera**
**Owns**:
- Cinemachine virtual camera priority and blending
- Camera framing algorithms
- Camera feedback state (bump, shake)
- Target-focus visual support

**Exposes** (read-only):
```csharp
CameraStateName GetCameraState()
bool IsFramingTarget()
Vector3 GetFrameDirection()
```

**Consumes**: Target context (read-only), Combat result (for feedback timing), Enemy telegraph, Player locomotion
**Forbidden**: Must NOT consume/own combat validation; must NOT drive gameplay truth
**Engine APIs**: `Cinemachine.CinemachineVirtualCamera`, `Cinemachine.CinemachineComposer`, `Cinemachine.CinemachineTransposer`

---

#### **Memory VFX Response**
**Owns**:
- Reveal VFX trigger and state
- Distortion shader parameters
- Reveal particle timing
- Memory state visual feedback

**Exposes** (read-only):
```csharp
MemoryVFXState GetMemoryVFXState()
```

**Consumes**: Memory State (read-only), Reveal request signal, Combat outcome
**Forbidden**: Must NOT own/validate reveal; must NOT drive memory gameplay truth
**Engine APIs**: `UnityEngine.VFX.VisualEffect` (VFX Graph), `UnityEngine.Material.SetFloat()`, `UnityEngine.ParticleSystem`

---

#### **Debug Overlay**
**Owns**:
- Debug snapshot assembly and display
- Frame-by-frame state visibility
- Debug toggle UI

**Exposes**:
- Read-only debug visualizations

**Consumes**: Combat state (read-only), Locomotion (read-only), Enemy Intent, Target Context, Memory State, Encounter state
**Forbidden**: Must NEVER own gameplay truth; must be toggleable without affecting gameplay
**Engine APIs**: `UI Toolkit` (`UIDocument`, labels)

---

## Dependency Diagram

```
INPUT MAPPING ─────────────────────────┐
                                       ↓
ENCOUNTER FRAMEWORK ← COMBAT CORE ← TARGET CONTEXT
        ↓                    ↓            ↓
   PLAYER LOCOMOTION    HEALTH/DAMAGE   ENEMY INTENT
        ↓                    ↓            ↓
        └────────────────────┴────────────┘
                    ↓
            MEMORY STATE
                    ↓
        ┌───────────┼───────────┐
        ↓           ↓           ↓
    CAMERA      VFX RESPONSE   DEBUG OVERLAY
   (Presentation — observation only, never owns gameplay truth)
```

---

## Data Flow

### Frame Update Path (60 fps Cycle)

```
[1] INPUT READS (Early)
    Input Mapping.OnUpdate()
    → MovementIntent, CombatIntent, LockOnToggle
    → Synchronous, no allocation

[2] GAMEPLAY SYSTEMS UPDATE (Mid)
    Encounter Framework orchestrates frame:
    ├─ Target Context (lock-on toggle intent)
    ├─ Player Locomotion (movement intent, recovery context)
    ├─ Combat Core (combat intent, enemy telegraph)
    ├─ Enemy Intent (telegraph state machine)
    ├─ Health / Damage (process hit result)
    └─ Memory State (reveal acceptance/rejection)

[3] RENDERING SYSTEMS (Late)
    ├─ Lock-On & Camera (framing, feedback)
    ├─ Memory VFX Response (distortion, particles)
    ├─ Debug Overlay (snapshot assembly)
    └─ Animator (visual sync)

All synchronous. Minimal allocations. Frame-readable state.
```

### Event/Signal Path (Cross-System Communication)

Counter success example:
```
Combat Core.ValidateParry() ← true
├─ Locomotion.LockMovement(recoveryFrames)
├─ Health.ProcessParrySuccess()
└─ Optional: R3 Observable for UI (non-truth)

Result:
├─ Combat state: CounterWindow open ✓
├─ Movement: Locked ✓
├─ Debug: "Counter window open: 12 frames" ✓
└─ UI: Optional counter timer (non-truth) ✓
```

### Initialization Order

1. Bootstrap → ProjectRootLifetimeScope
2. Systems → Persistent services
3. Gameplay → GameplayLifetimeScope (all systems instantiate)
4. Level → Environment, colliders
5. Camera → Cinemachine setup
6. UI → Debug overlay
7. Encounter.SetupEncounter() → All participants register and signal ready
8. Encounter.StartEncounter() → Active state, first frame updates begin

---

## API Boundaries (Public Contracts)

All modules expose explicit, synchronous, non-allocating APIs. No exceptions for normal rejections (use Result pattern from ADR-0005).

### Combat Core API

```csharp
public interface ICombatCoreService
{
    CombatStateName GetCurrentState();
    bool IsInCounterWindow();
    CounterWindowState GetCounterWindow();
    CombatRequestResult RequestLightAttack();
    CombatRequestResult RequestHeavyAttack();
    CombatRequestResult RequestDodge(Vector3 direction);
    CombatRequestResult RequestParry();
    HitResolutionResult ValidateHit(HitContext context);
    RevealRequestContext GetRevealContext();
    void DebugDumpState();
}
```

### Player Locomotion API

```csharp
public interface IPlayerLocomotionService
{
    Vector3 GetPosition();
    Quaternion GetFacing();
    Vector3 GetVelocity();
    bool IsRecovering();
    LocomotionStateName GetCurrentState();
    MovementRequestResult RequestMove(Vector2 direction, float speed);
    MovementRequestResult RequestDodge(Vector2 direction);
    void LockMovement(float frames);
    void DebugDumpState();
}
```

### Health / Damage API

```csharp
public interface IHealthService
{
    float GetCurrentHealth();
    float GetMaxHealth();
    bool IsDefeated();
    HitReactionType GetLastReactionType();
    DamageApplicationResult ApplyDamage(DamageContext damage);
    void Reset();
    void DebugDumpState();
}
```

### Enemy Intent API

```csharp
public interface IEnemyIntentService
{
    TelegraphState GetTelegraphState();
    bool IsVulnerable();
    FrameRange GetVulnerabilityWindow();
    IReadOnlySet<AttackTag> GetCurrentAttackTags();
    int GetRecoveryFramesRemaining();
    void Reset();
    void DebugDumpState();
}
```

### Lock-On / Target Context API

```csharp
public interface ITargetContextService
{
    TargetEntity GetCurrentTarget();
    bool IsLockedOn();
    bool IsTargetValid();
    Vector3 GetTargetDirection();
    float GetTargetDistance();
    TargetRequestResult RequestAcquireTarget(TargetEntity target);
    TargetRequestResult RequestReleaseTarget();
    void Reset();
    void DebugDumpState();
}
```

### Memory State API

```csharp
public interface IMemoryStateService
{
    MemoryStateValue GetCurrentMemoryState();
    bool CanRevealAgain();
    float GetTimeUntilNextReveal();
    RevealRequestResult ProcessRevealRequest(RevealRequestContext context);
    void Reset();
    void DebugDumpState();
}
```

### Encounter Framework API

```csharp
public interface IEncounterFrameworkService
{
    EncounterState GetCurrentState();
    bool IsEncounterActive();
    EncounterSetupResult SetupEncounter();
    EncounterStartResult StartEncounter();
    void EndEncounter(EncounterEndReason reason);
    void ResetEncounter();
    bool RegisterParticipant(IEncounterParticipant participant);
    void SignalParticipantReady(IEncounterParticipant participant);
    void DebugDumpState();
}
```

### Input Mapping API

```csharp
public interface IInputMappingService
{
    Vector2 GetMovementIntent();
    Vector2 GetLookIntent();
    bool GetLightAttackPressed();
    bool GetHeavyAttackPressed();
    bool GetDodgePressed();
    bool GetParryPressed();
    bool GetLockOnToggled();
    void EnableInput();
    void DisableInput();
    bool IsInputEnabled { get; }
    void DebugDumpState();
}
```

---

## ADR Audit & Traceability

### Existing ADRs (All Accepted)

| ADR | Title | Status | Traceability |
|---|---|---|---|
| ADR-0001 | M0 Runtime Foundation and Scene Composition | Accepted | ✓ Covers Foundation layer, TR-ENCOUNTER-* |
| ADR-0002 | M0 Gameplay Truth Ownership Boundaries | Accepted | ✓ Covers all Core layer, TR-COMBAT-* through TR-MEMORY-* |
| ADR-0003 | M0 Presentation and Debug Read-Only Boundaries | Accepted | ✓ Covers Presentation layer, TR-CAMERA-*, TR-MEMORYVFX-*, TR-DEBUG-* |
| ADR-0004 | M0 DI and Assembly Boundary Strategy | Accepted | ✓ Covers Infrastructure, TR-INPUT-* |
| ADR-0005 | M0 Shared Contracts Strategy | Accepted | ✓ Covers cross-system communication contracts |

### Technical Requirements Coverage

**25/25 Technical Requirements Traced** to existing ADRs (zero gaps):
- TR-COMBAT-001 through TR-COMBAT-004: ADR-0002
- TR-LOCO-001 through TR-LOCO-003: ADR-0002, ADR-0003
- TR-HEALTH-001 through TR-HEALTH-003: ADR-0002, ADR-0005
- TR-ENEMY-001, TR-ENEMY-002: ADR-0002
- TR-TARGETING-001, TR-TARGETING-002: ADR-0002, ADR-0005
- TR-CAMERA-001, TR-CAMERA-002: ADR-0003
- TR-MEMORY-001, TR-MEMORY-002: ADR-0002
- TR-MEMORYVFX-001: ADR-0003
- TR-ENCOUNTER-001, TR-ENCOUNTER-002: ADR-0001
- TR-INPUT-001, TR-INPUT-002: ADR-0004
- TR-DEBUG-001, TR-DEBUG-002: ADR-0003

### Recommended New ADRs (Enhance Implementation Guidance)

**Must Have Before Coding** (High Priority):

1. **ADR-0006: Combat State Machine Design Pattern**
   - Covers: TR-COMBAT-001, TR-COMBAT-002, TR-COMBAT-004
   - Defines: Pure C# FSM structure, state transitions, validation rules
   - Unblocks: Combat Core implementation

2. **ADR-0007: Player Locomotion Movement Truth Implementation**
   - Covers: TR-LOCO-001, TR-LOCO-002, TR-LOCO-003
   - Defines: Movement ownership, coordinate systems, recovery windows
   - Unblocks: Locomotion service implementation

3. **ADR-0010: New Input System Integration and Intent Routing**
   - Covers: TR-INPUT-001, TR-INPUT-002
   - Defines: Action mapping pattern, intent query (no legacy Input), parity
   - Unblocks: Input Mapping service implementation

**Should Have Before Relevant System Built** (Medium Priority):

4. **ADR-0008: Counter-Window Timing Formula and Ratios**
   - Covers: TR-COMBAT-002
   - Defines: Counter timing contract (e.g., counter ≤ enemy recovery × 0.35)
   - Unblocks: Combat tuning phase

5. **ADR-0009: Encounter Framework Scene Composition and Lifecycle**
   - Covers: TR-ENCOUNTER-001, TR-ENCOUNTER-002
   - Defines: Participant init order, readiness signals, state transitions
   - Unblocks: Integration testing

---

## Architecture Principles

These principles govern all technical decisions for M0 and beyond:

1. **Gameplay Truth Ownership is Explicit**
   - All gameplay state lives in Pure C# services, not MonoBehaviours or presentation
   - State transitions are synchronous and frame-readable
   - No hidden truth in animations, VFX, or camera state

2. **Presentation is Always Downstream**
   - Camera, UI, VFX, and Animator observe gameplay state only
   - Presentation never makes gameplay decisions
   - Presentation responds to gameplay state; gameplay never depends on presentation timing

3. **Systems are Small and Focused**
   - Each system owns one clear responsibility
   - Systems communicate through explicit contracts and Result patterns
   - No "manager" systems that aggregate all responsibility

4. **Input is Intent Only**
   - Input Mapping routes raw input to intent (movement, attack, dodge, parry, lock-on)
   - Systems request actions; Input does not decide what happens
   - Input enable/disable is explicit and controlled by Encounter

5. **Core Gameplay is Synchronous**
   - Frame update cycle is entirely synchronous and deterministic
   - No async/await in hot gameplay path
   - Optional R3 Observables for UI binding (non-truth)

6. **Debugging is First-Class**
   - Every service exposes `DebugDumpState()` for inspection
   - Debug Overlay displays frame snapshot without affecting gameplay
   - State visibility supports iteration and tuning

---

## Open Questions

| ID | Summary | Priority | Resolution Path |
|---|---|---|---|
| QQ-01 | Counter-window timing ratios not yet published | High | ADR-0008 (publish formula before tuning iteration) |
| QQ-02 | Root motion decision (animation-driven vs manual control) | High | ADR-0007 (Locomotion design decision) |
| QQ-03 | Enemy AI system scope (included in M0 or deferred?) | Medium | ADR for Enemy Intent if behavior becomes complex |
| QQ-04 | Save/load scope for M0 (encounter-reset only or persistent?) | Low | Deferred; M0 uses encounter-reset only |
| QQ-05 | VContainer source generation (official vs custom tooling?) | Low | Deferred post-M0; manual VContainer for now (ADR-0004) |

---

## Assembly Definition Architecture

Per ADR-0004, M0 uses these assembly definitions:

```
GlassRefrain.Core
  ↑
GlassRefrain.Combat / Memory / Gameplay
GlassRefrain.Infrastructure
  ↑
GlassRefrain.Camera / UI / VFX
  ↑
GlassRefrain.Bootstrap
  ↑
GlassRefrain.Tests
```

**Forbidden Dependencies**:
- Core → anything
- Combat → Camera, UI, VFX, Bootstrap
- Memory → VFX, Camera, UI
- Domain → Bootstrap
- Runtime → Tests

---

## Deployment and Testing Strategy

### Unit Testing (EditMode)

- Combat Core: State machine transitions, action validation, hit resolution
- Locomotion: Movement request validation, recovery state
- Health: Damage application, defeat condition
- Memory State: Reveal acceptance/rejection rules
- Target Context: Target acquisition/release validation

### Integration Testing (PlayMode)

- Encounter lifecycle (Setup → Ready → Active → Ended)
- Frame-by-frame state consistency across all systems
- Cross-system data flows (Combat → Health → Memory VFX)
- Input routing and intent propagation
- Scene composition and initialization order

### Manual Testing (Prototype)

- Combat feel and readability (enemy telegraph, counter window)
- Dodge and parry feedback
- Reveal response and memory visual
- Camera framing during duel
- Input response on gamepad and keyboard

---

## Known Constraints and Risk Mitigations

| Constraint | Risk | Mitigation |
|---|---|---|
| New Input System (post-cutoff) | API may differ from training data | Verified against engine reference; Input Mapping abstraction shields gameplay from API details |
| Pure C# FSM complexity | May become hard to debug if states explode | Debug overlay + explicit state machine logging; ADR-0006 will establish FSM patterns |
| Presentation coupling to gameplay | Camera or UI may accidentally own state | Explicit forbidden dependencies in code review; Debug Overlay reads-only pattern enforces this |
| Counter-window tuning | Timing ratios not published; may cause spikes | ADR-0008 to publish timing formula before tuning iteration |

---

## Next Steps

1. **Write Required ADRs** (before coding):
   - ADR-0006: Combat State Machine Design
   - ADR-0007: Locomotion Movement Truth
   - ADR-0010: New Input System Integration

2. **Run `/create-control-manifest`** once required ADRs are written
   - Produces actionable rules sheet for programmers

3. **Run `/test-setup`** to scaffold unit and integration test structure

4. **Run `/ux-design`** to initialize interaction patterns and accessibility

5. **Gate-Check Pre-Production** when all required ADRs, test setup, and UX design are complete

---

## Document History

| Date | Version | Change | Author |
|---|---|---|---|
| 2025-01-15 | 1.0 | Initial master architecture document | Copilot (Codex Agent) |

---

**End of Master Architecture Document**
