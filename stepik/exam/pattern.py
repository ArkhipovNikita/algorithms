import string
from typing import List


def _rec(idx: int, idxs: List[int], s: List[str], res: List[str]):
    if idx == len(idxs):
        res.append(''.join(s))
        return

    i = idxs[idx]

    for rc in string.ascii_lowercase[:5]:
        s[i] = rc
        _rec(idx + 1, idxs, s, res)


def solve(s: str) -> List[str]:
    res = []
    idxs = [i for i, c in enumerate(s) if c == '?']
    _rec(0, idxs, list(s), res)

    return res
