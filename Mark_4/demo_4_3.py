# Array

from array import *

vals = array('i',[5,4,-6,8,9])

print(vals.buffer_info())

newArr = array(vals.typecode,( a+a for a in vals))

for i in range(len(newArr)):
    print(vals[i])

for e in newArr:
    print(e)