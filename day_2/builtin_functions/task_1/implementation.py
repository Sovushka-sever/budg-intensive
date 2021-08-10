from day_2.common import MyException


class Value:
    def __init__(self, val=0):
        self.value = val

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        try:
            return self.value / other
        except Exception:
            raise MyException
