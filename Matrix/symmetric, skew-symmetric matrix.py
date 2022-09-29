import numpy as np

# symmetric matrix, A^T = A
A = np.array([[1, 2, 3],
              [2, 4, 5],
              [3, 5, 6]])

# skew-symmetric matrix, B^T = -B
B = np.array([[0, 2, 3],
              [-2, 0, 5],
              [-3, -5, 0]])

print(A.transpose())
print(A)

print(B.transpose())
print(-B)