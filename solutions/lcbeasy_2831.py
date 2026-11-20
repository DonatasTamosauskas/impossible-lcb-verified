from math import gcd
from typing import List


def countBeautifulPairs(nums: List[int]) -> int:
    cnt = [0] * 10
    total = 0
    for x in nums:
        last = x % 10
        for d in range(1, 10):
            if cnt[d] and gcd(d, last) == 1:
                total += cnt[d]
        cnt[int(str(x)[0])] += 1
    return total
