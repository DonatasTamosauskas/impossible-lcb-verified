def getEncryptedString(s: str, k: int) -> str:
    n = len(s)
    return "".join(s[(i + k) % n] for i in range(n))
