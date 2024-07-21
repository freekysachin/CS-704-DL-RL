# Q.2 Calculate the mode of the array: data = [1, 2, 2, 3, 4, 4, 4, 5, 6].

import numpy as np

values , counts =  np.unique(np.array([1, 2, 2, 3, 4, 4, 4, 5, 6]) , return_counts=True)

maxCount =np.max(counts)

modeArray = values[counts == maxCount]

print(modeArray)