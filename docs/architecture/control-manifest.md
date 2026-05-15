# Control Manifest

> **Engine**: Unity 6000.3.x + URP
> **Last Updated**: 2026-05-15
> **Manifest Version**: 2026-05-15
> **ADRs Covered**: ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0005
> **Status**: Active — regenerate with `/create-control-manifest update` when ADRs change

`Manifest Version` is the date this manifest was generated. Story files embed this date when created. `/story-readiness` compares a story's embedded version to this field to detect stories written against stale rules.

This manifest is a programmer's quick-reference extracted from all Accepted ADRs and technical preferences. For the reasoning behind each rule, see the referenced ADR.

---

## Foundation Layer Rules

*Applies to: scene management, event architecture, DI composition, bootstrap*

### Required Patterns
- **Unity 6000.3.x + URP** — Strictly adhere to Unity 6 LTS and URP features. — source: [ADR-0001]
- **Additive Scene Composition** — Load scenes in strict order: Bootstrap → Systems → Level → Gameplay → Camera → UI. — source: [ADR-0001]
- **Manual VContainer Registration** — All registrations MUST be manual in composition roots. — source: [ADR-0004]
- **Scene-Scoped Lifetimes** — Gameplay truth must be registered in `GameplayScope`, not `ProjectRoot`. — source: [ADR-0001]
- **Bootstrap Responsibility** — Bootstrap owns scene orchestration and global config only. — source: [ADR-0001]

### Forbidden Approaches
- **Never use Generated DI** — Nhem-generated DI or automatic scanning is explicitly deferred for M0. — source: [ADR-0004]
- **Never use Legacy Input Manager** — Only Unity New Input System (Input Actions) is permitted. — source: [ADR-0002]
- **No Global Singletons for Truth** — Gameplay state must not live in `ProjectRoot` or static singletons. — source: [ADR-0002]
- **No Cross-Scene Implicit Dependencies** — All dependencies must be explicitly wired via VContainer scopes. — source: [ADR-0001]

---

## Core Layer Rules

*Applies to: combat, locomotion, target context, health, enemy intent, pure C# truth*

### Required Patterns
- **Pure C# Authority** — All authoritative gameplay state MUST exist in Pure C# classes/structs. — source: [ADR-0002]
- **Input Intents Only** — Input system MUST emit raw intents (Axis2, bool) only; no interpretation. — source: [ADR-0002]
- **M0Contracts Contracts-Only** — `M0Contracts.cs` is a contracts-only hub (DTOs, enums, structs, interfaces). — source: [ADR-0005]
- **Ownership Separation** — Locomotion owns movement; Combat Core owns validity; Enemy Intent owns telegraphs. — source: [ADR-0002]
- **Lock/Recovery Request Pattern** — Combat Core requests locks/recovery; Locomotion expresses them. — source: [ADR-0002]

### Forbidden Approaches
- **Never store truth in MonoBehaviours** — MonoBehaviours may cache view/scene state, but must not own gameplay truth (combat, locomotion, health, etc.). — source: [ADR-0002]
- **No Behavior in M0Contracts** — Never add logic, service location, or Unity object ownership to the contracts hub. — source: [ADR-0005]
- **Core references nothing** — The `Core` assembly/layer MUST NOT reference any other implementation assembly. — source: [ADR-0002]
- **No hidden authorities** — Systems must not "infer" truth owned by another system; consume owned snapshots instead. — source: [ADR-0002]

---

## Presentation Layer Rules

*Applies to: camera, animator, VFX, UI, debug overlay*

### Required Patterns
- **Read-Only Observation** — Presentation systems MUST observe gameplay truth as read-only snapshots or context. — source: [ADR-0003]
- **Animator Presentation-Only** — The Animator state machine is a view of combat/locomotion, not the owner. — source: [ADR-0003]
- **Camera Movement Basis** — Camera provides read-only basis (forward/right); Locomotion interprets it. — source: [ADR-0002]
- **Debug Snapshot Aggregation** — Debug Overlay groups read-only snapshots from gameplay systems. — source: [ADR-0003]

### Forbidden Approaches
- **No Mutation from Presentation** — Presentation systems (Camera, VFX, UI) MUST NOT mutate gameplay state. — source: [ADR-0003]
- **No Inference in Debug** — Debug Overlay must not create, infer, repair, or override gameplay truth. — source: [ADR-0003]
- **Camera does not drive targets** — Camera framing follows target context truth; it does not decide the target. — source: [ADR-0002]

---

## Global Rules

### Naming Conventions
| Element | Convention | Example |
|---------|-----------|---------|
| Snapshots | `[System]Snapshot` | `CombatSnapshot` |
| Contexts | `[System]Context` | `RecoveryContext` |
| Intents | `[Action]Intent` | `DodgeIntent` |
| Contracts | `I[Name]` or `[Name]Result` | `IInputIntentSource` |

### Forbidden APIs (Unity 6.3)
- `Input.GetKey/GetAxis` — source: [ADR-0002]
- `Resources.Load` — use Addressables later or scene references now.
- `GameObject.Find` — use dependency injection via VContainer.
- `Canvas / UGUI` — UI Toolkit is preferred for M0.

### Approved Libraries
- **VContainer** — Authoritative DI.
- **Input System** — Authoritative Input.
- **Cinemachine 3** — Authoritative Camera.
- **R3** — Approved for event streams (used cautiously).
