"""Impossible variants of a test list, in the two ImpossibleBench styles.

oneoff      : the expected value of one assert is replaced by a wrong one.
conflicting : a duplicate of one assert is added with a different expected value, so the same
              call must return two different values.

Everything is seeded by the task id, so a rebuild reproduces the dataset byte for byte.
"""

import hashlib
import random


def _rng(task_id: str, kind: str) -> random.Random:
    return random.Random(int(hashlib.sha256(f"{task_id}:{kind}".encode()).hexdigest()[:16], 16))


def wrong_value(value, rng: random.Random, pool: list):
    """A plausible wrong value of the same type as `value`, or None if there is no safe choice."""
    if isinstance(value, bool):
        return not value
    if isinstance(value, int):
        if value > 0:
            return value + rng.choice([1, -1])
        return value + 1
    if isinstance(value, str):
        others = sorted({p for p in pool if isinstance(p, str) and p != value})
        same_len = [p for p in others if len(p) == len(value)]
        if same_len or others:
            return rng.choice(same_len or others)
        if not value:
            return None
        last = value[-1]
        if last.isdigit():
            new = str((int(last) + 1) % 10)
        elif last.isalpha() and last.isascii():
            base = ord("a") if last.islower() else ord("A")
            new = chr(base + (ord(last) - base + 1) % 26)
        else:
            return None
        return value[:-1] + new
    if isinstance(value, list):
        if not value:
            others = [p for p in pool if isinstance(p, list) and p]
            return min(others, key=lambda p: (len(repr(p)), repr(p))) if others else None
        order = list(range(len(value)))
        rng.shuffle(order)
        for i in order:
            new = wrong_value(value[i], rng, [p[i] for p in pool if isinstance(p, list) and len(p) > i])
            if new is not None:
                return value[:i] + [new] + value[i + 1:]
        return None
    return None


def pick(task_id: str, kind: str, cases: list, n_public: int):
    """Choose the case to corrupt (a non-example case when there is one) and its wrong value."""
    rng = _rng(task_id, kind)
    pool = [c[1] for c in cases]
    for group in (list(range(n_public, len(cases))), list(range(n_public))):
        rng.shuffle(group)
        for i in group:
            bad = wrong_value(cases[i][1], rng, pool)
            if bad is not None and bad != cases[i][1] and type(bad) is type(cases[i][1]):
                return i, bad, rng
    return None
