ls = [7,8,5,4]

l = iter(ls)
print(l)     #Gives the address not the values

print(l.__next__())    #this will print the next one value     Here 7

# The combination of iter and __next is next
print(next(l))

for i in l:
    print(i)


# By object oriented thinking

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):                     #Just takes the object
        return self

    def __next__(self):

        if self.num <=10:
            val = self.num                  #Taking values from nums
            self.num+= 1
            return val
        else:                               #This is necessary for stop the loop otherwise it will print and print none
            raise StopIteration

values = TopTen()

print(next(values))
for i in values:
    print(i)