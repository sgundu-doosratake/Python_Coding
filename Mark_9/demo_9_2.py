# fibonacci with upper value limit


def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n+1):
        c = a+b
        a = b
        b = c
        if c > n:
            break
        print(c)


x = int(input("enter the range for fibonacci series:"))

if x < 0:
    print("Please enter correct value")

else:
    fib(x)
