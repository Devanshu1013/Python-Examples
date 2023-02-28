def person(name,age):
    print(name,age)


person('dev',34)

# Keyword

person(age=34,name="Devanshu")

# Default
def stud(name,age=18):
    print(name,age)

stud('Dev')
stud('Devashu',33)

# variable length

def sum(a, *b):
    c=a
    for i in b:
        c=c+i
    print(c)

sum(1,1,1,1,1)

