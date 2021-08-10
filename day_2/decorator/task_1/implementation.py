import time
from day_2.common import factorial


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(*args):
        start_time = time.perf_counter_ns()
        result = func(*args)
        runtime = time.perf_counter_ns() - start_time
        print(f'Время исполнения {func.__name__}: {runtime} нс')
        return result

    return wrapper


if __name__ == "__main__":
    runtime_factorial = time_execution(factorial)
    runtime_factorial(0)
    runtime_factorial(77)
    runtime_factorial(4520)
