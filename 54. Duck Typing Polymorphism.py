class Pycharm:

    def execute(self):
        print("Compling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spelling check")
        print("Logic Alignment")
        print("Compling")
        print("Running")


class Laptop:

    def code(self,ide):
        ide.execute()

# ide = Pycharm()
# or
ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)