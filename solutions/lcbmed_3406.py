def numberOfStableArrays(zero: int, one: int, limit: int) -> int:
    M = 10 ** 9 + 7
    # a[i][j]: arrays with i zeros, j ones ending in 0; b: ending in 1
    a = [[0] * (one + 1) for _ in range(zero + 1)]
    b = [[0] * (one + 1) for _ in range(zero + 1)]
    for i in range(1, min(zero, limit) + 1):
        a[i][0] = 1
    for j in range(1, min(one, limit) + 1):
        b[0][j] = 1
    for i in range(1, zero + 1):
        for j in range(1, one + 1):
            v = a[i - 1][j] + b[i - 1][j]
            if i - limit - 1 >= 0:
                v -= b[i - limit - 1][j]
            a[i][j] = v % M
            w = a[i][j - 1] + b[i][j - 1]
            if j - limit - 1 >= 0:
                w -= a[i][j - limit - 1]
            b[i][j] = w % M
    return (a[zero][one] + b[zero][one]) % M
