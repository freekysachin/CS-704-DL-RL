# Q.5 Multiply a 1D array of shape (5,) by a 2D array of shape (5, 5) using broadcasting.

import numpy as np

array = np.multiply((np.arange(1,6)), np.full((5,5) , 2)) 
print(array)