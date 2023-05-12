import random
import datetime


def generate_random_no():
    print(random.random())
    print(random.randint(1, 10))


generate_random_no()


def generate_unique_value():
    curr_date_time = str(datetime.datetime.now())
    random_number = str(random.randint(1000, 9999))
    print(random_number + curr_date_time)


generate_unique_value()
