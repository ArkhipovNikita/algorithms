from typing import List, Tuple


def solve(t: int, tasks: List[int]) -> Tuple[int, int]:
    tasks.sort(reverse=False)
    fine = 0
    cnt = 0
    last = 0

    for task in tasks:
        if t - task < 0:
            break

        t -= task
        cnt += 1
        last += task
        fine += last

    return cnt, fine
