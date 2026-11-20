def isSubstringPresent(s: str) -> bool:
    r = s[::-1]
    return any(s[i:i + 2] in r for i in range(len(s) - 1))
