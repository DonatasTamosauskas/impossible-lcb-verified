def minOperations(k: int) -> int:
    best = k
    for v in range(1, k + 1):
        best = min(best, v - 1 + (k + v - 1) // v - 1)
    return best
