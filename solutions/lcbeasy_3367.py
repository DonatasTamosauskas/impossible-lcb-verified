from typing import List


def sumOfEncryptedInt(nums: List[int]) -> int:
    t = 0
    for x in nums:
        d = str(x)
        t += int(max(d) * len(d))
    return t
