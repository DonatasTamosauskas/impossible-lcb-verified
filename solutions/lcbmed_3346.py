def getSmallestString(s: str, k: int) -> str:
    out = []
    for ch in s:
        o = ord(ch) - 97
        d = min(o, 26 - o)
        if d <= k:
            out.append('a')
            k -= d
        else:
            out.append(chr(97 + o - k))
            k = 0
    return ''.join(out)
