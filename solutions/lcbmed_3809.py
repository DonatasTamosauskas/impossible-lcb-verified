from typing import List


def numberOfComponents(properties: List[List[int]], k: int) -> int:
    n = len(properties)
    sets = [set(p) for p in properties]
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    comps = n
    for i in range(n):
        for j in range(i + 1, n):
            if len(sets[i] & sets[j]) >= k:
                a, b = find(i), find(j)
                if a != b:
                    parent[a] = b
                    comps -= 1
    return comps
