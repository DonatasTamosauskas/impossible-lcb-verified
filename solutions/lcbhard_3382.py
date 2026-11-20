from typing import List


def numberOfSubarrays(nums: List[int]) -> int:
    stack = []  # [value, count], values strictly decreasing
    total = 0
    for x in nums:
        while stack and stack[-1][0] < x:
            stack.pop()
        if stack and stack[-1][0] == x:
            stack[-1][1] += 1
            total += stack[-1][1]
        else:
            stack.append([x, 1])
            total += 1
    return total
