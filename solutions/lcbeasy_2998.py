def countSymmetricIntegers(low: int, high: int) -> int:
    c = 0
    for x in range(low, high + 1):
        t = str(x)
        n = len(t)
        if n % 2:
            continue
        h = n // 2
        if sum(map(int, t[:h])) == sum(map(int, t[h:])):
            c += 1
    return c
