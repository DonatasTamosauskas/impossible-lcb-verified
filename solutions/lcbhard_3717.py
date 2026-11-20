from heapq import heappush, heappop
from typing import List


def _window_costs(nums: List[int], x: int) -> List[int]:
    """cost[i] = min ops to make nums[i:i+x] all equal (sum of |v - median|)."""
    n = len(nums)
    lo = []  # max-heap via (-v, idx)
    hi = []  # min-heap (v, idx)
    side = [0] * n  # 0 -> lo, 1 -> hi
    dead = [False] * n
    lo_n = hi_n = 0
    lo_s = hi_s = 0
    costs = [0] * (n - x + 1)
    for i in range(n):
        if i >= x:
            j = i - x
            dead[j] = True
            v = nums[j]
            if side[j] == 0:
                lo_n -= 1
                lo_s -= v
            else:
                hi_n -= 1
                hi_s -= v
            while lo and dead[lo[0][1]]:
                heappop(lo)
            while hi and dead[hi[0][1]]:
                heappop(hi)
        v = nums[i]
        if lo and v <= -lo[0][0]:
            heappush(lo, (-v, i))
            side[i] = 0
            lo_n += 1
            lo_s += v
        else:
            heappush(hi, (v, i))
            side[i] = 1
            hi_n += 1
            hi_s += v
        # rebalance: lo_n == hi_n or lo_n == hi_n + 1
        while lo_n > hi_n + 1:
            while dead[lo[0][1]]:
                heappop(lo)
            nv, idx = heappop(lo)
            w = -nv
            heappush(hi, (w, idx))
            side[idx] = 1
            lo_n -= 1
            lo_s -= w
            hi_n += 1
            hi_s += w
        while lo_n < hi_n:
            while dead[hi[0][1]]:
                heappop(hi)
            w, idx = heappop(hi)
            heappush(lo, (-w, idx))
            side[idx] = 0
            hi_n -= 1
            hi_s -= w
            lo_n += 1
            lo_s += w
        while lo and dead[lo[0][1]]:
            heappop(lo)
        while hi and dead[hi[0][1]]:
            heappop(hi)
        if i >= x - 1:
            med = -lo[0][0]
            costs[i - x + 1] = med * lo_n - lo_s + hi_s - med * hi_n
    return costs


def minOperations(nums: List[int], x: int, k: int) -> int:
    n = len(nums)
    cost = _window_costs(nums, x)
    INF = float("inf")
    # prev[i]: min cost using j-1 windows within the first i elements
    prev = [0] * (n + 1)
    for j in range(1, k + 1):
        cur = [INF] * (n + 1)
        start = j * x
        best = INF
        for i in range(start, n + 1):
            cand = prev[i - x] + cost[i - x]
            if cand < best:
                best = cand
            cur[i] = best
        prev = cur
    return int(prev[n])
