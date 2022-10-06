import scipy.sparse.linalg as sla
import numpy as np

A = np.array([[1, 1, 1],
             [1, 2, 3],
             [1, 3, 6]])

slu = sla.splu(A, permc_spec = "NATURAL",
               diag_pivot_thresh=0,
               options={"SymmetricMode":True})

L = slu.L.toarray()
U = slu.U.toarray()

print(L)
print(U)