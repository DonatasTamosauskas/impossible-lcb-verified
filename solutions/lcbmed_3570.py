def countOfSubstrings(word: str, k: int) -> int:
    n = len(word)
    V = "aeiou"
    ans = 0
    for i in range(n):
        seen = set()
        cons = 0
        for j in range(i, n):
            c = word[j]
            if c in V:
                seen.add(c)
            else:
                cons += 1
                if cons > k:
                    break
            if cons == k and len(seen) == 5:
                ans += 1
    return ans
