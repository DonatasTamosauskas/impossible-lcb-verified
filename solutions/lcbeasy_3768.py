def hasSameDigits(s: str) -> bool:
    d = [int(x) for x in s]
    while len(d) > 2:
        d = [(d[i] + d[i + 1]) % 10 for i in range(len(d) - 1)]
    return d[0] == d[1]
