"""
Что будет выведено после выполнения кода? Почему?
"""
x = 42


def some_func():
    global x
    x = x + 1
    print(x)


some_func()
print(x)

"""
После выполнения кода будет выведено: 
43
43
В коде существует два объявления переменной: 
- глобальной области (х=42)
- локальной области (непосредственно в функции some_func)
после того как глобальная переменная становится доступной в функции, 
то ей было установлено другое значение (х=43), 
которое и было выведено на экран: 
- print, который в функции some_func
- print(x)
"""