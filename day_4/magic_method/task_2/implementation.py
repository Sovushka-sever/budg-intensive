class MathClock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def get_time(self):

        return "{00:02}:{01:02}".format(self.hours, self.minutes)

    def __add__(self, other):

        if not isinstance(other, int):
            raise TypeError('Минуты должны быть целым числом')

        self.hours = (self.hours + (self.minutes + other) // 60) % 24
        self.minutes = (self.minutes + other) % 60

        return self

    def __mul__(self, other):

        if not isinstance(other, int):
            raise TypeError('Минуты должны быть целым числом')

        self.hours = (self.hours + other) % 24

        return self

    def __sub__(self, other):

        if not isinstance(other, int):
            raise TypeError('Минуты должны быть целым числом')

        next_hour, minute = divmod(self.minutes - other, 60)
        self.minutes = minute
        self.hours = (self.hours + next_hour) % 24
        return self

    def __truediv__(self, other):

        if not isinstance(other, int):
            raise TypeError('Минуты должны быть целым числом')

        if self.hours - other < 0:
            self.hours = (24 + (self.hours - other)) % 24
        else:
            self.hours = (self.hours - other) % 24

        return self

