from typing import List


def validStrings(n: int) -> List[str]:
    res = []

    def go(s, last):
        if len(s) == n:
            res.append(s)
            return
        go(s + "1", "1")
        if last != "0":
            go(s + "0", "0")

    go("", "1")
    return sorted(res)
