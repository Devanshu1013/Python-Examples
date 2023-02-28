def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2==0 :
            even+=1
        else:
            odd+=1

    return even,odd

lst = []
n= int(input("enter the no of the list: "))

for i in range(n):
    ls = int(input("Enter the no: "))
    lst.append(ls)

even,odd = count(lst)
print("even: {} and odd: {}".format(even,odd))