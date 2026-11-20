from typing import List


def minimumMoves(nums: List[int], k: int, maxChanges: int) -> int:
    n = len(nums)
    # c = longest run of consecutive ones, capped at 3 (ones at distance <= 1 from Alice)
    c = 0
    run = 0
    for x in nums:
        if x:
            run += 1
            if run > c:
                c = run
        else:
            run = 0
    c = min(c, 3)
    if c >= k:
        return k - 1 if k > 0 else 0
    if c + maxChanges >= k:
        return max(c - 1, 0) + (k - c) * 2
    pos = [i for i, x in enumerate(nums) if x]
    m = k - maxChanges
    pre = [0]
    for p in pos:
        pre.append(pre[-1] + p)
    best = None
    for l in range(len(pos) - m + 1):
        r = l + m - 1
        mid = (l + r) // 2
        pm = pos[mid]
        cost = pm * (mid - l) - (pre[mid] - pre[l]) + (pre[r + 1] - pre[mid + 1]) - pm * (r - mid)
        if best is None or cost < best:
            best = cost
    return best + maxChanges * 2
