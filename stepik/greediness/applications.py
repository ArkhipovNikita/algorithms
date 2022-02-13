from typing import List, Tuple


def arrange_applications(n: int, applications: List[Tuple[int, int]]) -> int:
    applications.sort(key=lambda x: x[1])

    res = [applications[0]] if len(applications) > 0 else []

    for i in range(1, len(applications)):
        if applications[i][0] >= res[-1][1]:
            res.append(applications[i])

    return len(res)
