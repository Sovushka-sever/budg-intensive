from day_2.common import MyException


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(arg):
        if arg is None or not isinstance(arg, int) or arg < 0:
            raise MyException
        return func(arg)
    return wrapper


def memoize_func(func):
    """
    Обертка, которая кэширует результат.
    """
    memo = dict()

    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]

    return wrapper
