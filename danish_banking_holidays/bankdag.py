import warnings
from datetime import date, timedelta
from .calendar import DanishBankingCalendar
from functools import wraps

# Create a singleton instance of the calendar
_calendar = DanishBankingCalendar()

def _deprecation_warning(func):
    """Decorator to show deprecation warnings for old functions."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn(
            f"{func.__name__} is deprecated and will be removed in version 1.0.0. "
            f"Use DanishBankingCalendar class instead. "
            f"See documentation for migration guide.",
            DeprecationWarning,
            stacklevel=2
        )
        return func(*args, **kwargs)
    return wrapper

@_deprecation_warning
def danish_bank_holiday(year: int, hellidagNavn: str = None) -> dict:
    """Calculate Danish bank holidays for a given year.

    Deprecated: Use DanishBankingCalendar.get_holidays() or get_holiday() instead.

    Args:
        year (int): The year for which to calculate bank holidays.
        hellidagNavn (str, optional): The name of the holiday to retrieve.
        Defaults to None.

    Returns:
        dict: A dictionary of all bank holidays for the year.
    """
    if hellidagNavn:
        result = _calendar.get_holiday(year, hellidagNavn)
        return result if result else {"error": "Holiday not found"}
    return _calendar.get_holidays(year)


@_deprecation_warning
def is_danish_bank_holiday(date_obj: date) -> bool:
    """Check if a given date is a Danish bank holiday.

    Deprecated: Use DanishBankingCalendar.is_holiday() instead.

    Args:
        date_obj (date): The date to check for being a Danish bank holiday.

    Returns:
        bool: True if the date is a Danish bank holiday, False otherwise.
    """
    return _calendar.is_holiday(date_obj)


@_deprecation_warning
def first_non_bank_holiday_before(date_obj: date) -> date:
    """Find the first non-bank holiday before a given date.

    Deprecated: Use DanishBankingCalendar.previous_business_day() instead.

    Args:
        date_obj (date): The date to search for the non-bank holiday.

    Returns:
        date: The first non-bank holiday before the given date.
    """
    return _calendar.previous_business_day(date_obj)


@_deprecation_warning
def first_non_bank_holiday_after(date_obj: date) -> date:
    """Find the first non-bank holiday after a given date.

    Deprecated: Use DanishBankingCalendar.next_business_day() instead.

    Args:
        date_obj (date): The date to start searching from.

    Returns:
        date: The first non-bank holiday date after the input date.
        ValueError: If no non-bank holiday is found within the range.
    """
    for i in range(9):
        date_to_check = date_obj + timedelta(i)
        if not is_danish_bank_holiday(date_to_check):
            return date_to_check
