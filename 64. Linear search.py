# pos =-1
#
# def search(list,n):
#     i=0
#     while i < len(list):
#         if list[i] == n:
#             globals()['pos'] = i
#             return True
#         i +=1
#
#     return False
#
#
# list = [4,7,3,5,6,2,9]
# n =6
#
# if search(list,n):
#     print("found at:",pos+1)
# else:
#     print("not Found")
#

pos = -1
def search(list,n):

    for i in range(len(list)):
        if list[i] ==n:
            globals()['pos'] = i+1
            return True

            return False

list= [ 4,6,1,4,3,2]
n=1

if search(list,n):
    print("Found " ,pos)
else:
    print("NOt FOUnd")

