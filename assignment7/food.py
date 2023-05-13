class Food:
    name = 'X'
    kind = 'Y'

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    @classmethod
    def describe(cls):
        print('I am of type {} and my name is {}'.format(cls.kind, cls.name))


Food.name = 'Banana'
Food.kind = 'Fruit'
Food.describe()
