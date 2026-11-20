def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
    d = sum(int(c) for c in str(x))
    return d if x % d == 0 else -1
