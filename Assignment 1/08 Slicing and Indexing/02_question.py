# Q.2 Slice the first layer of a 3D array: array_3d = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11,12]]].

import numpy as np

array = np.arange(1,13).reshape(2,2,3)
print(array[0])