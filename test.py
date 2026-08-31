from datetime import date

from danish_banking_holidays import DanishBankingCalendar

# Create a calendar instance
holidayCalendar = DanishBankingCalendar()

# find the first bankingday in a month
first_banking_day = holidayCalendar.next_business_day(date(2026, 8, 1))
print(f"First banking day in Aug 2026: {first_banking_day}")
print(30 * "-")

last_banking_day = holidayCalendar.previous_business_day(date(2026, 9, 1))
print(f"Last banking day in Aug 2026: {last_banking_day}")
print(30 * "-")

# Get all holidays for a year
holidays = holidayCalendar.get_holidays(2026)
for day, name in holidays.items():
    print(f"{name}: {day}")
    print(f"Is {day} a holiday? {holidayCalendar.is_holiday(day)}")
    print("*" * 30)

print(30 * "-")
# Check if a date is a holiday or weekend
is_holiday = holidayCalendar.is_holiday(date(2025, 12, 25))  # True for Christmas
print(f"Is Dec 25, 2025 a holiday? {is_holiday}")

print(30 * "-")
# Get next business day after Christmas Eve
next_working_day = holidayCalendar.next_business_day(
    date(2025, 12, 24)
)  # Should skip holidays (24-26) and weekend (27-28) to land on Dec 29
print(f"Next business day after Dec 24, 2025 is {next_working_day}")
print(30 * "-")
# Get previous business day before Christmas
prev_working_day = holidayCalendar.previous_business_day(
    date(2025, 12, 26)
)  # Should land on Dec 23
print(f"Previous business day before Dec 26, 2025 is {prev_working_day}")

print(30 * "-")
# Add business days to a date
future_date = holidayCalendar.add_business_days(
    date(2025, 1, 1), 5
)  # Skips weekends and holidays (e.g. Nytårsdag)
print(f"5 business days after Jan 1, 2025 is {future_date}")

print(30 * "-")
# Get holiday name
holiday_name = holidayCalendar.get_holiday_name(date(2025, 12, 25))
print(f"Holiday name for 2025-12-25: {holiday_name}")

# add business days in the past
furture_date = holidayCalendar.add_business_days(
    date(2025, 1, 1), 3
)  # Should land on Jan 6, 2025 (skipping Jan 1)
print(f"3 business days after Jan 1, 2025 is {furture_date}")