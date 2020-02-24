# factorial of a number


def fact(n):

    x = 1

    for i in range(1, n+1):

        x = i * x

    print(x)


fact(5)
