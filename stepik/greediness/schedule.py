from typing import List


def schedule(n: int, deadlines: List[int], costs: List[int]) -> int:
    sum_ = 0
    used = [False] * n
    data = list(zip(deadlines, costs))
    data.sort(reverse=True, key=lambda e: e[1])

    for deadline, cost in data:
        t = deadline - 1
        while t >= 0 and used[t]:
            t -= 1
        if t == -1:
            continue
        used[t] = True
        sum_ += cost

    return sum_


f = open('/Users/arkhipov/Downloads/schedule2.in', 'r')
n_ = int(f.readline().rstrip('\n'))
d = []
c = []
for line in f.readlines():
    if line == '\n':
        continue
    d_, c_ = list(map(int, filter(lambda x: x.strip(' \n'), line.split(' '))))
    d.append(d_)
    c.append(c_)
f.close()

print(schedule(n_, d, c))
