# Q.5 Calculate the correlation coefficient between two arrays: a = [1, 2, 3, 4, 5] and b = [2,4, 6, 8, 10].

import numpy as np 

array1 = np.arange(1,6)
array2 = np.arange(2,11,2)

correlation_matrix = np.corrcoef(array1, array2)
correlation_coefficient = correlation_matrix[0, 1]

print(correlation_coefficient)