from typing import List


def findAnswer(parent: List[int], s: str) -> List[bool]:
    n = len(parent)
    children = [[] for _ in range(n)]
    for i in range(1, n):
        children[parent[i]].append(i)

    # Iterative post-order traversal (children in increasing order).
    order = []
    end_pos = [0] * n
    size = [1] * n
    stack = [(0, 0)]
    while stack:
        node, ci = stack.pop()
        ch = children[node]
        if ci < len(ch):
            stack.append((node, ci + 1))
            stack.append((ch[ci], 0))
        else:
            end_pos[node] = len(order)
            order.append(s[node])
            p = parent[node]
            if p >= 0:
                size[p] += size[node]

    t_chars = ['#'] * (2 * n + 1)
    for i, c in enumerate(order):
        t_chars[2 * i + 1] = c
    # Sentinels
    t = '^' + ''.join(t_chars) + '$'
    m = len(t)
    p = [0] * m
    center = right = 0
    for i in range(1, m - 1):
        if i < right:
            mirror = 2 * center - i
            v = p[mirror]
            r = right - i
            p[i] = v if v < r else r
        pi = p[i]
        while t[i + pi + 1] == t[i - pi - 1]:
            pi += 1
        p[i] = pi
        if i + pi > right:
            center = i
            right = i + pi

    ans = [False] * n
    for x in range(n):
        r = end_pos[x]
        l = r - size[x] + 1
        # In t (with leading '^'), char at original index i is at 2*i + 2.
        c = l + r + 2
        ans[x] = p[c] >= r - l + 1
    return ans
