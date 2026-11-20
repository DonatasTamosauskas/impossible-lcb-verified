from typing import List


def longestSpecialPath(edges: List[List[int]], nums: List[int]) -> List[int]:
    n = len(nums)
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    last = [-1] * (max(nums) + 1)   # depth of last occurrence of each value on the current path
    dist = [0] * (n + 1)            # dist[d] = distance from root to the path node at depth d
    best_len = 0
    best_nodes = 1

    # entries: (node, parent, depth, top, weight_from_parent_or_saved_last, entering)
    stack = [(0, -1, 0, 0, 0, True)]
    while stack:
        node, par, d, top, x, entering = stack.pop()
        v = nums[node]
        if not entering:
            last[v] = x
            continue
        if d > 0:
            dist[d] = dist[d - 1] + x
        prev = last[v]
        if prev + 1 > top:
            top = prev + 1
        length = dist[d] - dist[top]
        cnt = d - top + 1
        if length > best_len or (length == best_len and cnt < best_nodes):
            best_len = length
            best_nodes = cnt
        last[v] = d
        stack.append((node, par, d, top, prev, False))
        for nxt, w in adj[node]:
            if nxt != par:
                stack.append((nxt, node, d + 1, top, w, True))
    return [best_len, best_nodes]
