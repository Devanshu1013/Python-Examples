from numpy import *

# 1 Creating the arrays

arr = array([ [1,2,3], [2,5,6] ])
print(arr)

print(arr.ndim)
print(arr.shape)
print(arr.size)


# 2 Convert MD into lower dim

arr2 = arr.flatten()
print(arr2)

# 3 Reshape

arr3 = arr.reshape(3,2)
print(arr3)
