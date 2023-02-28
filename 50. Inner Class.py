# Class inside class

class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.Lap = self.Laptop()      # Using inner class

    def show(self):
        print(self.name,self.rollno)
        self.Lap.show()                             # by doing so we can can call when we call this show function

    # Inner Clas

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8gb'

        def show(self):                                 # But we have to add it in the outer class show method
            print(self.brand,self.ram,self.cpu)

s1 = Student('Devanshu',4)
s2 = Student('Dhruv', 2)

# print(s1.name,s2.name)
s1.show()
s2.show()

# By using inner class
# l1 = s1.Lap
l1 = s1.Lap
l2 = s2.Lap

l1.brand = 'Dell'    # we can change it later
print(l1.brand)
print(l1.ram)

# Explicetly calling the inner class

# l1 = Student.Laptop()
# print(l1.brand)