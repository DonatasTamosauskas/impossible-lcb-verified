MOD = 10**9 + 7


def _count_upto(s: str, min_sum: int, max_sum: int) -> int:
    # Number of integers x in [0, int(s)] with min_sum <= digit_sum(x) <= max_sum.
    cap = max_sum + 1  # sums above max_sum collapse into one bucket
    # free[t] = count of prefixes already strictly less than s with digit sum t (capped)
    free = [0] * (cap + 1)
    tight_sum = 0
    for ch in s:
        d = int(ch)
        new = [0] * (cap + 1)
        for t in range(cap + 1):
            c = free[t]
            if c:
                for k in range(10):
                    nt = t + k
                    if nt > cap:
                        nt = cap
                    new[nt] = (new[nt] + c) % MOD
        for k in range(d):
            nt = tight_sum + k
            if nt > cap:
                nt = cap
            new[nt] = (new[nt] + 1) % MOD
        tight_sum = min(tight_sum + d, cap)
        free = new
    total = 0
    for t in range(min_sum, max_sum + 1):
        if t <= cap:
            total += free[t]
    if min_sum <= tight_sum <= max_sum:
        total += 1
    return total % MOD


def count(num1: str, num2: str, min_sum: int, max_sum: int) -> int:
    a = _count_upto(num2, min_sum, max_sum)
    b = _count_upto(num1, min_sum, max_sum)
    ds = sum(int(c) for c in num1)
    extra = 1 if min_sum <= ds <= max_sum else 0
    return (a - b + extra) % MOD
