from typing import List, Any


def _permute(idx: int, arr: List[Any], used: List[bool], res: List[List[Any]], buff: List[Any]):
    if idx == len(arr):
        res.append(buff.copy())
        return

    for i, e in enumerate(arr):
        if used[i]:
            continue
        buff[idx] = e
        used[i] = True
        _permute(idx + 1, arr, used, res, buff)
        used[i] = False


def permute(arr: List[Any]) -> List[List[Any]]:
    used = [False for _ in range(len(arr))]
    buff = [None for _ in range(len(arr))]
    res = []

    _permute(0, arr, used, res, buff)

    return res
