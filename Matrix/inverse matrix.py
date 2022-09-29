import numpy as np

A = np.array([[2, -3],
              [1, 7]])

B = np.array([[2, 4],
              [1, -3]])

C = np.array([[2, 4],
              [1, 2]])

print(np.linalg.inv(A)) # print inverse matrix of A
print(np.linalg.inv(B)) # print inverse matrix of B
# print(np.linalg.inv(C)) # ad - bc = 0, so noninvertible
