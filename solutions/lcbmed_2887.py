def sortVowels(s: str) -> str:
    v = set("aeiouAEIOU")
    vs = sorted(c for c in s if c in v)
    it = iter(vs)
    return "".join(next(it) if c in v else c for c in s)
