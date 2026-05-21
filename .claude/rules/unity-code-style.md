# Unity Code Style Rules — Glass Refrain

## Purpose

These rules define how Unity-facing C# code should be written in `Glass Refrain`. The goal is clean, testable gameplay code where Unity components adapt the engine to the project instead of owning all gameplay truth.

## MonoBehaviour Rule

MonoBehaviours should be thin adapters.

Allowed in MonoBehaviour:

- Unity lifecycle methods
- serialized references
- scene binding
- calling injected services
- presentation updates
- forwarding input/view events

Avoid in MonoBehaviour:

- combat truth
- state machine truth
- damage validation
- target validity rules
- memory reveal rules
- complex gameplay rules

Good:

```csharp
public sealed class PlayerLocomotionView : MonoBehaviour
{
    [SerializeField] private CharacterController characterController;
    [SerializeField] private Animator animator;

    private IPlayerLocomotionStateReader _locomotion;

    [Inject]
    public void Construct(IPlayerLocomotionStateReader locomotion)
    {
        _locomotion = locomotion;
    }

    private void Update()
    {
        var snapshot = _locomotion.CurrentSnapshot;
        animator.SetFloat("Speed", snapshot.Speed);
    }
}
```

Bad:

```csharp
public sealed class PlayerController : MonoBehaviour
{
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            // input, dodge validation, stamina, parry, damage, animation, camera, VFX all here
        }
    }
}
```

## Serialized Fields

Use `[SerializeField] private` instead of public fields.

Good:

```csharp
[SerializeField] private float moveSpeed = 5f;
[SerializeField] private Transform cameraRoot;
```

Bad:

```csharp
public float moveSpeed;
public Transform cameraRoot;
```

## Field Ordering

Recommended order inside a class:

```txt
constants
static readonly fields
serialized fields
private fields
public properties
constructor / Inject methods
Unity lifecycle
public methods
private methods
debug methods
```

Example:

```csharp
public sealed class Example : MonoBehaviour
{
    private const float DefaultSpeed = 5f;

    [Title("References")]
    [SerializeField] private Transform cameraRoot;

    [Title("Tuning")]
    [SerializeField] private float moveSpeed = DefaultSpeed;

    private IInputReader _inputReader;
    private Vector3 _velocity;

    public bool IsActive { get; private set; }

    [Inject]
    public void Construct(IInputReader inputReader)
    {
        _inputReader = inputReader;
    }

    private void Awake() { }
    private void OnEnable() { }
    private void Update() { }
    private void OnDisable() { }
    private void OnDestroy() { }

    private void Move() { }
}
```

## Unity Lifecycle

Keep lifecycle methods short.

Good:

```csharp
private void Update()
{
    _locomotion.Tick(Time.deltaTime);
}
```

Bad:

```csharp
private void Update()
{
    // 200 lines of input, movement, combat, camera, animation, VFX
}
```

## Awake / Start Rule

Use `Awake` for local component setup.

Use `Start` only when scene objects need to finish initialization first.

Prefer VContainer injection for dependencies.

Avoid:

```csharp
private void Start()
{
    _combat = FindObjectOfType<CombatCoreService>();
}
```

## No Runtime Object Search

Avoid runtime usage of:

```csharp
FindObjectOfType<T>();
FindFirstObjectByType<T>();
GameObject.Find();
Camera.main;
```

Allowed only in:

- temporary prototype code
- editor tools
- debug-only code
- clearly marked migration code

Temporary usage must be marked:

```csharp
// TODO M0_PROTOTYPE: Replace with VContainer injection.
```

## No Hidden Singleton Gameplay Truth

Avoid:

```csharp
GameManager.Instance
CombatManager.Instance
ServiceLocator.Get<T>()
```

Gameplay truth should come from explicit dependency injection or explicit scene ownership.

## New Input System Only

Use Unity New Input System.

Do not use legacy input for gameplay:

```csharp
Input.GetKey
Input.GetAxis
Input.GetButton
```

Allowed only for temporary editor/debug shortcuts guarded by project define symbols.

```csharp
#if GR_DEBUG_OVERLAY
if (Keyboard.current.f1Key.wasPressedThisFrame)
{
    _debugOverlay.Toggle();
}
#endif
```

## Animator Rule

Animator is presentation only.

Animator must not own:

- combat truth
- locomotion truth
- dodge timing
- parry timing
- recovery duration
- hit validity
- counter window

Good:

```csharp
_combatStateMachine.EnterDodge();
_animator.Play(DodgeAnimationName);
```

Bad:

```csharp
if (animator.GetCurrentAnimatorStateInfo(0).IsName("Dodge"))
{
    isInvincible = true;
}
```

Animation events may request sync points, but gameplay systems must validate timing.

## DOTween Rule

DOTween must not drive authoritative combat motion or locomotion.

DOTween is allowed for:

- UI animation (menus, HUD transitions)
- camera polish (subtle shakes, blend smoothing)
- reveal beats and memory presentation
- environmental motion (ambient, non-interactive)
- visual polish that does not decide combat outcomes

DOTween must not:

- move the player character (use Player Locomotion service)
- move the enemy (use Enemy Intent / Telegraph service)
- decide dodge distance, attack range, or hit position
- override movement restrictions
- set gameplay truth

DOTween animation of camera is allowed for presentation, but must not circumvent the combat camera's framing logic.

## Root Motion Rule

Root motion is not gameplay authority by default.

Allowed:

- presentation polish
- synced movement after gameplay approval
- authored attack movement if validated by Player Locomotion

Not allowed:

- root motion secretly deciding hit range
- root motion bypassing movement restrictions
- root motion owning dodge distance without gameplay state

## Debug Code

Debug-only code must be guarded by project defines.

Allowed defines:

```txt
GR_M0_PROTOTYPE
GR_DEBUG_OVERLAY
GR_COMBAT_DEBUG
GR_MEMORY_DEBUG
```

Avoid generic defines:

```txt
DEBUG
TEST
ENABLE
```

Good:

```csharp
#if GR_COMBAT_DEBUG
public void DebugForceCounterWindow()
{
    _combatCore.DebugForceCounterWindow();
}
#endif
```

## Comments

Prefer code clarity over comments.

Use comments for:

- design intent
- non-obvious tradeoff
- temporary prototype limitation
- ownership boundary
- performance reason

Avoid comments that repeat code.

Bad:

```csharp
// Set speed to 5
moveSpeed = 5f;
```

Good:

```csharp
// M0: Keep dodge distance authored here until locomotion tuning stabilizes.
[SerializeField] private float dodgeDistance = 3f;
```
