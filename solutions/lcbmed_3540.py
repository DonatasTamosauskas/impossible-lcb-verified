def stringHash(s: str, k: int) -> str:
    out = []
    for i in range(0, len(s), k):
        out.append(chr(97 + sum(ord(c) - 97 for c in s[i:i + k]) % 26))
    return "".join(out)
