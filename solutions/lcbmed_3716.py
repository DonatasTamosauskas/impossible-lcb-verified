from typing import List


def longestSubsequence(nums: List[int]) -> int:
    M = 300
    best = [None] * (M + 1)
    ans = 1
    seen = []
    for x in nums:
        cand = [1] * (M + 1)
        for v in seen:
            t = abs(x - v)
            val = best[v][t] + 1
            if val > cand[t]:
                cand[t] = val
        for d in range(M - 1, -1, -1):
            if cand[d + 1] > cand[d]:
                cand[d] = cand[d + 1]
        if best[x] is None:
            best[x] = cand
            seen.append(x)
        else:
            b = best[x]
            for d in range(M + 1):
                if cand[d] > b[d]:
                    b[d] = cand[d]
        if cand[0] > ans:
            ans = cand[0]
    return ans
