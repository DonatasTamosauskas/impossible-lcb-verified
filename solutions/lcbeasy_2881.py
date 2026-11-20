from typing import List


def splitWordsBySeparator(words: List[str], separator: str) -> List[str]:
    return [p for w in words for p in w.split(separator) if p]
