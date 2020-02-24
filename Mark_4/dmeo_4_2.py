#Prime Numbers

k=20

for i in range(2,k):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print("prime number :",i)
