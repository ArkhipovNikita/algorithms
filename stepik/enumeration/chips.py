from typing import List


def _rec(n: int, m: int, idx: int, arranged: int, buff: List[str], res: List[str]):
    # if m - arranged > n - idx:
    #     return

    if idx == n:
        if m == arranged:
            res.append(''.join(buff))
        return

    if idx > 0 and buff[idx - 1] == '*':
        buff[idx] = '.'
        _rec(n, m, idx + 1, arranged, buff, res)
    else:
        buff[idx] = '*'
        _rec(n, m, idx + 1, arranged + 1, buff, res)
        buff[idx] = '.'
        _rec(n, m, idx + 1, arranged, buff, res)


def get_all_chip_arrangements(n: int, m: int) -> List[List[int]]:
    buff = [''] * n
    res = []

    _rec(n, m, 0, 0, buff, res)

    return res
