def differenceOfSums(n: int, m: int) -> int:
    total = n * (n + 1) // 2
    c = n // m
    div = m * c * (c + 1) // 2
    return total - 2 * div
