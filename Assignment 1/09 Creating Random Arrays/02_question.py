# Q.2 Create a 4x4 array with random integers between 10 and 20.

import numpy as np 

array = np.random.randint(10,20,size=16).reshape(4,4)
print(array)