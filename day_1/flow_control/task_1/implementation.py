def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    start_number = 1000
    end_number = 2000

    numbers = []

    if start_number >= end_number:
        print('Range is set incorrectly')

    for number in range(start_number, end_number):
        if number % 7 == 0 and number % 5 != 0:
            numbers.append(number)

    return numbers


