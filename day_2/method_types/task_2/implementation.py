from day_2.common import MyException


class ClassFather:
    registered_list = []

    def __init__(self):
        pass

    @classmethod
    def register(cls):
        if cls != ClassFather:
            cls.registered_list.append(cls)
        else:
            raise MyException

    def get_name(self):
        if self.__class__ in self.registered_list:
            return self._name
        else:
            raise MyException


class User1(ClassFather):
    _name = 'first_user'


class User2(ClassFather):
    _name = 'second_user'
