from typing import List


def numberOfAlternatingGroups(colors: List[int], queries: List[List[int]]) -> List[int]:
    n = len(colors)
    col = list(colors)

    # Fenwick over edge positions (edge i joins tile i and tile i+1 mod n); 1 if "bad" (same colours).
    pos_tree = [0] * (n + 1)
    LOG = 1
    while (1 << LOG) <= n:
        LOG += 1

    def pos_add(i, v):
        i += 1
        while i <= n:
            pos_tree[i] += v
            i += i & -i

    def pos_prefix(i):  # count of bad edges in [0, i)
        s = 0
        while i > 0:
            s += pos_tree[i]
            i -= i & -i
        return s

    def pos_kth(k):  # 0-based index of the k-th (1-based) bad edge
        idx = 0
        for b in range(LOG, -1, -1):
            nxt = idx + (1 << b)
            if nxt <= n and pos_tree[nxt] < k:
                idx = nxt
                k -= pos_tree[nxt]
        return idx

    # Fenwick over run lengths 1..n: count and sum.
    cnt_tree = [0] * (n + 1)
    sum_tree = [0] * (n + 1)

    def len_add(L, c):
        i = L
        while i <= n:
            cnt_tree[i] += c
            sum_tree[i] += c * L
            i += i & -i

    def len_prefix(i):
        c = s = 0
        while i > 0:
            c += cnt_tree[i]
            s += sum_tree[i]
            i -= i & -i
        return c, s

    bad = [False] * n
    total = 0

    def dist(p, q):
        d = (q - p) % n
        return d if d else n

    def pred(e):
        c = pos_prefix(e)
        k = c if c > 0 else total
        return pos_kth(k)

    def succ(e):
        c = pos_prefix(e + 1)
        k = c + 1 if c < total else 1
        return pos_kth(k)

    def add_edge(e):
        nonlocal total
        if total == 0:
            len_add(n, 1)
        else:
            p = pred(e)
            q = succ(e)
            len_add(dist(p, q), -1)
            len_add(dist(p, e), 1)
            len_add(dist(e, q), 1)
        bad[e] = True
        pos_add(e, 1)
        total += 1

    def remove_edge(e):
        nonlocal total
        bad[e] = False
        pos_add(e, -1)
        total -= 1
        if total == 0:
            len_add(n, -1)
        else:
            p = pred(e)
            q = succ(e)
            len_add(dist(p, e), -1)
            len_add(dist(e, q), -1)
            len_add(dist(p, q), 1)

    for i in range(n):
        if col[i] == col[(i + 1) % n]:
            add_edge(i)

    res = []
    for q in queries:
        if q[0] == 1:
            k = q[1]
            if total == 0:
                res.append(n)
            else:
                ac, as_ = len_prefix(n)
                bc, bs = len_prefix(k - 1)
                c = ac - bc
                s = as_ - bs
                res.append(s - (k - 1) * c)
        else:
            idx, c = q[1], q[2]
            if col[idx] == c:
                continue
            col[idx] = c
            for e in ((idx - 1) % n, idx):
                nb = col[e] == col[(e + 1) % n]
                if nb != bad[e]:
                    if nb:
                        add_edge(e)
                    else:
                        remove_edge(e)
    return res
