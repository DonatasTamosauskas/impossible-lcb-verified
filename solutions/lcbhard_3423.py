from typing import List


def maximumSumSubsequence(nums: List[int], queries: List[List[int]]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    size = 1
    while size < n:
        size *= 2
    # a: first excluded, last excluded; b: first excluded, last any;
    # c: first any, last excluded; d: first any, last any.
    a = [0] * (2 * size)
    b = [0] * (2 * size)
    c = [0] * (2 * size)
    d = [0] * (2 * size)
    for i, v in enumerate(nums):
        d[size + i] = v if v > 0 else 0

    def pull(p: int) -> None:
        l = 2 * p
        r = l + 1
        la, lb, lc, ld = a[l], b[l], c[l], d[l]
        ra, rb, rc, rd = a[r], b[r], c[r], d[r]
        x = lc + rd
        y = ld + rb
        d[p] = x if x > y else y
        x = lc + rc
        y = ld + ra
        c[p] = x if x > y else y
        x = la + rd
        y = lb + rb
        b[p] = x if x > y else y
        x = la + rc
        y = lb + ra
        a[p] = x if x > y else y

    for p in range(size - 1, 0, -1):
        pull(p)

    total = 0
    for pos, x in queries:
        p = size + pos
        d[p] = x if x > 0 else 0
        p >>= 1
        while p:
            pull(p)
            p >>= 1
        total += d[1]
    return total % MOD
