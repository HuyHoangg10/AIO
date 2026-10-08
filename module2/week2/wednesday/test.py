import numpy as np

u = np.ones(9).reshape(3,3)
v = np.zeros(9).reshape(3,3)

r = np.einsum('ij,ij->ij', u, v)
print(r)