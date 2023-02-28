def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp =nums[j]
                nums[j] = nums[j+1]
                nums[j+1]  = temp

nums = [5,2,31,22,55,6,7,8,45,67,34,99]
sort(nums)

print(nums)