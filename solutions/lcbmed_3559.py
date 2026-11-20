from typing import List


def _z(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def minValidStrings(words: List[str], target: str) -> int:
    n = len(target)
    best = [0] * n
    for w in set(words):
        s = w + '#' + target
        z = _z(s)
        off = len(w) + 1
        for i in range(n):
            v = z[off + i]
            if v > best[i]:
                best[i] = v
    # greedy jump game
    jumps = 0
    cur_end = 0
    far = 0
    for i in range(n):
        if i > far:
            return -1
        far = max(far, i + best[i])
        if i == cur_end:
            if far <= i:
                return -1
            jumps += 1
            cur_end = far
            if cur_end >= n:
                return jumps
    return jumps if cur_end >= n else -1
