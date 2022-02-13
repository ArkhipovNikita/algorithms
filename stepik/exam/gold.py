import math
from typing import List


# Перебор по битовым маскам
def solve(n: int, weights: List[int]) -> int:
    ans = math.inf
    sums = [0] * (1 << n)

    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue

            sums[mask] = sums[mask ^ (1 << i)] + weights[i]
            break

    for mask in range(1 << n):
        opposite_mask = mask ^ ((1 << n) - 1)
        ans = min(ans, abs(sums[mask] - sums[opposite_mask]))

    return ans


# Динамика
# def solve(n: int, weights: List[int]) -> int:
#     sum_ = sum(weights)
#     half_sum = sum_ // 2
#     d = [[0] * (half_sum + 1) for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         for j in range(1, half_sum + 1):
#             d[i][j] = d[i - 1][j]
#
#             if j - weights[i - 1] >= 0:
#                 d[i][j] = max(d[i][j], d[i - 1][j - weights[i - 1]] + weights[i - 1])
#
#     return sum_ - 2 * d[-1][-1]


f = open('/Users/arkhipov/Downloads/gold3.in', 'r')
n_ = int(f.readline())
weights_ = list(map(int, f.readline().strip(' \n').split(' ')))

# n_ = 5
# weights_ = [1, 2, 3, 4, 5]

print(solve(n=n_, weights=weights_))
