from typing import List


def largest_common_subsequence(a: List, b: List) -> List:
    lengths = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    dirs = [[None] * (len(b) + 1) for _ in range(len(a) + 1)]

    # заполнение lengths и dirs
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                length = lengths[i - 1][j - 1] + 1
                dir_ = (-1, -1)
            else:
                length, dir_ = max(
                    [
                        (lengths[i - 1][j], (-1, 0)),
                        (lengths[i][j - 1], (0, -1))
                    ],
                    key=lambda x: x[0]
                )

            lengths[i][j] = length
            dirs[i][j] = dir_

    # восстановление маршрута
    res = []
    i, j = len(a), len(b)
    while dirs[i][j] is not None:
        di, dj = dirs[i][j]
        if di == dj:
            res.append(a[i - 1])
        i += di
        j += dj

    # разворот маршрута
    res.reverse()

    return res
