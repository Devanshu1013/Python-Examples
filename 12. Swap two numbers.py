a=5
b=6

#1. Simple logic

temp = a
a=b
b=temp

print(a)
print(b)

#2. it will 1 bit extra

a= a+b
b= a-b
a= a-b

print(a)
print(b)

#3. without losing anything

a=a^b
b=a^b
a=a^b

print(a)
print(b)

#4. even simple

a,b = b,a
print(a)
print(b)