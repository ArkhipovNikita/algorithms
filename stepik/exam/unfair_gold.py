from typing import List


def solve(n: int, weights: List[int]) -> int:
    weights.sort(reverse=True)

    half_sum = 0
    for i in range(n // 2):
        half_sum += weights[i]

    sum_ = half_sum
    for i in range(n // 2, n):
        sum_ += weights[i]

    return abs(sum_ - 2 * half_sum)


f = open('/Users/arkhipov/Downloads/gold4.in', 'r')
n_ = int(f.readline())
weights_ = list(map(int, f.readline().strip(' \n').split(' ')))

# n_ = 4
# weights_ = [1, 2, 3, 4]

print(solve(n=n_, weights=weights_))
