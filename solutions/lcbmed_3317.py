from typing import List


def maxPalindromesAfterOperations(words: List[str]) -> int:
    total = sum(len(w) for w in words)
    cnt = {}
    for w in words:
        for ch in w:
            cnt[ch] = cnt.get(ch, 0) + 1
    pairs = sum(v // 2 for v in cnt.values())
    res = 0
    for L in sorted(len(w) for w in words):
        need = L // 2
        if pairs >= need:
            pairs -= need
            res += 1
        else:
            break
    return res
