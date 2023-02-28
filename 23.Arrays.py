from array import *

vals = array('i', [6,6,8,9,7])
print(vals)

print(vals.buffer_info())

vals.reverse()
print(vals)


# for print one by one
for i in vals:
    print(i)

for i in range(len(vals)):
    print(vals[i])

# We can also take vale from old array
newArr = array(vals.typecode,(a*a for a in vals))
for e in newArr:
    print(e)
