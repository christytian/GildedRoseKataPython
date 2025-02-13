# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Base class for all item updaters
class ItemUpdater:
    def update_quality(self, item):
        pass


# Updater for normal items
class NormalItemUpdater(ItemUpdater):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


# Updater for "Aged Brie"
class AgedBrieUpdater(ItemUpdater):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


# Updater for "Sulfuras, Hand of Ragnaros"
class SulfurasUpdater(ItemUpdater):
    def update_quality(self, item):
        pass  # Sulfuras does not change


# Updater for "Backstage passes to a TAFKAL80ETC concert"
class BackstagePassesUpdater(ItemUpdater):
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1
        item.sell_in -= 1
        if item.quality > 50:
            item.quality = 50


# Updater for "Conjured" items
class ConjuredItemUpdater(ItemUpdater):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality -= 2
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2


class GildedRose(object):
    
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        # Map item names to their corresponding strategies
        self.updaters = {
            "Aged Brie": AgedBrieUpdater(),
            "Sulfuras, Hand of Ragnaros": SulfurasUpdater(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassesUpdater(),
            "Conjured": ConjuredItemUpdater(),
        }


    def update_quality(self):
        for item in self.items:
            # Use the appropriate updater for the item, defaulting to NormalItemUpdater
            updater = self.updaters.get(item.name, NormalItemUpdater())
            updater.update_quality(item)