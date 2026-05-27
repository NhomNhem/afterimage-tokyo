from __future__ import annotations

import subprocess


def run(args: list[str], cwd: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False,
    )


def get_submodule_paths() -> list[str]:
    result = run(["git", "config", "--file", ".gitmodules", "--get-regexp", "path"])

    if result.returncode != 0:
        return []

    paths: list[str] = []

    for line in result.stdout.splitlines():
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            paths.append(parts[1].strip())

    return paths


def main() -> int:
    paths = get_submodule_paths()

    if not paths:
        print("[PASS] No submodules found.")
        return 0

    failed = False

    for path in paths:
        branch_result = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=path)

        if branch_result.returncode != 0:
            print(f"[FAIL] Could not inspect submodule branch: {path}")
            failed = True
            continue

        branch = branch_result.stdout.strip()

        if branch == "HEAD":
            print(f"[FAIL] Submodule is detached HEAD: {path}")
            failed = True
            continue

        upstream_result = run(
            ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"],
            cwd=path,
        )

        if upstream_result.returncode != 0:
            print(f"[WARN] Submodule has no upstream configured: {path}")
            continue

        ahead_result = run(["git", "rev-list", "--count", "@{u}..HEAD"], cwd=path)

        if ahead_result.returncode != 0:
            print(f"[WARN] Could not check upstream delta for submodule: {path}")
            continue

        ahead = int(ahead_result.stdout.strip() or "0")

        if ahead > 0:
            print(f"[FAIL] Submodule has {ahead} unpushed commit(s): {path}")
            failed = True

    if failed:
        print()
        print("Push submodule commits first, then push parent repo.")
        return 1

    print("[PASS] Submodule commits appear pushed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
