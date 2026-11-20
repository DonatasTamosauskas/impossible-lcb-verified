from typing import List


def buyChoco(prices: List[int], money: int) -> int:
    a, b = sorted(prices)[:2]
    return money - a - b if a + b <= money else money
