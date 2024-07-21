# Q.1 Create two matrices: a = [[2, 3], [4, 5]] and b = [[1, 0], [0, 1]]. Perform matrix multiplication.
import numpy as np

array1 = np.array([[2, 3], [4, 5]])
array2= np.array([[1, 0], [0, 1]])

result = np.dot(array1, array2)

print(result)

