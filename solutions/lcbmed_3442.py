from typing import List


def maxTotalReward(rewardValues: List[int]) -> int:
    mask = 1
    for v in sorted(set(rewardValues)):
        if v <= 0:
            continue
        low = mask & ((1 << v) - 1)
        mask |= low << v
    return mask.bit_length() - 1
