def kthCharacter(k: int) -> str:
    return chr(ord("a") + bin(k - 1).count("1") % 26)
