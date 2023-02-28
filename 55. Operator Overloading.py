a = 5
b = 6

print(a+b)
print(int.__add__(a,b))

# Adding the functions

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        a1 = self.m1 + other.m1
        a2 = self.m2 + other.m2
        s3 = Student(a1,a2)
        return s3

    def __sub__(self, other):
        s1 = self.m1 - other.m1
        s2 = self.m2 - other.m2
        s4 = Student(s1,s2)
        return s4

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1> r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {} '.format(self.m1, self.m2)

s1 = Student(44,55)
s2 = Student(65,78)

if s1>s2:
    print("s1 winss")
else:
    print("s2 winss")

s3 = s1+s2
s5 = s1-s2
print(s5.m1)
print(s3.m1)



print(s1)



