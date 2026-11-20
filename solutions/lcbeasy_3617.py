def possibleStringCount(word: str) -> int:
    return 1 + sum(1 for i in range(1, len(word)) if word[i] == word[i - 1])
