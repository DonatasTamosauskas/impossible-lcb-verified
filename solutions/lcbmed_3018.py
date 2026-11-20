def canMakeSubsequence(str1: str, str2: str) -> bool:
    j = 0
    m = len(str2)
    for c in str1:
        if j < m:
            t = str2[j]
            if c == t or chr((ord(c) - 97 + 1) % 26 + 97) == t:
                j += 1
    return j == m
