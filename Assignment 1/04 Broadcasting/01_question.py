# Q.1 Create a 1D array: array = [10, 20, 30]. Subtract a scalar value, 5, using broadcasting.

import numpy as np

array = np.arange(10,31,10)
array = array -5
print(array)