from typing import List


def countTestedDevices(batteryPercentages: List[int]) -> int:
    c = 0
    for v in batteryPercentages:
        if v - c > 0:
            c += 1
    return c
