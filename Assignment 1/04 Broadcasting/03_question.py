# Q.3 Divide a 4x4 array by a scalar value, 2, using broadcasting.

import numpy as np

array = np.full((4,4) , 10)
array = np.divide(array,2)

print(array)
