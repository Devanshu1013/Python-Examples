import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="Devanshu",password="Devanshu@1013",database="devanshu")

mycursor = mydb.cursor()
mycursor.execute("select * from stu")

# for i in mycursor:
#     print(i)


# or

# result = mycursor.fetchall()
# for i in result:
#     print(i)

# or

result = mycursor.fetchone()
for i in result:
    print(i)
