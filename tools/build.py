"""work/ + solutions/ -> dataset/{original,oneoff,conflicting}.jsonl

  python3 tools/build.py [--verified curation/verified.json]

Only tasks whose reference solution passed every official test (curation/verified.json, written by
tools/verify_all.py) are included.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from ilcb.mutate import pick  # noqa: E402
from ilcb.render import MIN_ASSERTS, assert_line, render_check, select_visible  # noqa: E402

COLUMNS = ["task_id", "prompt", "test", "original_test", "impossible_type", "entry_point",
           "difficulty", "platform", "question_id", "question_title", "contest_date",
           "canonical_solution", "mutated_assert", "source_assert", "n_asserts", "statement_defect",
           "impossiblebench_task_id"]


def build_task(task: dict, cases: list, solution: str, xref: str, bad_asserts: set = frozenset(),
               defect: str = "none") -> dict | str:
    visible, n_pub = select_visible(cases, task["n_public"])
    # asserts the audit judged unfair (input outside the stated constraints, undefined behaviour)
    # are removed, not replaced, so that every remaining assert has been audited
    keep = [assert_line(*c).strip() not in bad_asserts for c in visible]
    n_pub = sum(keep[:n_pub])
    visible = [c for c, k in zip(visible, keep) if k]
    if len(visible) < MIN_ASSERTS:
        return f"only {len(visible)} usable short official tests"
    lines = [assert_line(*c) for c in visible]
    original = render_check(lines, n_pub)
    tid = task["task_id"]
    base = {"task_id": tid, "prompt": task["prompt"], "original_test": original, "entry_point": task["entry_point"],
            "difficulty": task["difficulty"], "platform": task["platform"], "question_id": task["question_id"],
            "question_title": task["question_title"], "contest_date": task["contest_date"],
            "canonical_solution": solution, "n_asserts": len(lines), "statement_defect": defect,
            "impossiblebench_task_id": xref}
    rows = {"original": {**base, "test": original, "impossible_type": "original", "mutated_assert": "", "source_assert": ""}}

    choice = pick(tid, "oneoff", visible, n_pub)
    if not choice:
        return "no safe wrong value for oneoff"
    i, bad, _ = choice
    mutated = list(lines)
    mutated[i] = assert_line(visible[i][0], bad)
    rows["oneoff"] = {**base, "test": render_check(mutated, n_pub), "impossible_type": "oneoff",
                      "mutated_assert": mutated[i].strip(), "source_assert": lines[i].strip()}

    choice = pick(tid, "conflicting", visible, n_pub)
    if not choice:
        return "no safe wrong value for conflicting"
    i, bad, rng = choice
    extra = assert_line(visible[i][0], bad)
    pos = rng.randrange(n_pub, len(lines) + 1)          # anywhere after the statement examples
    mutated = lines[:pos] + [extra] + lines[pos:]
    rows["conflicting"] = {**base, "test": render_check(mutated, n_pub), "impossible_type": "conflicting",
                           "mutated_assert": extra.strip(), "source_assert": lines[i].strip(), "n_asserts": len(mutated)}
    for r in rows.values():
        compile(r["test"], "<test>", "exec")
    return rows


def main():
    verified = json.loads((ROOT / "curation" / "verified.json").read_text())
    xref_path = ROOT / "curation" / "xref.json"
    xref = json.loads(xref_path.read_text()) if xref_path.exists() else {}
    excluded_path = ROOT / "curation" / "excluded.json"
    excluded = json.loads(excluded_path.read_text()) if excluded_path.exists() else {}
    bad_path = ROOT / "curation" / "excluded_asserts.json"
    bad = json.loads(bad_path.read_text()) if bad_path.exists() else {}
    audit = json.loads((ROOT / "curation" / "audit_reports.json").read_text())
    out = {"original": [], "oneoff": [], "conflicting": []}
    dropped = dict(excluded)
    order = {"easy": 0, "medium": 1, "hard": 2}
    tasks = [json.loads(p.read_text()) for p in sorted((ROOT / "work" / "tasks").glob("*.json"))]
    tasks.sort(key=lambda t: (order[t["difficulty"]], int(t["question_id"])))
    for task in tasks:
        tid = task["task_id"]
        if tid in excluded:
            continue
        if verified.get(tid, {}).get("status") != "PASS":
            dropped[tid] = "no reference solution passes all official tests"
            continue
        cases = json.loads((ROOT / "work" / "tests" / f"{tid}.json").read_text())["cases"]
        solution = (ROOT / "solutions" / f"{tid}.py").read_text().rstrip() + "\n"
        rows = build_task(task, cases, solution, xref.get(tid, {}).get("impossiblebench_task_id", ""),
                          set(bad.get(tid, [])), audit.get(tid, {}).get("statement_defect", "none"))
        if isinstance(rows, str):
            dropped[tid] = rows
            continue
        if tid not in audit and "--allow-unaudited" not in sys.argv:
            dropped[tid] = "not audited"
            continue
        for split, row in rows.items():
            out[split].append({k: row[k] for k in COLUMNS})
    (ROOT / "dataset").mkdir(exist_ok=True)
    for split, rows in out.items():
        with open(ROOT / "dataset" / f"{split}.jsonl", "w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    (ROOT / "dataset" / "dropped.json").write_text(json.dumps(dropped, indent=1, sort_keys=True))
    by = {}
    for r in out["original"]:
        by[r["difficulty"]] = by.get(r["difficulty"], 0) + 1
    print(f"built {len(out['original'])} tasks x 3 splits {by}; dropped {len(dropped)}")


if __name__ == "__main__":
    main()
