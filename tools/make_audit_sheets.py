"""dataset/original.jsonl -> work/audit/<task_id>.md (+ batch lists) for the independent audit.

  python3 tools/make_audit_sheets.py [difficulty ...]     e.g. easy medium
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCH = 8


def main(difficulties):
    out = ROOT / "work" / "audit"
    out.mkdir(parents=True, exist_ok=True)
    bdir = ROOT / "work" / "audit_batches"
    bdir.mkdir(exist_ok=True)
    done_path = ROOT / "curation" / "audit_reports.json"
    done = set(json.loads(done_path.read_text())) if done_path.exists() else set()
    ids = []
    for line in open(ROOT / "dataset" / "original.jsonl", encoding="utf-8"):
        r = json.loads(line)
        if r["difficulty"] not in difficulties or r["task_id"] in done:
            continue
        (out / f"{r['task_id']}.md").write_text(
            f"# {r['task_id']}\n\n## Prompt given to the solver (the only specification)\n\n```python\n{r['prompt']}\n```\n\n"
            f"## Visible tests\n\n```python\n{r['test']}\n```\n")
        ids.append(r["task_id"])
    tag = "_".join(difficulties)
    for f in bdir.glob(f"{tag}_*.txt"):
        f.unlink()
    n = 0
    for i in range(0, len(ids), BATCH):
        (bdir / f"{tag}_{n:02d}.txt").write_text("\n".join(ids[i:i + BATCH]) + "\n")
        n += 1
    print(f"{len(ids)} sheets, {n} batches with prefix {tag}_")


if __name__ == "__main__":
    main(sys.argv[1:] or ["easy", "medium", "hard"])
