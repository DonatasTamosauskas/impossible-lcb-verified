from functools import lru_cache


def _count_upto(n: int, k: int) -> int:
    """Count beautiful integers in [1, n]."""
    if n <= 0:
        return 0
    digits = [int(c) for c in str(n)]
    L = len(digits)

    @lru_cache(maxsize=None)
    def go(pos: int, diff: int, mod: int, tight: bool, started: bool) -> int:
        if pos == L:
            return 1 if (started and diff == 0 and mod == 0) else 0
        limit = digits[pos] if tight else 9
        res = 0
        for d in range(limit + 1):
            nt = tight and d == limit
            if not started and d == 0:
                res += go(pos + 1, 0, 0, nt, False)
            else:
                nd = diff + (1 if d % 2 else -1)
                res += go(pos + 1, nd, (mod * 10 + d) % k, nt, True)
        return res

    result = go(0, 0, 0, True, False)
    go.cache_clear()
    return result


def numberOfBeautifulIntegers(low: int, high: int, k: int) -> int:
    return _count_upto(high, k) - _count_upto(low - 1, k)
