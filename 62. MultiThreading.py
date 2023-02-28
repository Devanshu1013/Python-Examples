from time import sleep
from threading import *

class Hello(Thread):

    def run(self):
        for i  in range(5):
            print("Hello")
            sleep(1.3)

class Hi(Thread):

    def run(self):
        for i in range(5):
            print("hi")
            sleep(1.3)

t1 = Hello()
sleep(1)
t2 = Hi()


t1.start()
t2.start()

t1.join()
t2.join()

print("bye")