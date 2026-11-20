from typing import List

MOD = 10**9 + 7


def sumOfPower(nums: List[int]) -> int:
    arr = sorted(nums)
    ans = 0
    s = 0  # sum over j<i of arr[j] * 2^(i-j-1)
    for x in arr:
        xm = x % MOD
        ans = (ans + xm * xm % MOD * ((xm + s) % MOD)) % MOD
        s = (2 * s + xm) % MOD
    return ans
