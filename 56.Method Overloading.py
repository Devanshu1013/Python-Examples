# Method overloading is not supported in python

class A:

    def sum(self,a=None,b=None,c=None):

        s = 0

        if a!=None and b!=None and c!=None:
            s = a+ b + c
        elif a!= None and b!= None:
            s= a+b
        else:
            s=a

        return s

s1 = A()
print(s1.sum(3))
print(s1.sum(3,4))
print(s1.sum(3,5,3))