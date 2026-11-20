def generateString(str1: str, str2: str) -> str:
    n = len(str1)
    m = len(str2)
    L = n + m - 1
    word = ['a'] * L
    fixed = [False] * L
    end = 0  # positions < end already fixed by a previous T
    prev = -1
    for i in range(n):
        if str1[i] == 'T':
            if prev >= 0 and i < prev + m:
                d = i - prev
                if str2[d:] != str2[:m - d]:
                    return ""
            start = max(i, end)
            for j in range(start, i + m):
                word[j] = str2[j - i]
                fixed[j] = True
            end = i + m
            prev = i
    # last_free[x] = largest free index <= x, or -1
    last_free = [-1] * L
    lf = -1
    for i in range(L):
        if not fixed[i]:
            lf = i
        last_free[i] = lf
    for i in range(n):
        if str1[i] == 'F':
            if ''.join(word[i:i + m]) == str2:
                p = last_free[i + m - 1]
                if p < i:
                    return ""
                word[p] = 'b'
    return ''.join(word)
