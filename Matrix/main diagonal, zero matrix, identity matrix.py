import numpy as np

A = np.array([[1, 4, 7],
              [2, 5, 8],
              [6, 3, 2]])

print(np.diag(A)) # main diagonal entries of A

O = np.zeros((3, 3)) # 3 x 3 zero matrix
print(O)

O = np.zeros((3, 4)) # 3 x 4 zero matrix
print(O)

I = np.eye(3) # identity matrix of size 3
print(I)