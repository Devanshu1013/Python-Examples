# There are three types of methods

# 1. Insatance Methods
# 2. Class Methods      @classmethod
# 3. Static methods    @staticmethod

class Student:
    school = "Praj"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):                                  #Instance Method
        return (self.m1+self.m2+self.m3)/3

    @classmethod                                    #Class Method
    def school_name(cls):
        return cls.school

    @staticmethod                                   #Static Method
    def info():
        print("This is student info")

s1 = Student(55,66,44)
s2 = Student(78,55,41)

print(s1.avg())
print(s2.avg())

print(Student.school_name())

print(Student.info())





