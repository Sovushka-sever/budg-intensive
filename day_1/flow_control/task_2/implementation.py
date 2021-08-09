def convert_temperature(value, to_scale):
    """Конвертирует температуру в нужную системы счисления

    Args:
        value: значение температуры
        to_scale: система счисления, в которую нужно конвертировать значение

    Returns: значение как результат конвертации
    """
    if value == '' or value is None:
        raise ValueError("Temperature value cannot be empty.")

    if to_scale == 'C':
        temperature = (5 / 9) * (int(value) - 32)
    elif to_scale == 'F':
        temperature = (9 / 5) * int(value) + 32
    else:
        temperature = value

    return int(temperature)
