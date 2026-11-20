def _ok(s: str, target: int) -> bool:
    if target < 0:
        return False
    if not s:
        return target == 0
    v = 0
    for i, c in enumerate(s):
        v = v * 10 + int(c)
        if v > target:
            break
        if _ok(s[i + 1:], target - v):
            return True
    return False


def punishmentNumber(n: int) -> int:
    return sum(i * i for i in range(1, n + 1) if _ok(str(i * i), i))
