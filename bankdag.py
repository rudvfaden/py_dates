from easter import easter
from datetime import timedelta, date


def erDanskBankdag(date_obj):
    paaske = easter(date_obj.year)
    helligdag = [
        paaske,  # påske
        paaske + timedelta(days=-3),  # Skærtorsdag
        paaske + timedelta(days=-2),  # Langfredag
        paaske + timedelta(days=1),  # andenPåskedag
        paaske + timedelta(days=26) if date_obj.year < 2024 else None, # storeBededag
        paaske + timedelta(days=39),  # Kr_himmelfart
        paaske + timedelta(days=49),  # pinsedag
        paaske + timedelta(days=50) if date_obj.year>2007 else None,  # fredag efter kr_himmelfart
        paaske + timedelta(days=50),  # andenPinsedag
        date(date_obj.year, 12, 24),  # juleaftensdag
        date(date_obj.year, 12, 25),  # juledag
        date(date_obj.year, 12, 26),  # andenJuledag
        date(date_obj.year, 12, 31) if date_obj.year>2002 else None,  # nytaarsdag
        date(date_obj.year, 6, 5),  # grundlovsdag
    ]

    if date_obj in helligdag:
        return False

    if date_obj.weekday() >= 5:
        return False

    return True