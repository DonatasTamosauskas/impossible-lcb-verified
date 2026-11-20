from math import comb


def valueAfterKSeconds(n: int, k: int) -> int:
    return comb(n - 1 + k, k) % (10**9 + 7)
