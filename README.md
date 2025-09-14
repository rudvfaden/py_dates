# Danish Banking Holidays

A Python package for calculating Danish banking holidays and business days.

## Installation

```bash
pip install danish_holidays
```

## Usage

### New Interface (Recommended)

```python
from danish_banking_holidays.calendar import DanishBankingCalendar
from datetime import date

# Create a calendar instance
calendar = DanishBankingCalendar()

# Get all holidays for a year
holidays = calendar.get_holidays(2023)
for day, name in holidays.items():
    print(f"{name}: {day}")

# Check if a date is a holiday or weekend
is_holiday = calendar.is_holiday(date(2023, 12, 25))  # True for Christmas

# Get next business day
next_working_day = calendar.next_business_day(date(2023, 12, 24))  # Dec 27th (after Christmas)

# Get previous business day
prev_working_day = calendar.previous_business_day(date(2023, 12, 26))  # Dec 22nd

# Add business days to a date
future_date = calendar.add_business_days(date(2023, 1, 1), 5)  # Skips weekends and holidays
```

### Legacy Interface (Deprecated)

> Note: The following interface is deprecated and will be removed in version 1.0.0.
> Please migrate to the new DanishBankingCalendar class.

```python
from danish_banking_holidays.bankdag import danish_bank_holiday, is_danish_bank_holiday
from datetime import date

holidays = danish_bank_holiday(2023)
for day, name in holidays.items():
    print(f"{name}: {day}")
```

## Migration Guide

To migrate from the old interface to the new one:

1. Replace function imports with the DanishBankingCalendar class:
   ```python
   # Old
   from danish_banking_holidays.bankdag import danish_bank_holiday, is_danish_bank_holiday
   
   # New
   from danish_banking_holidays.calendar import DanishBankingCalendar
   ```

2. Create a calendar instance:
   ```python
   calendar = DanishBankingCalendar()
   ```

3. Update function calls:
   - `danish_bank_holiday(year)` → `calendar.get_holidays(year)`
   - `danish_bank_holiday(year, holiday_name)` → `calendar.get_holiday(year, holiday_name)`
   - `is_danish_bank_holiday(date)` → `calendar.is_holiday(date)`
   - `first_non_bank_holiday_before(date)` → `calendar.previous_business_day(date)`
   - `first_non_bank_holiday_after(date)` → `calendar.next_business_day(date)`


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
