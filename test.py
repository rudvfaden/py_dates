from datetime import date

from danish_banking_holidays import DanishBankingCalendar

# Create a calendar instance
holidayCalendar = DanishBankingCalendar()

# Find the first banking day in a month
first_banking_day = holidayCalendar.next_business_day(date(2026, 8, 1))
print(f"First banking day in Aug 2026: {first_banking_day}")
print(30 * "-")

# Find the last banking day in a month
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
# Check if a date is a holiday, weekend, or business day
check_date = date(2025, 12, 25)
print(f"Date: {check_date}")
print(f"Is holiday or weekend? {holidayCalendar.is_holiday(check_date)}")
print(f"Is official bank holiday? {holidayCalendar.is_bank_holiday(check_date)}")
print(f"Is business day? {holidayCalendar.is_business_day(check_date)}")

print(30 * "-")
# Get next business day after Christmas Eve
next_working_day = holidayCalendar.next_business_day(
    date(2025, 12, 24)
)  # Skips holidays (24-26) and weekend (27-28) to land on Dec 29
print(f"Next business day after Dec 24, 2025 is {next_working_day}")
print(30 * "-")

# Get previous business day before Christmas
prev_working_day = holidayCalendar.previous_business_day(
    date(2025, 12, 26)
)  # Lands on Dec 23
print(f"Previous business day before Dec 26, 2025 is {prev_working_day}")
print(30 * "-")

# Add business days to a date
future_date = holidayCalendar.add_business_days(
    date(2025, 1, 1), 5
)  # Skips weekends and holidays (e.g. Nytårsdag)
print(f"5 business days after Jan 1, 2025 is {future_date}")

# Add 3 business days
future_date_3 = holidayCalendar.add_business_days(
    date(2025, 1, 1), 3
)  # Lands on Jan 6, 2025
print(f"3 business days after Jan 1, 2025 is {future_date_3}")
print(30 * "-")

# Get holiday name
holiday_name = holidayCalendar.get_holiday_name(date(2025, 12, 25))
print(f"Holiday name for 2025-12-25: {holiday_name}")

# Get holiday date by name
easter_date = holidayCalendar.get_holiday(2025, "påskedag")
print(f"Easter Sunday in 2025: {easter_date}")
print(30 * "-")

# Validate boundary years
try:
    holidayCalendar.get_holidays(1582)
except ValueError as exc:
    print(f"Correctly caught error for year 1582: {exc}")

print(30 * "-")
print(holidayCalendar.get_holidays(2025))