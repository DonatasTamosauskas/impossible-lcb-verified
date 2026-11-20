from typing import List


def colorTheArray(n: int, queries: List[List[int]]) -> List[int]:
    a = [0] * n
    cnt = 0
    out = []
    for i, c in queries:
        old = a[i]
        if old != 0:
            if i > 0 and a[i - 1] == old:
                cnt -= 1
            if i + 1 < n and a[i + 1] == old:
                cnt -= 1
        a[i] = c
        if i > 0 and a[i - 1] == c:
            cnt += 1
        if i + 1 < n and a[i + 1] == c:
            cnt += 1
        out.append(cnt)
    return out
