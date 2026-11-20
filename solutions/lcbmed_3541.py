from typing import List


def reportSpam(message: List[str], bannedWords: List[str]) -> bool:
    b = set(bannedWords)
    return sum(1 for w in message if w in b) >= 2
