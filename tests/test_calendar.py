import pytest
from datetime import date
from danish_banking_holidays.calendar import DanishBankingCalendar


@pytest.fixture
def calendar():
    return DanishBankingCalendar()


def test_calendar_get_holidays(calendar):
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
    assert holidays[date(2023, 6, 5)] == 'Grundlovsdag'
    assert holidays[date(2023, 12, 31)] == 'Nytåraftensdag'
    assert holidays[date(2023, 5, 5)] == 'Stor Bededag'
    assert holidays[date(2023, 5, 19)] == 'Fredag efter Kristi himmelfartsdag'


def test_calendar_invalid_year(calendar):
    with pytest.raises(ValueError):
        calendar.get_holidays(1581)
    with pytest.raises(ValueError):
        calendar.get_holidays(2100)


def test_calendar_get_specific_holiday(calendar):
    result = calendar.get_holiday(2023, "påske")
    assert result is not None
    assert date(2023, 4, 9) in result
    assert result[date(2023, 4, 9)] == 'Påske'

    result = calendar.get_holiday(2023, "invalid holiday")
    assert result is None


def test_calendar_is_holiday(calendar):
    assert calendar.is_holiday(date(2023, 4, 9))  # Easter Sunday
    assert calendar.is_holiday(date(2023, 12, 25))  # Christmas
    assert calendar.is_holiday(date(2023, 4, 8))  # Saturday
    assert not calendar.is_holiday(date(2023, 4, 11))  # Regular Tuesday


def test_calendar_next_business_day(calendar):
    # Test over weekend
    assert calendar.next_business_day(date(2023, 4, 7)) == date(2023, 4, 11)  # Friday to Tuesday (Monday is Easter Monday)
    # Test over holiday
    assert calendar.next_business_day(date(2023, 12, 24)) == date(2023, 12, 27)  # Christmas Eve to first working day after Christmas


def test_calendar_previous_business_day(calendar):
    # Test over weekend
    # The implementation returns the first prior non-holiday business day (skipping all holidays),
    # which for Easter Monday 2023 is Wednesday 2023-04-05.
    assert calendar.previous_business_day(date(2023, 4, 10)) == date(2023, 4, 5)
    # Test over holiday
    assert calendar.previous_business_day(date(2023, 12, 26)) == date(2023, 12, 22)  # Christmas to last working day before


def test_calendar_add_business_days(calendar):
    # Add positive days
    assert calendar.add_business_days(date(2023, 4, 6), 1) == date(2023, 4, 11)  # Thursday before Easter to Tuesday after
    # Adding 3 business days from 2023-12-22 skips weekend and the 24-26 holidays,
    # landing on 2023-12-29 with the current semantics.
    assert calendar.add_business_days(date(2023, 12, 22), 3) == date(2023, 12, 29)  # Before Christmas

    # Add zero days
    assert calendar.add_business_days(date(2023, 4, 6), 0) == date(2023, 4, 6)

    # Add negative days
    # With current semantics the previous business day before 2023-04-11 is 2023-04-05
    assert calendar.add_business_days(date(2023, 4, 11), -1) == date(2023, 4, 5)  # Tuesday after Easter to previous business day