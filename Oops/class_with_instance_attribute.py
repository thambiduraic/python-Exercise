# Create a Class with instance attributes
#
# Write a Python program to create a Vehicle class
# with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


v1 = Vehicle(120, 50)
print("Maximum Speed : {}    Mileage : {}".format(v1.max_speed, v1.mileage))
