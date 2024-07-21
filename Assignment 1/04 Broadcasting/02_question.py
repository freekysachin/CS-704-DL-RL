# Q.2 Create a 3x3 array and a 3x1 array. Add them using broadcasting.

import numpy as np

array1 = np.full((3,3),1)
array2 = np.full((3,1),2)

addArray = array1 + array2
print(addArray)
