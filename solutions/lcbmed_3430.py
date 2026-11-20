from typing import List


def countDays(days: int, meetings: List[List[int]]) -> int:
    covered = 0
    end = 0
    for s, e in sorted(meetings):
        if s > end:
            covered += e - s + 1
            end = e
        elif e > end:
            covered += e - end
            end = e
    return days - covered
