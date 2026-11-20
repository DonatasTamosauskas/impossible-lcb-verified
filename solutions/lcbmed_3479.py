def numberOfSubstrings(s: str) -> int:
    n = len(s)
    zs = [i for i, c in enumerate(s) if c == '0']
    z = len(zs)
    nxt = [0] * (n + 1)
    idx = z
    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            idx -= 1
        nxt[i] = idx
    total = 0
    for i in range(n):
        idx = nxt[i]
        k = 0
        while True:
            need = i + k * k + k - 1
            if need >= n:
                break
            if idx + k > z:
                break
            start = i if k == 0 else zs[idx + k - 1]
            hi = zs[idx + k] - 1 if idx + k < z else n - 1
            lo = start if start > need else need
            if hi >= lo:
                total += hi - lo + 1
            k += 1
    return total
