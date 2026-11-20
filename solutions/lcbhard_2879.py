def minimumChanges(s: str, k: int) -> int:
    n = len(s)
    INF = float("inf")
    divs = [[] for _ in range(n + 1)]
    for d in range(1, n + 1):
        for L in range(2 * d, n + 1, d):
            divs[L].append(d)
    # cost[i][j]: min changes to make s[i:j] a semi-palindrome
    cost = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 2, n + 1):
            sub = s[i:j]
            best = INF
            for d in divs[j - i]:
                c = 0
                for r in range(d):
                    g = sub[r::d]
                    c += sum(1 for a, b in zip(g, g[::-1]) if a != b)
                c //= 2
                if c < best:
                    best = c
                    if best == 0:
                        break
            cost[i][j] = best
    prev = [INF] * (n + 1)
    prev[0] = 0
    for p in range(1, k + 1):
        cur = [INF] * (n + 1)
        for j in range(2 * p, n + 1):
            b = INF
            for i in range(2 * (p - 1), j - 1):
                pv = prev[i]
                if pv != INF:
                    v = pv + cost[i][j]
                    if v < b:
                        b = v
            cur[j] = b
        prev = cur
    return int(prev[n])
