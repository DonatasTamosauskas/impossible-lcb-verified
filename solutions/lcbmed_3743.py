from typing import List


def maxFreeTime(eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
    n = len(startTime)
    gaps = [startTime[0]]
    for i in range(1, n):
        gaps.append(startTime[i] - endTime[i - 1])
    gaps.append(eventTime - endTime[-1])
    w = k + 1
    s = sum(gaps[:w])
    best = s
    for i in range(w, len(gaps)):
        s += gaps[i] - gaps[i - w]
        if s > best:
            best = s
    return best
