from typing import List


def countMentions(numberOfUsers: int, events: List[List[str]]) -> List[int]:
    res = [0] * numberOfUsers
    until = [0] * numberOfUsers
    evs = sorted(events, key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))
    for typ, ts, s in evs:
        t = int(ts)
        if typ == "OFFLINE":
            until[int(s)] = t + 60
        else:
            if s == "ALL":
                for i in range(numberOfUsers):
                    res[i] += 1
            elif s == "HERE":
                for i in range(numberOfUsers):
                    if until[i] <= t:
                        res[i] += 1
            else:
                for tok in s.split():
                    res[int(tok[2:])] += 1
    return res
