import pytest

from datetime import date
from danish_banking_holidays.bankdag import (
    danish_bank_holiday,
    is_danish_bank_holiday,
    danish_bank_holiday_before,
    danish_bank_holiday_after
)


def test_danish_bank_holiday():
    assert danish_bank_holiday(2023, 'Påske') == date(2023, 4, 9)
    assert danish_bank_holiday(2023, 'Skærtorsdag') == date(2023, 4, 6)
    assert danish_bank_holiday(2023, 'Langfredag') == date(2023, 4, 7)
    assert danish_bank_holiday(2023, '2. Påskedag') == date(2023, 4, 10)
    assert danish_bank_holiday(
        2023, 'Kristi himmelfartsdag') == date(2023, 5, 18)
    assert danish_bank_holiday(2023, 'Pinsedag') == date(2023, 5, 28)
    assert danish_bank_holiday(2023, '2. Pinsedag') == date(2023, 5, 29)
    assert danish_bank_holiday(2023, 'Juleaftensdag') == date(2023, 12, 24)
    assert danish_bank_holiday(2023, 'Juledag') == date(2023, 12, 25)
    assert danish_bank_holiday(2023, '2. Juledag') == date(2023, 12, 26)
    assert danish_bank_holiday(2023, 'Nytårsdag') == date(2023, 1, 1)
    assert danish_bank_holiday(2023, 'Grundlovsdag') == date(2023, 6, 5)
    assert danish_bank_holiday(2023, 'Nytåraftensdag') == date(2023, 12, 31)
    assert danish_bank_holiday(2023, 'Stor Bededag') == date(2023, 5, 5)
    assert danish_bank_holiday(
        2023, 'Fredag efter Kristi himmelfartsdag') == date(2023, 5, 19)


def test_bank_holidays():
    assert is_danish_bank_holiday(date(2023, 4, 9))  # Easter 2023
    assert is_danish_bank_holiday(date(2023, 4, 6))  # Skærtorsdag 2023
    assert is_danish_bank_holiday(date(2023, 4, 7))  # Langfredag 2023
    assert is_danish_bank_holiday(date(2023, 4, 10))  # andenPåskedag 2023
    assert is_danish_bank_holiday(date(2023, 5, 5))  # storeBededag 2023
    assert is_danish_bank_holiday(date(2023, 5, 18))  # Kr_himmelfart 2023
    # fredag efterKr_himmelfart 2023
    assert is_danish_bank_holiday(date(2023, 5, 19))
    assert is_danish_bank_holiday(date(2023, 5, 29))  # andenPinsedag 2023
    assert is_danish_bank_holiday(date(2023, 12, 24))  # juleaftensdag 2023
    assert is_danish_bank_holiday(date(2023, 12, 25))  # juledag 2023
    assert is_danish_bank_holiday(date(2023, 12, 26))  # andenJuledag 2023
    assert is_danish_bank_holiday(date(2023, 12, 31))  # nytaarsdag 2023
    assert is_danish_bank_holiday(date(2023, 6, 5))  # grundlovsdag 2023


def test_weekends():
    assert is_danish_bank_holiday(date(2023, 4, 8))  # Saturday
    assert is_danish_bank_holiday(date(2023, 4, 9))  # Sunday


def test_weekdays():
    assert not is_danish_bank_holiday(date(2023, 4, 11))  # Tuesday
    assert not is_danish_bank_holiday(date(2023, 4, 12))  # Wednesday


def test_danish_bank_holiday_before():
    assert danish_bank_holiday_before(date(2024, 7, 13)) == date(2024, 7, 12)

    with pytest.raises(ValueError):
        danish_bank_holiday_before(date(2022, 4, 0))


def test_danish_bank_holiday_after():
    assert danish_bank_holiday_after(date(2024, 7, 13)) == date(2024, 7, 15)

    with pytest.raises(ValueError):
        danish_bank_holiday_after(date(2022, 12, 32))
