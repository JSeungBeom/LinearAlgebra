import numpy as np

A = np.array([[0, 1],
              [-2, -3]])

w, x = np.linalg.eig(A)

print(w) # eigen value
print(x) # eigen vector

A = np.array([[1, 5],
              [6, 2]])

w, x = np.linalg.eig(A)

print(w) # eigen value
print(x) # eigen vector

A = np.array([[1, 0, -1],
              [1, 2, 1],
              [2, 2, 3]])

w, x = np.linalg.eig(A)

print(w) # eigen value
print(x) # eigen vector

A = np.array([[1, -3, 3],
              [3, -5, 3],
              [6, -6, 4]])

w, x = np.linalg.eig(A)

print(w) # eigen value
print(x) # eigen vector