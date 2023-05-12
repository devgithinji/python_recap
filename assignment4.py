def function_one(func):
    print(func(10))


function_one(lambda x: x / 5)


def function_one2(func, *args):
    for arg in args:
        print(func(arg))


function_one2(lambda x: x * 2, 1, 4, 8, 9)


def function_one3(func, *args):
    for arg in args:
        print('Result: {:^20.2f}'.format(func(arg)))


function_one3(lambda x: x * 2, 1, 4, 8, 9)
