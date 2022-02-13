from typing import List


def solve(ice_creams: List[str]) -> int:
    res = 1
    t = set()

    for ice_cream in ice_creams:
        if ice_cream in t:
            res += 1
            t = set()

        t.add(ice_cream)

    return res
