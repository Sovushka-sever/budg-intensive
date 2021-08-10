def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """

    func.__invocation_count__ = 0

    def wrapper():
        func.__invocation_count__ += 1
        print(f'{func.__name__} была вызвана: {func.__invocation_count__} раз')
        return func.__invocation_count__

    return wrapper



