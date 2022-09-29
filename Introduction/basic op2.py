import numpy as np

# 3 x 3 square matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# 2 x 3 matrix
B = np.array([[1, 2, 3],
              [4, 5, 6]])

# 3 x 1 column vector
v = np.array([[1],
              [2],
              [3]])

# 1 x 3 row vector
# 1차원 배열의 경우, shape이 정확하게 출력 X -> 2차원 배열로 선언
w = np.array([[1, 2, 3]])

print(A) # print matrix A
print(B) # print matrix B
print(v) # print vector v
print(w) # print vector w

print(A.shape) # print shape of A
print(B.shape) # print shape of B
print(v.shape) # print shape of v
print(w.shape) # print shape of w