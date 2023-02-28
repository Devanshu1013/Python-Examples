# Generators will be used instead of interators


def Topten():

    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n += 1

values = Topten()

for i in values:
    print(i)