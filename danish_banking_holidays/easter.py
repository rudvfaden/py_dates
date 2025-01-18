from datetime import date


def easter(year: int) -> date:
    """Calculate the date of Easter Sunday for a given year.

        Args:
            year (int): The year for which to calculate Easter Sunday.

        Returns:
            date: The date of Easter Sunday for the given year.

        Example:
            >>> easter(2023)
            datetime.date(2023, 4, 9)
    """
    try:
        a = year % 19
        b = year // 100
        c = year % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        ll = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * ll) // 451
        n = (h + ll - 7 * m + 114) // 31
        p = (h + ll - 7 * m + 114) % 31
        easter_date = date(year=year, month=n, day=p + 1)
        return easter_date
    except ValueError as e:
        return str(e)
