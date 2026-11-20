import heapq


def minOperations(n: int, m: int) -> int:
    L = len(str(n))
    if len(str(m)) != L:
        return -1
    lim = 10 ** L
    sieve = bytearray([1]) * lim
    sieve[0] = sieve[1] = 0
    for i in range(2, int(lim ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, lim, i)))
    if sieve[n] or sieve[m]:
        return -1
    lo = 10 ** (L - 1) if L > 1 else 0
    dist = {n: n}
    pq = [(n, n)]
    while pq:
        d, u = heapq.heappop(pq)
        if dist.get(u, 1 << 60) < d:
            continue
        if u == m:
            return d
        p = 1
        for _ in range(L):
            dg = (u // p) % 10
            for nd in (dg - 1, dg + 1):
                if 0 <= nd <= 9:
                    v = u + (nd - dg) * p
                    if v < lo or sieve[v]:
                        continue
                    nd2 = d + v
                    if nd2 < dist.get(v, 1 << 60):
                        dist[v] = nd2
                        heapq.heappush(pq, (nd2, v))
            p *= 10
    return -1
