from collections import Counter


def findValidPair(s: str) -> str:
    c = Counter(s)
    for a, b in zip(s, s[1:]):
        if a != b and c[a] == int(a) and c[b] == int(b):
            return a + b
    return ""
