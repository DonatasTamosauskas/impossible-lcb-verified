from bisect import bisect_left, bisect_right


def _occurrences(text: str, pat: str):
    n = len(text)
    m = len(pat)
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []
    t = pat + "\x00" + text
    pi = [0] * len(t)
    res = []
    k = 0
    for i in range(1, len(t)):
        c = t[i]
        while k and t[k] != c:
            k = pi[k - 1]
        if t[k] == c:
            k += 1
        pi[i] = k
        if k == m:
            res.append(i - 2 * m)
    return res


def shortestMatchingSubstring(s: str, p: str) -> int:
    a, b, c = p.split("*")
    la, lb, lc = len(a), len(b), len(c)
    occ_a = _occurrences(s, a)
    occ_b = _occurrences(s, b)
    occ_c = _occurrences(s, c)
    if not occ_a or not occ_b or not occ_c:
        return -1
    best = -1
    for j in occ_b:
        # latest a-start i with i + la <= j
        idx = bisect_right(occ_a, j - la) - 1
        if idx < 0:
            continue
        i = occ_a[idx]
        kidx = bisect_left(occ_c, j + lb)
        if kidx == len(occ_c):
            continue
        k = occ_c[kidx]
        length = k + lc - i
        if best < 0 or length < best:
            best = length
    return best
