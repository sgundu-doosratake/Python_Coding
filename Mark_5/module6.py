# Matrices

from numpy import *

arr1 = array([
                [1,2,3,4],
                [5,6,7,8]
    
            ])

m = matrix('1 2 3 ;4 5 6; 7 8 9')
m2 = matrix('1 2 3 ;4 5 6; 7 8 9')
print(arr1)
print(m)


#diagonal matrix

print(diagonal(m))

#max value

print(m.max())

#min.value

print(m.min())

#matrix multiplication

m3 = m * m2

print(m3)