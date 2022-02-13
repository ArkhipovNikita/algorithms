from typing import List, Tuple


def solve(n: int, m: int, rels: List[Tuple[int, int]]) -> int:
    res = 0
    d = [0] * n

    for i, j in rels:
        d[i - 1] |= 1 << (j - 1)
        d[j - 1] |= 1 << (i - 1)

    for mask in range(1 << n):
        ones_count = 0
        is_full = True

        for i in range(n):
            if not (mask & (1 << i)):
                continue

            ones_count += 1
            new_mask = mask ^ (1 << i)
            if d[i] & new_mask != new_mask:
                is_full = False
                break

        if is_full and res < ones_count:
            res = ones_count

    return res


f = open('/Users/arkhipov/Downloads/friends2.in', 'r')
n_, m_ = tuple(map(int, f.readline().strip().split(' ')))
rels_ = [tuple(map(int, f.readline().strip().split(' '))) for _ in range(m_)]

# n_ = 4
# m_ = 4
# rels_ = [
#     (1, 2),
#     (2, 3),
#     (3, 1),
#     (2, 4),
# ]

print(
    solve(
        n=n_,
        m=m_,
        rels=rels_,
    )
)
