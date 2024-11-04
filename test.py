from danish_banking_holidays.bankdag import danish_bank_holiday

holidays = danish_bank_holiday(2023)
for holiday, date in holidays.items():
    print(f"{holiday}: {date}")
