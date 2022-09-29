import numpy as np

A = np.array([[2, 3],
              [3, 1],
              [4, 5]])

B = np.array([[1, 2, 3],
              [2, 3, 4]])

print(np.matmul(A, B))
print(np.dot(A, B))