from typing import List, Tuple


def solve(n: int, W: int, weights: List[int], costs: List[int]) -> Tuple[int, str]:
    d = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if j - weights[i - 1] >= 0 and d[i - 1][j - weights[i - 1]] + costs[i - 1] > d[i - 1][j]:
                d[i][j] = d[i - 1][j - weights[i - 1]] + costs[i - 1]
            else:
                d[i][j] = d[i - 1][j]

    items = []
    i, j = n, W

    while i != 0:
        if j - weights[i - 1] >= 0 and d[i - 1][j - weights[i - 1]] + costs[i - 1] > d[i - 1][j]:
            items.append(i)
            j -= weights[i - 1]
            i -= 1
        else:
            i -= 1

    items.sort()

    return d[n][W], ' '.join(map(str, items))


f = open('/Users/arkhipov/Downloads/rucksack.in', 'r')
n_, W_ = tuple(map(int, f.readline().strip('\n').split(' ')))
weights_ = []
costs_ = []
for row in f.readlines():
    item = tuple(map(int, row.strip('\n').split(' ')))
    weights_.append(item[0])
    costs_.append(item[1])

print(solve(n=n_, W=W_, weights=weights_, costs=costs_))
