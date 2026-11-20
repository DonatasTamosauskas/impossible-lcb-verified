MOD = 10**9 + 7


def countWinningSequences(s: str) -> int:
    idx = {'F': 0, 'W': 1, 'E': 2}
    n = len(s)
    size = 2 * n + 1
    off = n

    def delta(b, a):
        if (b - a) % 3 == 1:
            return 1
        if (a - b) % 3 == 1:
            return -1
        return 0

    a0 = idx[s[0]]
    dp = [[0] * size for _ in range(3)]
    for b in range(3):
        dp[b][off + delta(b, a0)] = 1

    for i in range(1, n):
        a = idx[s[i]]
        total = [(x + y + z) % MOD for x, y, z in zip(dp[0], dp[1], dp[2])]
        new = []
        for b in range(3):
            src = [(t - d) % MOD for t, d in zip(total, dp[b])]
            d = delta(b, a)
            if d == 1:
                arr = [0] + src[:-1]
            elif d == -1:
                arr = src[1:] + [0]
            else:
                arr = src
            new.append(arr)
        dp = new

    res = 0
    for b in range(3):
        row = dp[b]
        res += sum(row[off + 1:])
    return res % MOD
