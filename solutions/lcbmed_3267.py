def maximumLength(s: str) -> int:
    n = len(s)
    cnt = {}
    for i in range(n):
        j = i
        while j < n and s[j] == s[i]:
            j += 1
            cnt[(s[i], j - i)] = cnt.get((s[i], j - i), 0) + 1
    best = -1
    for (c, l), v in cnt.items():
        if v >= 3 and l > best:
            best = l
    return best
