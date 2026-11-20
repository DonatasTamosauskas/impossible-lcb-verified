def _count_segment(codes, k):
    n = len(codes)
    total = 0
    for m in range(1, 27):
        w = m * k
        if w > n:
            break
        cnt = [0] * 26
        good = 0  # number of letters whose count is exactly k
        for i in range(n):
            c = codes[i]
            x = cnt[c]
            if x == k:
                good -= 1
            x += 1
            cnt[c] = x
            if x == k:
                good += 1
            if i >= w:
                d = codes[i - w]
                y = cnt[d]
                if y == k:
                    good -= 1
                y -= 1
                cnt[d] = y
                if y == k:
                    good += 1
            if i >= w - 1 and good == m:
                total += 1
    return total


def countCompleteSubstrings(word: str, k: int) -> int:
    codes = [ord(ch) - 97 for ch in word]
    n = len(codes)
    res = 0
    start = 0
    for i in range(1, n + 1):
        if i == n or abs(codes[i] - codes[i - 1]) > 2:
            res += _count_segment(codes[start:i], k)
            start = i
    return res
