MOD = 10**9 + 7


def _count_upto(s: str) -> int:
    """Count stepping numbers in [1, int(s)]."""
    n = len(s)
    digits = [ord(c) - 48 for c in s]
    # Numbers with fewer digits than n: any stepping number of length L < n.
    total = 0
    # ways[d] = number of stepping numbers of current length ending in digit d
    ways = [0] + [1] * 9
    for length in range(1, n):
        total += sum(ways)
        nxt = [0] * 10
        for d in range(10):
            w = ways[d]
            if w:
                if d > 0:
                    nxt[d - 1] += w
                if d < 9:
                    nxt[d + 1] += w
        ways = [v % MOD for v in nxt]
    total %= MOD

    # Numbers with exactly n digits and <= s.
    # free[d] = count of non-tight prefixes ending in digit d.
    free = [0] * 10
    tight_ok = True
    first = digits[0]
    for d in range(1, first):
        free[d] += 1
    prev_tight = first
    for i in range(1, n):
        cur = digits[i]
        nxt = [0] * 10
        for d in range(10):
            w = free[d]
            if w:
                if d > 0:
                    nxt[d - 1] += w
                if d < 9:
                    nxt[d + 1] += w
        if tight_ok:
            for nd in (prev_tight - 1, prev_tight + 1):
                if 0 <= nd < cur:
                    nxt[nd] += 1
            if abs(cur - prev_tight) == 1:
                prev_tight = cur
            else:
                tight_ok = False
        free = [v % MOD for v in nxt]
    total += sum(free)
    if tight_ok:
        total += 1
    return total % MOD


def _is_stepping(s: str) -> bool:
    return all(abs(ord(s[i]) - ord(s[i + 1])) == 1 for i in range(len(s) - 1))


def countSteppingNumbers(low: str, high: str) -> int:
    res = _count_upto(high) - _count_upto(low)
    if _is_stepping(low):
        res += 1
    return res % MOD
