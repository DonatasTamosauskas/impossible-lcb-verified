def doesAliceWin(s: str) -> bool:
    return any(c in "aeiou" for c in s)
