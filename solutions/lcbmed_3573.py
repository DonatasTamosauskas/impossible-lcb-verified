def validSubstringCount(word1: str, word2: str) -> int:
    need = [0] * 26
    for c in word2:
        need[ord(c) - 97] += 1
    missing = sum(1 for x in need if x > 0)
    cnt = [0] * 26
    ans = 0
    l = 0
    n = len(word1)
    # for each l, find smallest r; sliding window
    r = 0
    for l in range(n):
        while r < n and missing > 0:
            i = ord(word1[r]) - 97
            cnt[i] += 1
            if cnt[i] == need[i] and need[i] > 0:
                missing -= 1
            r += 1
        if missing == 0:
            ans += n - r + 1
        else:
            break
        i = ord(word1[l]) - 97
        if cnt[i] == need[i] and need[i] > 0:
            missing += 1
        cnt[i] -= 1
    return ans
