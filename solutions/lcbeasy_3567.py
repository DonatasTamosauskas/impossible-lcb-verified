def convertDateToBinary(date: str) -> str:
    return "-".join(bin(int(p))[2:] for p in date.split("-"))
