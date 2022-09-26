import numpy as np

# 3 x 2 matrix
A = np.array([[3, 0],
             [-1, 2],
             [1, 1]])

# 3 x 2 matrix
B = np.array([[-3, -1],
              [2, 1],
              [4, 3]])

# 2 x 3 matrix
C = np.array([[1, 2, 3],
             [2, 0, 1]])

# column vector (3 x 1 matrix)
D = np.array([[1],
              [2],
              [3]])

print(A + 2*B) # calculate A + 2B
print(np.dot(A, C)) # calculate AC, dot(내적, 행렬곱)
print(3 * D) # calculate 3D