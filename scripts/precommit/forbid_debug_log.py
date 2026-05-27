from __future__ import annotations

import sys
from pathlib import Path

BANNED_PATTERNS = [
    "Debug.Log(",
    "Debug.LogWarning(",
    "Debug.LogError(",
    "UnityEngine.Debug.Log(",
    "UnityEngine.Debug.LogWarning(",
    "UnityEngine.Debug.LogError(",
]

ALLOWED_PATH_KEYWORDS = [
    "NhemLogger",
    "NhemLogging",
    "Logger",
    "Logging",
]

ALLOWED_FILE_NAMES = {
    "NhemLogger.cs",
    "NhemLogging.cs",
}


def is_allowed_path(path: Path) -> bool:
    path_text = str(path).replace("\\", "/")

    if path.name in ALLOWED_FILE_NAMES:
        return True

    return any(keyword in path_text for keyword in ALLOWED_PATH_KEYWORDS)


def main() -> int:
    failed = False

    for raw in sys.argv[1:]:
        path = Path(raw)

        if not path.exists() or path.suffix != ".cs":
            continue

        if is_allowed_path(path):
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")

        for pattern in BANNED_PATTERNS:
            if pattern in text:
                print(f"[FAIL] Direct Unity debug logging found: {path}")
                print(f"       Pattern: {pattern}")
                failed = True

    if failed:
        print()
        print("Use NhemLogger/NhemLogging wrapper instead of UnityEngine.Debug directly.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
