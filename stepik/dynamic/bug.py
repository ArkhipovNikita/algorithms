from typing import List, Tuple


def solve(n: int, m: int, arr: List[List[int]]) -> Tuple[int, str]:
    d = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            d[i][j] = arr[i][j]

            if i > 0:
                d[i][j] = max(d[i][j], d[i - 1][j] + arr[i][j])
            if j > 0:
                d[i][j] = max(d[i][j], d[i][j - 1] + arr[i][j])

    path = []
    i, j = n - 1, m - 1

    while i != 0 or j != 0:

        if i == 0 or j == 0:
            if i == 0:
                path.append('R')
                j -= 1
            else:
                path.append('D')
                i -= 1
        else:
            if d[i - 1][j] > d[i][j - 1]:
                path.append('D')
                i -= 1
            else:
                path.append('R')
                j -= 1

    path.reverse()

    return d[n - 1][m - 1], ''.join(path)


print(
    solve(
        n=4,
        m=5,
        arr=[
            [1, 4, 1, 2, 3],
            [2, 3, 2, 1, 4],
            [1, 1, 1, 2, 4],
            [2, 5, 1, 7, 1],
        ]
    )
)
