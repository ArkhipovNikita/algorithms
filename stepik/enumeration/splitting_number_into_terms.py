from typing import List


def _rec(idx: int, n: int, sum_: int, last: int, buff: List[int], res: List[List[int]]):
    if sum_ == n:
        res.append(buff[:idx])
        return

    for num in range(last, n - sum_ + 1):
        buff[idx] = num
        _rec(idx + 1, n, sum_ + num, num, buff, res)


def split_number_into_terms(n: int) -> List[List[int]]:
    buff = [0] * n
    res = []

    _rec(0, n, 0, 1, buff, res)

    return res
