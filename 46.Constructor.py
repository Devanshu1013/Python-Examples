class Comp():

    def __init__(self):
        self.name = "Devanshu"
        self.age = 20

    def update(self):
        self.age = 21


c1 = Comp()
c2 = Comp()

c1.name = "Dev"
c1.update()

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)