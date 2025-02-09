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
    if year < 1583:
        raise ValueError("Year must be greater than 1582")
    try:
        golden_number = year % 19
        century = year // 100
        year_in_century = year % 100
        century_leap_years = century // 4
        century_remainder = century % 4
        secular_correction = (century + 8) // 25
        lunar_correction = (century - secular_correction + 1) // 3
        moon_sync = (19 * golden_number + century -
                     century_leap_years - lunar_correction + 15) % 30
        century_years_div4 = year_in_century // 4
        year_remainder = year_in_century % 4
        day_offset = (32 + 2 * century_remainder + 2 *
                      century_years_div4 - moon_sync - year_remainder) % 7
        correction = (golden_number + 11 * moon_sync + 22 * day_offset) // 451
        month = (moon_sync + day_offset - 7 * correction + 114) // 31
        day = (moon_sync + day_offset - 7 * correction + 114) % 31
        easter_date = date(year=year, month=month, day=day + 1)
        return easter_date
    except ValueError as e:
        return str(e)
