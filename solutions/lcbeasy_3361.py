def findLatestTime(s: str) -> str:
    h0, h1, _, m0, m1 = s
    if h0 == '?':
        h0 = '1' if h1 in '?01' else '0'
    if h1 == '?':
        h1 = '1' if h0 == '1' else '9'
    if m0 == '?':
        m0 = '5'
    if m1 == '?':
        m1 = '9'
    return h0 + h1 + ':' + m0 + m1
