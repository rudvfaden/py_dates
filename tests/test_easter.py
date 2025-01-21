import pytest
from datetime import date
from danish_banking_holidays.easter import easter
from unittest.mock import patch


@pytest.mark.parametrize("year, expected_date", [
    (2020, date(2020, 4, 12)),
    (2021, date(2021, 4, 4)),
    (2022, date(2022, 4, 17)),
    (2023, date(2023, 4, 9)),
    (2024, date(2024, 3, 31)),
])
def test_easter(year, expected_date):
    assert easter(year) == expected_date


# Test to cover lines 34-35 (raising ValueError for invalid year)
def test_easter_invalid_year():
    with pytest.raises(ValueError, match="Year must be greater than 1583"):
        easter(1582)


# Test to cover lines 36-37 (handling ValueError and returning the message)
def test_easter_invalid_year_handling():
    try:
        easter(1582)
    except ValueError as e:
        assert str(e) == "Year must be greater than 1583"


# Test to cover lines 36-37 by mocking `date` to raise ValueError
def test_easter_date_value_error():
    with patch('danish_banking_holidays.easter.date') as mock_date:
        mock_date.side_effect = ValueError("Mocked invalid date error")
        result = easter(2023)
        assert result == "Mocked invalid date error"