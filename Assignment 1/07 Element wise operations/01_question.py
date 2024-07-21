# Q.1 Create two arrays: a = [1, 3, 5] and b = [2, 4, 6]. Perform element-wise division.

import numpy as np

array1 = np.arange(1,6,2)
array2 = np.arange(2,7,2)

divArray = np.divide(array1 , array2)
print(divArray)