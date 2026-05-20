# AGENTS.md — Glass Refrain / afterimage-tokyo

## Project Identity

`Glass Refrain` is a long-term single-player semi-linear action RPG with a sad, mysterious, memory-based tone.

M0 focuses on proving a katana combat feel prototype in a Tokyo Street duel space.

Current M0 loop:

```txt
read → evade/parry → counter → reveal
```

Build only what helps prove one readable duel with:

* one player
* one simple enemy
* one arena
* target focus
* camera readability
* hit reaction
* enemy telegraph
* restrained memory reveal response
* debug visibility

---

## Technology Stack

* Engine: Unity 6000.3.x
* Language: C#
* Render Pipeline: URP
* Input: Unity New Input System
* DI: VContainer
* Reactive: R3
* Async: Unity Awaitable first, UniTask when needed
* Inspector: Odin Inspector
* Version Control: Git with trunk-based development
* Build System: Unity Build Pipeline
* Asset Pipeline: Unity Asset Import Pipeline
* Addressables: planned long-term, not required for M0

---

## Rule Files

Follow project rules under:

```txt
.claude/rules/
```

Important rule groups:

```txt
csharp-naming.md
unity-code-style.md
solid-architecture.md
folder-ownership.md
odin-inspector.md
vcontainer.md
code-quality.md
testing.md
gameplay-scope.md
```

If a specific rule file conflicts with this root file, the more specific rule file wins.

---

## External References

Project structure:

```txt
.claude/docs/directory-structure.md
```

Engine version reference:

```txt
docs/engine-reference/unity/VERSION.md
```

Technical preferences:

```txt
.claude/docs/technical-preferences.md
```

Coordination rules:

```txt
.claude/docs/coordination-rules.md
```

Coding standards:

```txt
.claude/docs/coding-standards.md
```

Context management:

```txt
.claude/docs/context-management.md
```

---

## Collaboration Protocol

User-driven collaboration, not autonomous execution.

Large or ambiguous tasks should follow:

```txt
Question → Options → Decision → Draft → Approval
```

Rules:

* Ask before large, destructive, or multi-file changes unless the user explicitly requested file generation or editing.
* Show a draft or summary before writing major design/code files.
* Multi-file changes require explicit approval for the full changeset.
* No commits without user instruction.
* No destructive Git commands without explicit approval.
* Prefer small, reviewable patches.
* For very small edits, typo fixes, or explicitly requested file generation, agents may proceed directly if the intent is clear.

---

## Current Priority

The current priority is M0 combat feel.

Do not add systems that are not required to prove:

```txt
read → evade/parry → counter → reveal
```

Allowed M0 focus:

* input mapping
* player locomotion
* combat core
* health / damage / hit reaction
* enemy intent / telegraph
* lock-on / target context
* lock-on / combat camera
* memory state
* memory VFX response
* encounter framework
* debug overlay

Defer unless explicitly requested:

* full RPG stats
* loot
* equipment
* skill tree
* save system
* boss framework
* multi-enemy combat
* full HUD
* full narrative framework
* district reinterpretation
* broad enemy roster
* open-world systems
* multiplayer or network systems

---

## Core Working Rules

* Do not add survival mechanics unless explicitly requested.
* Prefer small, testable vertical slices over large speculative systems.
* Every new gameplay system must state:

  * intent
  * player-facing feel
  * dependencies
  * debug visibility
  * test strategy
* Combat feel, readability, and ownership boundaries are more important than feature quantity during M0.
* If a feature does not improve the M0 duel loop, defer it.

---

## Unity Rules

* Target Unity 6000.3.x unless the project version changes.
* Use URP.
* Use Unity New Input System.
* Do not use legacy `Input.GetKey`, `Input.GetAxis`, or `Input.GetButton` for gameplay input.
* Legacy input is allowed only for temporary debug code guarded by project defines.
* Keep MonoBehaviours thin.
* Prefer pure C# services for gameplay logic.
* Scene objects should adapt Unity lifecycle to application/domain services.
* Animator is presentation only and must not own gameplay truth.
* Root motion is not gameplay authority by default.
* Cinemachine/camera systems support readability; they must not decide combat outcomes.

---

## Architecture Rules

Follow Clean Architecture boundaries where practical:

```txt
Domain         → pure rules and data
Application    → orchestration / use cases
Infrastructure → Unity/package/external implementations
Presentation   → UI, camera, VFX, input presentation
Bootstrap      → dependency composition and scene setup
```

Rules:

* Do not let Presentation own gameplay truth.
* Do not let Infrastructure leak into Domain.
* Do not create global singleton managers unless explicitly approved.
* Avoid god classes such as `GameManager`, `CombatManager`, or `PlayerManager`.
* Prefer specific names like `CombatCoreService`, `TargetContextService`, `DamageResolver`, `EncounterLifecycleService`.
* Prefer composition over inheritance.
* Prefer small interfaces over broad service interfaces.
* Split read and command interfaces when it improves dependency direction.

---

## System Ownership Rules

`Combat Core` owns:

* combat action validity
* light/heavy attack request validation
* dodge result
* parry result
* counter opportunity
* `CounterWindow`
* hit resolution
* reveal request context

`Player Locomotion` owns:

* movement truth
* dodge movement expression
* facing/orientation support
* movement restrictions
* recovery movement

`Enemy Intent & Telegraph` owns:

* enemy telegraph
* commitment
* active/recovery timing
* attack tags
* enemy punish windows

`Health / Damage / Hit Reaction` owns:

* health values
* damage application after confirmed combat result
* hit reaction classification
* defeat/disabled consequence

`Lock-On / Target Context` owns:

* target focus active/inactive truth
* current target
* target validity
* target direction/context

`Lock-On & Combat Camera` owns:

* duel framing
* camera readability
* target-focus presentation support
* restrained camera feedback after confirmed context

`Memory State` owns:

* reveal request acceptance/rejection
* memory response state
* reveal cooldown/reset if needed

`Memory VFX Response` owns:

* visual response after accepted memory context
* restrained reveal VFX state
* VFX timing/intensity presentation

`Encounter Framework` owns:

* encounter lifecycle
* participant registration
* readiness blockers
* start/end/reset reasons

`Debug Overlay` owns:

* read-only display organization
* debug snapshot presentation
* visibility toggles
* debug labels

`Debug Overlay` must never own gameplay truth.

---

## Dependency Injection

* Use VContainer.
* Prefer constructor injection for pure services.
* Use method injection for MonoBehaviours.
* LifetimeScope should compose dependencies, not contain gameplay logic.
* Gameplay runtime truth should be scoped to gameplay scene scope.
* Do not register combat runtime truth in project root scope.
* Avoid manual `Resolve` during gameplay.
* Manual registration is allowed during M0, but mark it clearly as temporary.

Example temporary note:

```csharp
// M0 Technical Skeleton: manual registration until source-generation guardrails stabilize.
```

---

## Project Define Symbols

Use project-prefixed symbols:

```txt
GR_M0_PROTOTYPE
GR_DEBUG_OVERLAY
GR_COMBAT_DEBUG
GR_MEMORY_DEBUG
```

Avoid generic symbols:

```txt
DEBUG
TEST
ENABLE
```

---

## Naming Rules

Private runtime fields use `_camelCase`:

```csharp
private float _currentHealth;
private bool _isCounterWindowOpen;
private ICombatCoreService _combatCore;
```

Serialized private fields do not use `_`:

```csharp
[SerializeField] private float moveSpeed;
[SerializeField] private Transform cameraRoot;
```

Odin/Inspector-facing private fields also do not use `_`:

```csharp
[SerializeField, Required] private Animator animator;
[SerializeField, MinValue(0f)] private float dodgeDistance;
```

Private readonly dependencies use `_camelCase`:

```csharp
private readonly ITimeProvider _timeProvider;
private readonly ITargetContextReader _targetContext;
```

Constants use `PascalCase`:

```csharp
private const float DefaultMoveSpeed = 5f;
```

Static readonly fields use `PascalCase`:

```csharp
private static readonly int SpeedHash = Animator.StringToHash("Speed");
```

Properties and methods use `PascalCase`:

```csharp
public bool IsDodging { get; private set; }
public bool TryRequestDodge(out CombatRequestResult result);
```

Boolean names should prefer:

```txt
Is...
Has...
Can...
Should...
Requires...
```

Avoid vague names:

```txt
data
manager
handler
controller
temp
obj
thing
```

Use `Manager`, `Handler`, `Controller`, `Helper`, or `Util` only when the responsibility is truly broad and justified.

---

## File Naming Rules

* One main public type per file.
* File name must match the main public type.
* Use clear responsibility names.

Good:

```txt
CombatCoreService.cs
ICombatCoreService.cs
PlayerLocomotionMotor.cs
DamageRequest.cs
TargetContextSnapshot.cs
```

Bad:

```txt
CombatStuff.cs
GameplayHelpers.cs
NewBehaviourScript.cs
Manager.cs
```

Namespaces should match project and layer:

```csharp
namespace GlassRefrain.Domain.Combat;
namespace GlassRefrain.Application.Combat;
namespace GlassRefrain.Infrastructure.Input;
namespace GlassRefrain.Presentation.Debug;
```

---

## Odin / Serialization

* Prefer Odin Inspector for clearer authoring and debug visibility.
* Use `SerializedMonoBehaviour` only when Odin serialization is actually needed.
* Default to normal `MonoBehaviour` for simple Unity references.
* Use Odin for:

  * required references
  * grouped inspector fields
  * validation
  * read-only debug display
  * dictionaries
  * polymorphic serialized data
* Do not use Odin to hide messy architecture.
* Do not expose mutable runtime state unless it is explicitly a debug tool.

Use `SerializedMonoBehaviour` when needed for:

```txt
Dictionary
interface field
polymorphic serialized data
complex nested config
Odin-serialized authored data
```

Use normal `MonoBehaviour` when Unity serialization is enough.

---

## Code Quality

* Prefer small classes with one clear responsibility.
* Prefer small methods with early returns.
* Use request/result objects for gameplay actions that can fail.
* Do not throw exceptions for normal gameplay rejection.
* Use exceptions for programmer errors or invalid setup only.
* Avoid per-frame allocations in hot gameplay code.
* Avoid heavy LINQ in hot `Update`/tick paths.
* Use project logger wrapper instead of raw `Debug.Log` everywhere.
* Debug logs must be removable by define symbols or log level.
* Keep Unity lifecycle methods short.
* Prefer explicit state transitions over hidden side effects.
* Prefer boring, debuggable architecture over clever abstraction during M0.

---

## Async / Reactive Rules

* Use Unity Awaitable first for simple Unity async flows.
* Use UniTask when cancellation, composition, or performance control is needed.
* Use R3 for observable state, UI/debug observation, and reactive read models.
* Use MessagePipe for decoupled cross-system messages.
* Do not replace simple direct method calls with events/messages without a reason.
* Do not let reactive chains own hot combat truth.
* Hot combat state transitions should remain explicit and debug-visible.

---

## Testing

Prioritize tests for:

```txt
combat state transitions
damage request/result
target acquisition/release
memory reveal acceptance/rejection
input request routing
encounter lifecycle
debug snapshot shape
```

Use EditMode tests for pure C# rules.

Use PlayMode tests for Unity integration and scene composition.

Recommended test naming:

```csharp
MethodName_WhenCondition_ShouldExpectedResult()
```

Examples:

```csharp
RequestParry_WhenPlayerIsRecovering_ShouldReject()
ApplyDamage_WhenAmountIsPositive_ShouldReduceHealth()
AcquireTarget_WhenEnemyIsDefeated_ShouldReject()
```

Do not mark an M0 system complete unless:

* core behavior is implemented
* debug visibility exists
* key rejection reasons are testable
* ownership boundaries are respected
* no unrelated full-game systems were added

---

## Git / Workflow Rules

* Use trunk-based development unless project workflow changes.
* No commits without user instruction.
* No force push unless explicitly approved.
* No destructive Git commands without explicit approval.
* Summarize changed files, reason, risk, and test recommendation before commit.
* Keep changes patch-sized and reviewable.
* Do not commit Unity generated folders such as `Library/`, `Temp/`, `Obj/`, or build output.

---

## AI Agent Behavior

* Ask fewer questions; make reasonable assumptions and state them.
* Prefer patch-sized changes.
* Never invent APIs from packages.
* For Unity 6, VContainer, R3, UniTask, MessagePipe, Odin, ZLinq, DOTween, or new package APIs, verify against project code/docs before implementation.
* If uncertain, create a small spike or test first.
* When changing code, summarize:

  * changed files
  * reason
  * risk
  * test/run recommendation
* Respect user-driven collaboration.
* Do not perform large autonomous changes without approval.

---

## M0 Definition Of Done

M0 is not complete because many systems exist.

M0 is complete when a tester can repeatedly fight one simple enemy in the prototype arena and clearly understand:

* what the enemy intended
* what defensive answer was available
* when the counter window appeared
* why they succeeded or failed
* what changed when the reveal happened

If the tester cannot explain those points, the prototype has not proven M0 yet.


## Logging Rule — NhemLogger Only

Project code must use the project logging wrapper, `NhemLogger` / `NhemLogging`, built on ZLogger.

Do not add direct Unity logging calls in gameplay/application/presentation code:

- `UnityEngine.Debug.Log`
- `UnityEngine.Debug.LogWarning`
- `UnityEngine.Debug.LogError`
- `Debug.Log`
- `Debug.LogWarning`
- `Debug.LogError`

Allowed exceptions:
- Inside the NhemLogger/NhemLogging implementation itself.
- Temporary local experiments that are removed before commit.
- Vendor/package code that we do not own.
- Explicitly approved Unity tooling/editor diagnostics.

When adding logs, use structured, readable tags:

```txt
[M0Combat]
[M0Input]
[M0Enemy]
[M0Debug]
[M0Memory]
[M0Targeting]