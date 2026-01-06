from danish_banking_holidays.calendar import DanishBankingCalendar
from datetime import date

# Create a calendar instance
calendar = DanishBankingCalendar()

# Get all holidays for a year
holidays = calendar.get_holidays(2025)
for day, name in holidays.items():
    print(f"{name}: {day}")

# Check if a date is a holiday or weekend
is_holiday = calendar.is_holiday(date(2025, 12, 10))  # True for Christmas
print(f"Is Dec 10, 2025 a holiday? {is_holiday}")

# Get next business day
next_working_day = calendar.next_business_day(
    date(2025, 12, 10)
)  # Dec 10th (after Christmas)
print(f"Next business day after Dec 10, 2025 is {next_working_day}")

# Get previous business day
prev_working_day = calendar.previous_business_day(date(2025, 12, 26))  # Dec 22nd
print(f"Previous business day before Dec 26, 2025 is {prev_working_day}")

# Add business days to a date
future_date = calendar.add_business_days(
    date(2025, 1, 1), 5
)  # Skips weekends and holidays
print(f"5 business days after Jan 1, 2025 is {future_date}")

print("Holiday name for 2025-12-25:", calendar.get_holiday_name(date(2025, 12, 8)))  # Christmas