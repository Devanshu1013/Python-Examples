# Inputs
x= int(input("enter the no:"))
y= int(input("enter the no:"))
z=x+y
print(z)

# Note: Here by default the input will take as a string.

#Char
x= input("Enter the character")
print(x[0])

# Eval()

result= eval(input("Enteer the expression"))
print(result)

#argv

import sys
x=int(sys.argv[0])
y=int(sys.argv[1])
z=x+y
print(z)

