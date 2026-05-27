from __future__ import annotations

import sys
from pathlib import Path

FORBIDDEN_PARTS = {
    "Library",
    "library",
    "Temp",
    "temp",
    "Obj",
    "obj",
    "Build",
    "build",
    "Builds",
    "builds",
    "Logs",
    "logs",
    ".vs",
    ".idea",
}


def main() -> int:
    failed = False

    for raw in sys.argv[1:]:
        path = Path(raw)
        parts = set(path.parts)

        hits = parts & FORBIDDEN_PARTS

        if hits:
            print(f"[FAIL] Forbidden Unity/generated path staged: {path}")
            failed = True

    if failed:
        print()
        print("Do not commit Unity generated/cache folders.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
