from typing import List


def minProcessingTime(processorTime: List[int], tasks: List[int]) -> int:
    p = sorted(processorTime)
    t = sorted(tasks, reverse=True)
    return max(p[i] + t[4 * i] for i in range(len(p)))
