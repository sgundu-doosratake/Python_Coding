

def count(lst):

    odd = 0
    even = 0

    for i in lst:
        if len(i)>5:
            odd = odd + 1
        else:
            even = even +1

    return(even,odd)



lst =['sam','adam','chris','abhraham','daniel']


even,odd = count(lst)

print(even,odd)
print("Even : {} and Odd : {}".format(even,odd))