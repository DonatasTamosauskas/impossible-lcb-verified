def numberOfSubstrings(s: str, k: int) -> int:
    n = len(s)
    total = 0
    for i in range(n):
        cnt = {}
        for j in range(i, n):
            c = s[j]
            v = cnt.get(c, 0) + 1
            cnt[c] = v
            if v >= k:
                total += n - j
                break
    return total
