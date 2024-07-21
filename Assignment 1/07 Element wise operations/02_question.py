# Q.2 Create two arrays: a = [2, 4, 6] and b = [1, 3, 5]. Perform element-wise modulus.

import numpy as np

array1 = np.arange(2,7,2)
array2 = np.arange(1,6,2)

modArray = np.mod(array1,array2)
print(modArray)