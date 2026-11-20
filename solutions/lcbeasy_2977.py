from typing import List


def isAcronym(words: List[str], s: str) -> bool:
    return "".join(w[0] for w in words) == s
