from typing import List


def minCost(nums: List[int]) -> int:
    n = len(nums)
    # state (j, i): list is [nums[j]] + nums[i:]
    INF = float('inf')
    # dp over i descending; f[j] for fixed i
    nxt = {}
    # compute with i from n down to 1
    f = [[0] * n for _ in range(n + 2)]
    for i in range(n, 0, -1):
        for j in range(i):
            if 1 + n - i < 3:
                f[i][j] = max([nums[j]] + nums[i:])
            else:
                a, b = nums[i], nums[i + 1]
                f[i][j] = min(
                    max(a, b) + f[i + 2][j],
                    max(nums[j], b) + f[i + 2][i],
                    max(nums[j], a) + f[i + 2][i + 1],
                )
    if n < 3:
        return max(nums)
    return f[1][0]
