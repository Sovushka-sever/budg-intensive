def fib(n):
    """
    Функция, которая возвращает n-ое число последовательности Фибоначчи
    """
    number_1, number_2 = 1, 1

    if not isinstance(n, int):
        raise TypeError('Число n должно быть целым')

    for _ in range(n):
        yield number_1
        number_1, number_2 = number_2, number_1 + number_2
