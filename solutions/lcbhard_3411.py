from typing import List


def _bits_upto(m: int) -> int:
    # total popcount of 1..m
    total = 0
    b = 0
    while (1 << b) <= m:
        block = 1 << (b + 1)
        full = (m + 1) // block
        total += full * (1 << b)
        rem = (m + 1) % block - (1 << b)
        if rem > 0:
            total += rem
        b += 1
    return total


def _exp_sum_upto(m: int) -> int:
    # sum over 1..m of sum of exponents of set bits
    total = 0
    b = 0
    while (1 << b) <= m:
        block = 1 << (b + 1)
        full = (m + 1) // block
        cnt = full * (1 << b)
        rem = (m + 1) % block - (1 << b)
        if rem > 0:
            cnt += rem
        total += cnt * b
        b += 1
    return total


def _prefix(idx: int) -> int:
    # sum of exponents of the first idx elements of big_nums
    if idx <= 0:
        return 0
    lo, hi = 0, 1
    while _bits_upto(hi) <= idx:
        hi *= 2
    # largest m with _bits_upto(m) <= idx
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if _bits_upto(mid) <= idx:
            lo = mid
        else:
            hi = mid - 1
    m = lo
    res = _exp_sum_upto(m)
    r = idx - _bits_upto(m)
    nxt = m + 1
    b = 0
    while r > 0:
        if (nxt >> b) & 1:
            res += b
            r -= 1
        b += 1
    return res


def findProductsOfElements(queries: List[List[int]]) -> List[int]:
    ans = []
    for f, t, mod in queries:
        e = _prefix(t + 1) - _prefix(f)
        ans.append(pow(2, e, mod))
    return ans
