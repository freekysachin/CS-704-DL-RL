# Q.3 Create a 4x4 array and flatten it.

import numpy as np 

array  = np.full((4,4) ,1)
array = array.reshape(1,array.size)
print(array)