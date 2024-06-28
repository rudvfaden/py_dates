from datetime import datetime


def easter(date_str, input_format='%Y-%m-%d', output_format='%B %d, %Y'):
    try:
        date_obj = datetime.strptime(date_str, input_format)
        year = date_obj.year
        a = year % 19
        b = year // 100
        c = year % 100
        d = b // 4
        e = b % 4
        f = (b+8) // 25
        g = (b-f+1) // 3
        h = (19*a+b-d-g+15) % 30
        i = c // 4
        k = c % 4
        l = (32+2*e+2*i-h-k) % 7
        m = (a+11*h+22*l) // 451
        n = (h+l-7*m+114) // 31
        p = (h+l-7*m+114) % 31
        easter = datetime(year=year, month=n, day=p+1)
        formatted_date = easter.strftime(output_format)
        return formatted_date
    except ValueError as e:
        return str(e)


paaske = easter('2024-06-28',output_format='%Y-%m-%d')
print(paaske)
