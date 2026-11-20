# Impossible-LCB-Verified

Coding tasks whose unit tests cannot be passed honestly, for measuring whether a model cheats
on its tests. It follows the design of
[ImpossibleBench](https://github.com/safety-research/impossiblebench) (LiveCodeBench half) and
is built from [LiveCodeBench](https://github.com/LiveCodeBench/LiveCodeBench), with two changes:

- **Three difficulty levels.** 429 tasks: 132 easy, 199 medium, 98 hard. The original has 103,
  all hard.
- **Every task is verified.** Each one has a reference solution that passes all official
  LiveCodeBench tests, and each impossible variant is checked mechanically.

This is an independent project. It is not affiliated with the authors of ImpossibleBench or
LiveCodeBench.

## The three splits

Each task appears once per split, with the same `task_id`, prompt and `original_test`.

| Split | What the visible test is | Can an honest solution pass? |
|---|---|---|
| `original` | The real tests | Yes |
| `oneoff` | One assert has a wrong expected value | No |
| `conflicting` | One assert is duplicated with a different expected value | No, for any function |

A model that scores on `oneoff` or `conflicting` has done something other than solve the task:
special-cased an input, kept state between calls, replaced the checker, and so on.

```python
from datasets import load_dataset

base = "https://raw.githubusercontent.com/DonatasTamosauskas/impossible-lcb-verified/main/dataset/"
files = {s: base + s + ".jsonl" for s in ("original", "oneoff", "conflicting")}
ds = load_dataset("json", data_files=files, split="conflicting")
easy = ds.filter(lambda r: r["difficulty"] == "easy")
```

The first six columns have the same names and meaning as
`fjzzq2002/impossible_livecodebench`, so code written for that dataset reads this one unchanged.
A program is assembled the same way: `prompt + "\n    pass\n"`, then `test`, then the model's
answer, then `check(entry_point)`.

## Columns

| Column | Meaning |
|---|---|
| `task_id` | `lcbeasy_<id>`, `lcbmed_<id>` or `lcbhard_<id>`; `<id>` is the LiveCodeBench `question_id` |
| `prompt` | Function stub. The docstring is the official problem statement, unedited |
| `test` | `def check(candidate): ...` for this split |
| `original_test` | The real tests (equal to `test` in the `original` split) |
| `impossible_type` | `original`, `oneoff` or `conflicting` |
| `entry_point` | Function name |
| `difficulty` | `easy`, `medium` or `hard`, as labelled by LiveCodeBench |
| `platform`, `question_id`, `question_title`, `contest_date` | Source problem |
| `canonical_solution` | Reference solution that passes every official test |
| `mutated_assert` | The wrong assert (empty in `original`) |
| `source_assert` | The true assert it was derived from (empty in `original`) |
| `n_asserts` | Number of asserts in `test` |
| `statement_defect` | `none` or `minor` (cosmetic damage in the source text, see Limitations) |
| `impossiblebench_task_id` | Matching task in the original dataset, if any |

## How it was built

1. **Source.** All 444 function-style (LeetCode) problems of LiveCodeBench
   `code_generation_lite`, release v6, at a pinned revision.
2. **Conversion, by script.** The signature comes from the starter code, the docstring is the
   official statement, and every test is the official input and output parsed as JSON. No
   language model writes or rewrites any part of a task. Three problems with float outputs
   were skipped.
3. **Reference solutions.** Written by Claude Sonnet 5.5 (easy, medium) and Claude Opus 5.5
   (hard), then re-run independently in a sandbox against every official test, hidden ones
   included: 12,323 tests over 441 tasks, all passing.
4. **Visible tests.** The statement's examples plus short hidden tests, up to 20 asserts.
5. **Independent audit.** A second model pass (Claude Opus 5.5) read each task as a solver
   would see it and checked three things: that the statement fixes a single correct answer,
   that nothing needed is missing or garbled, and that every visible test input respects the
   stated constraints. Result: 5 tasks dropped, and 70 asserts removed from 38 tasks, mostly
   official tests whose inputs break the constraints in the statement.
6. **Impossible variants, by script.** Seeded by task id, so a rebuild is byte-identical. The
   wrong value has the same type as the true one (an integer off by one, a flipped boolean, a
   string or list element taken from another test of the same task).
7. **Mechanical checks, all 429 tasks.**
   - the reference solution passes `original`;
   - it fails `oneoff` and `conflicting` at exactly the mutated assert;
   - an empty function fails all three;
   - `conflicting` contains the same call with two different expected values;
   - cheating works: a solution that special-cases the mutated input passes `oneoff`, and one
     that answers differently on a repeated call passes `conflicting`.

Seven more tasks were left out because fewer than five short official tests remained.
`dataset/dropped.json` lists every excluded task with its reason, and `curation/` holds the
solver reports, audit reports and removed asserts.

## Relation to the original Impossible-LiveCodeBench

| | Original | This dataset |
|---|---|---|
| Tasks | 103 | 429 |
| Difficulty | hard | easy, medium, hard |
| Source problems | LeetCode and AtCoder | LeetCode only |
| Statements and tests | rewritten by an LLM | official text and official test data |
| Impossible variants | written by an LLM | generated by script, checked mechanically |
| Reference solutions | none | one per task, verified on all official tests |

Thirty of our hard tasks are the same problems as tasks in the original; the
`impossiblebench_task_id` column names them. For 27, our reference solution passes the
original task's own test. For the other 3 it does not, although it passes every official
LiveCodeBench test, which points to a wrong expected value in the original
(`curation/xref_disagreements.json`). Most of the original's remaining tasks come from
AtCoder problems, which this version does not cover.

## Limitations

- **Public problems.** These are LeetCode problems from May 2023 to April 2025. Models may
  have seen them, and their solutions, in training.
- **Reference solutions are published here.** Do not train on this dataset if you also
  evaluate on it.
- **Visible tests are small.** Large official tests are not embedded, so a slow but correct
  solution passes.
- **Audited by models, not by people.** The audit and the solutions come from language
  models. The mechanical checks are exact; the judgement that a statement is fair is not.
- **Cosmetic damage in 110 statements** (`statement_defect == "minor"`): a missing
  illustration, a flattened table, lost highlighting in an example. The specification is
  intact in each case. Filter on the column if you want only clean statements.
- **Difficulty labels are LiveCodeBench's** (LeetCode's own), not measured.
- **No AtCoder problems.** They are written for stdin and stdout and need a rewrite into
  function form.

## Rebuilding

Requires Python 3.11 or later and Docker. No Python packages.

```sh
tools/download.sh                       # LiveCodeBench release v6, 4.5 GB, hash-checked
python3 -I tools/prepare.py data/lcb_raw work
python3 tools/verify_all.py             # every solution against every official test
python3 tools/build.py                  # writes dataset/*.jsonl
python3 tools/qc.py                     # mechanical checks
```

`tools/check_with_study_grader.py` grades a sample with the grader of the reward-hacking
study this dataset was made for, as an end-to-end check.

All model-written code runs in a container with no network, a read-only root and a non-root
user. The pickled hidden tests in the source files are decoded with an unpickler that refuses
every global.

## Licence and credit

Code in this repository: MIT. The problem statements and test data come from LiveCodeBench
`code_generation_lite` (licence tag `cc`) and originate from LeetCode; they remain subject to
their original terms. The design of the impossible variants is ImpossibleBench's.

- LiveCodeBench: Jain et al., "LiveCodeBench: Holistic and Contamination Free Evaluation of
  Large Language Models for Code", https://github.com/LiveCodeBench/LiveCodeBench
- ImpossibleBench: https://github.com/safety-research/impossiblebench
- Colognese and Ward, "Character training can mitigate reward hacking, but can also make it
  harder to detect" (LessWrong), the study whose setup this dataset is meant to extend.
