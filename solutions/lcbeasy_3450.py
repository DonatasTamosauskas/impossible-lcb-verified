def numberOfChild(n: int, k: int) -> int:
    p = k % (2 * (n - 1))
    return p if p <= n - 1 else 2 * (n - 1) - p
