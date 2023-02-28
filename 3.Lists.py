nums = [3,5,6,7,3,4,5,9]

print(nums)

#Lsts are mutuable
nums[3]=9
print(nums)

# Lists are mutable

nums = [25,45,85,75,96,32]
print(nums)

#Slicing
print(nums[2])
print(nums[4])
print(nums[3:])
print(nums[:4])
print(nums[-1])

#Also includes strings
names = ['Devanshu', 'Dilip', 'Praj']
print(names)

values = [9.5, 'Devanshu', 23]
print(values)

#Also add the lists

mil = [nums, names, values]
print(mil)

#Different operations

# 1. append
nums.append(11)
print(nums)

# 2. extend
nums.extend([29,45,58])
print(nums)

#3. insert
nums.insert(2,77)
print(nums)

#4. pop
nums.pop(1)
print(nums)

#5. remove
nums.remove(77)
print(nums)

#6. reverse
nums.reverse()
print(nums)

#7. sort
nums.sort()
print(nums)

#For del multiple values

del nums[2:]
print(nums)

#min, max, sum
print(min(nums))
print(max(nums))
print(sum(nums))


