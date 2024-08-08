from datetime import timedelta, date
from easter import easter
from bankdag import danish_bank_holiday
dato=date(2023,4,5)
year = dato.year
paaske = easter(year)
helligdage=danish_bank_holiday(dato.year,date(2023, 4, 9))

print(danish_bank_holiday(
            2023,'Påske'), date(2023, 4, 9))