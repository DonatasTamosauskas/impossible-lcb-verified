from typing import List


def longestValidSubstring(word: str, forbidden: List[str]) -> int:
    fset = set(forbidden)
    maxlen = max(len(f) for f in forbidden)
    left = 0
    best = 0
    n = len(word)
    for right in range(n):
        lo = max(left, right - maxlen + 1)
        for st in range(right, lo - 1, -1):
            if word[st:right + 1] in fset:
                left = st + 1
                break
        if right - left + 1 > best:
            best = right - left + 1
    return best
