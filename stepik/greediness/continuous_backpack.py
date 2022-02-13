from typing import List


def solve(n: int, w: int, weights: List[int], costs: List[int]) -> int:
    res = 0

    items = list(zip(costs, weights))
    items.sort(reverse=True, key=lambda e: e[0] / e[1])

    for cost, weight in items:
        if w - weight < 0:
            res += w / weight * cost
            break

        w -= weight
        res += cost

    return res
