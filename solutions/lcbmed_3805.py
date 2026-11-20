def maxActiveSectionsAfterTrade(s: str) -> int:
    blocks = []
    i, n = 0, len(s)
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        blocks.append((s[i], j - i))
        i = j
    ones = s.count('1')
    gain = 0
    for k in range(1, len(blocks) - 1):
        if blocks[k][0] == '1':
            gain = max(gain, blocks[k - 1][1] + blocks[k + 1][1])
    return ones + gain
