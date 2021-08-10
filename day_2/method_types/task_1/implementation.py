class Coffee:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Ingredients for coffee {self.ingredients}'

    @classmethod
    def cappuccino(cls):
        return cls('espresso, oxygenated milk')

    @classmethod
    def latte(cls):
        return cls('cream, espresso, milk')

    @classmethod
    def glace(cls):
        return cls('coffee, ice cream')
