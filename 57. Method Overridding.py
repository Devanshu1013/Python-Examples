
class A:

    def show(self):
        print("A")

class B(A):

    def show(self):
        print("He he Its B")

s = B()
s.show()