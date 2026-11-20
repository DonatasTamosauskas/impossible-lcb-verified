def countSubstrings(s: str, c: str) -> int:
    n = s.count(c)
    return n * (n + 1) // 2
