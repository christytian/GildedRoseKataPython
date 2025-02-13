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
        self.assertEquals("Sulfuras", items[0].name)
        sulfuras_item = items[0]
        self.assertEqual(79, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # Ensures item quality is never negative after updating
    def test_quality_never_negative(self):
        items = [Item("Elixir of the Mongoose", 5, 0)]  # Quality starts at 0
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0, "Quality should not be negative")
    
    # Ensures Aged Brie quality does not exceed 50 after updating
    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 5, 50)]  # Aged Brie increases in quality
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50, "Quality should never be greater than 50")


    # Ensures Sulfuras quality and sell_in values remain unchanged after updating
    def test_sulfuras_does_not_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80, "Sulfuras should always have quality 80")
        self.assertEqual(items[0].sell_in, 5, "Sulfuras' sell_in should not decrease")

    # Ensures calling a non-existent method on GildedRose raises an AttributeError
    def test_gilded_rose_invalid_method(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        with self.assertRaises(AttributeError, msg="Expected method get_item_list() to not exist"):
            gilded_rose.get_item_list()

if __name__ == '__main__':
    unittest.main()
