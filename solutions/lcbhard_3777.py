from typing import List


def maxProduct(nums: List[int], k: int, limit: int) -> int:
    n = len(nums)
    max_abs = 12 * ((n + 1) // 2)
    if k > max_abs or k < -12 * (n // 2):
        return -1
    OFF = 12 * (n // 2)
    OVER = limit + 1  # sentinel: product exceeds limit (and is nonzero)
    # states[(parity, product)] = bitset of reachable alternating sums (offset by OFF)
    # parity = length % 2; next element added with sign + if parity == 0 else -
    states = {}
    for x in nums:
        new = dict(states)
        # transitions from existing non-empty subsequences
        for (par, prod), bits in states.items():
            if prod == OVER:
                np_ = 0 if x == 0 else OVER
            else:
                np_ = prod * x
                if np_ > limit:
                    np_ = OVER
            nb = (bits << x) if par == 0 else (bits >> x)
            key = (1 - par, np_)
            new[key] = new.get(key, 0) | nb
        # start new subsequence with x
        p0 = x if x <= limit else OVER
        key = (1, p0)
        new[key] = new.get(key, 0) | (1 << (x + OFF))
        states = new
    target = k + OFF
    best = -1
    for (par, prod), bits in states.items():
        if prod != OVER and prod > best and (bits >> target) & 1:
            best = prod
    return best
