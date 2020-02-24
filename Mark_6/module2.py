def greet():
    print("Hello")
    print("Good Morning!")

def add(x,y):
    z = x+y
    print("Addition of both values is z :",z)
    return z
    
x = int(input("Enter the value x:"))
y = int(input("Enter the value y:"))

greet()
result = add(x,y)

print("Value of result is : ",result)
print(add(x,y))
