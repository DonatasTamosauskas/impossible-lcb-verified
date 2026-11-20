def maxPartitionsAfterOperations(s: str, k: int) -> int:
    n = len(s)
    # left[i]: greedy state of prefix s[0..i-1] -> (completed partitions, mask, distinct count)
    left = [(0, 0, 0)] * n
    num = mask = count = 0
    for i in range(n - 1):
        b = 1 << (ord(s[i]) - 97)
        if not (mask & b):
            count += 1
            if count <= k:
                mask |= b
            else:
                num += 1
                mask = b
                count = 1
        left[i + 1] = (num, mask, count)
    # right[i]: greedy state of suffix s[i+1..] (processed right to left)
    right = [(0, 0, 0)] * n
    num = mask = count = 0
    for i in range(n - 1, 0, -1):
        b = 1 << (ord(s[i]) - 97)
        if not (mask & b):
            count += 1
            if count <= k:
                mask |= b
            else:
                num += 1
                mask = b
                count = 1
        right[i - 1] = (num, mask, count)
    best = 0
    for i in range(n):
        ln, lm, lc = left[i]
        rn, rm, rc = right[i]
        seg = ln + rn + 2
        tot = bin(lm | rm).count("1")
        if lc == k and rc == k and tot < 26:
            seg += 1
        elif min(tot + 1, 26) <= k:
            seg -= 1
        if seg > best:
            best = seg
    return best
