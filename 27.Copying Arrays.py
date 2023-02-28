from numpy import *

# Shallow Copy

arr1 = array([1,2,3,4,5])
arr2 = arr1.view()
print(arr1)
print(arr2)

arr1[3] = 8

print(arr1)
print(arr2)

# Deep Copy

arr3 = arr1.copy()
print(arr1)
print(arr3)

arr1[3] = 4
print(arr1)
print(arr3)