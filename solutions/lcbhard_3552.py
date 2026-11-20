def largestPalindrome(n: int, k: int) -> str:
    # Position i (0 <= i < half) of the first half mirrors position n-1-i.
    half = (n + 1) // 2
    pw = [0] * n
    p = 1 % k
    for e in range(n):
        pw[e] = p
        p = (p * 10) % k
    # Weight of digit at left position i (counting from most significant).
    w = [0] * half
    for i in range(half):
        a = n - 1 - i  # exponent of the left position
        b = i  # exponent of the mirrored right position
        if a == b:
            w[i] = pw[a]
        else:
            w[i] = (pw[a] + pw[b]) % k
    full = (1 << k) - 1

    def rot(s: int, sh: int) -> int:
        sh %= k
        if sh == 0:
            return s
        return ((s << sh) | (s >> (k - sh))) & full

    # reach[i] = bitmask of remainders achievable by positions i..half-1.
    reach = [0] * (half + 1)
    reach[half] = 1  # remainder 0
    for i in range(half - 1, -1, -1):
        s = reach[i + 1]
        acc = 0
        wi = w[i]
        lo = 1 if i == 0 else 0
        for d in range(lo, 10):
            acc |= rot(s, d * wi)
        reach[i] = acc
    if not (reach[0] & 1):
        return ""
    digits = []
    need = 0
    for i in range(half):
        lo = 1 if i == 0 else 0
        nxt = reach[i + 1]
        wi = w[i]
        for d in range(9, lo - 1, -1):
            r = (need - d * wi) % k
            if (nxt >> r) & 1:
                digits.append(d)
                need = r
                break
    first = "".join(map(str, digits))
    if n % 2 == 1:
        return first + first[-2::-1]
    return first + first[::-1]
