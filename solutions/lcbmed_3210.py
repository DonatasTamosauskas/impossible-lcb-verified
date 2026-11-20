def beautifulSubstrings(s: str, k: int) -> int:
    n = len(s)
    v = set("aeiou")
    cnt = 0
    for i in range(n):
        vo = 0
        co = 0
        for j in range(i, n):
            if s[j] in v:
                vo += 1
            else:
                co += 1
            if vo == co and (vo * co) % k == 0:
                cnt += 1
    return cnt
