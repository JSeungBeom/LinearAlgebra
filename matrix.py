import numpy as np

# 3X3 square matrix
A = np.array([[2, 3, 4],
              [4, 8, 2],
              [1, 2, 1]])

print(A) # martix A
print(A[1,]) # 2nd row of A
print(A[:,2]) # 3rd column of A
print(A.transpose()) # transpose matrix of A