"""Assemble the Hugging Face dataset folder: hf/README.md (card) and hf/data/*.jsonl.

  python3 tools/export_hf.py <hf_repo_id>
"""

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARD = """---
license: cc
language:
- en
pretty_name: Impossible-LCB-Verified
size_categories:
- 1K<n<10K
task_categories:
- text-generation
tags:
- code
- benchmark
- reward-hacking
- ai-safety
- impossiblebench
- livecodebench
configs:
- config_name: default
  data_files:
  - split: original
    path: data/original.jsonl
  - split: oneoff
    path: data/oneoff.jsonl
  - split: conflicting
    path: data/conflicting.jsonl
---

"""


def main(repo_id: str, github_url: str = ""):
    out = ROOT / "hf"
    (out / "data").mkdir(parents=True, exist_ok=True)
    for split in ("original", "oneoff", "conflicting"):
        shutil.copyfile(ROOT / "dataset" / f"{split}.jsonl", out / "data" / f"{split}.jsonl")
    body = (ROOT / "README.md").read_text()
    start = body.index('base = "https://raw.githubusercontent.com')
    end = body.index("easy = ds.filter")
    body = body[:start] + f'ds = load_dataset("{repo_id}", split="conflicting")\n' + body[end:]
    if github_url:
        body = body.replace("## The three splits", f"Code, reference solutions and curation records: {github_url}\n\n## The three splits", 1)
    (out / "README.md").write_text(CARD + body)
    print("wrote", out)


if __name__ == "__main__":
    main(*sys.argv[1:3])
