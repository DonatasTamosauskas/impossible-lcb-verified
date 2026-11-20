def longestString(x: int, y: int, z: int) -> int:
    m = min(x, y)
    if x == y:
        return 4 * m + 2 * z
    return 4 * m + 2 + 2 * z
