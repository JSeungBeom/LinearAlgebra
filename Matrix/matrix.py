import numpy as np

A = np.array([[1, 4, 7],
              [2, 5, 8],
              [6, 3, 2]])

B = np.array([[2],
              [5],
              [8]])

C = np.array([[-4, 9]])

D = np.array([[2, 4, 8, 4],
              [4, 8, 3, 1],
              [7, 3, 0, 5]])

# print matrix size
print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)

# index starts at 0
print(A[1,]) # matrix A's second row
print(D[:,2]) # matrix D's third column
