from datetime import date

import pytest

from danish_banking_holidays import DanishBankingCalendar


@pytest.fixture
def calendar():
    return DanishBankingCalendar()


def test_calendar_get_holidays(calendar):
    holidays = calendar.get_holidays(2023)
    assert date(2023, 1, 1) in holidays
    assert holidays[date(2023, 1, 1)] == "Nytårsdag"
    assert holidays[date(2023, 4, 9)] == "Påske"
    assert holidays[date(2023, 4, 6)] == "Skærtorsdag"
    assert holidays[date(2023, 4, 7)] == "Langfredag"
    assert holidays[date(2023, 4, 10)] == "2. Påskedag"
    assert holidays[date(2023, 5, 18)] == "Kristi himmelfartsdag"
    assert holidays[date(2023, 5, 28)] == "Pinsedag"
    assert holidays[date(2023, 5, 29)] == "2. Pinsedag"
    assert holidays[date(2023, 12, 24)] == "Juleaftensdag"
    assert holidays[date(2023, 12, 25)] == "Juledag"
    assert holidays[date(2023, 12, 26)] == "2. Juledag"
    assert holidays[date(2023, 6, 5)] == "Grundlovsdag"
    assert holidays[date(2023, 12, 31)] == "Nytåraftensdag"
    assert holidays[date(2023, 5, 5)] == "Stor Bededag"
    assert holidays[date(2023, 5, 19)] == ("Fredag efter Kristi himmelfartsdag")


def test_calendar_invalid_year(calendar):
    with pytest.raises(ValueError):
        calendar.get_holidays(1582)
    with pytest.raises(ValueError):
        calendar.get_holidays(2100)


def test_calendar_get_specific_holiday(calendar):
    result = calendar.get_holiday(2023, "påske")
    assert result is not None
    assert date(2023, 4, 9) in result
    assert result[date(2023, 4, 9)] == "Påske"

    result = calendar.get_holiday(2023, "invalid holiday")
    assert result is None


def test_calendar_get_holiday_name(calendar):
    # Test valid holiday
    name = calendar.get_holiday_name(date(2023, 12, 25))
    assert name == "Juledag"

    # Test non-holiday
    name = calendar.get_holiday_name(date(2023, 12, 10))
    assert name is None


def test_calendar_cache_mutability(calendar):
    holidays = calendar.get_holidays(2023)
    original_len = len(holidays)
    # Mutate the returned dictionary
    holidays.clear()
    assert len(holidays) == 0

    # Ensure next call still returns the full calendar
    fresh_holidays = calendar.get_holidays(2023)
    assert len(fresh_holidays) == original_len
    assert date(2023, 12, 25) in fresh_holidays


def test_calendar_is_holiday(calendar):
    assert calendar.is_holiday(date(2023, 4, 9))  # Easter Sunday
    assert calendar.is_holiday(date(2023, 12, 25))  # Christmas
    assert calendar.is_holiday(date(2023, 4, 8))  # Saturday
    assert not calendar.is_holiday(date(2023, 4, 11))  # Regular Tuesday


def test_calendar_next_business_day(calendar):
    # Test over weekend: Friday to Tuesday (Monday is Easter Monday)
    assert calendar.next_business_day(date(2023, 4, 7)) == date(2023, 4, 11)
    # Test over holiday: Christmas Eve to working day after Christmas
    assert calendar.next_business_day(date(2023, 12, 24)) == date(2023, 12, 27)


def test_calendar_previous_business_day(calendar):
    # Test over weekend
    # The implementation returns the first prior non-holiday business day,
    # which for Easter Monday 2023 is Wednesday 2023-04-05.
    assert calendar.previous_business_day(date(2023, 4, 10)) == date(2023, 4, 5)
    # Test over holiday: Christmas to last working day before
    assert calendar.previous_business_day(date(2023, 12, 26)) == date(2023, 12, 22)


def test_calendar_add_business_days(calendar):
    # Add positive days: Thursday before Easter to Tuesday after
    assert calendar.add_business_days(date(2023, 4, 6), 1) == date(2023, 4, 11)
    # Adding 3 business days from 2023-12-22 skips weekend and the 24-26
    # holidays, landing on 2023-12-29.
    assert calendar.add_business_days(date(2023, 12, 22), 3) == date(2023, 12, 29)

    # Add zero days
    assert calendar.add_business_days(date(2023, 4, 6), 0) == date(2023, 4, 6)

    # Add negative days
    assert calendar.add_business_days(date(2023, 4, 11), -1) == date(2023, 4, 5)
