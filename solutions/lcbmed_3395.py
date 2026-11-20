from collections import Counter


def minAnagramLength(s: str) -> int:
    n = len(s)
    for L in range(1, n + 1):
        if n % L:
            continue
        base = Counter(s[:L])
        if all(Counter(s[i:i + L]) == base for i in range(L, n, L)):
            return L
    return n
