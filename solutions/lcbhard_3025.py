from typing import List


def minOperations(nums: List[int], target: int) -> int:
    if sum(nums) < target:
        return -1
    cnt = [0] * 64
    for x in nums:
        cnt[x.bit_length() - 1] += 1
    ops = 0
    for i in range(62):
        if (target >> i) & 1:
            if cnt[i] > 0:
                cnt[i] -= 1
            else:
                j = i
                while j < 63 and cnt[j] == 0:
                    j += 1
                if cnt[j] == 0:
                    return -1
                ops += j - i
                cnt[j] -= 1
                # splitting 2^j down to 2^i leaves one piece at each level i..j-1
                # (two at level i, one of which is used now)
                for m in range(i, j):
                    cnt[m] += 1
        cnt[i + 1] += cnt[i] // 2
    return ops
