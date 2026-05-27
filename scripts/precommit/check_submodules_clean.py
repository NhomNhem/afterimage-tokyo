from __future__ import annotations

import subprocess


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
    )


def main() -> int:
    result = run(["git", "submodule", "foreach", "--recursive", "git status --short"])

    if result.returncode != 0:
        print("[FAIL] Could not inspect submodules.")
        print(result.stdout)
        print(result.stderr)
        return 1

    output = result.stdout.strip()
    dirty_entries: list[str] = []
    current_submodule = ""

    for line in output.splitlines():
        line = line.rstrip()

        if line.startswith("Entering '"):
            current_submodule = line
            continue

        if line.strip():
            dirty_entries.append(f"{current_submodule}\n  {line}")

    if dirty_entries:
        print("[FAIL] One or more submodules are dirty.")
        print()

        for entry in dirty_entries:
            print(entry)

        print()
        print("Fix:")
        print("  1. cd <dirty-submodule>")
        print("  2. git status")
        print("  3. commit/clean changes inside the submodule")
        print("  4. return to parent and commit the submodule pointer")
        return 1

    print("[PASS] All submodules are clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
