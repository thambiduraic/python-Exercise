# Create a child class Bus
# that will inherit all of the variables and methods of the Vehicle class
#
# Given:
#
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# Expected Output:
#
# Vehicle Name: School Volvo Speed: 180 Mileage: 12

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


bus = Bus("School Volvo", 180, 12)

print("Bus Name: {}  Speed : {}  Mileage : {}".format(bus.name, bus.max_speed, bus.mileage))
