def findMaximumNumber(k: int, x: int) -> int:
    def cost(n):
        m = n + 1
        t = 0
        p = x - 1
        while (1 << p) <= m:
            blk = 1 << (p + 1)
            t += (m // blk) * (1 << p) + max(0, m % blk - (1 << p))
            p += x
        return t
    lo, hi = 0, 1 << 62
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if cost(mid) <= k:
            lo = mid
        else:
            hi = mid - 1
    return lo
