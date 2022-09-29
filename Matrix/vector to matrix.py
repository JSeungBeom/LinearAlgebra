import numpy as np

print("np.vstack method")
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

# v1, v2, v3 are the rows of A
A = np.vstack([v1, v2, v3])
print(A)

# v1, v2 ,v3 are the columns of B
B = np.column_stack([v1, v2, v3])
print(B)

# Generating D by adding column v3 to C
C = np.array([[1, 2],
            [3, 4],
            [5, 6]])

D = np.column_stack([C, v3])
print(D)