def numberOfPowerfulInt(start: int, finish: int, limit: int, s: str) -> int:
    m = len(s)
    S = int(s)
    base = 10 ** m

    def count_upto_digits(B: int) -> int:
        # count integers in [0, B] whose digits are all <= limit
        if B < 0:
            return 0
        ds = str(B)
        L = len(ds)
        res = 0
        for i, ch in enumerate(ds):
            d = ord(ch) - 48
            res += min(d, limit + 1) * (limit + 1) ** (L - i - 1)
            if d > limit:
                return res
        return res + 1

    def f(x: int) -> int:
        if x < S:
            return 0
        P, r = divmod(x, base)
        bound = P if r >= S else P - 1
        return count_upto_digits(bound)

    return f(finish) - f(start - 1)
