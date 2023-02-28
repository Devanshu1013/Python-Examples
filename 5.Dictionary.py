data={1:'Devanshu', 2:'Dilip', 4:'Praja'}
print(data)

print(data[4])

# print(data[3])  Gives the error

print(data.get(1))
print(data.get(3))
print(data.get(3,'Not found'))


# Key + values

key = ('Devanshu', 'Dhruv', "Daksh", 'Om')
values= ['python','java','c','js']

dic=dict(zip(key,values))
print(dic)


