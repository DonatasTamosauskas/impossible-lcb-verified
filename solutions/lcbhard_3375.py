from typing import List
from math import gcd


def findKthSmallest(coins: List[int], k: int) -> int:
    cs = sorted(set(coins))
    # Drop coins that are multiples of a smaller coin; they add no new amounts.
    base = []
    for c in cs:
        if all(c % b for b in base):
            base.append(c)
    hi = min(base) * k
    # Inclusion-exclusion terms (lcm, sign), pruned when lcm exceeds hi.
    terms = []
    stack = [(0, 1, 0)]  # (start index, lcm, count)
    while stack:
        start, l, cnt = stack.pop()
        for i in range(start, len(base)):
            c = base[i]
            nl = l // gcd(l, c) * c
            if nl > hi:
                continue
            terms.append((nl, 1 if (cnt + 1) % 2 == 1 else -1))
            stack.append((i + 1, nl, cnt + 1))

    def count(x: int) -> int:
        s = 0
        for l, sg in terms:
            if l <= x:
                s += sg * (x // l)
        return s

    lo = 1
    while lo < hi:
        mid = (lo + hi) // 2
        if count(mid) >= k:
            hi = mid
        else:
            lo = mid + 1
    return lo
