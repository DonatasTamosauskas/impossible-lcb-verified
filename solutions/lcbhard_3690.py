def minLength(s: str, numOps: int) -> int:
    n = len(s)
    # L = 1: alternating pattern
    mis = sum(1 for i, ch in enumerate(s) if (ord(ch) - 48) != (i & 1))
    if min(mis, n - mis) <= numOps:
        return 1
    runs = []
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        runs.append(j - i)
        i = j
    lo, hi = 2, max(runs)
    while lo < hi:
        mid = (lo + hi) // 2
        need = 0
        for k in runs:
            need += k // (mid + 1)
        if need <= numOps:
            hi = mid
        else:
            lo = mid + 1
    return lo
