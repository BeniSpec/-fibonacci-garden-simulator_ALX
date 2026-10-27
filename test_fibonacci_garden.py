import unittest

from fibonacci_garden import flowers_on_day


class TestFlowersOnDay(unittest.TestCase):
    def test_first_days(self):
        expected = [1, 1, 2, 3, 5, 8, 13]
        self.assertEqual([flowers_on_day(d) for d in range(1, 8)], expected)

    def test_day_ten(self):
        self.assertEqual(flowers_on_day(10), 55)

    def test_invalid_day(self):
        with self.assertRaises(ValueError):
            flowers_on_day(0)


if __name__ == "__main__":
    unittest.main()