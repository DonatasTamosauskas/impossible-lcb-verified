def losingPlayer(x: int, y: int) -> str:
    t = min(x, y // 4)
    return "Alice" if t % 2 == 1 else "Bob"
