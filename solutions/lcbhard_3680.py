from typing import List


def countComponents(nums: List[int], threshold: int) -> int:
    parent = list(range(threshold + 1))

    def find(x: int) -> int:
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    big = 0
    small = []
    for x in nums:
        if x > threshold:
            big += 1
        else:
            small.append(x)

    for x in small:
        rx = find(x)
        for m in range(2 * x, threshold + 1, x):
            rm = find(m)
            if rm != rx:
                parent[rm] = rx

    roots = set()
    for x in small:
        roots.add(find(x))
    return big + len(roots)
