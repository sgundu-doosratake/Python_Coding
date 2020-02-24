


def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2 == 0:
            even = even +1
        else:
            odd = odd + 1

    return(even,odd)


lst =[20,22,28,24,26,3,21,29,27,31]


even,odd = count(lst)

print(even,odd)
print("Even : {} and Odd : {}".format(even,odd))