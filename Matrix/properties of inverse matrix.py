import numpy as np

A = np.array([[1, -3],
              [2, -4]])

B = np.array([[-2, 5],
              [-1, 3]])

inv_A = np.linalg.inv(A)
inv_B = np.linalg.inv(B)

print(inv_A) # A^-1
print(inv_B) # B^-1

print(np.matmul(inv_B, inv_A)) # (AB)^-1 = B^-1A^-1
print(inv_A/4) # (4A)^-1 = 1/4A^-1
print(np.linalg.matrix_power(inv_A, 2)) # (A^2)^-1 = (A^-1)^2