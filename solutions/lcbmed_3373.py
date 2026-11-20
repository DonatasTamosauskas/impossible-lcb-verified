from typing import List


def maximumPrimeDifference(nums: List[int]) -> int:
    def isp(x):
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True
    ps = [i for i, x in enumerate(nums) if isp(x)]
    return ps[-1] - ps[0]
