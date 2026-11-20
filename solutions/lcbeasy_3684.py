def hasMatch(s: str, p: str) -> bool:
    a, b = p.split('*')
    n = len(s)
    for i in range(n - len(a) + 1):
        if s[i:i + len(a)] == a:
            j = s.find(b, i + len(a)) if b else i + len(a)
            if j != -1:
                return True
    return False
