from typing import List


def minimumCost(target: str, words: List[str], costs: List[int]) -> int:
    n = len(target)

    # Suffix automaton of target; pref[j] is the state of the prefix target[:j].
    nxt = [{}]
    link = [-1]
    length = [0]
    pref = [0] * (n + 1)
    last = 0
    for j, ch in enumerate(target, 1):
        cur = len(nxt)
        nxt.append({})
        length.append(length[last] + 1)
        link.append(0)
        p = last
        while p != -1 and ch not in nxt[p]:
            nxt[p][ch] = cur
            p = link[p]
        if p != -1:
            q = nxt[p][ch]
            if length[p] + 1 == length[q]:
                link[cur] = q
            else:
                clone = len(nxt)
                nxt.append(dict(nxt[q]))
                length.append(length[p] + 1)
                link.append(link[q])
                while p != -1 and nxt[p].get(ch) == q:
                    nxt[p][ch] = clone
                    p = link[p]
                link[q] = clone
                link[cur] = clone
        last = cur
        pref[j] = cur
    m = len(nxt)

    # Cheapest cost per distinct word.
    best_cost = {}
    for w, c in zip(words, costs):
        old = best_cost.get(w)
        if old is None or c < old:
            best_cost[w] = c

    # Attach each word that occurs in target to its SAM state. Equal substrings share a state,
    # and every string of a state on the suffix-link path of pref[j] ends at position j.
    wlist = [None] * m
    for w, c in best_cost.items():
        u = 0
        for ch in w:
            u = nxt[u].get(ch)
            if u is None:
                break
        if u is None:
            continue
        if wlist[u] is None:
            wlist[u] = [(len(w), c)]
        else:
            wlist[u].append((len(w), c))

    # out[s]: nearest proper suffix-link ancestor of s that holds a word (0 = none).
    buckets = [[] for _ in range(n + 1)]
    for s in range(1, m):
        buckets[length[s]].append(s)
    out = [0] * m
    for L in range(1, n + 1):
        for s in buckets[L]:
            l = link[s]
            out[s] = l if wlist[l] is not None else out[l]

    # chains[s] (for word-holding s): all (len, cost) of words that are suffixes of s's strings.
    chains = [None] * m
    chains[0] = []

    def chain(s):
        stack = []
        w = s
        while chains[w] is None:
            stack.append(w)
            w = out[w]
        for node in reversed(stack):
            chains[node] = wlist[node] + chains[out[node]]
        return chains[s]

    INF = 1 << 60
    dp = [INF] * (n + 1)
    dp[0] = 0
    for j in range(1, n + 1):
        s = pref[j]
        if wlist[s] is None:
            s = out[s]
        cl = chains[s]
        if cl is None:
            cl = chain(s)
        if cl:
            b = min([dp[j - d] + c for d, c in cl])
            if b < INF:
                dp[j] = b
    return dp[n] if dp[n] < INF else -1
