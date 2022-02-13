from typing import List


def solve(s1: List[str], s2: List[str]) -> int:
    d = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

            if s1[i - 1] == s2[j - 1]:
                d[i][j] = max(d[i][j], d[i - 1][j - 1] + 1)

    return d[-1][-1]


f = open('/Users/arkhipov/Downloads/seq2.in', 'r')
f.readline()
s1_ = f.readline().strip('\n').split(' ')
f.readline()
s2_ = f.readline().strip('\n').split(' ')

print(solve(s1=s1_, s2=s2_))
