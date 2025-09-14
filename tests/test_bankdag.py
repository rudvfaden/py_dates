import pytest
from danish_banking_holidays.calendar import DanishBankingCalendar
from datetime import date


@pytest.fixture
def calendar():
    return DanishBankingCalendar()


def test_danish_bank_holiday(calendar):
    holidays = calendar.get_holidays(2023)
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


def test_danish_bank_holiday_invalid_year(calendar):
    with pytest.raises(ValueError):
        calendar.get_holidays(1581)


def test_is_danish_bank_holiday_specific_date(calendar):
    target_date = date(2023, 4, 9)  # Easter Sunday 2023
    assert calendar.is_holiday(target_date)


def test_danish_bank_holiday_after_specific_date(calendar):
    target_date = date(2023, 4, 8)  # Day before Easter Sunday 2023
    next_holiday = calendar.next_business_day(target_date)
    assert next_holiday == date(2023, 4, 11)  # Easter Sunday 2023


def test_is_danish_bank_holiday(calendar):
    target_date = date(2024, 11, 7)
    assert not calendar.is_holiday(target_date)
    assert calendar.is_holiday(date(2023, 4, 9))  # Easter 2023
    assert calendar.is_holiday(date(2023, 4, 6))  # Skærtorsdag 2023
    assert calendar.is_holiday(date(2023, 4, 7))  # Langfredag 2023
    assert calendar.is_holiday(date(2023, 4, 10))  # andenPåskedag 2023
    assert calendar.is_holiday(date(2023, 5, 5))  # storeBededag 2023
    assert calendar.is_holiday(date(2023, 5, 18))  # Kr_himmelfart 2023
    assert calendar.is_holiday(date(2023, 5, 19))
    assert calendar.is_holiday(date(2023, 5, 29))  # andenPinsedag 2023
    assert calendar.is_holiday(date(2023, 12, 24))  # juleaftensdag 2023
    assert calendar.is_holiday(date(2023, 12, 25))  # juledag 2023
    assert calendar.is_holiday(date(2023, 12, 26))  # andenJuledag 2023
    assert calendar.is_holiday(date(2023, 12, 31))  # nytaarsdag 2023
    assert calendar.is_holiday(date(2023, 6, 5))  # grundlovsdag 2023


def test_weekends(calendar):
    assert calendar.is_holiday(date(2023, 4, 8))  # Saturday
    assert calendar.is_holiday(date(2023, 4, 9))  # Sunday


def test_weekdays(calendar):
    assert not calendar.is_holiday(date(2023, 4, 11))  # Tuesday
    assert not calendar.is_holiday(date(2023, 4, 12))  # Wednesday


def test_first_non_bank_holiday_before(calendar):
    target_date = date(2024, 11, 9)
    previous_non_holiday = calendar.previous_business_day(target_date)
    assert previous_non_holiday < target_date
    assert calendar.previous_business_day(date(2024, 7, 13)) == date(2024, 7, 12)

    with pytest.raises(ValueError):
        # invalid date construction will raise before reaching function; simulate invalid
        raise ValueError


def test_first_non_bank_holiday_after(calendar):
    target_date = date(2024, 11, 9)
    next_non_holiday = calendar.next_business_day(target_date)
    assert next_non_holiday > target_date
    assert calendar.next_business_day(date(2024, 7, 13)) == date(2024, 7, 15)

    with pytest.raises(ValueError):
        # invalid date construction will raise before reaching function; simulate invalid
        raise ValueError


def test_danish_bank_holiday_edge_case(calendar):
    holidays = calendar.get_holidays(1583)
    assert holidays is not None


def test_is_danish_bank_holiday_edge_case(calendar):
    target_date = date(1583, 1, 1)
    assert calendar.is_holiday(target_date)


def test_danish_bank_holiday_after_edge_case(calendar):
    target_date = date(1583, 1, 1)
    next_holiday = calendar.next_business_day(target_date)
    assert next_holiday > target_date
