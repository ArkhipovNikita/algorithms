import pytest

from .main import pack_bag_01, Item


@pytest.mark.parametrize(
    ['W', 'items', 'expected_value', 'expected_items'],
    [
        [
            10,
            {
                Item('apple', 3, 5),
                Item('banana', 4, 3),
                Item('potato', 1, 4),
                Item('carrot', 2, 6),
            },
            18,
            {
                Item('apple', 3, 5),
                Item('banana', 4, 3),
                Item('potato', 1, 4),
                Item('carrot', 2, 6),
            },
        ],
        [
            7,
            [
                Item('apple', 3, 5),
                Item('banana', 4, 3),
                Item('potato', 1, 4),
                Item('carrot', 2, 6),
            ],
            15,
            {
                Item('apple', 3, 5),
                Item('potato', 1, 4),
                Item('carrot', 2, 6),
            },
        ],
    ]
)
def test_pack_bag(W, items, expected_value, expected_items):
    actual_value, actual_items = pack_bag_01(items, W)

    assert actual_value == expected_value
    assert actual_items == expected_items
