# Q.2 Horizontally stack two arrays: a = [[1, 2], [3, 4]] and b = [[5, 6], [7, 8]].

import numpy as np

hstkArray = np.hstack( (np.arange(1,5).reshape(2,2) , np.arange(5,9).reshape(2,2)) )
print(hstkArray)