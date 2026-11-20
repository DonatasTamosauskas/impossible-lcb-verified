from typing import List


def stringIndices(wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
    lens = [len(w) for w in wordsContainer]
    best_root = 0
    for i in range(1, len(wordsContainer)):
        if lens[i] < lens[best_root]:
            best_root = i
    children = [{}]
    best = [best_root]
    for i, w in enumerate(wordsContainer):
        li = lens[i]
        node = 0
        for ch in reversed(w):
            nxt = children[node].get(ch)
            if nxt is None:
                nxt = len(children)
                children[node][ch] = nxt
                children.append({})
                best.append(i)
            else:
                b = best[nxt]
                if li < lens[b]:
                    best[nxt] = i
            node = nxt
    ans = []
    for q in wordsQuery:
        node = 0
        for ch in reversed(q):
            nxt = children[node].get(ch)
            if nxt is None:
                break
            node = nxt
        ans.append(best[node])
    return ans
