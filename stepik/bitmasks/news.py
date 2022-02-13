import math
from typing import List, Tuple


def solve(n: int, m: int, rels: List[Tuple[int, int]]) -> int:
    res = math.inf
    d = [0] * n

    for i, j in rels:
        d[i - 1] |= 1 << (j - 1)
        d[j - 1] |= 1 << (i - 1)

    for mask in range(1 << n):
        ones_count = 0
        ans = 0

        for i in range(n):
            if not (mask & (1 << i)):
                continue

            ones_count += 1

            if ones_count > res:
                break

            ans |= d[i]
            ans |= 1 << i

        if ans != 0 and (ans + 1) & ((1 << n) - 1) == 0 and ones_count < res:
            res = ones_count

    return res


f = open('/Users/arkhipov/Downloads/new2.in', 'r')
n_, m_ = tuple(map(int, f.readline().strip().split(' ')))
rels_ = [tuple(map(int, f.readline().strip().split(' '))) for _ in range(m_)]

# n_ = 4
# m_ = 4
# rels_ = [
#     (1, 2),
#     (2, 3),
#     (3, 4),
# ]

print(
    solve(
        n=n_,
        m=m_,
        rels=rels_,
    )
)
