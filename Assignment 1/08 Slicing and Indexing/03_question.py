# Q.3 Access all elements in the last row of the array: array_2d = [[10, 20, 30], [40, 50, 60], [70, 80, 90]].

import numpy as np

array = np.arange(10,91,10).reshape(3,3)
print(array[-1])