def return_errors(filename):
    """
    Функция, которая возвращает строки из лога со словом error
    """
    with open(filename) as file:
        for line in file:
            if "error" in line.lower():
                yield line


if __name__ == '__main__':
    count = 0
    for line in return_errors('log.txt'):
        print(line)
        count += 1
    print(f'Количество строк со словом error: {count}')
