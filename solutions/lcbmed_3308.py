def lastNonEmptyString(s: str) -> str:
    if not s:
        return ""
    cnt = {}
    last = {}
    for i, ch in enumerate(s):
        cnt[ch] = cnt.get(ch, 0) + 1
        last[ch] = i
    m = max(cnt.values())
    idx = sorted(last[ch] for ch in cnt if cnt[ch] == m)
    return "".join(s[i] for i in idx)
