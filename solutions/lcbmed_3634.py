def calculateScore(s: str) -> int:
    st = [[] for _ in range(26)]
    total = 0
    for i, c in enumerate(s):
        v = ord(c) - 97
        m = 25 - v
        if st[m]:
            total += i - st[m].pop()
        else:
            st[v].append(i)
    return total
