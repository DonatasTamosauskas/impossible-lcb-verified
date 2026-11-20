from typing import List


def permute(n: int, k: int) -> List[int]:
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i

    def completions(o: int, e: int, q: int) -> int:
        # ways to arrange o odds and e evens alternating, starting with parity q (1=odd, 0=even)
        m = o + e
        if m == 0:
            return 1
        need_q = (m + 1) // 2
        need_other = m // 2
        if q == 1:
            if o != need_q or e != need_other:
                return 0
        else:
            if e != need_q or o != need_other:
                return 0
        return fact[o] * fact[e]

    used = [False] * (n + 1)
    odd_rem = (n + 1) // 2
    even_rem = n // 2
    res: List[int] = []
    prev_par = -1
    for _ in range(n):
        found = False
        for v in range(1, n + 1):
            if used[v]:
                continue
            p = v & 1
            if p == prev_par:
                continue
            o2 = odd_rem - (1 if p == 1 else 0)
            e2 = even_rem - (1 if p == 0 else 0)
            cnt = completions(o2, e2, 1 - p)
            if cnt == 0:
                continue
            if k <= cnt:
                used[v] = True
                res.append(v)
                odd_rem, even_rem = o2, e2
                prev_par = p
                found = True
                break
            k -= cnt
        if not found:
            return []
    return res
