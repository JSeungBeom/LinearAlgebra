import numpy as np

a = [[5, 2], [2, 1]] # coefficient matrix
b = [14, 4] # constant vector

# solve linear system when 2 variables and 2 equations exist
result = np.linalg.solve(a, b)
print(result)

c = [[5, 2, 1], [2, -3, -4], [1, 5, -2]] # coefficient matrix
d = [14, 4, 21] # constant vector

# solve linear system when 3 variables and 3 equations exist
result = np.linalg.solve(c, d)
print(result)
