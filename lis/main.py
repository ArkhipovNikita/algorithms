from typing import List


def largest_increasing_subsequence(a: List) -> List:
    if len(a) == 0:
        return []

    lengths = [0] * len(a)

    # заполнение длин
    for i in range(len(a)):
        max_ = 0
        for j in range(i):
            if a[i] > a[j] and lengths[j] > max_:
                max_ = lengths[j]

        lengths[i] = max_ + 1

    # восстановление
    res = []
    length = max(lengths)
    i = lengths.index(length)

    while length != 0:
        res.append(a[i])
        length -= 1
        for j in range(i):
            if a[j] < a[i] and lengths[j] == length:
                i = j

    # разворот маршрута
    res.reverse()

    return res
