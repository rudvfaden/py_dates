from easter import easter
from datetime import timedelta, date


def is_danish_bank_holiday(date_obj: date) -> bool:
    """Check if a given date is a Danish bank holiday.

        Args:
            date_obj (date): The date to check for being a Danish bank holiday.

        Returns:
            bool: True if the date is a Danish bank holiday, False otherwise.
    """
    if not isinstance(date_obj, date):
        raise TypeError("Input must be a `date` object.")

    paaske = easter(date_obj.year)
    helligdag = {
        # påske
        paaske,
        # Skærtorsdag
        paaske + timedelta(days=-3),
        # Langfredag
        paaske + timedelta(days=-2),
        # andenPåskedag
        paaske + timedelta(days=1),
        # storeBededag
        paaske + timedelta(days=26) if date_obj.year < 2024 else None,
        # Kr_himmelfart
        paaske + timedelta(days=39),
        # fredag efter kr_himmelfart
        paaske + timedelta(days=40) if date_obj.year > 2007 else None,
        # pinsedag
        paaske + timedelta(days=49),
        # andenPinsedag
        paaske + timedelta(days=50),
        # juleaftensdag
        date(date_obj.year, 12, 24),
        # juledag
        date(date_obj.year, 12, 25),
        # andenJuledag
        date(date_obj.year, 12, 26),
        # nytaarsdag
        date(date_obj.year, 12, 31) if date_obj.year > 2002 else None,
        # grundlovsdag
        date(date_obj.year, 6, 5)
    }

    if date_obj in helligdag or date_obj.weekday() > 4:
        return False

    return True


def danish_bank_holiday_before(date_obj: date) -> date:
    """Find the latest Danish bank holiday before a given date.

    Args:
        date_obj (date): The date to search for the bank holiday.

    Returns:
        date: The latest Danish bank holiday before the given date.

    Raises:
        TypeError: If the input is not a `date` object.
        ValueError: If no bank holiday is found within the range.
    """
    if not isinstance(date_obj, date):
        raise TypeError("Input must be a `date` object.")
    else:
        for i in range(9):
            date_to_check = date_obj + timedelta(-i)
            if is_danish_bank_holiday(date_to_check):
                return date_to_check
        raise ValueError("No bank holiday found within the range.")


def danish_bank_holiday_after(date_obj: date) -> date:
    """Find the next Danish bank holiday after a given date.

    Args:
        date_obj (date): The date to start searching from.

    Returns:
        date: The next Danish bank holiday date after the input date.

    Raises:
        TypeError: If the input is not a `date` object.
        ValueError: If no bank holiday is found within the range.
    """
    if not isinstance(date_obj, date):
        raise TypeError("Input must be a `date` object.")
    else:
        for i in range(9):
            date_to_check = date_obj + timedelta(i)
            if is_danish_bank_holiday(date_to_check):
                return date_to_check
        raise ValueError("No bank holiday found within the range.")