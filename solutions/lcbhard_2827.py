from typing import List


def canTraverseAllPairs(nums: List[int]) -> bool:
    n = len(nums)
    if n == 1:
        return True
    if 1 in nums:
        return False
    mx = max(nums)
    spf = list(range(mx + 1))
    i = 2
    while i * i <= mx:
        if spf[i] == i:
            for j in range(i * i, mx + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    parent = list(range(n + mx + 1))

    def find(x: int) -> int:
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for idx, v in enumerate(nums):
        x = v
        while x > 1:
            p = spf[x]
            union(idx, n + p)
            while x % p == 0:
                x //= p
    root = find(0)
    for idx in range(1, n):
        if find(idx) != root:
            return False
    return True
