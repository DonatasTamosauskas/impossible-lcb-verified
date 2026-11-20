from collections import Counter


def minimumLength(s: str) -> int:
    t = 0
    for c in Counter(s).values():
        t += 1 if c % 2 == 1 else 2
    return t
