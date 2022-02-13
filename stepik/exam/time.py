from typing import List


def solve(n: int, times: List[int], deadlines: List[int]) -> int:
    max_time = sorted(map(sum, zip(times, deadlines)), reverse=True)[0]
    d = [[0] * (max_time + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max_time + 1):
            d[i][j] = d[i - 1][j]

            if j - times[i - 1] >= 0 and j <= (deadlines[i - 1] + times[i - 1]):
                d[i][j] = max(d[i][j], d[i - 1][j - times[i - 1]] + 1)

    return max(d[-1])


f = open('/Users/arkhipov/Downloads/time2.in', 'r')
n_ = int(f.readline())
times_, deadlines_ = [], []

for line in f.readlines():
    t = tuple(map(int, line.strip(' \n').split(' ')))
    times_.append(t[0])
    deadlines_.append(t[1])

# n_ = 10
# times_ = [8, 5, 7, 11, 3, 6, 10, 5, 7, 6]
# deadlines_ = [25, 12, 10, 28, 18, 32, 45, 34, 28, 42]

print(solve(n=n_, times=times_, deadlines=deadlines_))
