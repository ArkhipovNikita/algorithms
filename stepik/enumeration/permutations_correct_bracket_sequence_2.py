from typing import List


def _rec(n: int, idx: int, balance1: int, balance2: int, buff: List[str], stack: List[str], res: List[str]):
    opened_bracket = None

    # can be optimized
    if idx == 2 * n:
        if balance1 == 0 and balance2 == 0:
            res.append(''.join(buff))
        return

    if idx > 1:
        prev_c = buff[idx - 1]
        if prev_c in [')', ']']:
            opened_bracket_temp = stack[-1]
            if (
                    (opened_bracket_temp == '(' and prev_c == ')') or
                    (opened_bracket_temp == '[' and prev_c == ']')
            ):
                opened_bracket = stack.pop()
            else:
                return

    buff[idx] = '('
    stack.append('(')
    _rec(n, idx + 1, balance1 + 1, balance2, buff, stack, res)
    stack.pop()

    if balance1 != 0:
        buff[idx] = ')'
        _rec(n, idx + 1, balance1 - 1, balance2, buff, stack, res)

    buff[idx] = '['
    stack.append('[')
    _rec(n, idx + 1, balance1, balance2 + 1, buff, stack, res)
    stack.pop()

    if balance2 != 0:
        buff[idx] = ']'
        _rec(n, idx + 1, balance1, balance2 - 1, buff, stack, res)

    if opened_bracket:
        stack.append(opened_bracket)


def get_all_correct_bracket_seqs(n: int) -> List[str]:
    res = []
    buff = [''] * 2 * n

    _rec(n, 0, 0, 0, buff, [], res)

    return res
