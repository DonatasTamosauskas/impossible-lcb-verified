from typing import List


def minimumAddedCoins(coins: List[int], target: int) -> int:
    coins = sorted(coins)
    reach = 0
    added = 0
    i = 0
    n = len(coins)
    while reach < target:
        if i < n and coins[i] <= reach + 1:
            reach += coins[i]
            i += 1
        else:
            reach += reach + 1
            added += 1
    return added
