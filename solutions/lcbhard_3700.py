from typing import List
from collections import Counter


def _c2(k):
    return k * (k - 1) // 2


def subsequencesWithMiddleMode(nums: List[int]) -> int:
    MOD = 10 ** 9 + 7
    n = len(nums)
    # compress values
    idx = {}
    arr = []
    for v in nums:
        if v not in idx:
            idx[v] = len(idx)
        arr.append(idx[v])
    D = len(idx)
    L = [0] * D
    R = [0] * D
    for v in arr:
        R[v] += 1
    total = 0
    for i in range(n):
        x = arr[i]
        R[x] -= 1
        lt = i
        rt = n - 1 - i
        a = L[x]
        b = R[x]
        if lt >= 2 and rt >= 2:
            ln = lt - a
            rn = rt - b
            # k >= 2 : x appears at least 3 times in total
            cl = [_c2(ln), a * ln, _c2(a)]  # ways to pick 2 from left with p x's
            cr = [_c2(rn), b * rn, _c2(b)]
            good = 0
            for p in range(3):
                for q in range(3):
                    if p + q >= 2:
                        good += cl[p] * cr[q]
            # k == 1, other three values pairwise distinct and != x
            sumC2L = 0
            sumC2R = 0
            S1 = 0  # sum L*R*(rn - R)
            S2 = 0  # sum R*L*(ln - L)
            for u in range(D):
                if u == x:
                    continue
                lu = L[u]
                ru = R[u]
                if lu > 1:
                    sumC2L += lu * (lu - 1) // 2
                if ru > 1:
                    sumC2R += ru * (ru - 1) // 2
                if lu and ru:
                    S1 += lu * ru * (rn - ru)
                    S2 += ru * lu * (ln - lu)
            P = _c2(rn) - sumC2R
            Q = _c2(ln) - sumC2L
            caseA = a * (ln * P - S1)
            caseB = b * (rn * Q - S2)
            total += good + caseA + caseB
        L[x] += 1
    return total % MOD
