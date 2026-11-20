from typing import List


def maximumNumberOfStringPairs(words: List[str]) -> int:
    seen = set()
    count = 0
    for w in words:
        if w[::-1] in seen:
            count += 1
            seen.discard(w[::-1])
        else:
            seen.add(w)
    return count
