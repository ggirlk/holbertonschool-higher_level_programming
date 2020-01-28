#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_inc(self):
        b1 = Base()
        b2 = Base()
        self.assertTrue(b2.id == b1.id +1,
                         'id does not increment')


if __name__ == '__main__':
    unittest.main()
