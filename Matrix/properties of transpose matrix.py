import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[-2, 4],
              [1, 3]])

print(A.transpose().transpose()) # (A^T)^T = A
print(A)

print((A+B).transpose())
print(A.transpose() + B.transpose()) # (A + B)^T = A^T + B^T

print(np.matmul(A, B).transpose())
print(np.matmul(B.transpose(), A.transpose())) # (AB)^T = B^T * A^T

print((3*A).transpose())
print(3 * A.transpose()) # (3A)^T = 3A^T

print(np.linalg.inv(B.transpose()))
print(np.linalg.inv(B).transpose()) # (B^T)^-1 = (B^-1)^T