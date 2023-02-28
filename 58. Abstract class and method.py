# We have to import ABC --> Abstract Base Class

from abc import ABC,abstractmethod

class Comp(ABC):

    @abstractmethod
    def process(self):
        # print("hi")      --> Even though it has print it will create error because abstract class --> empty abstract method
        pass

class Lap(Comp):

    def process(self):
        print("HEEEEEEE")

c1 = Lap()
c1.process()