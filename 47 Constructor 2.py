class Comp():

    def __init__(self):
        self.name = "Devanshu"
        self.age = 20

    def update(self):
        self.age = 21

    def compare(self,c2):
        if self.age == c2.age:
            return True
        else:
            return False


c1 = Comp()
c2 = Comp()

c1.update()

if c1.compare(c2):
    print("Same")
else:
    print("Different")

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)