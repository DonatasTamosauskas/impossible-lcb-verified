def countKConstraintSubstrings(s: str, k: int) -> int:
    cnt = [0, 0]
    l = 0
    res = 0
    for r, ch in enumerate(s):
        cnt[int(ch)] += 1
        while cnt[0] > k and cnt[1] > k:
            cnt[int(s[l])] -= 1
            l += 1
        res += r - l + 1
    return res
