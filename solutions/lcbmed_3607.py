from typing import List

_N = 10**6 + 1
_spf = None


def _build():
    global _spf
    spf = list(range(_N))
    i = 2
    while i * i < _N:
        if spf[i] == i:
            for j in range(i * i, _N, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    _spf = spf


def minOperations(nums: List[int]) -> int:
    if _spf is None:
        _build()
    ops = 0
    prev = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        x = nums[i]
        if x > prev:
            x = _spf[x]
            ops += 1
            if x > prev:
                return -1
        prev = x
    return ops
