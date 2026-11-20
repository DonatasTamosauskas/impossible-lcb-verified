def isBalanced(num: str) -> bool:
    d = [int(c) for c in num]
    return sum(d[0::2]) == sum(d[1::2])
