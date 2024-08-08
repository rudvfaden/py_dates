import unittest
from datetime import date
from bankdag import danish_bank_holiday, is_danish_bank_holiday, danish_bank_holiday_before, danish_bank_holiday_after


class Testis_danish_bank_holiday(unittest.TestCase):
    def test_danish_bank_holiday(self):
        self.assertEqual(
            danish_bank_holiday(2023, 'Påske'), date(2023, 4, 9)
        )
        self.assertEqual(danish_bank_holiday(
            2023, 'Skærtorsdag'), date(2023, 4, 6))
        self.assertEqual(danish_bank_holiday(
            2023, 'Langfredag'), date(2023, 4, 7))
        self.assertEqual(danish_bank_holiday(
            2023, '2. Påskedag'), date(2023, 4, 10))
        self.assertEqual(danish_bank_holiday(
            2023, 'Kristi himmelfartsdag'), date(2023, 5, 18))
        self.assertEqual(danish_bank_holiday(
            2023, 'Pinsedag'), date(2023, 5, 28))
        self.assertEqual(danish_bank_holiday(
            2023, '2. Pinsedag'), date(2023, 5, 29))
        self.assertEqual(danish_bank_holiday(
            2023, 'Julseaftensdag'), date(2023, 12, 24))
        self.assertEqual(danish_bank_holiday(
            2023, 'Juledag'), date(2023, 12, 25))
        self.assertEqual(danish_bank_holiday(
            2023, '2. Juledag'), date(2023, 12, 26))
        self.assertEqual(danish_bank_holiday(
            2023, 'Nytårsdag'), date(2023, 1, 1))
        self.assertEqual(danish_bank_holiday(
            2023, 'Grundlovsdag'), date(2023, 6, 5))
        self.assertEqual(danish_bank_holiday(
            2023, 'Nytåraftensdag'), date(2023, 12, 31))
        self.assertEqual(danish_bank_holiday(
            2023, 'Stor Bededag'), date(2023, 5, 5))
        self.assertEqual(danish_bank_holiday(
            2023, 'Fredag efter Kristi himmelfartsdag'), date(2023, 5, 19))

    def test_bank_holidays(self):
        # Test known bank holidays
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 4, 9)))  # Easter 2023
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 4, 6)))  # Skærtorsdag 2023
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 4, 7)))  # Langfredag 2023
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 4, 10)))  # andenPåskedag 2023
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 5, 5)))  # storeBededag 2023
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 5, 18)))  # Kr_himmelfart 2023
        # fredag efterKr_himmelfart 2023
        self.assertTrue(is_danish_bank_holiday(date(2023, 5, 19)))
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 5, 29)))  # andenPinsedag 2023
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 12, 24)))  # juleaftensdag 2023
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 12, 25)))  # juledag 2023
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 12, 26)))  # andenJuledag 2023
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 12, 31)))  # nytaarsdag 2023
        self.assertTrue(is_danish_bank_holiday(
            date(2023, 6, 5)))  # grundlovsdag 2023

    def test_weekends(self):
        # Test weekends
        self.assertTrue(is_danish_bank_holiday(date(2023, 4, 8)))  # Saturday
        self.assertTrue(is_danish_bank_holiday(date(2023, 4, 9)))  # Sunday

    def test_weekdays(self):
        # Test regular weekdays
        self.assertFalse(is_danish_bank_holiday(date(2023, 4, 11)))  # Tuesday
        self.assertFalse(is_danish_bank_holiday(
            date(2023, 4, 12)))  # Wednesday

    def test_danish_bank_holiday_before(self):
        # Test for finding a Danish bank holiday before the given date
        self.assertEqual(danish_bank_holiday_before(
            date(2024, 7, 13)), date(2024, 7, 12))

        # Test for no bank holiday found within the range
        with self.assertRaises(ValueError):
            danish_bank_holiday_before(date(2022, 4, 0))

    def test_danish_bank_holiday_after(self):
        # Test for finding a Danish bank holiday after the given date
        self.assertEqual(danish_bank_holiday_after(
            date(2024, 7, 13)), date(2024, 7, 15))

        # Test for no bank holiday found within the range
        with self.assertRaises(ValueError):
            danish_bank_holiday_after(date(2022, 12, 32))


if __name__ == '__main__':
    unittest.main()
