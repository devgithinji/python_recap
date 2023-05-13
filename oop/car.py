from vehicle import Vehicle


class Car(Vehicle):
    # top_speed = 100
    # warnings = []

    def brag(self):
        print('Look how cool my car is!')


car1 = Car()
car1.drive()
car1.add_warning('New warning')
print(car1)

Car.top_speed = 200

car2 = Car(200)
car2.drive()
# print(car2.__warnings)

car3 = Car(250)
car3.drive()
# print(car3.__warnings)
