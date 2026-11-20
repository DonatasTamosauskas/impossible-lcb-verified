def hasSpecialSubstring(s: str, k: int) -> bool:
    i, n = 0, len(s)
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        if j - i == k:
            return True
        i = j
    return False
