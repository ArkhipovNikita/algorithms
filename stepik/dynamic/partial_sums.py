from typing import List, Tuple


def solve(n: int, m: int, arr: List[List[int]], q: List[Tuple[int, int, int, int]]) -> int:
    s = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + arr[i - 1][j - 1]

    q_sum = 0

    for x1, x2, y1, y2 in q:
        q_sum += s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]

    return q_sum


f = open('', 'r')
n, m = tuple(map(int, f.readline().strip('\n').split(' ')))
nums = []
qs = []
for _ in range(n):
    nums.append(list(map(int, f.readline().strip('\n').split(' '))))
qn = int(f.readline().strip('\n'))
for _ in range(qn):
    qs.append(tuple(map(int, f.readline().strip('\n').split(' '))))


print(
    solve(
        n=n,
        m=m,
        arr=nums,
        q=qs,
    )
)
