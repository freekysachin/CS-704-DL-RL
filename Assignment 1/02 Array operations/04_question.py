# Q,4 Find the element-wise modulus of two arrays: a = [5, 10, 15], b = [2, 3, 4].

# two method: using operand and mod()

import numpy as np

array1 = np.arange(5,16,5)
array2 = np.arange(2,5)
print(array1)
print(array2)

modArray = array1 % array2
print(modArray)