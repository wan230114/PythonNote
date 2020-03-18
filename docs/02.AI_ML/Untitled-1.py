# %%
import sklearn.preprocessing as sp
import numpy as np

L = np.array([17, 20, 23])

newL = L - L.mean()
newL /= newL.std()
print(newL)

A = sp.scale(L)
print(A)
