from typing import List


def minDifference(nums: List[int]) -> int:
    n = len(nums)
    base = 0
    for i in range(n - 1):
        a, b = nums[i], nums[i + 1]
        if a != -1 and b != -1:
            d = a - b if a > b else b - a
            if d > base:
                base = d
    segs = []
    i = 0
    while i < n:
        if nums[i] == -1:
            j = i
            while j + 1 < n and nums[j + 1] == -1:
                j += 1
            l = nums[i - 1] if i > 0 else None
            r = nums[j + 1] if j + 1 < n else None
            if l is not None or r is not None:
                segs.append((l, r, j - i + 1))
            i = j + 1
        else:
            i += 1
    if not segs:
        return base
    vals = []
    for l, r, _ in segs:
        if l is not None:
            vals.append(l)
        if r is not None:
            vals.append(r)
    lo = min(vals)
    hi = max(vals)

    def check(d: int) -> bool:
        x = lo + d
        y = hi - d
        for l, r, length in segs:
            if l is None or r is None:
                v = l if r is None else r
                if abs(v - x) > d and abs(v - y) > d:
                    return False
                continue
            lx = abs(l - x) <= d
            rx = abs(r - x) <= d
            ly = abs(l - y) <= d
            ry = abs(r - y) <= d
            if (lx and rx) or (ly and ry):
                continue
            if length >= 2 and abs(x - y) <= d and ((lx and ry) or (ly and rx)):
                continue
            return False
        return True

    left, right = base, max(base, hi - lo)
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left
