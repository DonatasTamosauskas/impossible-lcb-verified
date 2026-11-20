def canAliceWin(n: int) -> bool:
    moves = 0
    take = 10
    while take > 0 and n >= take:
        n -= take
        take -= 1
        moves += 1
    return moves % 2 == 1
