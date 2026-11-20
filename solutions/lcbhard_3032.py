from typing import List


def getMaxFunctionValue(receiver: List[int], k: int) -> int:
    n = len(receiver)
    up = list(receiver)          # node after 2^j passes
    sm = list(receiver)          # sum of ids received over 2^j passes
    cur = list(range(n))         # current position for each start
    total = list(range(n))       # accumulated f for each start
    while k:
        if k & 1:
            total = [total[x] + sm[c] for x, c in enumerate(cur)]
            cur = [up[c] for c in cur]
        k >>= 1
        if k:
            sm = [sm[x] + sm[u] for x, u in enumerate(up)]
            up = [up[u] for u in up]
    return max(total)
