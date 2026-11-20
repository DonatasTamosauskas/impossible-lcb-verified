from typing import List


def countSeniors(details: List[str]) -> int:
    return sum(1 for d in details if int(d[11:13]) > 60)
