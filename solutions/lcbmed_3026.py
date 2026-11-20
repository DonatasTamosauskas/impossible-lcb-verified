def minimumPossibleSum(n: int, target: int) -> int:
    k = min(n, target // 2)
    r = n - k
    total = k * (k + 1) // 2 + r * target + r * (r - 1) // 2
    return total % (10**9 + 7)
