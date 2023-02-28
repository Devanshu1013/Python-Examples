#break
av =5
x=int(input("enter the number of candies:"))
i=1
while i<=x:

    if i>av:
        print("Opps ! Out of Stock..")
        break

    print("candies")
    i+=1

# Continue

for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)

#pass
for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)
