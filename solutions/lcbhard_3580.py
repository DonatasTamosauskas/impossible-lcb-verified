def _z_function(s):
    n = len(s)
    z = [0] * n
    if n == 0:
        return z
    z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            zi = z[i - l]
            if zi > r - i:
                zi = r - i
        else:
            zi = 0
        while i + zi < n and s[zi] == s[i + zi]:
            zi += 1
        z[i] = zi
        if i + zi > r:
            l = i
            r = i + zi
    return z


def minStartingIndex(s: str, pattern: str) -> int:
    n = len(s)
    m = len(pattern)
    z1 = _z_function(pattern + "#" + s)
    z2 = _z_function(pattern[::-1] + "#" + s[::-1])
    off = m + 1
    for i in range(n - m + 1):
        pref = z1[off + i]
        # suffix match ending at position i + m - 1 in s
        end = i + m - 1
        rev_pos = n - 1 - end
        suf = z2[off + rev_pos]
        if pref + suf >= m - 1:
            return i
    return -1
