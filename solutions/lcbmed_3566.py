from typing import List


def stringSequence(target: str) -> List[str]:
    res = []
    prefix = ""
    for ch in target:
        for c in range(ord('a'), ord(ch) + 1):
            res.append(prefix + chr(c))
        prefix += ch
    return res
