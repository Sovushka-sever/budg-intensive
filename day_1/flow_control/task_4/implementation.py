from datetime import date


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    year = some_date.year
    month = some_date.month
    day = some_date.day

    if year % 400 == 0 or year % 4 == 0 and month == 2:
        next_data = date(year, month, day + 1)
    elif month == 2 and day == 28:
        next_data = date(year, month + 1, 1)
    elif month == 12 and day == 31:
        next_data = date(year + 1, 1, 1)
    elif day == 31:
        next_data = date(year, month + 1, 1)
    elif day == 30 and month in [4, 6, 9, 11]:
        next_data = date(year, month + 1, 1)
    else:
        next_data = date(year, month, day + 1)

    return next_data
