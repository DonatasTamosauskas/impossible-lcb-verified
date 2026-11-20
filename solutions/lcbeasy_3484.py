def getSmallestString(s: str) -> str:
    for i in range(len(s) - 1):
        if s[i] > s[i + 1] and int(s[i]) % 2 == int(s[i + 1]) % 2:
            return s[:i] + s[i + 1] + s[i] + s[i + 2:]
    return s
