import unittest
from app import add, subtract

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-2, -1), -1)
        self.assertEqual(subtract(0, 0), 0)

if _name_ == '_main_':
    unittest.main()
