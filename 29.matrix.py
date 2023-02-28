from numpy import *

m= matrix('1 2 5 ; 6 8 4')
print(m)

m1 = matrix('4 5 6;7 98 55;6 5 47')
print(m1)

print(diagonal(m1))
print(m.min())
print(m.max)

m2 = matrix('2 4 6 ; 3 6 9 ; 2 6 4')
m3 = matrix('4 6 5 ; 8 9 10 ; 3 7 8')
m4 = m2*m3
print(m4)