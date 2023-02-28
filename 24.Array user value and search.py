from array import *

arr = array('i',[])
n=int(input("enter the length of array"))

for i in range(n):
    x=int(input("Enter the next number:"))
    arr.append(x)

print(arr)

val = int(input("enter the search value"))


# Manually
k=0
for e in arr:
    if e == val:
        print(k)

        break

    k+=1

# Direct

print(arr.index(val))