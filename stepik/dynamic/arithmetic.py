from typing import List


def solve(n: int, x: int, nums: List[int]):
    nums_sum = sum(nums)
    sum_ = (nums_sum - x) // 2
    d = [[0] * (sum_ + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(1, sum_ + 1):
            d[i][j] = d[i - 1][j]

            if j - nums[i - 1] >= 0:
                d[i][j] = max(d[i][j], d[i - 1][j - nums[i - 1]] + nums[i - 1])

    neg_num_idxs = []
    i, j = n, sum_

    while i != 0:
        if j - nums[i - 1] >= 0 and d[i - 1][j - nums[i - 1]] + nums[i - 1] > d[i - 1][j]:
            neg_num_idxs.append(i - 1)
            j -= nums[i - 1]
            i -= 1
        else:
            i -= 1

    for neg_num_idx in neg_num_idxs:
        nums[neg_num_idx] *= -1

    print(nums[0], end='')
    for idx in range(1, len(nums)):
        if nums[idx] > 0:
            print('+', end='')
        print(nums[idx], end='')


# solve(10, 25, [21, 27, 34, 20, 29, 24, 38, 38, 22, 24])
solve(50, -3360,
      [91, 67, 84, 50, 69, 74, 78, 58, 62, 64, 55, 95, 81, 77, 61, 91, 95, 92, 77, 86, 91, 54, 52,
       53, 92, 82, 71, 66, 68, 95, 97, 76, 71, 88, 69, 62, 67, 99, 85, 94, 53, 61, 72, 83, 73, 64,
       91, 61, 53, 68])
