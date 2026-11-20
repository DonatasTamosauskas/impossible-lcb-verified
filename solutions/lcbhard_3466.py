from typing import List


def countSubarrays(nums: List[int], k: int) -> int:
    # For each right end, keep the distinct AND values of subarrays ending there
    # (at most ~31 of them, ordered from the shortest subarray to the longest) with counts.
    res = 0
    prev = []  # list of [and_value, count]
    for x in nums:
        cur = [[x, 1]]
        for v, c in prev:
            nv = v & x
            if nv == cur[-1][0]:
                cur[-1][1] += c
            else:
                cur.append([nv, c])
        prev = cur
        for v, c in cur:
            if v == k:
                res += c
                break
    return res
