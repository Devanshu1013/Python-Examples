def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('Devanshu', age=20,city='Nad', mob=635145)



