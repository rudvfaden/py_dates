from datetime import datetime

def easter(date_str, input_format='%Y-%m-%d'):
    try:
        date_obj = datetime.strptime(date_str, input_format)
        year = date_obj.year
        a = year % 19
        b = year // 100
        c = year % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        n = (h + l - 7 * m + 114) // 31
        p = (h + l - 7 * m + 114) % 31
        easter_date = datetime(year=year, month=n, day=p + 1)
        return easter_date
    except ValueError as e:
        return str(e)

# Example usage
paaske = easter('2018-06-28')
print(paaske)  # Output: 2024-03-31 00:00:00
print(paaske.date())