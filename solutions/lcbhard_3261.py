from typing import List


def minOrAfterOperations(nums: List[int], k: int) -> int:
    mask = 0
    for b in range(29, -1, -1):
        m = mask | (1 << b)
        cnt = 0
        cur = -1
        for x in nums:
            cur &= x
            if cur & m:
                cnt += 1
                if cnt > k:
                    break
            else:
                cur = -1
        if cnt <= k:
            mask = m
    return ((1 << 30) - 1) & ~mask
