# Danish Banking Holidays

A Python package for calculating Danish banking holidays and business days.

## Installation

```bash
pip install danish-banking-holidays
```

## Usage

```python
from danish_banking_holidays import DanishBankingCalendar
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
next_working_day = calendar.next_business_day(
    date(2023, 12, 24)
)  # Dec 27th (after Christmas)

# Get previous business day
prev_working_day = calendar.previous_business_day(date(2023, 12, 26))  # Dec 22nd

# Add business days to a date
future_date = calendar.add_business_days(
    date(2023, 1, 1), 5
)  # Skips weekends and holidays
```


