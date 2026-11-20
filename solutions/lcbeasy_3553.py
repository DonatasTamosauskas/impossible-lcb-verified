def checkTwoChessboards(coordinate1: str, coordinate2: str) -> bool:
    def p(c):
        return (ord(c[0]) - 97 + int(c[1])) % 2
    return p(coordinate1) == p(coordinate2)
