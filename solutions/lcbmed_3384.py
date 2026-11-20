from collections import Counter


def minimumOperationsToMakeKPeriodic(word: str, k: int) -> int:
    c = Counter(word[i:i + k] for i in range(0, len(word), k))
    return len(word) // k - max(c.values())
