def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """

    if month in ['январь', 'март', 'май', 'июль',
                 'август', 'октябрь', 'декабрь']:
        number_of_days = 31
    elif month in ['апрель', 'июнь', 'сентябрь', 'ноябрь']:
        number_of_days = 30
    elif month == 'февраль':
        number_of_days = 28
    else:
        number_of_days = 0

    return number_of_days
