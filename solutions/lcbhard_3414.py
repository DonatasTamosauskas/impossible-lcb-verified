from math import comb


def waysToReachStair(k: int) -> int:
    # After j up-jumps and d down-steps (no two consecutive downs), position is
    # 1 + (2^j - 1) - d = 2^j - d, with 0 <= d <= j + 1 and C(j+1, d) arrangements.
    total = 0
    for j in range(0, 64):
        d = (1 << j) - k
        if d < 0:
            continue
        if d > j + 1:
            if (1 << j) > k + 64:
                break
            continue
        total += comb(j + 1, d)
    return total
