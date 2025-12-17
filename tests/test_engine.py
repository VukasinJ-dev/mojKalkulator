import unittest
from engine import izracunaj

class TestEngine(unittest.TestCase):

    def test_add(self):
        self.assertEqual(izracunaj(2, 3, "+"), 5)

    def test_sub(self):
        self.assertEqual(izracunaj(5, 2, "-"), 3)

    def test_mul(self):
        self.assertEqual(izracunaj(4, 3, "*"), 12)

    def test_div(self):
        self.assertEqual(izracunaj(10, 2, "/"), 5)

    def test_pow(self):
        self.assertEqual(izracunaj(2, 3, "^"), 8)

    def test_div_zero(self):
        with self.assertRaises(ValueError):
            izracunaj(5, 0, "/")

if __name__ == "__main__":
    unittest.main()