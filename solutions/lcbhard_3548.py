def countGoodIntegers(n: int, k: int) -> int:
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i

    half = (n + 1) // 2
    seen = set()
    lo = 10 ** (half - 1)
    hi = 10 ** half
    for h in range(lo, hi):
        s = str(h)
        if n % 2 == 0:
            p = s + s[::-1]
        else:
            p = s + s[-2::-1]
        if int(p) % k == 0:
            seen.add("".join(sorted(p)))

    total = 0
    for key in seen:
        cnt = [0] * 10
        for ch in key:
            cnt[ord(ch) - 48] += 1
        denom = 1
        for c in cnt:
            denom *= fact[c]
        perms = fact[n] // denom
        if cnt[0] > 0:
            # subtract arrangements with a leading zero
            denom0 = 1
            for d in range(10):
                c = cnt[d] - (1 if d == 0 else 0)
                denom0 *= fact[c]
            perms -= fact[n - 1] // denom0
        total += perms
    return total
