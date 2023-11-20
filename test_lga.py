from unittest import TestCase
from lga import get_geo_political_zones


class Test(TestCase):
    def test_get_geo_political_zones(self):
        self.assertEqual("south_west", get_geo_political_zones("oyo"))
