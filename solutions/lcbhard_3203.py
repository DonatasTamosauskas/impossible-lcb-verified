from typing import List


def canMakePalindromeQueries(s: str, queries: List[List[int]]) -> List[bool]:
    n = len(s)
    m = n // 2
    left = s[:m]
    right = s[m:][::-1]
    # mismatch prefix
    mis = [0] * (m + 1)
    for i in range(m):
        mis[i + 1] = mis[i] + (1 if left[i] != right[i] else 0)
    # per-letter prefix counts
    pl = [[0] * (m + 1) for _ in range(26)]
    pr = [[0] * (m + 1) for _ in range(26)]
    for c in range(26):
        ch = chr(97 + c)
        arr = pl[c]
        acc = 0
        for i in range(m):
            if left[i] == ch:
                acc += 1
            arr[i + 1] = acc
        arr = pr[c]
        acc = 0
        for i in range(m):
            if right[i] == ch:
                acc += 1
            arr[i + 1] = acc

    def mism(lo: int, hi: int) -> int:
        # inclusive range, empty if lo > hi
        if lo > hi:
            return 0
        return mis[hi + 1] - mis[lo]

    res: List[bool] = []
    for a, b, c, d in queries:
        c2 = n - 1 - d
        d2 = n - 1 - c
        # outside union must have no mismatches
        lo = a if a < c2 else c2
        hi = b if b > d2 else d2
        if mism(0, lo - 1) or mism(hi + 1, m - 1):
            res.append(False)
            continue
        ok = True
        if b < c2 or d2 < a:
            # disjoint
            if b < c2:
                if mism(b + 1, c2 - 1):
                    res.append(False)
                    continue
            else:
                if mism(d2 + 1, a - 1):
                    res.append(False)
                    continue
            for ci in range(26):
                L = pl[ci]
                R = pr[ci]
                if L[b + 1] - L[a] != R[b + 1] - R[a] or L[d2 + 1] - L[c2] != R[d2 + 1] - R[c2]:
                    ok = False
                    break
        elif a <= c2 and d2 <= b:
            # A contains B
            for ci in range(26):
                L = pl[ci]
                R = pr[ci]
                if L[b + 1] - L[a] != R[b + 1] - R[a]:
                    ok = False
                    break
        elif c2 <= a and b <= d2:
            # B contains A
            for ci in range(26):
                L = pl[ci]
                R = pr[ci]
                if L[d2 + 1] - L[c2] != R[d2 + 1] - R[c2]:
                    ok = False
                    break
        elif a < c2:
            # a < c2 <= b < d2: union [a, d2]
            # left free on [a,b], left fixed on (b, d2]
            # right free on [c2,d2], right fixed on [a, c2)
            for ci in range(26):
                L = pl[ci]
                R = pr[ci]
                lf = L[b + 1] - L[a]
                need_r_fixed = R[c2] - R[a]
                rf = R[d2 + 1] - R[c2]
                need_l_fixed = L[d2 + 1] - L[b + 1]
                x = lf - need_r_fixed
                y = rf - need_l_fixed
                if x < 0 or y < 0 or x != y:
                    ok = False
                    break
        else:
            # c2 < a <= d2 < b: union [c2, b]
            # right free on [c2,d2], right fixed on (d2, b]
            # left free on [a,b], left fixed on [c2, a)
            for ci in range(26):
                L = pl[ci]
                R = pr[ci]
                rf = R[d2 + 1] - R[c2]
                need_l_fixed = L[a] - L[c2]
                lf = L[b + 1] - L[a]
                need_r_fixed = R[b + 1] - R[d2 + 1]
                x = rf - need_l_fixed
                y = lf - need_r_fixed
                if x < 0 or y < 0 or x != y:
                    ok = False
                    break
        res.append(ok)
    return res
