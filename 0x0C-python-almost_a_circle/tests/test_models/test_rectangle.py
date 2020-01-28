import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

   def test_area(self):
       r1 = Rectangle(3, 2)
       self.assertEqual(r1.area(), 3*2, "False area")

if __name__ == '__main__':
    unittest.main()
