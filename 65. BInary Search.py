pos =-1

def search(list,n):

    l = 0
    u = len(list)-1

    while l <= u :

        mid = (l+u)//2

        if list[mid] == n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l = mid +1
            else:
                u = mid -1

    return False

list = [12,22,34,56,222,765,8887]
m = 8887

if search(list,m):
    print("found",pos+1)
else:
    print("Not Found")