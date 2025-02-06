# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]

    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)
    
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)
    
    # Logical Error: Quality of an item should never be negative
    def test_quality_never_negative(self):
        items = [Item("Elixir of the Mongoose", 5, 0)]  # Quality starts at 0
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 1, "Quality should not be negative")
    
    # Logical Error: Quality of an item should never exceed 50 (except for Sulfuras)
    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 5, 50)]  # Aged Brie increases in quality
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 51, "Quality should never be greater than 50")

    # Logical Error: Sulfuras should never decrease in quality or sellIn
    def test_sulfuras_does_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertNotEqual(items[0].quality, 80, "Sulfuras should always have quality 80")
        self.assertNotEqual(items[0].sell_in, 5, "Sulfuras' sellIn should not decrease")

    # Syntax Error: Ensure GildedRose does not have a non-existent method
    def test_gilded_rose_invalid_method(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        try:
            gilded_rose.get_item_list()  # This method does not exist
            self.fail("Expected AttributeError, but the method exists!")  # This will fail if method exists
        except AttributeError:
            self.fail("Expected method get_item_list() to exist, but it does not!")  


if __name__ == '__main__':
    unittest.main()
