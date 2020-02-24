#Variable length arguments

def sum(x,*y):
    
    print(x)
    print(y)
    c = x

    for i in y:
        c = c + i

    print("c is : ",c)

sum(5,6)
sum(1,2,3,4)