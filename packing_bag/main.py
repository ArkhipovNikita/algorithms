from collections import namedtuple
from typing import List, Set

Item = namedtuple('Item', ['name', 'weight', 'value'])


# с повторным взятием предметов
def pack_bag(items: List[Item], W: int):
    C = [(0, None, None)] * (W + 1)

    for w in range(1, W + 1):
        chosen_item = 0
        max_value = 0

        for item in items:
            if item.weight > w:
                continue

            cur_value = item.value + C[w - item.weight][0]

            if cur_value > max_value:
                chosen_item = item
                max_value = cur_value

        previous_item_idx = w - chosen_item.weight
        C[w] = (max_value, chosen_item, previous_item_idx)

    chosen_items = []
    i = C[-1][-1]
    while i is not None:
        chosen_items.append(C[i][1])
        i = C[i][-1]

    return C[-1][0], chosen_items


def pack_bag_01(items: Set[Item], W: int):
    """
    Находит множество объектов с максимальной стоимостью

    :param items: множество объектов
    :param W: максимальный вес рюкзака
    :return: максимально возможная стоимость, множество объектов
    """
    items = list(items)
    # заполнение массива стоимостей 0
    # С[i][j] = 0 при i или j = 0
    C = [[0] * (W + 1) for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        item = items[i - 1]

        for j in range(1, W + 1):
            # если вес объекта больше допустимого,
            # то взять стоимость для такого же веса, но для другого объекта
            if item.weight > j:
                C[i][j] = C[i - 1][j]
            # иначе найти максимальную стоимость из другого объекта с этой же стоимостью
            # и текущего объекта со стоимостью для оставшегося веса
            else:
                C[i][j] = max(
                    C[i - 1][j],
                    C[i - 1][j - item.weight] + item.value
                )

    # восстановление объектов
    chosen_items = set()
    i, j = len(items), W - 1
    while i != 0:
        item = items[i - 1]
        w = j + 1

        if item.weight <= w and C[i - 1][j] < C[i - 1][w - item.weight] + item.value:
            chosen_items.add(item)
            j = w - item.weight
        i -= 1

    return C[-1][-1], chosen_items
