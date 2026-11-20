def generateKey(num1: int, num2: int, num3: int) -> int:
    a, b, c = (f"{n:04d}" for n in (num1, num2, num3))
    return int("".join(min(x, y, z) for x, y, z in zip(a, b, c)))
