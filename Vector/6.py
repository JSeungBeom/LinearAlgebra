import numpy as np

A = np.array([[1, 0, 2, 1],
             [0, 1, 1, 0],
             [1, 0, 2, 1]])

print(np.linalg.matrix_rank(A))