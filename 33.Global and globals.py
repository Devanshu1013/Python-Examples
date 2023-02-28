# simple EG
a=10

def something():
    a= 9
    print("inside",a)

something()
print("outsode",a)

# Globaling the variable
b=4

def seco():
    global b
    b = 7
    print("insdie",b)

seco()
print("outsi",b)

# Globals() ['a']
c= 10
def third():
    c= 8
    x= globals()['c']
    print("Local inside c" ,c)
    print("Local inside x = global c",x)


third()
print("outsid",c)
