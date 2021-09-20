import pytest

from .main import two_pipelines


@pytest.mark.parametrize(
    ['N', 'S', 'E', 'A', 'T', 'expected_cost', 'expected_route'],
    [
        [
            6,
            (2, 4),
            (3, 2),
            [
                [7, 9, 3, 4, 8, 4],
                [8, 5, 6, 4, 5, 7],
            ],
            [
                [2, 1, 2, 2, 1],
                [2, 3, 1, 3, 4],
            ],
            38,
            [
                (0, 0),
                (1, 1),
                (0, 2),
                (1, 3),
                (1, 4),
                (0, 5)
            ],
        ],
        [
            4,
            (4, 2),
            (1, 3),
            [
                [1, 4, 3, 8],
                [7, 0, 1, 2],
            ],
            [
                [1, 2, 4, 6],
                [2, 1, 2, 1],
            ],
            13,
            [
                (0, 0),
                (1, 1),
                (1, 2),
                (1, 3),
            ]
        ]
    ]
)
def test_two_pipelines(N, S, E, A, T, expected_cost, expected_route):
    actual_cost, actual_route = two_pipelines(N, S, E, A, T)

    assert actual_cost == expected_cost
    assert actual_route == expected_route
