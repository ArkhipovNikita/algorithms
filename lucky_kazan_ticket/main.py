from typing import List


def lucky_kazan_ticket(numbers: List[int]):
    numbers_sum = sum(numbers)

    # если сумма нечетна,
    # то нет двух подмножеств с равной суммой
    if numbers_sum % 2 != 0:
        return False

    # по Ox веса от 0 до K
    # по Oy подмножества из цифр от 0 до по i (пустое подмножество тоже есть)
    K = numbers_sum // 2
    S = [[False] * (K + 1) for _ in range(len(numbers) + 1)]
    S[0][0] = True

    for i in range(1, len(numbers) + 1):
        for j in range(K + 1):

            if (
                    # если на предыдущем подмножестве набралась нужная сумма, то True
                    # или если на предыдущем подмножестве и
                    # на сумме меньше текущей на текущее значение числа, то True
                    S[i - 1][j] or
                    (
                        j >= numbers[i - 1] and
                        S[i - 1][j - numbers[i - 1]]
                    )
            ):
                S[i][j] = True
            else:
                # иначе False
                S[i][j] = False

    return S[-1][-1]
