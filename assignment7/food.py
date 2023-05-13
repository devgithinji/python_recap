class Food:
    name = 'X'
    kind = 'Y'

    # def __init__(self, name, kind):
    #     self.name = name
    #     self.kind = kind

    @staticmethod
    def describe(kind, name):
        print('I am of type {} and my name is {}'.format(kind, name))


Food.describe('Fruit', 'Banana')
