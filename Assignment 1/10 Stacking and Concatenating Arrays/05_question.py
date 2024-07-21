# Q.5 Concatenate two 3x3 arrays along columns: a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] and b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]].

import numpy as np

array1 = np.arange(1,10).reshape(3,3)
array2 = np.arange(10,19).reshape(3,3)

cncArray = np.concatenate((array1,array2),axis=1)
print(cncArray)