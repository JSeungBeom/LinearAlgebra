import numpy as np

A = np.array([[1, 2],
              [3, 4]])

print(A ** 2) # A^2
print(np.linalg.matrix_power(A, 0)) # A^0 = I
print(np.linalg.matrix_power(A, 2)) # A^2 = AA
print(np.linalg.matrix_power(A, 3)) # A^3 = AAA
