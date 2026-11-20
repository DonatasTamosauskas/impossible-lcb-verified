"""Raw LiveCodeBench -> work/ (tasks, full official tests, problem sheets for solution writers).

  python3 -I tools/prepare.py data/lcb_raw work
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ilcb.convert import Skip, convert  # noqa: E402
from ilcb.lcb import iter_rows  # noqa: E402

SHEET = """# {task_id}: {question_title}

Difficulty: {difficulty}. Write a correct and efficient reference solution.

## Required function (top level, exactly this name and signature)

```python
{header}{signature}
```

## Statement

{statement}
"""


def main(raw_dir: str, work_dir: str):
    work = Path(work_dir)
    for sub in ("tasks", "tests", "problems"):
        (work / sub).mkdir(parents=True, exist_ok=True)
    kept, skipped = [], []
    for row in iter_rows(raw_dir):
        if row["platform"] != "leetcode":
            continue
        try:
            out = convert(row)
        except Skip as exc:
            skipped.append({"question_id": row["question_id"], "difficulty": row["difficulty"], "reason": str(exc)})
            continue
        except Exception as exc:  # unexpected: report, never guess
            skipped.append({"question_id": row["question_id"], "difficulty": row["difficulty"], "reason": "error: " + repr(exc)[:200]})
            continue
        task = out["task"]
        tid = task["task_id"]
        (work / "tasks" / f"{tid}.json").write_text(json.dumps(task, ensure_ascii=False, indent=1))
        (work / "tests" / f"{tid}.json").write_text(json.dumps({"entry_point": task["entry_point"], "cases": out["cases"]}))
        header = task["prompt"].split("def ", 1)[0]
        (work / "problems" / f"{tid}.md").write_text(SHEET.format(header=header, statement=row["question_content"].strip(), **task))
        kept.append(tid)
    (work / "prepare_report.json").write_text(json.dumps({"kept": kept, "skipped": skipped}, indent=1))
    by = {}
    for tid in kept:
        by[tid.split("_")[0]] = by.get(tid.split("_")[0], 0) + 1
    print(f"kept {len(kept)} {by}; skipped {len(skipped)}")
    reasons = {}
    for s in skipped:
        reasons[s["reason"][:60]] = reasons.get(s["reason"][:60], 0) + 1
    print(json.dumps(reasons, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
