from typing import List


def minimumValueSum(nums: List[int], andValues: List[int]) -> int:
    n = len(nums)
    INF = float("inf")
    # prev[i] = min cost covering nums[0..i-1] with j segments
    prev = [INF] * (n + 1)
    prev[0] = 0
    for a in andValues:
        cur = [INF] * (n + 1)
        groups = []  # list of [and_value, min prev[l]] for subarrays ending at r
        for r in range(n):
            x = nums[r]
            new_groups = []
            for v, best in groups:
                nv = v & x
                if new_groups and new_groups[-1][0] == nv:
                    if best < new_groups[-1][1]:
                        new_groups[-1][1] = best
                else:
                    new_groups.append([nv, best])
            p = prev[r]
            if new_groups and new_groups[-1][0] == x:
                if p < new_groups[-1][1]:
                    new_groups[-1][1] = p
            else:
                new_groups.append([x, p])
            groups = new_groups
            for v, best in groups:
                if v == a:
                    if best != INF:
                        cur[r + 1] = best + x
                    break
        prev = cur
    res = prev[n]
    return -1 if res == INF else int(res)
