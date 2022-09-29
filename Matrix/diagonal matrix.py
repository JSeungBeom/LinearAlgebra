import numpy as np

A = np.diag([3, 4, 5, 2])
B = np.diag([1, 3, 2, 5]) # diagonal matrix
C = np.array([[1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 2, 1],
              [3, 2, 1, 0]])

print(A + B) # addition between diagonal matrix = diagonal matrix
print(np.matmul(A, B)) # multiplication between diagonal matrix = diagonal matrix
print(np.matmul(A, C)) # AC