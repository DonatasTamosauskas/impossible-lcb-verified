from typing import List


def numberOfEmployeesWhoMetTarget(hours: List[int], target: int) -> int:
    return sum(1 for h in hours if h >= target)
