import numpy as np

A = np.array([[2, 3, 4],
              [1, 4, 2]])

B = np.array([[1, 2, 2],
              [4, 5, 6]])

C = A + B # sum of matrix A and matrix B
# must size of A and B same
print(C)