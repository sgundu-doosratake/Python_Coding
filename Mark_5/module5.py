from numpy import *

#Multidimensional array

arr = array([
                [1,2,3,6,2,9],
                [4,5,6,7,5,3]
            ])

print(arr)
print(arr.dtype)
print("Array dimensions : ",arr.ndim)
print("Array Size : ",arr.size)
print("Flattened array : ",arr.flatten())

arr2 = arr.flatten()

arr3 = arr2.reshape(2,2,3)

print ("Array 2 : ",arr2)

print ("Reshaped Array : ", arr3)