def countKeyChanges(s: str) -> int:
    t = s.lower()
    return sum(1 for i in range(1, len(t)) if t[i] != t[i - 1])
