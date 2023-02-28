a= 3
b = 4

try:
    print("resource open")

    print(a/b)

    i = int(input("Enter the number:"))
    print(i)

except ZeroDivisionError as e:
    print("You cannot divide no by 0",e)

except ValueError as e:
    print("Enter the int",e)

except Exception as e :
    print("SOmething went wrong:")

finally:
    print("Resource Closed")

