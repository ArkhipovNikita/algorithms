def solve(n: int, k: int):
    d = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        d[i][0] = 1
        d[i][i] = 1

        for j in range(1, i):
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j]

    return d[n][k]


print(solve(50, 20))
