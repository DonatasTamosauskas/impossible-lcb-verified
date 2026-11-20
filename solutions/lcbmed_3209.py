from typing import List


def minimumCoins(prices: List[int]) -> int:
    n = len(prices)
    f = [0] * (n + 2)
    for i in range(n, 0, -1):
        if 2 * i >= n:
            f[i] = prices[i - 1]
        else:
            f[i] = prices[i - 1] + min(f[i + 1:2 * i + 2])
    return f[1]
