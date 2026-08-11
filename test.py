from datetime import date

from danish_banking_holidays.calendar import DanishBankingCalendar

# Create a calendar instance
calendar = DanishBankingCalendar()

# Get all holidays for a year
holidays = calendar.get_holidays(2026)
for day, name in holidays.items():
    print(f"{name}: {day}")

print(30*'-')
# Check if a date is a holiday or weekend
is_holiday = calendar.is_holiday(date(2025, 12, 25))  # True for Christmas
print(f"Is Dec 25, 2025 a holiday? {is_holiday}")

print(30*'-')
# Get next business day after Christmas Eve
next_working_day = calendar.next_business_day(
    date(2025, 12, 24)
)  # Should skip holidays (24-26) and weekend (27-28) to land on Dec 29
print(f"Next business day after Dec 24, 2025 is {next_working_day}")
print(30*'-')
# Get previous business day before Christmas
prev_working_day = calendar.previous_business_day(
    date(2025, 12, 26)
)  # Should land on Dec 23
print(f"Previous business day before Dec 26, 2025 is {prev_working_day}")

print(30*'-')
# Add business days to a date
future_date = calendar.add_business_days(
    date(2025, 1, 1), 5
)  # Skips weekends and holidays (e.g. Nytårsdag)
print(f"5 business days after Jan 1, 2025 is {future_date}")

print(30*'-')
# Get holiday name
holiday_name = calendar.get_holiday_name(date(2025, 12, 25))
print(f"Holiday name for 2025-12-25: {holiday_name}")