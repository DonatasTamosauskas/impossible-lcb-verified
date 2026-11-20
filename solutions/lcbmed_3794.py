from typing import List


def minTime(skill: List[int], mana: List[int]) -> int:
    n = len(skill)
    pre = [0] * (n + 1)
    for i, x in enumerate(skill):
        pre[i + 1] = pre[i] + x
    try:
        import numpy as np
        p = np.array(pre, dtype=np.int64)
        lo, hi = p[:-1], p[1:]
        start = 0
        for j in range(1, len(mana)):
            a, b = mana[j - 1], mana[j]
            start += int((hi * a - lo * b).max())
        return start + pre[n] * mana[-1]
    except ImportError:
        start = 0
        for j in range(1, len(mana)):
            a, b = mana[j - 1], mana[j]
            start += max(pre[i + 1] * a - pre[i] * b for i in range(n))
        return start + pre[n] * mana[-1]
