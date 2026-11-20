from typing import List


def solveQueries(nums: List[int], queries: List[int]) -> List[int]:
    n = len(nums)
    pos = {}
    for i, v in enumerate(nums):
        pos.setdefault(v, []).append(i)
    ans = [-1] * n
    for p in pos.values():
        m = len(p)
        if m < 2:
            continue
        for t in range(m):
            best = n
            for q in (p[t - 1], p[(t + 1) % m]):
                dd = abs(p[t] - q)
                best = min(best, dd, n - dd)
            ans[p[t]] = best
    return [ans[q] for q in queries]
