class Multiplier:

    def __init__(self, value) -> None:
        super().__init__()
        self.value = value


class Hundred(Multiplier):
    """Множитель на 100"""

    def __init__(self, value):
        super().__init__(value)
        self.value = value * 100

    def get_value(self):
        return int(self.value)

    def __add__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Hundred((self.value + other.get_value()) / 100)
        return result

    def __sub__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Hundred((self.value - other.get_value()) / 100)

        return result

    def __mul__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Hundred((self.value * other.get_value()) / 100)

        return result

    def __truediv__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Hundred(self.value / other.get_value())

        return result


class Thousand(Multiplier):
    """Множитель на 1 000"""

    def __init__(self, value):
        super().__init__(value)
        self.value = value * 1_000

    def get_value(self):
        return int(self.value)

    def __add__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Thousand(self.value + other.get_value())
        return result

    def __sub__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Thousand((self.value - other.get_value()) / 1_000)

        return result

    def __mul__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Thousand((self.value * other.get_value()) / 1_000)

        return result

    def __truediv__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Thousand((self.value / other.get_value()) / 1_000)

        return result


class Million(Multiplier):
    """Множитель на 1 000 000"""

    def __init__(self, value):
        super().__init__(value)
        self.value = value * 1_000_000

    def get_value(self):
        return int(self.value)

    def __add__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Million((self.value + other.get_value()) / 1_000_000)
        return result

    def __sub__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Million((self.value - other.get_value()) / 1_000_000)

        return result

    def __mul__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Million((self.value * other.get_value()) / 1_000_000)

        return result

    def __truediv__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        result = Million((self.value / other.get_value()) / 1_000_000)

        return result
