# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_aged_brie_increase_quality(self):
        items = [Item('Aged Brie', 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == 9
        assert items[0].quality == 1

    def test_aged_brie_increase_quality_outOfDate(self):
        items = [Item('Aged Brie', -5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == -6
        assert items[0].quality == 2

    def test_conjured_mana_cake(self):
        items = [Item('Conjured Mana Cake', 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == 9
        assert items[0].quality == 8

    def test_conjured_mana_cake_outOfDate(self):
        items = [Item('Conjured Mana Cake', -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == -2
        assert items[0].quality == 6

    def test_backstage_passes_tenDaysOrLess(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == 9
        assert items[0].quality == 22

    def test_backstage_passes_fiveDaysOrLess(self):
        items = [Item('Backstage passes to a TAFKAL80ETC concert', 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == 4
        assert items[0].quality == 23


if __name__ == '__main__':
    unittest.main()