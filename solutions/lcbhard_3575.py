from typing import List


def maxValue(nums: List[int], k: int) -> int:
    n = len(nums)
    if k <= 0 or 2 * k > n:
        return 0
    B = max(1, max(nums).bit_length())
    V = 1 << B
    FULL = (1 << V) - 1
    # bitmasks[b] = set of values in [0, V) whose bit b is set
    bitmasks = []
    for b in range(B):
        m = 0
        for v in range(V):
            if (v >> b) & 1:
                m |= 1 << v
        bitmasks.append(m)

    def apply_or(S, num):
        # map every value v in set S to v | num
        for b in range(B):
            if (num >> b) & 1:
                M = bitmasks[b]
                S = (S & M) | (((S & (FULL ^ M)) << (1 << b)) & FULL)
        return S

    def sweep(arr):
        # res[i] = set (as mask) of ORs of exactly k elements chosen from arr[0..i]
        dp = [0] * (k + 1)
        dp[0] = 1  # value 0 with zero elements
        res = [0] * len(arr)
        for i, num in enumerate(arr):
            top = min(i + 1, k)
            for j in range(top, 0, -1):
                if dp[j - 1]:
                    dp[j] |= apply_or(dp[j - 1], num)
            res[i] = dp[k]
        return res

    pre = sweep(nums)
    suf = sweep(nums[::-1])[::-1]  # suf[i] = set from nums[i..]

    def to_list(mask):
        return [v for v in range(V) if (mask >> v) & 1]

    memo = {}
    best = 0
    for i in range(k - 1, n - k):
        pm = pre[i]
        sm = suf[i + 1]
        if not pm or not sm:
            continue
        key = (pm, sm)
        val = memo.get(key)
        if val is None:
            pl = to_list(pm)
            val = 0
            found = False
            for x in range(V - 1, -1, -1):
                for a in pl:
                    if (sm >> (a ^ x)) & 1:
                        val = x
                        found = True
                        break
                if found:
                    break
            memo[key] = val
        if val > best:
            best = val
    return best
