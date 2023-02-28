class Computer:

    def config(self):
        print("i5, 16gb, 1tb")

comp1 = Computer()
comp2 = Computer()

print(type(comp1))

# Just for knowledge   MOstly we will not use this
Computer.config(comp1)
Computer.config(comp2)

# We will use this
comp1.config()
comp2.config()