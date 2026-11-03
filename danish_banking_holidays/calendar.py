from datetime import date, timedelta
from functools import lru_cache

from .easter import easter

MIN_YEAR = 1583


@lru_cache(maxsize=128)
def _calculate_holidays(year: int) -> dict[date, str]:
    """Calculate holidays for a given year with caching."""
    if not isinstance(year, int) or year < MIN_YEAR:
        raise ValueError(f"Year must be greater than or equal to {MIN_YEAR}")

    easter_sunday = easter(year)
    holidays = {
        easter_sunday: "Påskedag",
        easter_sunday + timedelta(days=-3): "Skærtorsdag",
        easter_sunday + timedelta(days=-2): "Langfredag",
        easter_sunday + timedelta(days=1): "2. Påskedag",
        easter_sunday + timedelta(days=39): "Kristi himmelfartsdag",
        easter_sunday + timedelta(days=49): "Pinsedag",
        easter_sunday + timedelta(days=50): "2. Pinsedag",
        date(year, 12, 24): "Juleaftensdag",
        date(year, 12, 25): "Juledag",
        date(year, 12, 26): "2. Juledag",
        date(year, 1, 1): "Nytårsdag",
        date(year, 6, 5): "Grundlovsdag",
    }

    if year > 2002:
        holidays[date(year, 12, 31)] = "Nytårsaftensdag"

    if year < 2024:
        stor_bededag = easter_sunday + timedelta(days=26)
        holidays[stor_bededag] = "Stor Bededag"

    if year > 2007:
        fredag_efter_kristi = easter_sunday + timedelta(days=40)
        holidays[fredag_efter_kristi] = "Fredag efter Kristi himmelfartsdag"

    return dict(sorted(holidays.items()))


class DanishBankingCalendar:
    """A class to handle Danish banking holidays and business calculations."""

    MIN_YEAR = MIN_YEAR

    def __init__(self):
        """Initialize the Danish Banking Calendar."""

    def get_holidays(self, year: int) -> dict[date, str]:
        """Get all holidays for a given year."""
        return _calculate_holidays(year).copy()

    def get_holiday(self, year: int, holiday_name: str) -> date | None:
        """Get the date of a specific holiday by name for a given year."""
        name_lower = holiday_name.strip().lower()
        for dt, name in _calculate_holidays(year).items():
            if name.lower() == name_lower:
                return dt
            # Also support searching "påske" for "Påskedag"
            if name_lower == "påske" and name == "Påskedag":
                return dt
        return None

    def get_holiday_name(self, check_date: date) -> str | None:
        """Get the name of the holiday for a given date, if it is a holiday."""
        return _calculate_holidays(check_date.year).get(check_date)

    def is_holiday(self, check_date: date) -> bool:
        """Check if a given date is a holiday or weekend."""
        holidays = _calculate_holidays(check_date.year)
        return check_date in holidays or check_date.weekday() > 4

    def is_bank_holiday(self, check_date: date) -> bool:
        """Check if a given date is an official banking holiday (excluding regular weekends)."""
        holidays = _calculate_holidays(check_date.year)
        return check_date in holidays

    def is_weekend(self, check_date: date) -> bool:
        """Check if a given date falls on a weekend (Saturday or Sunday)."""
        return check_date.weekday() > 4

    def is_business_day(self, check_date: date) -> bool:
        """Check if a given date is an open business/banking day."""
        return not self.is_holiday(check_date)

    def next_business_day(self, from_date: date, include_current: bool = False) -> date:
        """Get the next business day after (or optionally on) the given date."""
        if include_current and not self.is_holiday(from_date):
            return from_date
        next_date = from_date + timedelta(days=1)
        while self.is_holiday(next_date):
            next_date += timedelta(days=1)
        return next_date

    def previous_business_day(self, from_date: date, include_current: bool = False) -> date:
        """Get the previous business day before (or optionally on) the given date."""
        if include_current and not self.is_holiday(from_date):
            return from_date
        prev_date = from_date + timedelta(days=-1)
        while self.is_holiday(prev_date):
            prev_date += timedelta(days=-1)
        return prev_date

    def add_business_days(self, start_date: date, days: int) -> date:
        """Add a number of business days to a date."""
        if days == 0:
            return start_date

        current_date = start_date
        step = 1 if days > 0 else -1
        remaining_days = abs(days)

        while remaining_days > 0:
            current_date += timedelta(days=step)
            if not self.is_holiday(current_date):
                remaining_days -= 1

        return current_date
