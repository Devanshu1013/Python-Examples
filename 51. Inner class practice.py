# Practice

class Vech:

    def __init__(self,wheels,person):
        self.wheels = wheels
        self.person = person
        self.Ty = self.Type()

    def show(self):
        print(self.wheels,self.person)

    class Type:

        def __init__(self):
            self.name = "BMW"



w1 = int(input("Enter the no of wheels for w1 : "))
w2 = int(input("Enter the no of wheels"))
p1 = int(input("Enter the no of person"))
p2 = int(input("Enter the no of person"))

v1 = Vech(w1,p1)
v2 = Vech(w2,p2)

v1.show()
v2.show()

t1 = v1.Ty
t2 = v2.Ty

print(t1.name)
