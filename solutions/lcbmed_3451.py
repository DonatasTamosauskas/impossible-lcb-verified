def compressedString(word: str) -> str:
    out = []
    i = 0
    n = len(word)
    while i < n:
        j = i
        while j < n and j - i < 9 and word[j] == word[i]:
            j += 1
        out.append(str(j - i) + word[i])
        i = j
    return "".join(out)
