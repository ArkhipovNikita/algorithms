import copy
import math
from typing import List, Tuple


def solve(n: int, arr: List[List[int]]) -> Tuple[int, str]:
    d = [[math.inf] * n for _ in range(1 << n)]
    d[0][0] = 0

    p = copy.deepcopy(d)

    for mask in range(1 << n):
        for i in range(n):

            if math.isinf(d[mask][i]):
                continue

            for j in range(n):
                if mask & (1 << j):
                    continue

                new_mask = mask ^ (1 << j)
                if d[new_mask][j] > d[mask][i] + arr[i][j]:
                    d[new_mask][j] = d[mask][i] + arr[i][j]
                    p[new_mask][j] = i

    mask, j = (1 << n) - 1, 0
    d_path = [j]

    while mask != 0:
        prev_p = p[mask][j]
        d_path.append(prev_p)
        mask ^= 1 << j
        j = prev_p

    r_path = d_path.copy()
    r_path.reverse()

    path = r_path if r_path[1] < d_path[1] else d_path
    path = ' '.join(map(str, path[:-1]))

    return int(d[-1][0]), path


f = open('/Users/arkhipov/Downloads/salesman2.in', 'r')
n_ = int(f.readline())
arr_ = [
    list(map(int, line.strip(' \n').split(' ')))
    for line in f.readlines()
]

# n_ = 4
# arr_ = [
#     [0, 1, 4, 6],
#
#     [1, 0, 5, 2],
#
#     [4, 5, 0, 3],
#
#     [6, 2, 3, 0],
# ]

print(solve(n=n_, arr=arr_))
