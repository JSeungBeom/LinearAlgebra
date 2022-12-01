import numpy as np

A = np.array([[1, 5, -6],
             [-1, -4, 4],
            [-2, -7, 9]])

B = np.array([[1, 5, -3],
             [3, -3, 3],
            [2, 13, -7]])

print(np.linalg.det(A))
print(np.linalg.det(B))