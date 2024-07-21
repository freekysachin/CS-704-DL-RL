# Q.1 Reshape a 1D array of 12 elements to a 3x4 array.

import numpy as np

array =np.random.randint(10,108,size=12).reshape(3,4)
print(array)