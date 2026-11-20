from typing import List


def minimizeConcatenatedLength(words: List[str]) -> int:
    INF = float("inf")
    w = words[0]
    dp = {(w[0], w[-1]): len(w)}
    for w in words[1:]:
        f, l = w[0], w[-1]
        nd = {}
        for (a, b), v in dp.items():
            # append w: (a, l)
            k = (a, l)
            c = v + len(w) - (1 if b == f else 0)
            if nd.get(k, INF) > c:
                nd[k] = c
            # prepend w: (f, b)
            k = (f, b)
            c = v + len(w) - (1 if l == a else 0)
            if nd.get(k, INF) > c:
                nd[k] = c
        dp = nd
    return min(dp.values())
