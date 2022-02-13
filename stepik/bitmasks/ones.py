from typing import List


def count_ones(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    m = n // 2

    if n % 2 == 0:
        return count_ones(m)
    else:
        return count_ones(m) + 1


def solve(nums: List[int]) -> str:
    ones = []

    for num in nums:
        ones.append(count_ones(num))

    return ' '.join(map(str, ones))


print(solve([1361955, 207579012, 628145516, 376140462, 883515280, 186969585, 762888635, 326402539]))