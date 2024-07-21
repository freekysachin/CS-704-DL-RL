# Create a 3D array: array_3d = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]. Access the element at [1, 1, 1].

import numpy as np

array = np.arange(1,13).reshape(2,2,3)

print(array[1,1,1])