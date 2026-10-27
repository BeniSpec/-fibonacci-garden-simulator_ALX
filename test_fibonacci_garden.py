import unittest

from fibonacci_garden import flowers_on_day


class TestFlowersOnDay(unittest.TestCase):
    def test_first_two_days_are_one(self):
        self.assertEqual(flowers_on_day(1), 1)
        self.assertEqual(flowers_on_day(2), 1)

    def test_first_days(self):
        expected = [1, 1, 2, 3, 5, 8, 13]
        self.assertEqual([flowers_on_day(d) for d in range(1, 8)], expected)

    def test_day_ten(self):
        self.assertEqual(flowers_on_day(10), 55)

    def test_large_day(self):
        self.assertEqual(flowers_on_day(30), 832040)

    def test_invalid_day(self):
        for bad in (0, -1, -50):
            with self.assertRaises(ValueError):
                flowers_on_day(bad)


if __name__ == "__main__":
    unittest.main()