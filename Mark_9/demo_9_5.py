# factorial recursion


def fact(n):

    result = 1
    x = 1
    result = result * n

    if n > 1:
        x = fact(n-1)

    result = result * x

    return result


y = fact(5)

print(y)
