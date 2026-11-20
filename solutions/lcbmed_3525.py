from typing import List


def maxEnergyBoost(energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
    a = b = 0
    pa = pb = 0
    # a: best ending drinking A at hour i; pa: best total through hour i-2
    for x, y in zip(energyDrinkA, energyDrinkB):
        na = max(a, pb) + x
        nb = max(b, pa) + y
        pa, pb = a, b
        a, b = na, nb
    return max(a, b)
