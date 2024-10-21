from datetime import timedelta, date
from easter import easter
from bankdag import danish_bank_holiday, get_holidays
dato=date(2023,4,5)
year = dato.year
paaske = easter(year)

# combined_dict = {}
# for y in range(2025,2030):
#     yearly_dict = danish_bank_holiday(y)
#     combined_dict.update(yearly_dict)

# sorted_dict=dict(sorted(combined_dict.items(), key=lambda item: item[1]))
print(get_holidays(2101))
# for k,v in sorted_dict.items():
#     print(k,v)