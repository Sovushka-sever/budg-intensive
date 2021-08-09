"""
Что будет выведено после выполнения кода? Почему?
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)

"""
После выполнения кода будет выведено: 
3
3
т.к. даже то, что  в функцию  print_msg передали аргумент 9, 
для функции printer не имело никакого значения из-за nonlocal, 
который учитывает переменные в ближайшей заключающей области, исключая глобальные значения,
в итоге number = 3, который был выведен и из функции printer и из print(number) в print_msg
"""