from typing import List


def minMaxWeight(n: int, edges: List[List[int]], threshold: int) -> int:
    def ok(w):
        radj = [[] for _ in range(n)]
        for a, b, c in edges:
            if c <= w:
                radj[b].append(a)
        seen = [False] * n
        seen[0] = True
        st = [0]
        cnt = 1
        while st:
            u = st.pop()
            for v in radj[u]:
                if not seen[v]:
                    seen[v] = True
                    cnt += 1
                    st.append(v)
        return cnt == n

    ws = sorted(set(e[2] for e in edges))
    if not ok(ws[-1]):
        return -1
    lo, hi = 0, len(ws) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(ws[mid]):
            hi = mid
        else:
            lo = mid + 1
    return ws[lo]
