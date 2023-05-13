class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        print('I am of type {} and my name is {}'.format(self.kind, self.name))


banana = Food('Banana', 'fruit')
banana.describe()
pork = Food('Pork', 'meat')
pork.describe()
