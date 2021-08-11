"""
Посмотрите сколько памяти занимают следующие объекты.
Сколько будет занимать памяти список с двумя элементами после добавления в него
еще одно элемента с помощью append? Почему?
"""

first_tuple = (1, 2)
second_tuple = (1, 2, 3)
first_list = [1, 2]
second_list = [1, 2, 3]
first_list.append(3)

if __name__ == "__main__":
    print(first_tuple.__sizeof__())  # 40
    print(second_tuple.__sizeof__())  # 48
    print(first_list.__sizeof__())  # 56
    print(second_list.__sizeof__())  # 104
    print(first_list.__sizeof__())  # 104


"""
После добавления нового элемента 
список будет занимать больше памяти, чем если бы мы сразу объявили список с этим элементом.
Это из-за того, что часть этой памяти резервируется под возможные последующие изменения.
"""