from time import sleep
from day_2.common import MyException


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """

    def function_call(func):

        def wrapper(*args):
            for _ in range(times):
                try:
                    result = func(*args)
                    break
                except Exception:
                    sleep(delay)
            else:
                raise MyException

            return result

        return wrapper

    return function_call

