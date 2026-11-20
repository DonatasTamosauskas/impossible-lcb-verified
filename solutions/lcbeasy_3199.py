def distributeCandies(n: int, limit: int) -> int:
    cnt = 0
    for a in range(min(n, limit) + 1):
        for b in range(min(n - a, limit) + 1):
            if n - a - b <= limit:
                cnt += 1
    return cnt
