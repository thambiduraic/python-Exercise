# Define a class attribute”color” with a default value white.
# I.e., Every Vehicle should be white.
#
# Use the following code for this exercise.
#
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# Expected Output:
#
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

class Vehicle:

    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


obj1 = Bus("school Volvo", 180, 12)
obj2 = Car("Audi Q5", 240, 18)

print("color: {},  Name : {},  Speed : {},  Mileage : {}".format(obj1.color, obj1.name, obj1.max_speed, obj1.mileage))
print("color: {},  Name : {},  Speed : {},  Mileage : {}".format(obj2.color, obj2.name, obj2.max_speed, obj2.mileage))
