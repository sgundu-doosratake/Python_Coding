#Keyworded Variable length Arguments

def person(name, **data):

    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)


person ('sam',age=24,city='Atlanta',phone=4703265455)