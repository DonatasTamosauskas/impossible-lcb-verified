def _tables(maxL):
    f = [{(0, 1): 1}]
    for _ in range(maxL):
        prev = f[-1]
        cur = {}
        for (s, p), c in prev.items():
            for d in range(1, 10):
                key = (s + d, p * d)
                cur[key] = cur.get(key, 0) + c
        f.append(cur)
    return f


def _count(N, f):
    # beautiful numbers in [1, N]
    if N <= 0:
        return 0
    D = list(map(int, str(N)))
    m = len(D)
    memo = {}

    def comp(s0, p0, hasZero, L):
        if hasZero:
            return 10 ** L
        key = (s0, p0, L)
        if key in memo:
            return memo[key]
        total = 10 ** L - 9 ** L
        for (s, p), c in f[L].items():
            if (p0 * p) % (s0 + s) == 0:
                total += c
        memo[key] = total
        return total

    res = 0
    for L in range(1, m):
        for d in range(1, 10):
            res += comp(d, d, False, L - 1)
    s0, p0, hz = 0, 1, False
    for i in range(m):
        lo = 1 if i == 0 else 0
        for x in range(lo, D[i]):
            res += comp(s0 + x, p0 * x, hz or x == 0, m - i - 1)
        s0 += D[i]
        p0 *= D[i]
        if D[i] == 0:
            hz = True
    if p0 % s0 == 0:
        res += 1
    return res


def beautifulNumbers(l: int, r: int) -> int:
    f = _tables(len(str(r)))
    return _count(r, f) - _count(l - 1, f)
