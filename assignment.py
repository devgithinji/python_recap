name = input('Enter your name: ')
age = input('Enter your age: ')


def print_data(data_one, data_two):
    print(data_one + " " + data_two)


def get_decades_lived():
    print(int(age) // 10)


print_data(name, age)
get_decades_lived()
