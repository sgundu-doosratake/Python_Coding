
a =10

def sample():
    a = 5
    print(a)

def sample2():
    print(a)

def val():
    # If global a value needs to be used
    global a
    a =25
    print(a)

def values():
    a = 9

    x = globals()['a']
    print("in values a :",a)

    globals()['a'] = 30

    
print(a)
#sample()
#sample2()
#val()
values()
print(a)