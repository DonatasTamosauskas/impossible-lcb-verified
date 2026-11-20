def minimumSteps(s: str) -> int:
    res = 0
    zeros = 0
    for c in reversed(s):
        if c == '0':
            zeros += 1
        else:
            res += zeros
    return res
