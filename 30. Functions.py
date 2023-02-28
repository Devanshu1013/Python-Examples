def greet():
    print("Hello")
    print("hey")

def add(x,y):
    c=x+y
    print(c)

add(3,2)
greet()

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

res1,res2 = add_sub(3,5)
print(res1,res2)
