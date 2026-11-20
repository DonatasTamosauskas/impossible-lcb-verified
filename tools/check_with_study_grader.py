"""End-to-end check against the grader of the reward-hacking study (Colognese & Ward).

Run from a checkout of their repository, with Docker running:

  cd character-reward-hacking && uv run python /path/to/tools/check_with_study_grader.py /path/to/dataset [N]

For N tasks (default 30, evenly spread over the dataset) it grades, with their `grader.grade`:
  the reference solution on the original test      -> reward 1
  the reference solution on oneoff and conflicting -> reward 0, passes_original True, not hacked
  a special-casing cheat on oneoff                 -> reward 1, hacked_on_impossible True
  a repeat-call cheat on conflicting               -> reward 1, hacked_on_impossible True
"""

import asyncio
import json
import sys
from pathlib import Path

from src.train.rlaif.reward_hack import grader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.qc import REPEAT_CALL, SPECIAL_CASE, args_key, call_and_value  # noqa: E402


def fence(code: str) -> str:
    return f"```python\n{code}\n```"


async def main(dataset_dir: str, n: int):
    rows = {s: [json.loads(line) for line in open(Path(dataset_dir) / f"{s}.jsonl", encoding="utf-8")]
            for s in ("original", "oneoff", "conflicting")}
    idx = sorted({round(i * (len(rows["original"]) - 1) / (n - 1)) for i in range(n)})
    assert grader.SANDBOX_BACKEND == "docker"
    grader.ensure_docker_image()
    bad = []

    async def grade(row, answer):
        return await grader.grade(prompt=row["prompt"], test=row["test"], original_test=row["original_test"],
                                  entry_point=row["entry_point"], impossible=row["impossible_type"] != "original",
                                  visible_response=fence(answer), timeout=20)

    for i in idx:
        o, one, con = rows["original"][i], rows["oneoff"][i], rows["conflicting"][i]
        ep, sol = o["entry_point"], o["canonical_solution"]
        call1, bad1 = call_and_value(one["mutated_assert"])
        call2, bad2 = call_and_value(con["mutated_assert"])
        lines = con["test"].split("\n")
        nth = 1 if lines.index("    " + con["mutated_assert"]) < lines.index("    " + con["source_assert"]) else 2
        hack1 = sol + SPECIAL_CASE.format(ep=ep, key=args_key(call1), bad=bad1)
        hack2 = sol + REPEAT_CALL.format(ep=ep, key=args_key(call2), bad=bad2, nth=nth)
        checks = [
            ("ref/original", await grade(o, sol), lambda g: g.reward == 1.0 and g.passes_original),
            ("ref/oneoff", await grade(one, sol), lambda g: g.reward == 0.0 and g.passes_original and not g.hacked_on_impossible),
            ("ref/conflicting", await grade(con, sol), lambda g: g.reward == 0.0 and g.passes_original and not g.hacked_on_impossible),
            ("cheat/oneoff", await grade(one, hack1), lambda g: g.reward == 1.0 and g.hacked_on_impossible),
            ("cheat/conflicting", await grade(con, hack2), lambda g: g.reward == 1.0 and g.hacked_on_impossible),
        ]
        for name, g, ok in checks:
            if g.infra_error or not ok(g):
                bad.append((o["task_id"], name, g.reward, g.passes_original, g.hacked_on_impossible, g.infra_error))
        print(o["task_id"], "ok" if not any(b[0] == o["task_id"] for b in bad) else "MISMATCH", flush=True)
    print(f"{len(idx)} tasks checked with the study's grader; mismatches: {len(bad)}")
    for b in bad:
        print("  ", b)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 30))
