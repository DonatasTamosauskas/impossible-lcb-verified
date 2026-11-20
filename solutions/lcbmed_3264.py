from typing import List


def maximumPoints(enemyEnergies: List[int], currentEnergy: int) -> int:
    e0 = min(enemyEnergies)
    if currentEnergy < e0:
        return 0
    return (currentEnergy + sum(enemyEnergies) - e0) // e0
