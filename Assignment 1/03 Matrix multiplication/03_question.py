# Q.3 Perform matrix multiplication on two 3x3 matrices: a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# and b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]].

import numpy as np

array1 = np.arange(1,10).reshape(3,3)

array2 = np.arange(1,10)
array2 = np.sort(array2)[::-1].reshape(3,3)

dotArray = np.dot(array1, array2)
print(dotArray)