"""Check a reference solution against EVERY official LiveCodeBench test of a task (sandboxed).

  python3 tools/verify.py <task_id> [solution.py]     (default: solutions/<task_id>.py)

Prints one JSON line; exit code 0 only on PASS. Results must match the official output exactly
(same value and same type).
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from ilcb.sandbox import docker_run  # noqa: E402


def verify(task_id: str, solution: Path | None = None, per_test: int = 10, wall: int = 900) -> dict:
    tests = ROOT / "work" / "tests" / f"{task_id}.json"
    solution = (solution or ROOT / "solutions" / f"{task_id}.py").resolve()
    if not tests.exists():
        return {"status": "ERROR", "error": f"unknown task {task_id}"}
    if not solution.exists():
        return {"status": "ERROR", "error": f"missing {solution}"}
    r = docker_run(["python", "-I", "/w/runner.py", str(per_test)],
                   mounts={str(tests): "/w/tests.json", str(solution): "/w/solution.py",
                           str(ROOT / "ilcb" / "runner.py"): "/w/runner.py"}, timeout=wall)
    line = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""
    try:
        out = json.loads(line)
    except Exception:
        out = {"status": "ERROR", "error": (r.stderr or r.stdout)[-1500:] or f"exit code {r.returncode}"}
    out["task_id"] = task_id
    return out


if __name__ == "__main__":
    res = verify(sys.argv[1], Path(sys.argv[2]) if len(sys.argv) > 2 else None)
    print(json.dumps(res))
    sys.exit(0 if res.get("status") == "PASS" else 1)
