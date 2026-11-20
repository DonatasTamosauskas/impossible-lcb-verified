from typing import List


def minCostToEqualizeArray(nums: List[int], cost1: int, cost2: int) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    mx = max(nums)
    mn = min(nums)
    S = mx * n - sum(nums)  # total deficit at target mx
    d = mx - mn  # largest single deficit at target mx

    if n <= 2 or 2 * cost1 <= cost2:
        return (S * cost1) % MOD

    def cost_at(x: int) -> int:
        # target = mx + x
        T = S + n * x
        D = d + x
        rest = T - D
        if D <= rest:
            return (T // 2) * cost2 + (T % 2) * cost1
        return rest * cost2 + (D - rest) * cost1

    # Unbalanced region (D > T - D) is linear in x, balanced region is linear
    # apart from parity; check x = 0 and a window around the balance point.
    gap = 2 * d - S  # D - rest at x = 0; decreases by (n - 2) per step
    if gap <= 0:
        x0 = 0
    else:
        x0 = (gap + n - 3) // (n - 2)
    best = cost_at(0)
    for x in range(max(0, x0 - 2), x0 + 4):
        c = cost_at(x)
        if c < best:
            best = c
    return best % MOD
