# Q.2 Multiply a 3x3 matrix with a 3x1 vector.

import numpy as np

array1 = np.arange(1,10).reshape(3,3)
array2 = np.arange(10,13).reshape(3,1)

dotArray = np.dot(array1,array2)
print(dotArray)


