def check(s: str) -> bool:
    stack = []

    for c in s:
        try:
            prev_c = stack.pop()
        except IndexError:
            stack.append(c)
            continue

        if (prev_c == '(' and c == ')') or (prev_c == '[' and c == ']'):
            continue

        stack.append(prev_c)
        stack.append(c)

    return len(stack) == 0


print(check('()()[[[]()]]([()][][()[]])[]()()'))
print(check('[[]](()()[[[]]][]()()()[()])()]'))
print(check('[[[((]))[](][)(()())]][[][]()[]]'))
print(check('(()[([][]())[()][()][][])]([])()'))
print(check('(()[([][]())[()][()][][]])([])()'))