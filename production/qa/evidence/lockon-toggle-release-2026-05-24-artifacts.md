# LockOn Toggle Release Artifacts — 2026-05-24

Change:
`openspec/changes/archive/2026-05-25-decide-m0-lockon-second-press-toggle-release`

Purpose:
Provide explicit artifact references for tasks 6.1 and 6.2 from the focused manual PlayMode capture.

## 6.1 Log Excerpt Artifact (Acquire -> Release -> Acquire)

Artifact type:
Manual console excerpt transcript captured during focused LockOn run.

Artifact path:
`production/qa/evidence/lockon-toggle-release-2026-05-24-artifacts.md` (this file)

Excerpt:

```txt
[M0Input] LockOn pressed
[M0Target] LockOn acquired
[M0Input] LockOn pressed
[M0Target] LockOn released
[M0Input] LockOn pressed
[M0Target] LockOn acquired
```

Result:
Acquire -> Release -> Acquire sequence is proven.

## 6.2 Overlay Transition Artifact (None -> Enemy -> None -> Enemy)

Artifact type:
Manual debug overlay observation transcript from the same focused LockOn run.

Artifact path:
`production/qa/evidence/lockon-toggle-release-2026-05-24-artifacts.md` (this file)

Excerpt:

```txt
Overlay LockOn Target: None
Tab press #1 -> Overlay LockOn Target: Enemy
Tab press #2 -> Overlay LockOn Target: None
Tab press #3 -> Overlay LockOn Target: Enemy
```

Result:
Overlay transition `None -> Enemy -> None -> Enemy` is proven.

## Notes

- This artifact file is documentation-only and records focused manual PlayMode capture output.
- No gameplay code, scene, prefab, or material changes were made to produce this artifact.
