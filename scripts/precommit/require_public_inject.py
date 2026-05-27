# scripts/precommit/require_public_inject.py
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

INJECT_METHOD_PATTERN = re.compile(
    r"""
    \[ \s* Inject \s* \]
    \s*
    (?P<mods>
        (?:
            public|private|internal|protected|
            static|virtual|override|sealed|async|
            new|\s
        )*
    )
    \s*
    (?P<return_type>
        void|[A-Za-z_][A-Za-z0-9_<>,\.\?\s]*
    )
    \s+
    (?P<name>[A-Za-z_][A-Za-z0-9_]*)
    \s*
    \(
    """,
    re.VERBOSE | re.MULTILINE,
)


def default_log_path() -> Path:
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return Path(".logs/precommit") / f"{stamp}_require_public_inject.log"


def write_log(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-file", default=None)
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    log_path = Path(args.log_file) if args.log_file else default_log_path()
    log_lines: list[str] = []

    failed = False
    checked = 0

    log_lines.append("require_public_inject.py")
    log_lines.append(f"Started: {dt.datetime.now().isoformat()}")
    log_lines.append("")

    for raw in args.files:
        path = Path(raw)

        if not path.exists() or path.suffix != ".cs":
            continue

        checked += 1
        text = path.read_text(encoding="utf-8", errors="ignore")

        for match in INJECT_METHOD_PATTERN.finditer(text):
            mods = match.group("mods") or ""
            name = match.group("name")
            normalized_mods = set(mods.split())

            if "public" not in normalized_mods:
                message = (
                    f"[FAIL] {path}: [Inject] method '{name}' must be public. "
                    "Reason: VContainer Source Generator generated injectors may not access "
                    "non-public injection methods."
                )
                print(message)
                log_lines.append(message)
                failed = True

    log_lines.append("")
    log_lines.append(f"Checked files: {checked}")
    log_lines.append(f"Result: {'FAIL' if failed else 'PASS'}")
    log_lines.append(f"Finished: {dt.datetime.now().isoformat()}")

    write_log(log_path, log_lines)

    print(f"[INFO] Hook log: {log_path}")

    if failed:
        print()
        print("Fix example:")
        print("  [Inject]")
        print("  public void Construct(IDependency dependency) { ... }")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
