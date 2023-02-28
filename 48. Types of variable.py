# Variales are of two types

# 1. Instance variable
# 2. Class Varibles

class Car:

    wheels =5    #Class variables

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 5      # Because of the class variale it wll be done by the name of the car.

print(c1.mil,c1.wheels,c1.com)
print(c2.mil,c2.wheels,c2.com)



