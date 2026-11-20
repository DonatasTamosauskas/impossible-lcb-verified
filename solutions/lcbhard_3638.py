def makeStringGood(s: str) -> int:
    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - 97] += 1
    best = len(s)
    mx = max(cnt)
    for t in range(1, mx + 1):
        # state for previous letter: target 0 -> (excess, cost); target t -> (excess, cost)
        c0 = cnt[0]
        ex_a, cost_a = c0, 0  # target 0
        ex_b, cost_b = (c0 - t if c0 > t else 0), (t - c0 if c0 < t else 0)  # target t
        for i in range(1, 26):
            c = cnt[i]
            # choose target 0: deficit 0
            na_cost = min(cost_a + ex_a, cost_b + ex_b)
            na_ex = c
            # choose target t
            d = t - c if c < t else 0
            nb_cost = min(cost_a + (ex_a if ex_a > d else d), cost_b + (ex_b if ex_b > d else d))
            nb_ex = c - t if c > t else 0
            ex_a, cost_a, ex_b, cost_b = na_ex, na_cost, nb_ex, nb_cost
        r = min(cost_a + ex_a, cost_b + ex_b)
        if r < best:
            best = r
    return best
