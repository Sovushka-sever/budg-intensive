from math import sqrt


def great_comprehension(list1, list2, list3):
    """
    Возвращает список с перемноженными элементами списков list1, list2 и list3 согласно условию
    """
    list_common = [(int(str(x)[0])+int(str(x)[-1]))*int(sqrt(y))*z
            for x in list1 if str(x)[0] == str(x)[-1] and len(str(x)) != 1
            for y in list2 if len(str(y)) == 3 and y % 2 == 0
            for z in list3 if z == 4 or z % 2 != 0]
    return list_common


list1 = [12, 2, 17, 44, 131]
list2 = [127, 69, 144, 0, 1024]
list3 = [8, 6, 5, 4, 7]
