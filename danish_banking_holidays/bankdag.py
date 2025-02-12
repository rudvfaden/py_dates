from .easter import easter
from datetime import timedelta, date


def danish_bank_holiday(year: int, hellidagNavn: str = None) -> dict:
    """Calculate Danish bank holidays for a given year.

    Args:
        year (int): The year for which to calculate bank holidays.
        hellidagNavn (str, optional): The name of the holiday to retrieve.
        Defaults to None.

    Returns:
        dict: A dictionary of all bank holidays for the year.
    """
    if not isinstance(year, int) or year < 1582:
        raise ValueError("Year must be a valid positive integer larger\
            than 1582 .")

    paaske = easter(year)
    helligdag = {
        paaske: "Påske",
        paaske + timedelta(days=-3): "Skærtorsdag",
        paaske + timedelta(days=-2): "Langfredag",
        paaske + timedelta(days=1): "2. Påskedag",
        paaske + timedelta(days=39): "Kristi himmelfartsdag",
        paaske + timedelta(days=49): "Pinsedag",
        paaske + timedelta(days=50): "2. Pinsedag",
        date(year, 12, 24): "Juleaftensdag",
        date(year, 12, 25): "Juledag",
        date(year, 12, 26): "2. Juledag",
        date(year, 1, 1): "Nytårsdag",
        date(year, 6, 5): "Grundlovsdag"
    }

    if year > 2002:
        helligdag[date(year, 12, 31)] = "Nytåraftensdag"

    if year < 2024:
        storBededag = paaske + timedelta(days=26)
        helligdag[storBededag] = "Stor Bededag"
    if year > 2007:
        fredagEfterKristiHimmelfartsdag = paaske + timedelta(days=40)
        helligdag[fredagEfterKristiHimmelfartsdag] =\
            "Fredag efter Kristi himmelfartsdag"
    # If hellidagNavn is provided, check if it exists in the holidays
    if hellidagNavn:
        for dt, name in helligdag.items():
            if name.lower() == hellidagNavn.lower():
                return {dt: name}
        return {"error": "Holiday not found"}

    # If no hellidagNavn is provided, return the entire dictionary
    sorted_helligdag = dict(sorted(helligdag.items()))
    return sorted_helligdag


def is_danish_bank_holiday(date_obj: date) -> bool:
    """Check if a given date is a Danish bank holiday.

        Args:
            date_obj (date): The date to check for being a Danish bank holiday.

        Returns:
            bool: True if the date is a Danish bank holiday, False otherwise.
    """
    holidays = danish_bank_holiday(date_obj.year)
    if date_obj in holidays or date_obj.weekday() > 4:
        return True
    return False


def danish_bank_holiday_before(date_obj: date) -> date:
    """Find the latest Danish bank holiday before a given date.

    Args:
        date_obj (date): The date to search for the bank holiday.

    Returns:
        date: The latest Danish bank holiday before the given date.

    Raises:
        ValueError: If no bank holiday is found within the range.
    """
    for i in range(9):
        date_to_check = date_obj + timedelta(-i)
        if is_danish_bank_holiday(date_to_check) is False:
            return date_to_check
    raise ValueError("No bank holiday found within the range.")


def danish_bank_holiday_after(date_obj: date) -> date:
    """Find the next Danish bank holiday after a given date.

    Args:
        date_obj (date): The date to start searching from.

    Returns:
        date: The next Danish bank holiday date after the input date.

    Raises:
        ValueError: If no bank holiday is found within the range.
    """
    for i in range(9):
        date_to_check = date_obj + timedelta(i)
        if is_danish_bank_holiday(date_to_check) is False:
            return date_to_check
    raise ValueError("No bank holiday found within the range.")
