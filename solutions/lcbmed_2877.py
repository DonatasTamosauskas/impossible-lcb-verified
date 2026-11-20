from itertools import permutations


def _merge(s: str, t: str) -> str:
    if t in s:
        return s
    for k in range(min(len(s), len(t)), -1, -1):
        if s.endswith(t[:k]):
            return s + t[k:]
    return s + t


def minimumString(a: str, b: str, c: str) -> str:
    best = None
    for p in permutations((a, b, c)):
        r = _merge(_merge(p[0], p[1]), p[2])
        if best is None or (len(r), r) < (len(best), best):
            best = r
    return best
