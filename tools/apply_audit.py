"""Turn the solver and auditor reports into curation/excluded.json and curation/excluded_asserts.json.

  python3 tools/apply_audit.py

A task is excluded when either reviewer found that the statement does not fix a single correct
answer, or the auditor found a blocking statement defect. Asserts the auditor judged unfair are
excluded individually (they must match a visible assert exactly, otherwise this script stops).
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "curation"


def main():
    solver = json.loads((C / "solution_reports.json").read_text())
    audit = json.loads((C / "audit_reports.json").read_text())
    visible = {}
    for line in open(ROOT / "dataset" / "original.jsonl", encoding="utf-8"):
        r = json.loads(line)
        visible[r["task_id"]] = {ln.strip() for ln in r["test"].split("\n") if ln.strip().startswith("assert ")}
    old_bad = json.loads((C / "excluded_asserts.json").read_text()) if (C / "excluded_asserts.json").exists() else {}
    excluded, bad, unmatched = {}, {k: list(v) for k, v in old_bad.items()}, []
    for tid, rep in sorted(solver.items()):
        if not rep["unique_answer"]:
            excluded[tid] = "answer not unique (solution writer): " + rep["notes"][:200]
    for tid, rep in sorted(audit.items()):
        if not rep["unique_answer"]:
            excluded[tid] = "answer not unique (auditor): " + rep["statement_note"][:300]
        elif rep["statement_defect"] == "blocking" or rep["verdict"] == "drop":
            excluded[tid] = "blocking statement defect (auditor): " + rep["statement_note"][:300]
        for a in rep["bad_asserts"]:
            a = a.strip()
            if tid in visible and a not in visible[tid] and a not in bad.get(tid, []):
                unmatched.append((tid, a[:120]))
            elif a not in bad.setdefault(tid, []):
                bad[tid].append(a)
    bad = {k: v for k, v in bad.items() if v and k not in excluded}
    (C / "excluded.json").write_text(json.dumps(excluded, indent=1, sort_keys=True, ensure_ascii=False))
    (C / "excluded_asserts.json").write_text(json.dumps(bad, indent=1, sort_keys=True, ensure_ascii=False))
    print(f"excluded tasks: {len(excluded)}; tasks with removed asserts: {len(bad)} ({sum(map(len, bad.values()))} asserts)")
    if unmatched:
        print("UNMATCHED bad asserts (fix by hand):")
        for u in unmatched:
            print("  ", u)
        sys.exit(1)


if __name__ == "__main__":
    main()
