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
