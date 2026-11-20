def furthestDistanceFromOrigin(moves: str) -> int:
    return abs(moves.count("L") - moves.count("R")) + moves.count("_")
