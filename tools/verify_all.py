"""Independently re-verify every solution in solutions/ against all official tests.

  python3 tools/verify_all.py [--jobs 6] [--only-missing]

Writes curation/verified.json: {task_id: {status, passed, total, slowest_test_seconds, sha256}}.
A stored PASS is reused only while the solution file's hash is unchanged.
"""

import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from tools.verify import verify  # noqa: E402


def main():
    jobs = int(sys.argv[sys.argv.index("--jobs") + 1]) if "--jobs" in sys.argv else 6
    store = ROOT / "curation" / "verified.json"
    old = json.loads(store.read_text()) if store.exists() else {}
    tasks = sorted(p.stem for p in (ROOT / "work" / "tasks").glob("*.json"))
    todo, res = [], {}
    for tid in tasks:
        sol = ROOT / "solutions" / f"{tid}.py"
        if not sol.exists():
            res[tid] = {"status": "MISSING"}
            continue
        digest = hashlib.sha256(sol.read_bytes()).hexdigest()
        if old.get(tid, {}).get("status") == "PASS" and old[tid].get("sha256") == digest:
            res[tid] = old[tid]
        else:
            todo.append((tid, digest))

    def run(item):
        tid, digest = item
        out = verify(tid)
        out["sha256"] = digest
        return tid, out

    with ThreadPoolExecutor(jobs) as ex:
        for n, (tid, out) in enumerate(ex.map(run, todo), 1):
            res[tid] = out
            if out["status"] != "PASS":
                print(tid, json.dumps(out)[:400], flush=True)
            if n % 50 == 0:
                print(f"... {n}/{len(todo)}", flush=True)
    store.write_text(json.dumps(res, indent=1, sort_keys=True))
    counts = {}
    for v in res.values():
        counts[v["status"]] = counts.get(v["status"], 0) + 1
    print(f"verified {len(todo)} new; totals {counts}")


if __name__ == "__main__":
    main()
