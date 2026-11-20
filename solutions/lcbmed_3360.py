from collections import Counter


def minimumDeletions(word: str, k: int) -> int:
    fs = sorted(Counter(word).values())
    best = len(word)
    for lo in fs:
        cost = 0
        for f in fs:
            if f < lo:
                cost += f
            elif f > lo + k:
                cost += f - lo - k
        best = min(best, cost)
    return best
