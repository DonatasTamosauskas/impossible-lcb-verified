import heapq


def minimizeStringValue(s: str) -> str:
    cnt = [0] * 26
    for c in s:
        if c != '?':
            cnt[ord(c) - 97] += 1
    heap = [(cnt[i], i) for i in range(26)]
    heapq.heapify(heap)
    chosen = []
    for c in s:
        if c == '?':
            n, i = heapq.heappop(heap)
            chosen.append(i)
            heapq.heappush(heap, (n + 1, i))
    chosen.sort()
    it = iter(chosen)
    return ''.join(chr(97 + next(it)) if c == '?' else c for c in s)
