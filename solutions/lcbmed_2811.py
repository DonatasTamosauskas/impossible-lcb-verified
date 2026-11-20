def minimumSum(n: int, k: int) -> int:
    used = set()
    v = 1
    total = 0
    while len(used) < n:
        if (k - v) not in used:
            used.add(v)
            total += v
        v += 1
    return total
