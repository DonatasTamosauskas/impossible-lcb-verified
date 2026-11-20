def shortestBeautifulSubstring(s: str, k: int) -> str:
    best = ""
    n = len(s)
    for i in range(n):
        c = 0
        for j in range(i, n):
            if s[j] == '1':
                c += 1
            if c == k:
                t = s[i:j + 1]
                if not best or len(t) < len(best) or (len(t) == len(best) and t < best):
                    best = t
                break
            if c > k:
                break
    return best
