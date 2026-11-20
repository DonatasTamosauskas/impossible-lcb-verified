from collections import deque
from typing import List


def countNonDecreasingSubarrays(nums: List[int], k: int) -> int:
    n = len(nums)
    dq = deque()  # segments [value, count], leftmost first; value = prefix max of those elements
    cost = 0
    j = n - 1
    total = 0
    for i in range(n - 1, -1, -1):
        v = nums[i]
        cnt = 1
        while dq and dq[0][0] <= v:
            pv, pc = dq.popleft()
            cost += (v - pv) * pc
            cnt += pc
        dq.appendleft([v, cnt])
        while cost > k:
            seg = dq[-1]
            cost -= seg[0] - nums[j]
            seg[1] -= 1
            if seg[1] == 0:
                dq.pop()
            j -= 1
        total += j - i + 1
    return total
