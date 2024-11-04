# Danish Banking Holidays

This package provides functions to calculate Danish banking holidays.

## Installation

```bash
pip install danish_holidays
```

## usage

```python
from danish_holidays.holidays import get_danish_banking_holidays

holidays = get_danish_banking_holidays(2023)
for holiday, date in holidays.items():
    print(f"{holiday}: {date}")
```
