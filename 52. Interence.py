# Inheritance

# 1. Single-Level Inheritance

class A:

    def feat1(self):
        print("Feat1")

    def feat2(self):
        print("Feat2")

class B(A):

    def feat3(self):
        print("Feat3")

    def feat4(self):
        print("Feat4")

# 2. Multi-Level inheritance

class C(B):

    def feat5(self):
        print("Feat5")

    def feat6(self):
        print("Feat6")

# 3. Multiple level
class D:

    def d(self):
        print("2nd")

class E(A,D):

    def e(self):
        print("3d")

a1 = A()
a1.feat1()
a1.feat2()

b1 = B()
b1.feat1()
b1.feat2()
b1.feat3()
b1.feat4()

c1 = C()
c1.feat1()
c1.feat3()
c1.feat5()

e1 = E()
e1.feat2()
e1.e()
