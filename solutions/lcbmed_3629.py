def lengthAfterTransformations(s: str, t: int) -> int:
    MOD = 10**9 + 7
    f = [1] * 26
    for _ in range(t):
        g = f[1:] + [(f[0] + f[1]) % MOD]
        f = g
    total = 0
    for ch in s:
        total += f[ord(ch) - 97]
    return total % MOD
