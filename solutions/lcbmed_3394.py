def minEnd(n: int, x: int) -> int:
    d = n - 1
    res = x
    bit = 1
    while d:
        if not (x & bit):
            if d & 1:
                res |= bit
            d >>= 1
        bit <<= 1
    return res
