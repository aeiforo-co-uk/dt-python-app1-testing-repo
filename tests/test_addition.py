import unittest
from app import add  # Assuming your function is in app.py

class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)

if __name__ == '__main__':
    unittest.main()
