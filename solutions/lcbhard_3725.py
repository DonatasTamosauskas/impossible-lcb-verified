from typing import List


def _tri(t: int) -> int:
    return t * (t + 1) // 2 if t > 0 else 0


def _count(p: int, q: int, m: int) -> int:
    # #{(a, b): 0 <= a < p, 0 <= b < q, a + b < m}
    return _tri(m) - _tri(m - p) - _tri(m - q) + _tri(m - p - q)


def _contrib(nums: List[int], k: int, less) -> int:
    # Sum over subarrays of length <= k of the extreme chosen by `less`
    # (strict comparator: less(a, b) means a beats b).
    n = len(nums)
    left = [-1] * n
    right = [n] * n
    st = []
    for i in range(n):
        v = nums[i]
        # pop elements that are not strictly better than v -> v's left boundary is strictly better
        while st and not less(nums[st[-1]], v):
            right[st.pop()] = i  # i is first to the right with nums[i] beating-or-equal
        left[i] = st[-1] if st else -1
        st.append(i)
    total = 0
    for i in range(n):
        total += nums[i] * _count(i - left[i], right[i] - i, k)
    return total


def minMaxSubarraySum(nums: List[int], k: int) -> int:
    mn = _contrib(nums, k, lambda a, b: a < b)
    mx = _contrib(nums, k, lambda a, b: a > b)
    return mn + mx
