from src.gilded_rose import GildedRose
from src.item import Item


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "fixme" == items[0].name
