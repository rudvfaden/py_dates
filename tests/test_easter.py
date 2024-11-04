import pytest
from datetime import date
from danish_banking_holidays.easter import easter


@pytest.mark.parametrize("year, expected_date", [
    (2020, date(2020, 4, 12)),
    (2021, date(2021, 4, 4)),
    (2022, date(2022, 4, 17)),
    (2023, date(2023, 4, 9)),
    (2024, date(2024, 3, 31)),
])
def test_easter(year, expected_date):
    assert easter(year) == expected_date
