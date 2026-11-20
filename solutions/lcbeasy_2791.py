from typing import List


def circularGameLosers(n: int, k: int) -> List[int]:
    seen = {0}
    pos = 0
    step = 1
    while True:
        pos = (pos + step * k) % n
        if pos in seen:
            break
        seen.add(pos)
        step += 1
    return [i + 1 for i in range(n) if i not in seen]
