def isValid(word: str) -> bool:
    if len(word) < 3:
        return False
    v = c = False
    for ch in word:
        if not ch.isalnum() or not ch.isascii():
            return False
        if ch.isalpha():
            if ch.lower() in "aeiou":
                v = True
            else:
                c = True
    return v and c
