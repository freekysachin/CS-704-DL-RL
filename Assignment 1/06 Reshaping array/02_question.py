# Q.2 Reshape a 2D array of shape (6, 2) to (3, 4).

import numpy as np

array = np.random.randint(1,55,size=12).reshape(6,2).reshape(3,4)
print(array)