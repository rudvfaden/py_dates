# Danish Banking Holidays

This package provides functions to calculate Danish banking holidays.

## Installation

```bash
pip install danish_holidays
```

## usage

```python
from danish_banking_holidays.bankdag import danish_bank_holiday, is_danish_bank_holiday, danish_bank_holiday_after, danish_bank_holiday_before
from datetime import date

holidays = danish_bank_holiday(2023)
for holiday, dates in holidays.items():
    print(f"{holiday}: {dates}")


# Define the date for which you want to check if it's a Danish bank holiday
target_date_1 = date(2024, 11, 7)
is_danish_bank_holiday = is_danish_bank_holiday(target_date_1)
print(f"Is {target_date_1} a Danish bank holiday? {is_danish_bank_holiday}")

# Define the second date for checking the next Danish bank holiday after it
target_date_2 = date(2024, 11, 9)
danish_bank_holiday_after = danish_bank_holiday_after(target_date_2)
print(
    f"The next Danish bank holiday after {target_date_2} is on {danish_bank_holiday_after}")

# Define the same second date for checking the previous Danish bank holiday before it
danish_bank_holiday_before = danish_bank_holiday_before(target_date_2)
print(
    f"The last Danish bank holiday before {target_date_2} was on {danish_bank_holiday_before}")
```
