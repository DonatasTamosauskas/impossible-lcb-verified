from collections import Counter


def maximumLengthSubstring(s: str) -> int:
    cnt = Counter()
    l = 0
    best = 0
    for r, ch in enumerate(s):
        cnt[ch] += 1
        while cnt[ch] > 2:
            cnt[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best
