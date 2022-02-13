from typing import List


def _rec(n: int, m: int, idx: int, buff: List[int], res: List[List[int]]):
    if idx == n:
        res.append(buff.copy())
        return

    for e in range(1, m + 1):
        buff[idx] = e
        _rec(n, m, idx + 1, buff, res)


def get_all_sequences(n: int, m: int):
    buff = [0 for _ in range(n)]
    res = []

    _rec(n, m, 0, buff, res)

    return res
