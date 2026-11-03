from datetime import date

import pytest

from danish_banking_holidays import DanishBankingCalendar


@pytest.fixture
def calendar():
    return DanishBankingCalendar()


def test_calendar_get_holidays_2023(calendar):
    holidays = calendar.get_holidays(2023)
    assert date(2023, 1, 1) in holidays
    assert holidays[date(2023, 1, 1)] == "Nytårsdag"
    assert holidays[date(2023, 4, 6)] == "Skærtorsdag"
    assert holidays[date(2023, 4, 7)] == "Langfredag"
    assert holidays[date(2023, 4, 9)] == "Påskedag"
    assert holidays[date(2023, 4, 10)] == "2. Påskedag"
    assert holidays[date(2023, 5, 5)] == "Stor Bededag"
    assert holidays[date(2023, 5, 18)] == "Kristi himmelfartsdag"
    assert holidays[date(2023, 5, 19)] == "Fredag efter Kristi himmelfartsdag"
    assert holidays[date(2023, 5, 28)] == "Pinsedag"
    assert holidays[date(2023, 5, 29)] == "2. Pinsedag"
    assert holidays[date(2023, 6, 5)] == "Grundlovsdag"
    assert holidays[date(2023, 12, 24)] == "Juleaftensdag"
    assert holidays[date(2023, 12, 25)] == "Juledag"
    assert holidays[date(2023, 12, 26)] == "2. Juledag"
    assert holidays[date(2023, 12, 31)] == "Nytårsaftensdag"


def test_calendar_historical_rules(calendar):
    # Stor Bededag exists before 2024, abolished from 2024
    holidays_2023 = calendar.get_holidays(2023)
    assert any(name == "Stor Bededag" for name in holidays_2023.values())
    holidays_2024 = calendar.get_holidays(2024)
    assert not any(name == "Stor Bededag" for name in holidays_2024.values())

    # Fredag efter Kristi himmelfartsdag exists after 2007 (from 2008)
    holidays_2007 = calendar.get_holidays(2007)
    assert not any(name == "Fredag efter Kristi himmelfartsdag" for name in holidays_2007.values())
    holidays_2008 = calendar.get_holidays(2008)
    assert any(name == "Fredag efter Kristi himmelfartsdag" for name in holidays_2008.values())

    # Nytårsaftensdag exists after 2002 (from 2003)
    holidays_2002 = calendar.get_holidays(2002)
    assert date(2002, 12, 31) not in holidays_2002
    holidays_2003 = calendar.get_holidays(2003)
    assert holidays_2003[date(2003, 12, 31)] == "Nytårsaftensdag"


def test_calendar_invalid_year(calendar):
    with pytest.raises(ValueError, match="Year must be greater than or equal to 1583"):
        calendar.get_holidays(1582)

    with pytest.raises(ValueError, match="Year must be greater than or equal to 1583"):
        calendar.get_holidays("2023")  # type: ignore[arg-type]


def test_calendar_boundary_1583(calendar):
    holidays = calendar.get_holidays(1583)
    assert holidays is not None
    assert date(1583, 1, 1) in holidays
    assert calendar.is_holiday(date(1583, 1, 1))


def test_calendar_get_specific_holiday(calendar):
    # Lookup by name returns date
    assert calendar.get_holiday(2023, "Påskedag") == date(2023, 4, 9)
    assert calendar.get_holiday(2023, "påske") == date(2023, 4, 9)
    assert calendar.get_holiday(2023, "nytårsaftensdag") == date(2023, 12, 31)
    assert calendar.get_holiday(2023, "ikke en helligdag") is None


def test_calendar_get_holiday_name(calendar):
    assert calendar.get_holiday_name(date(2023, 12, 25)) == "Juledag"
    assert calendar.get_holiday_name(date(2023, 12, 10)) is None


def test_calendar_cache_mutability(calendar):
    holidays = calendar.get_holidays(2023)
    original_len = len(holidays)
    holidays.clear()
    assert len(holidays) == 0

    fresh_holidays = calendar.get_holidays(2023)
    assert len(fresh_holidays) == original_len
    assert date(2023, 12, 25) in fresh_holidays


def test_calendar_holiday_and_weekend_checks(calendar):
    # is_holiday: True for holidays and weekends
    assert calendar.is_holiday(date(2023, 4, 9))   # Easter Sunday
    assert calendar.is_holiday(date(2023, 12, 25)) # Christmas Day (Monday)
    assert calendar.is_holiday(date(2023, 4, 8))   # Saturday
    assert not calendar.is_holiday(date(2023, 4, 11)) # Regular Tuesday

    # is_bank_holiday: True only for official banking holidays, False for ordinary weekends
    assert calendar.is_bank_holiday(date(2023, 12, 25))
    assert calendar.is_bank_holiday(date(2023, 4, 9))
    assert not calendar.is_bank_holiday(date(2023, 4, 8))   # Normal Saturday
    assert not calendar.is_bank_holiday(date(2023, 4, 11))  # Normal Tuesday

    # is_weekend
    assert calendar.is_weekend(date(2023, 4, 8))   # Saturday
    assert calendar.is_weekend(date(2023, 4, 9))   # Sunday
    assert not calendar.is_weekend(date(2023, 4, 11)) # Tuesday

    # is_business_day
    assert calendar.is_business_day(date(2023, 4, 11))
    assert not calendar.is_business_day(date(2023, 4, 8))
    assert not calendar.is_business_day(date(2023, 12, 25))


def test_calendar_next_business_day(calendar):
    # Over weekend: Friday to Tuesday (Monday 2023-04-10 is Easter Monday)
    assert calendar.next_business_day(date(2023, 4, 7)) == date(2023, 4, 11)
    # Over Christmas: Christmas Eve to Wednesday Dec 27
    assert calendar.next_business_day(date(2023, 12, 24)) == date(2023, 12, 27)
    # Saturday to Monday
    assert calendar.next_business_day(date(2024, 7, 13)) == date(2024, 7, 15)

    # With include_current=True
    # On a business day (Tuesday), returns itself
    assert calendar.next_business_day(date(2023, 4, 11), include_current=True) == date(2023, 4, 11)
    # On a holiday/weekend, advances to next business day
    assert calendar.next_business_day(date(2023, 4, 7), include_current=True) == date(2023, 4, 11)


def test_calendar_previous_business_day(calendar):
    # Before Easter Monday lands on Wednesday 2023-04-05 (skips Maundy Thu & Good Fri)
    assert calendar.previous_business_day(date(2023, 4, 10)) == date(2023, 4, 5)
    # Before 2. Juledag lands on Friday Dec 22
    assert calendar.previous_business_day(date(2023, 12, 26)) == date(2023, 12, 22)
    # Saturday to Friday
    assert calendar.previous_business_day(date(2024, 7, 13)) == date(2024, 7, 12)

    # With include_current=True
    # On a business day, returns itself
    assert calendar.previous_business_day(date(2023, 4, 11), include_current=True) == date(2023, 4, 11)
    # On a holiday, moves to previous business day
    assert calendar.previous_business_day(date(2023, 12, 26), include_current=True) == date(2023, 12, 22)


def test_calendar_add_business_days(calendar):
    # Add positive days: Thursday before Easter to Tuesday after
    assert calendar.add_business_days(date(2023, 4, 6), 1) == date(2023, 4, 11)
    # Adding 3 business days from 2023-12-22 skips weekend and holidays 24-26, landing on 2023-12-29
    assert calendar.add_business_days(date(2023, 12, 22), 3) == date(2023, 12, 29)

    # Add zero days
    assert calendar.add_business_days(date(2023, 4, 6), 0) == date(2023, 4, 6)

    # Add negative days
    assert calendar.add_business_days(date(2023, 4, 11), -1) == date(2023, 4, 5)
