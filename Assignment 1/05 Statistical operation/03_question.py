# Q.3 Calculate the range of the array: data = [10, 20, 30, 40, 50].

import numpy as np

array = np.sort(np.arange(10,51,10))
range = np.subtract(np.max(array) , np.min(array))
print(range)