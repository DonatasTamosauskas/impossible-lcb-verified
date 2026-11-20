from typing import List


def findWinningPlayer(skills: List[int], k: int) -> int:
    n = len(skills)
    cur = 0
    wins = 0
    for i in range(1, n):
        if skills[i] > skills[cur]:
            cur = i
            wins = 1
        else:
            wins += 1
        if wins >= k:
            return cur
    return cur
