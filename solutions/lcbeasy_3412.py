def findPermutationDifference(s: str, t: str) -> int:
    return sum(abs(i - t.index(c)) for i, c in enumerate(s))
