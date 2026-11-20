def makeTheIntegerZero(num1: int, num2: int) -> int:
    for k in range(1, 61):
        t = num1 - k * num2
        if t >= k and bin(t).count("1") <= k:
            return k
    return -1
