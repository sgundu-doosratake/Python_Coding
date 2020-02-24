
from numpy import *

a = 10

b = a

print(id(a))

print(id(b))

arr = array([1,2,3,4,5])

#deep copy
arr1 = arr.copy()

print(arr)
print(arr1)

print(id(arr))
print(id(arr1))

arr[1] = 7

print(arr)
print(arr1)

print(id(arr))
print(id(arr1))