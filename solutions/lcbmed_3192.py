def maximumXorProduct(a: int, b: int, n: int) -> int:
    M = 10**9 + 7
    A = (a >> n) << n
    B = (b >> n) << n
    diff_seen = A != B
    a_bigger = A > B
    for i in range(n - 1, -1, -1):
        ai = (a >> i) & 1
        bi = (b >> i) & 1
        if ai == bi:
            A |= 1 << i
            B |= 1 << i
        else:
            if not diff_seen:
                diff_seen = True
                a_bigger = True
                A |= 1 << i
            elif a_bigger:
                B |= 1 << i
            else:
                A |= 1 << i
    return (A * B) % M
