from typing import List


def countOfPeaks(nums: List[int], queries: List[List[int]]) -> List[int]:
    nums = list(nums)
    n = len(nums)
    peak = [0] * n
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peak[i] = 1
    tree = [0] * (n + 1)
    for i in range(n):
        if peak[i]:
            j = i + 1
            while j <= n:
                tree[j] += 1
                j += j & -j

    def add(i: int, delta: int) -> None:
        j = i + 1
        while j <= n:
            tree[j] += delta
            j += j & -j

    def prefix(i: int) -> int:
        # sum of peak[0..i-1]
        s = 0
        j = i
        while j > 0:
            s += tree[j]
            j -= j & -j
        return s

    ans: List[int] = []
    for q in queries:
        if q[0] == 1:
            l, r = q[1], q[2]
            if r - l < 2:
                ans.append(0)
            else:
                ans.append(prefix(r) - prefix(l + 1))
        else:
            idx, val = q[1], q[2]
            if nums[idx] == val:
                continue
            nums[idx] = val
            for i in (idx - 1, idx, idx + 1):
                if 0 < i < n - 1:
                    p = 1 if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]) else 0
                    if p != peak[i]:
                        add(i, p - peak[i])
                        peak[i] = p
    return ans
