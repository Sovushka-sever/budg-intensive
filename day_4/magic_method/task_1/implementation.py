class Multiplier:

    def __init__(self, value) -> None:
        super().__init__()


class Hundred(Multiplier):
    """Множитель на 100"""

    def __init__(self, value):
        self.value_hundred = value * 100

    def get_value(self):
        return self.value_hundred

    def __add__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Hundred(self.value_hundred + other.get_value())
        else:
            result = Hundred(self.value_hundred + other)

        return result

    def __sub__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Hundred(self.value_hundred - other.get_value())
        else:
            result = Hundred(self.value_hundred - other)

        return result

    def __mul__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Hundred(self.value_hundred * other.get_value())
        else:
            result = Hundred(self.value_hundred * other)

        return result

    def __truediv__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Hundred(self.value_hundred / other.get_value())
        else:
            result = Hundred(self.value_hundred + other)

        return result


class Thousand(Multiplier):
    """Множитель на 1 000"""

    def __init__(self, value):
        self.value_thousand = value * 1_000

    def get_value(self):
        return self.value_thousand

    def __add__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Thousand(self.value_thousand + other.get_value())
        else:
            result = Thousand(self.value_thousand + other)

        return result

    def __sub__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Thousand(self.value_thousand - other.get_value())
        else:
            result = Thousand(self.value_thousand - other)

        return result

    def __mul__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Thousand(self.value_thousand * other.get_value())
        else:
            result = Thousand(self.value_thousand * other)

        return result

    def __truediv__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Thousand(self.value_thousand / other.get_value())
        else:
            result = Thousand(self.value_thousand + other)

        return result


class Million(Multiplier):
    """Множитель на 1 000 000"""

    def __init__(self, value):
        self.value_million = value * 1_000_000

    def get_value(self):
        return self.value_million

    def __add__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Million(self.value_million + other.get_value())
        else:
            result = Million(self.value_million + other)

        return result

    def __sub__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Million(self.value_million - other.get_value())
        else:
            result = Hundred(self.value_million - other)

        return result

    def __mul__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Hundred(self.value_million * other.get_value())
        else:
            result = Hundred(self.value_million * other)

        return result

    def __truediv__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)) or isinstance(other, (int, float)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            result = Million(self.value_million / other.get_value())
        else:
            result = Million(self.value_million + other)

        return result