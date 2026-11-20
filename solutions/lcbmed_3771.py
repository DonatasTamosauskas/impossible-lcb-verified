def maxSubstringLength(s: str, k: int) -> bool:
    n = len(s)
    first = {}
    last = {}
    for i, c in enumerate(s):
        first.setdefault(c, i)
        last[c] = i
    ivs = []
    for c in first:
        l = first[c]
        r = last[c]
        i = l
        ok = True
        while i <= r:
            ch = s[i]
            if first[ch] < l:
                ok = False
                break
            if last[ch] > r:
                r = last[ch]
            i += 1
        if ok and not (l == 0 and r == n - 1):
            ivs.append((r, l))
    ivs.sort()
    cnt = 0
    end = -1
    for r, l in ivs:
        if l > end:
            cnt += 1
            end = r
    return cnt >= k
