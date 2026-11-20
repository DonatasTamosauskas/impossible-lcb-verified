from collections import Counter


def maxDifference(s: str) -> int:
    c = Counter(s).values()
    return max(v for v in c if v % 2) - min(v for v in c if v % 2 == 0)
