"""Map our tasks to task ids of the original Impossible-LiveCodeBench (fjzzq2002/impossible_livecodebench).

  python3 tools/xref.py work/original_ilcb.jsonl      (rows of the original's `original` split)

A pair is a candidate when the two tasks share test inputs. It is accepted when our verified
reference solution passes the original task's own test (proof that it is the same problem), or
when at least half of the original's test inputs (and five or more) are official inputs of ours.
Writes curation/xref.json {our_task_id: {"impossiblebench_task_id", "evidence"}}.
"""

import ast
import collections
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from ilcb.sandbox import docker_run  # noqa: E402


def calls(test: str) -> list[tuple]:
    out = []
    try:
        tree = ast.parse(test)
    except SyntaxError:
        return out
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "candidate":
            try:
                out.append(tuple(sorted(json.dumps(ast.literal_eval(a), sort_keys=True) for a in n.args)))
            except Exception:
                pass
    return out


def main(original_path: str):
    originals = [json.loads(line) for line in open(original_path, encoding="utf-8")]
    inv = collections.defaultdict(set)
    for p in (ROOT / "work" / "tests").glob("lcbhard_*.json"):
        for args, _ in json.loads(p.read_text())["cases"]:
            if len(json.dumps(args)) < 400:
                inv[tuple(sorted(json.dumps(a, sort_keys=True) for a in args))].add(p.stem)
    progs, overlap = {}, {}
    for o in originals:
        cs = calls(o["original_test"])
        cnt = collections.Counter(t for c in cs for t in inv.get(c, ()))
        for ours, n in cnt.items():
            sol = (ROOT / "solutions" / f"{ours}.py").read_text()
            ep = json.loads((ROOT / "work" / "tasks" / f"{ours}.json").read_text())["entry_point"]
            key = f"{o['task_id']}|{ours}"
            overlap[key] = (n, len(cs))
            progs[key] = "\n".join([sol, o["original_test"], f"check({ep})"])
    with tempfile.NamedTemporaryFile("w", suffix=".json", dir=ROOT / "work", delete=False) as fh:
        json.dump(progs, fh)
    r = docker_run(["python", "-I", "/w/qc_runner.py"],
                   mounts={fh.name: "/w/programs.json", str(ROOT / "ilcb" / "qc_runner.py"): "/w/qc_runner.py"}, timeout=1800)
    Path(fh.name).unlink()
    res = json.loads(r.stdout.strip().splitlines()[-1])
    xref, disagreements = {}, {}
    for key, out in sorted(res.items()):
        orig, ours = key.split("|")
        n, total = overlap[key]
        if out["exit"] == 0:
            xref[ours] = {"impossiblebench_task_id": orig, "evidence": "our reference solution passes the original task's test"}
        elif n >= 5 and n * 2 >= total:
            xref[ours] = {"impossiblebench_task_id": orig, "evidence": f"{n} of {total} test inputs are official inputs of ours"}
            disagreements[key] = {"shared_inputs": f"{n}/{total}", "failing_line": out["failing_line"], "error": out["last"]}
    (ROOT / "curation" / "xref.json").write_text(json.dumps(xref, indent=1, sort_keys=True))
    (ROOT / "curation" / "xref_disagreements.json").write_text(json.dumps(disagreements, indent=1, sort_keys=True))
    print(f"{len(xref)} of our tasks map to an original task; {len(disagreements)} of those fail the original's test")
    for k, v in disagreements.items():
        print(k, v)


if __name__ == "__main__":
    main(sys.argv[1])
