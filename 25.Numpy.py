import numpy as np



# array
arr = np.array([1,3,5,7,8,6])

print(arr.dtype)
print(arr)

arr1 = np.array([1,3,5,7,8,6],float)
print(arr.dtype)
print(arr)

# Linespace

l = np.linspace(0,15,8)
print(l)

# Logspace

ls= np.logspace(1,40,6)
print(ls)

# arange

ar = np.arange(0,15,3)
print(ar)

# zeroes
zr= np.zeros(6)
print(zr)

# Ones
on = np.ones([5])
print(on)