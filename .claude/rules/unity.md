# Unity Rules — Glass Refrain

## Engine

- Target Unity 6000.3.x.
- Use URP.
- Use Unity New Input System.
- Do not use Legacy Input Manager for gameplay.

## MonoBehaviour Rule

MonoBehaviours should be thin adapters.

Allowed in MonoBehaviour:

- Unity lifecycle
- serialized references
- scene binding
- presentation hooks
- calling application/domain services

Avoid in MonoBehaviour:

- combat truth
- timing authority
- state machine truth
- business/gameplay rules
- hidden singleton access

## DOTween Rule

DOTween must not drive authoritative combat motion or locomotion.

Allowed for:
- UI animation, camera polish, reveal beats, memory presentation, environmental polish

Forbidden:
- player/enemy movement, dodge distance, attack range, hit position, overriding movement restrictions, setting gameplay truth

## Animator Rule

Animator is presentation only.

Animator must not own:

- combat state
- locomotion state
- cancel rules
- parry timing
- dodge timing
- recovery duration
- hit validity

Pure C# FSM owns gameplay truth.

## Scene Rule

Use additive scene separation:

- Bootstrap
- Systems
- Gameplay
- Camera
- UI
- Level

Scene scopes own gameplay lifetime.

Combat truth must not be registered globally.
