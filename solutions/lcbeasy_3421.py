from typing import List


def countCompleteDayPairs(hours: List[int]) -> int:
    cnt = [0] * 24
    res = 0
    for h in hours:
        r = h % 24
        res += cnt[(24 - r) % 24]
        cnt[r] += 1
    return res
