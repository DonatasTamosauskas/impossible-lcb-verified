from typing import List


def buttonWithLongestTime(events: List[List[int]]) -> int:
    best_t, best_i = -1, 0
    prev = 0
    for i, t in events:
        d = t - prev
        prev = t
        if d > best_t or (d == best_t and i < best_i):
            best_t, best_i = d, i
    return best_i
