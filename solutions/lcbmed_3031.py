from typing import List


def constructProductMatrix(grid: List[List[int]]) -> List[List[int]]:
    M = 12345
    n, m = len(grid), len(grid[0])
    flat = [v % M for row in grid for v in row]
    L = len(flat)
    suf = [1] * (L + 1)
    for i in range(L - 1, -1, -1):
        suf[i] = suf[i + 1] * flat[i] % M
    pre = 1
    res = []
    for i in range(L):
        res.append(pre * suf[i + 1] % M)
        pre = pre * flat[i] % M
    return [res[i * m:(i + 1) * m] for i in range(n)]
