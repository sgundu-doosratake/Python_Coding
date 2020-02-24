#nput array from user

from array import *

x = array('i',[])

n = int(input("enter array size"))

for i in range(n):
    y = int(input("Enter the num"))
    x.append(y)

print(x)