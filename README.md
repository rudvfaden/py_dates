# Danish Banking Holidays

A Python package for calculating Danish banking holidays, weekends, and business days.

## Installation

```bash
pip install danish-banking-holidays
```

## Features

- Accurate calculations of all Danish banking holidays (*banklukkedage*).
- Historical awareness (e.g. abolition of *Store Bededag* from 2024, inclusion of Friday after Ascension Day from 2008, New Year's Eve from 2003).
- Business day arithmetic: next/previous banking day, roll forward, adding/subtracting business days.
- 100% test coverage and zero external dependencies.

## Usage

```python
from datetime import date
from danish_banking_holidays import DanishBankingCalendar

# Create a calendar instance
calendar = DanishBankingCalendar()

# Get all holidays for a year (returns a dict[date, str])
holidays = calendar.get_holidays(2024)
for day, name in holidays.items():
    print(f"{name}: {day}")

# Check day types
calendar.is_holiday(date(2024, 12, 25))       # True (holiday or weekend)
calendar.is_bank_holiday(date(2024, 12, 25))  # True (official bank holiday)
calendar.is_weekend(date(2024, 12, 28))       # True (Saturday)
calendar.is_business_day(date(2024, 12, 27))  # True (open banking day)

# Look up holiday by name or date
easter_date = calendar.get_holiday(2024, "Påskedag")       # date(2024, 3, 31)
name = calendar.get_holiday_name(date(2024, 12, 25))      # "Juledag"

# Business day navigation
next_day = calendar.next_business_day(date(2024, 12, 24))  # Dec 27th (after Christmas)
prev_day = calendar.previous_business_day(date(2024, 12, 27))  # Dec 23rd

# Add or subtract business days
future_date = calendar.add_business_days(date(2024, 1, 1), 5)  # Skips weekends and holidays
```

## Requirements

Python `>= 3.10`
