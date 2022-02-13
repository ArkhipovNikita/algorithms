from typing import List, Tuple


def _rec(
    n: int,
    idx: int,
    length: int,
    min_length: List[float],
    arr: List[List[int]],
    used: List[int],
    buff: List[int],
    res: List[int],
):
    if length >= min_length[0]:
        return

    if idx == n:
        cur_length = length + arr[buff[idx - 1]][0]

        if min_length[0] > cur_length:
            min_length[0] = cur_length
            res[:] = buff.copy()

        return

    for i in range(1, n):
        if used[i]:
            continue
        buff[idx] = i
        used[i] = True
        _rec(n, idx + 1, length + arr[buff[idx - 1]][i], min_length, arr, used, buff, res)
        used[i] = False


def find_shortest_path(n: int, arr: List[List[int]]) -> Tuple[int, List[int]]:
    buff = [0] * n
    used = [False] * n
    res = []
    min_length = [float('inf')]

    _rec(n, 1, 0, min_length, arr, used, buff, res)

    print('Минимальная длина – {}'.format(min_length[0]))
    print('Путь – {}'.format(res))

    return int(min_length[0]), res
