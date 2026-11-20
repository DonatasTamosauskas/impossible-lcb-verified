from typing import List


def lastVisitedIntegers(words: List[str]) -> List[int]:
    nums = []
    res = []
    k = 0
    for w in words:
        if w == "prev":
            k += 1
            res.append(nums[-k] if k <= len(nums) else -1)
        else:
            k = 0
            nums.append(int(w))
    return res
