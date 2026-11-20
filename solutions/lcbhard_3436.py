from typing import List


def minimumDifference(nums: List[int], k: int) -> int:
    best = abs(nums[0] - k)
    cur = set()
    for v in nums:
        cur = {o | v for o in cur}
        cur.add(v)
        for o in cur:
            d = o - k if o > k else k - o
            if d < best:
                best = d
        if best == 0:
            return 0
    return best
