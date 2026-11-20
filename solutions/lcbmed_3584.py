from bisect import bisect_left
from typing import List


def validSequence(word1: str, word2: str) -> List[int]:
    n, m = len(word1), len(word2)
    # s[j] = largest p such that word2[j:] is a subsequence of word1[p:]
    s = [-1] * (m + 1)
    s[m] = n
    p = n
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and word1[i] == word2[j]:
            s[j] = i
            j -= 1
    # s[j] for j > the matched count stays -1 (infeasible); fill properly
    # (greedy from the end gives s[j] for suffixes that fit)
    pos = [[] for _ in range(26)]
    for i, c in enumerate(word1):
        pos[ord(c) - 97].append(i)
    res = []
    cur = 0
    used = False
    for j in range(m):
        c = ord(word2[j]) - 97
        if cur >= n:
            return []
        if word1[cur] == word2[j]:
            res.append(cur)
            cur += 1
            continue
        if not used and s[j + 1] >= cur + 1:
            used = True
            res.append(cur)
            cur += 1
            continue
        lst = pos[c]
        k = bisect_left(lst, cur)
        if k == len(lst):
            return []
        i = lst[k]
        res.append(i)
        cur = i + 1
    return res
