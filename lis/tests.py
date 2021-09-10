import pytest

from .main import largest_increasing_subsequence


@pytest.mark.parametrize(
    ['a', 'expected'],
    [
        [[2, 4, 9, 1, 10, 3, 11], [2, 4, 9, 10, 11]],
        [[4, 5, 6, 7, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
        [[4, 3, 2, 1], [4]],
        [[-1, -2, 0, -7, -6], [-2, 0]],
        [[], []]
    ]
)
def test_largest_increasing_subsequence(a, expected):
    actual = largest_increasing_subsequence(a)

    assert actual == expected
