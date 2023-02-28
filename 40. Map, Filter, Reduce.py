from functools import reduce

nums = [3,2,4,5,3,2,2,6,8,9,10]

evens = list(filter(lambda n: n%2==0,nums))
print(evens)

doubles = list(map(lambda n:n*2,evens))
print(doubles)

sum = reduce(lambda a,b:a+b,doubles)
print(sum)
