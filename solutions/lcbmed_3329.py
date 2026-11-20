from typing import List


def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
    pre = set()
    for x in arr1:
        while x:
            pre.add(x)
            x //= 10
    best = 0
    for y in arr2:
        while y:
            if y in pre:
                best = max(best, len(str(y)))
                break
            y //= 10
    return best
