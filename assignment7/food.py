class Food:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __repr__(self):
        return 'Name: {}, Kind: {}'.format(self.name, self.kind)

    def describe(self):
        print('I am of type {} and my name is {}'.format(self.kind, self.name))


class Meat(Food):

    def __init__(self, name):
        super().__init__(name, 'Meat')

    def cook(self):
        print('i am cooking')


class Fruit(Food):
    def __init__(self, name):
        super().__init__(name, 'Fruit')

    def clean(self):
        print('I am cleaning')


banana = Fruit('Banana')
banana.clean()
print(banana)

pork = Meat('Pork')
pork.cook()
print(pork)
