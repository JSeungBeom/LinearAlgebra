import scipy.sparse.linalg as sla
import numpy as np

<<<<<<< HEAD
A = np.array([[1, 1, 1],
             [1, 2, 3],
             [1, 3, 6]])

slu = sla.splu(A, permc_spec = "NATURAL",
=======
A = np.array([[1, -1, 2],
             [2, 1, 0],
             [0, 4, 2]])

slu = sla.splu(A, permc_spec= "NATURAL",
>>>>>>> origin/master
               diag_pivot_thresh=0,
               options={"SymmetricMode":True})

L = slu.L.toarray()
U = slu.U.toarray()

print(L)
<<<<<<< HEAD
print(U)
=======
print(U)

>>>>>>> origin/master
