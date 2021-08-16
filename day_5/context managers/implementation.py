from contextlib import contextmanager


@contextmanager
def open_file(file_name):
    """Менеджер контекста, по умолчанию печатает количество строк в файле."""
    f = open(file_name, 'r')
    try:
        count = sum(1 for _ in f)
        print(f'Количество строк в файле:{count + 1}')
        yield f

    finally:
        f.close()


if __name__ == '__main__':
    with open_file('log.txt') as f:
        print('Файл открыт для чтения')
