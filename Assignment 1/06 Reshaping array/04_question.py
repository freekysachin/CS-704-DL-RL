# Q.4 Reshape a 3D array of shape (2, 3, 4) to (4, 3, 2).

import numpy as np

array = np.random.randint(1,10,size=24).reshape((2,3,4)).reshape((4,3,2))
print(array)