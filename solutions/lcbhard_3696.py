def countSubstrings(s: str) -> int:
    n = len(s)
    ans = 0
    # dp[d][r]: number of substrings ending at previous position with value mod d == r
    mods = (3, 4, 6, 7, 8, 9)
    dp = {d: [0] * d for d in mods}
    trans = {}
    for d in mods:
        for c in range(10):
            trans[(d, c)] = [(r * 10 + c) % d for r in range(d)]
    psum3 = 0
    for i in range(n):
        c = ord(s[i]) - 48
        for d in mods:
            old = dp[d]
            t = trans[(d, c)]
            new = [0] * d
            for r in range(d):
                v = old[r]
                if v:
                    new[t[r]] += v
            new[c % d] += 1
            dp[d] = new
        if c == 1 or c == 2 or c == 5:
            ans += i + 1
        elif c != 0:
            ans += dp[c][0]
    return ans
