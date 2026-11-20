"""LiveCodeBench LeetCode-style ("functional") problem -> function-form task.

No LLM is involved: the signature comes from the starter code, the docstring is the official
statement verbatim, and every test case is the official input/output parsed as JSON.
"""

import json
import re

from .lcb import decode_private

PREFIX = {"easy": "lcbeasy", "medium": "lcbmed", "hard": "lcbhard"}
TYPING_NAMES = ("List", "Optional", "Tuple", "Dict", "Set")
SIG_RE = re.compile(r"def\s+(\w+)\(\s*self\s*,?\s*(.*?)\)\s*(->\s*[^:]+?)?\s*:\s*$", re.M | re.S)


class Skip(Exception):
    """The problem cannot be converted deterministically; the message says why."""


def split_params(params: str) -> list[str]:
    out, depth, cur = [], 0, ""
    for ch in params:
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur.strip()); cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


def has_float(v) -> bool:
    if isinstance(v, float):
        return True
    if isinstance(v, (list, tuple)):
        return any(has_float(x) for x in v)
    if isinstance(v, dict):
        return any(has_float(x) for x in v.values())
    return False


def parse_case(case: dict, n_params: int):
    if case.get("testtype") != "functional":
        raise Skip("non-functional test case")
    args = [json.loads(line) for line in case["input"].split("\n")]
    if len(args) != n_params:
        raise Skip(f"test has {len(args)} arguments, signature has {n_params}")
    return [args, json.loads(case["output"])]


def render_prompt(signature: str, statement: str) -> str:
    names = [t for t in TYPING_NAMES if re.search(rf"\b{t}\b", signature)]
    header = f"from typing import {', '.join(names)}\n\n\n" if names else ""
    body = "\n".join(("    " + ln.rstrip()) if ln.strip() else "" for ln in statement.split("\n"))
    quote = 'r"""' if "\\" in statement else '"""'
    return f"{header}{signature}\n    {quote} {body.lstrip()}\n    \"\"\""


def convert(row: dict) -> dict:
    """Return {'task': {...}, 'cases': [[args, expected], ...] (public first)} or raise Skip."""
    if row["platform"] != "leetcode":
        raise Skip("not a function-style problem")
    starter = row["starter_code"]
    if starter.count("def ") != 1:
        raise Skip("starter code does not define exactly one method")
    m = SIG_RE.search(starter)
    if not m:
        raise Skip("unrecognised starter code")
    name, params, ret = m.group(1), " ".join(m.group(2).split()), (m.group(3) or "").strip()
    if json.loads(row["metadata"]).get("func_name", name) != name:
        raise Skip("metadata func_name differs from starter code")
    statement = row["question_content"].strip()
    if '"""' in statement or statement.endswith("\\"):
        raise Skip("statement cannot be embedded in a docstring")
    plist = split_params(params)
    signature = f"def {name}({', '.join(plist)}){' ' + ret if ret else ''}:"
    prompt = render_prompt(signature, statement)
    ns: dict = {}
    exec(compile(prompt + "\n    pass\n", "<stub>", "exec"), ns)  # annotations must resolve
    doc = ns[name].__doc__ or ""
    if " ".join(doc.split()) != " ".join(statement.split()):
        raise Skip("docstring does not round-trip the statement")

    public = [parse_case(c, len(plist)) for c in json.loads(row["public_test_cases"])]
    private = [parse_case(c, len(plist)) for c in decode_private(row["private_test_cases"])]
    seen, cases, n_public = set(), [], 0
    for i, case in enumerate(public + private):
        key = json.dumps(case[0], sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        cases.append(case)
        if i < len(public):
            n_public += 1
    if any(has_float(c[1]) for c in cases):
        raise Skip("float outputs (equality asserts would be fragile)")
    task = {
        "task_id": f"{PREFIX[row['difficulty']]}_{row['question_id']}",
        "difficulty": row["difficulty"],
        "platform": row["platform"],
        "question_id": row["question_id"],
        "question_title": row["question_title"],
        "contest_id": row["contest_id"],
        "contest_date": row["contest_date"][:10],
        "source_file": row["_source_file"],
        "entry_point": name,
        "signature": signature,
        "prompt": prompt,
        "n_public": n_public,
        "n_cases": len(cases),
    }
    return {"task": task, "cases": cases}
