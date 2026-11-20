def smallestNumber(n: int, t: int) -> int:
    x = n
    while True:
        p = 1
        for c in str(x):
            p *= int(c)
        if p % t == 0:
            return x
        x += 1
