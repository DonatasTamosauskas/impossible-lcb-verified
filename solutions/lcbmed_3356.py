from typing import List


def shortestSubstrings(arr: List[str]) -> List[str]:
    n = len(arr)
    subs = []
    for s in arr:
        subs.append({s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)})
    res = []
    for i in range(n):
        others = set()
        for j in range(n):
            if j != i:
                others |= subs[j]
        cand = [x for x in subs[i] if x not in others]
        res.append(min(cand, key=lambda x: (len(x), x)) if cand else "")
    return res
