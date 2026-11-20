from typing import List


def countPairs(nums: List[int]) -> int:
    def ok(x, y):
        if x == y:
            return True
        a, b = str(x), str(y)
        L = max(len(a), len(b))
        a, b = a.zfill(L), b.zfill(L)
        d = [i for i in range(L) if a[i] != b[i]]
        return len(d) == 2 and a[d[0]] == b[d[1]] and a[d[1]] == b[d[0]]

    n = len(nums)
    return sum(1 for i in range(n) for j in range(i + 1, n) if ok(nums[i], nums[j]))
