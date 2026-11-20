def minCostGoodCaption(caption: str) -> str:
    n = len(caption)
    if n < 3:
        return ""
    INF = float("inf")
    s = [ord(ch) - 97 for ch in caption]
    # dp[i][c]: min cost for suffix i.. given t[i] = c and the run starting at i
    # (within the suffix) has length >= 3. Defined for i <= n-3.
    # best[i]: (min over c of dp[i][c], smallest argmin); best[n] = (0, -1).
    dp = [None] * (n + 1)
    best_val = [INF] * (n + 3)
    best_arg = [-1] * (n + 3)
    best_val[n] = 0
    # choice[i][c]: -2 means step (t[i+1] = c continues), else jump 3 with next letter (-1 = end)
    choice = [None] * n
    letters = range(26)
    for i in range(n - 3, -1, -1):
        a, b, d = s[i], s[i + 1], s[i + 2]
        mv = best_val[i + 3]
        mk = best_arg[i + 3]
        cur = [0] * 26
        ch = [0] * 26
        nxt = dp[i + 1] if i + 1 <= n - 3 else None
        bv = INF
        ba = -1
        for c in letters:
            ca = a - c if a >= c else c - a
            r2 = mv + ca + (b - c if b >= c else c - b) + (d - c if d >= c else c - d)
            if nxt is not None:
                r1 = nxt[c] + ca
                if r1 < r2 or (r1 == r2 and not (mk < c)):
                    cur[c] = r1
                    ch[c] = -2
                else:
                    cur[c] = r2
                    ch[c] = mk
            else:
                cur[c] = r2
                ch[c] = mk
            if cur[c] < bv:
                bv = cur[c]
                ba = c
        dp[i] = cur
        choice[i] = ch
        best_val[i] = bv
        best_arg[i] = ba
    if best_val[0] == INF:
        return ""
    out = []
    i = 0
    c = best_arg[0]
    while i < n:
        k = choice[i][c]
        if k == -2:
            out.append(c)
            i += 1
        else:
            out.append(c)
            out.append(c)
            out.append(c)
            i += 3
            c = k
    return "".join(chr(97 + v) for v in out)
