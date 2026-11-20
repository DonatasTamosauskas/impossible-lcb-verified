from typing import List


def longestCommonPrefix(words: List[str], k: int) -> List[int]:
    n = len(words)
    if n - 1 < k:
        return [0] * n
    children = [{}]
    cnt = [0]
    depth = [0]
    cnt[0] = n
    for w in words:
        node = 0
        for ch in w:
            nxt = children[node].get(ch)
            if nxt is None:
                nxt = len(cnt)
                children[node][ch] = nxt
                children.append({})
                cnt.append(0)
                depth.append(depth[node] + 1)
            node = nxt
            cnt[node] += 1
    maxd = max(depth)
    cntK = [0] * (maxd + 1)
    lastNode = [-1] * (maxd + 1)
    for v in range(len(cnt)):
        if cnt[v] >= k:
            cntK[depth[v]] += 1
            lastNode[depth[v]] = v
    D1 = -1
    D2 = -1
    for d in range(maxd + 1):
        if cntK[d] >= 1:
            D1 = d
        if cntK[d] >= 2:
            D2 = d
    deepNode = lastNode[D1] if (D1 >= 0 and cntK[D1] == 1) else -1
    res = []
    for w in words:
        node = 0
        A = 0
        through = (deepNode == 0)
        for ch in w:
            node = children[node][ch]
            if cnt[node] >= k + 1:
                A = depth[node]
            if node == deepNode:
                through = True
        if deepNode == -1:
            B = D1
        else:
            B = D2 if through else D1
        res.append(max(A, B, 0))
    return res
