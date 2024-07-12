import unittest
from datetime import date
from bankdag import is_danish_bank_holiday

class Testis_danish_bank_holiday(unittest.TestCase):
    def test_bank_holidays(self):
        # Test known bank holidays
        self.assertFalse(is_danish_bank_holiday(date(2023, 4, 9)))  # Easter 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 4, 6)))  # Skærtorsdag 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 4, 7)))  # Langfredag 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 4, 10)))  # andenPåskedag 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 5, 5)))  # storeBededag 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 5, 18)))  # Kr_himmelfart 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 5, 19)))  # fredag efterKr_himmelfart 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 5, 29)))  # andenPinsedag 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 12, 24)))  # juleaftensdag 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 12, 25)))  # juledag 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 12, 26)))  # andenJuledag 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 12, 31)))  # nytaarsdag 2023
        self.assertFalse(is_danish_bank_holiday(date(2023, 6, 5)))  # grundlovsdag 2023

    def test_weekends(self):
        # Test weekends
        self.assertFalse(is_danish_bank_holiday(date(2023, 4, 8)))  # Saturday
        self.assertFalse(is_danish_bank_holiday(date(2023, 4, 9)))  # Sunday

    def test_weekdays(self):
        # Test regular weekdays
        self.assertTrue(is_danish_bank_holiday(date(2023, 4, 11)))  # Tuesday
        self.assertTrue(is_danish_bank_holiday(date(2023, 4, 12)))  # Wednesday

if __name__ == '__main__':
    unittest.main()