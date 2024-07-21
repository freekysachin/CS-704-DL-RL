# Q.1 Create two arrays: a = [1, 3, 5, 7, 9] and b = [2, 4, 6, 8, 10]. Perform element-wise subtraction

import numpy as np

array1 = np.arange(1,11,2)
array2 = np.arange(2,11,2)
print(array2)
# two method using operand and subtract() function
# using operand
subArray =  array1 - array2
# using subtract()
# subArray = np.subtract(array1 , array2)

print(subArray)