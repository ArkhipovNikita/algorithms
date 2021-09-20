from typing import List, Tuple


def two_pipelines(
        N: int,
        S: Tuple[int, int],
        E: Tuple[int, int],
        A: List[List[int]],
        T: List[List[int]],
):
    """
    Задача о двух конвейерах

    :param N: количество этапов
    :param E: матрица, где i ячейка показывает стоимость начала работы i конвейера
    :param S: матрица, где i ячейка показывает стоимость завершения работы i конвейера
    :param A: матрица, где i, j ячейка показывает стоимость исполнения j этапа на i конвейере
    :param T: матрица, где i, j ячейка показывает стоимость перехода с j - 1 этапа i - 1 конвейера
    на j этап на i конвейер

    :return: стоимость наименьшего маршрута и сам маршрут, состоящий из
     листа таплов, где 1-е число – конвейер, 2-е – этап
    """

    # заполнение массива F,
    # где F[i][j] - наименьшая стоимость маршрута до этапа j на конвейере i
    F = [[0] * N for _ in range(2)]
    F[0][0], F[1][0] = S[0] + A[0][0], S[1] + A[1][0]

    R = [[0] * N for _ in range(2)]
    R[0][0], R[1][0] = 0, 1

    for j in range(1, N):
        for i in range(2):
            ni = 0 if i == 1 else 1

            F[i][j], R[i][j] = min(
                (F[i][j - 1] + A[i][j], i),
                (F[ni][j - 1] + A[i][j] + T[i][j - 1], ni),
                key=lambda x: x[0],
            )

    cost, end_r = min(
        (F[0][-1] + E[0], 0),
        (F[1][-1] + E[1], 1),
        key=lambda x: x[0],
    )

    # восстановление маршрута
    i, j = end_r, N - 1
    route = []
    while j != -1:
        route.append((i, j))
        i = R[i][j]
        j -= 1

    route.reverse()

    # принт
    for l_, s in route:
        print(f'Конвейер {l_ + 1}, этап {s + 1} ')

    return cost, route
