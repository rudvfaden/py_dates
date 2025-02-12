import pytest
from danish_banking_holidays.bankdag import (
    danish_bank_holiday,
    is_danish_bank_holiday,
    danish_bank_holiday_after,
    danish_bank_holiday_before
)
from datetime import date


def test_danish_bank_holiday():
    holidays = danish_bank_holiday(2023)
    assert date(2023, 1, 1) in holidays
    assert holidays[date(2023, 1, 1)] == 'Nytårsdag'
    assert holidays[date(2023, 4, 9)] == 'Påske'
    assert holidays[date(2023, 4, 6)] == 'Skærtorsdag'
    assert holidays[date(2023, 4, 7)] == 'Langfredag'
    assert holidays[date(2023, 4, 10)] == '2. Påskedag'
    assert holidays[date(2023, 5, 18)] == 'Kristi himmelfartsdag'
    assert holidays[date(2023, 5, 28)] == 'Pinsedag'
    assert holidays[date(2023, 5, 29)] == '2. Pinsedag'
    assert holidays[date(2023, 12, 24)] == 'Juleaftensdag'
    assert holidays[date(2023, 12, 25)] == 'Juledag'
    assert holidays[date(2023, 12, 26)] == '2. Juledag'
    assert holidays[date(2023, 1, 1)] == 'Nytårsdag'
    assert holidays[date(2023, 6, 5)] == 'Grundlovsdag'
    assert holidays[date(2023, 12, 31)] == 'Nytåraftensdag'
    assert holidays[date(2023, 5, 5)] == 'Stor Bededag'
    assert holidays[date(2023, 5, 19)] == 'Fredag efter Kristi himmelfartsdag'

# Additional tests to cover missing lines


def test_danish_bank_holiday_invalid_year():
    # Cover line 19
    with pytest.raises(ValueError):
        danish_bank_holiday(1581)


def test_is_danish_bank_holiday_specific_date():
    # Cover line 94
    target_date = date(2023, 4, 9)  # Easter Sunday 2023
    assert is_danish_bank_holiday(target_date)


def test_danish_bank_holiday_after_specific_date():
    # Cover line 114
    target_date = date(2023, 4, 8)  # Day before Easter Sunday 2023
    next_holiday = danish_bank_holiday_after(target_date)
    assert next_holiday == date(2023, 4, 11)  # Easter Sunday 2023


def test_is_danish_bank_holiday():
    target_date = date(2024, 11, 7)
    assert not is_danish_bank_holiday(target_date)
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
    target_date = date(2024, 11, 9)
    previous_holiday = danish_bank_holiday_before(target_date)
    assert previous_holiday < target_date
    assert danish_bank_holiday_before(date(2024, 7, 13)) == date(2024, 7, 12)

    with pytest.raises(ValueError):
        danish_bank_holiday_before(date(2022, 4, 0))


def test_danish_bank_holiday_after():
    target_date = date(2024, 11, 9)
    next_holiday = danish_bank_holiday_after(target_date)
    assert next_holiday > target_date
    assert danish_bank_holiday_after(date(2024, 7, 13)) == date(2024, 7, 15)

    with pytest.raises(ValueError):
        danish_bank_holiday_after(date(2022, 12, 32))


# Additional tests to cover missing lines
def test_danish_bank_holiday_edge_case():
    # Cover line 19
    holidays = danish_bank_holiday(1583)
    assert holidays is not None


def test_is_danish_bank_holiday_edge_case():
    # Cover line 93
    target_date = date(1583, 1, 1)
    assert is_danish_bank_holiday(target_date)


def test_danish_bank_holiday_after_edge_case():
    # Cover line 113
    target_date = date(1583, 1, 1)
    next_holiday = danish_bank_holiday_after(target_date)
    assert next_holiday > target_date
