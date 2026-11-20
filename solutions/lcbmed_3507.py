from math import isqrt


def nonSpecialCount(l: int, r: int) -> int:
    lim = isqrt(r)
    sieve = bytearray([1]) * (lim + 1)
    sieve[0:2] = b"\x00\x00"[: min(2, lim + 1)]
    for i in range(2, isqrt(lim) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, lim + 1, i)))
    special = 0
    for p in range(2, lim + 1):
        if sieve[p] and l <= p * p <= r:
            special += 1
    return (r - l + 1) - special
