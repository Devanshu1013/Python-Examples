class A:

    def __init__(self):
        print("A")

class B(A):

    def __init__(self):                         # it will call sub class first
        super().__init__()                      # This will call the super class
        print("B")

    def fea(self):
        print("func B")

a1 = B()

# Now just say for the multiple inheritance

class C:

    def __init__(self):
        print("C")

class D(A,C):

    def __init__(self):
        super(D, self).__init__()           # Due to MRO
        print("D")

b1 = D()