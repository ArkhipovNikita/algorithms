import pytest

from .main import lucky_kazan_ticket


@pytest.mark.parametrize(
    ['numbers', 'expected'],
    [
        [
            [3, 4, 2, 1, 4, 0],
            True,
        ],
        [
            [3, 1, 1, 2, 2, 1],
            True,
        ],
        [
            [14, 1, 1, 2, 3, 5],
            False,
        ]
    ]
)
def test_lucky_kazan_ticket(numbers, expected):
    actual = lucky_kazan_ticket(numbers)

    assert actual == expected
