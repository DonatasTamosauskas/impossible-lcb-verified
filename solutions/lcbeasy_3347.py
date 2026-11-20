from typing import List


def resultArray(nums: List[int]) -> List[int]:
    a = [nums[0]]
    b = [nums[1]]
    for x in nums[2:]:
        if a[-1] > b[-1]:
            a.append(x)
        else:
            b.append(x)
    return a + b
