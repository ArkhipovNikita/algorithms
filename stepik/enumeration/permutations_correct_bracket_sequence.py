from typing import List


def _rec(idx: int, balance: int, buff: List[str], res: List[str]):
    if balance > len(buff) - idx:
        return

    if idx == len(buff):
        res.append(''.join(buff))
        return

    buff[idx] = '('
    _rec(idx + 1, balance + 1, buff, res)
    if balance == 0:
        return
    buff[idx] = ')'
    _rec(idx + 1, balance - 1, buff, res)


def get_all_correct_bracket_seqs(n: int) -> List[str]:
    res = []
    buff = [''] * 2 * n

    _rec(0, 0, buff, res)

    return res
