# Q.4 Calculate the 25th percentile of the array: data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

import numpy as np

array = np.percentile(np.arange(1,11),25)
print(array)

