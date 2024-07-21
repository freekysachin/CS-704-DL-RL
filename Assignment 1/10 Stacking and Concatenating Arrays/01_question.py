# Q.1 Vertically stack two arrays: a = [[1, 2], [3, 4]] and b = [[5, 6], [7, 8]].   

import numpy as np

array1 = np.arange(1,5).reshape(2,2)
array2 = np.arange(5,9).reshape(2,2)

stkArray = np.vstack((array1,array2))
print(stkArray)