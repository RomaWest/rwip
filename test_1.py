import unittest
from test1 import distance

class DistanceCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(distance(x1=0, x2=0, y1=0, y2=0), 0)

    def test2(self):
        self.assertGreater(distance(x1=0, x2=0, y1=5, y2=0), 1000000)