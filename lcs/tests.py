import pytest

from .main import largest_common_subsequence


@pytest.mark.parametrize(
    ['a', 'b', 'expected'],
    [
        [
            ['A', 'B', 'C', 'B', 'D', 'A', 'B'],
            ['B', 'D', 'C', 'A', 'B', 'A'],
            ['B', 'C', 'B', 'A']
        ],
        [[], [1, 2, 3], []],
        [[], [], []]
    ]
)
def test_largest_common_subsequence(a, b, expected):
    actual = largest_common_subsequence(a, b)

    assert actual == expected
