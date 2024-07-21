# Q.4 Create a 2x3 matrix and a 3x2 matrix. Perform matrix multiplication.

import numpy as np

array1 = np.arange(1,7).reshape(2,3)
array2 = np.arange(1,7).reshape(3,2)

dotArray = np.dot(array1 , array2)
print(dotArray)
