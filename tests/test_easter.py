import unittest
from datetime import date
from easter import easter

class TestEasterFunction(unittest.TestCase):
    def test_easter(self):
        # Known Easter dates for specific years
        known_dates = {
            2020: date(2020, 4, 12),
            2021: date(2021, 4, 4),
            2022: date(2022, 4, 17),
            2023: date(2023, 4, 9),
            2024: date(2024, 3, 31),
        }

        for year, expected_date in known_dates.items():
            with self.subTest(year=year):
                self.assertEqual(easter(year), expected_date)

if __name__ == '__main__':
    unittest.main()