from typing import List

MOD = 10**9 + 7


def maxSum(nums: List[int], k: int) -> int:
    # The operation preserves the per-bit counts; greedily concentrate bits
    # into the k largest possible numbers.
    bits = [0] * 31
    for x in nums:
        b = 0
        while x:
            if x & 1:
                bits[b] += 1
            x >>= 1
            b += 1
    ans = 0
    for _ in range(k):
        val = 0
        for b in range(31):
            if bits[b]:
                bits[b] -= 1
                val |= 1 << b
        if val == 0:
            break
        ans = (ans + val * val) % MOD
    return ans
