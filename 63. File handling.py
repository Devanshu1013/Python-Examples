# Read the file
f = open("MyData",'r')
# print(f.read())
# print(f.readline(7))
# print(f.readlines())

# Write the file
# w is to overwrite and a is to append at last
f1 = open("MyData2",'a')
# f1.write("Heeeee")
for i in f:
    f1.write(i)

# For image related stuff
f3 = open("p1.jpeg",'rb')
# print(f3.read())

f4 = open('p2.jpeg','wb')
for i in f3:
    f4.write(i)