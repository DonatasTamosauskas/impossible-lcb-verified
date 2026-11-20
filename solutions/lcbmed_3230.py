def removeAlmostEqualCharacters(word: str) -> int:
    cnt = 0
    i = 1
    while i < len(word):
        if abs(ord(word[i]) - ord(word[i - 1])) <= 1:
            cnt += 1
            i += 2
        else:
            i += 1
    return cnt
