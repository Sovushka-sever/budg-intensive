class Multiplier:

    def __init__(self, value) -> None:
        super().__init__()


class Hundred(Multiplier):
    """Множитель на 100"""

    def __init__(self, value):
        self.value = value * 100

    def get_value(self):
        return int(self.value)

    def __add__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value += other.get_value()
        else:
            self.value += other

        return self

    def __sub__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value -= other.get_value()
        else:
            self.value -= other

        return self

    def __mul__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value *= other.get_value()
        else:
            self.value *= other

        return self

    def __truediv__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value /= other.get_value()
        else:
            self.value /= other

        return self


class Thousand(Multiplier):
    """Множитель на 1 000"""

    def __init__(self, value):
        self.value = value * 1_000

    def get_value(self):
        return int(self.value)

    def __add__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value += other.get_value()
        else:
            self.value += other

        return self

    def __sub__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value -= (other.get_value())
        else:
            self.value -= other

        return self

    def __mul__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value *= other.get_value()
        else:
            self.value *= other

        return self

    def __truediv__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value /= other.get_value()
        else:
            self.value /= other

        return self


class Million(Multiplier):
    """Множитель на 1 000 000"""

    def __init__(self, value):
        self.value = value * 1_000_000

    def get_value(self):
        return int(self.value)

    def __add__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value += other.get_value()
        else:
            self.value += other

        return self

    def __sub__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value -= other.get_value()
        else:
            self.value -= other

        return self

    def __mul__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value *= other.get_value()
        else:
            self.value *= other

        return self

    def __truediv__(self, other):

        if not isinstance(other, (Hundred, Thousand, Million)):
            raise TypeError

        if isinstance(other, (Hundred, Thousand, Million)):
            self.value /= other.get_value()
        else:
            self.value /= other

        return self
