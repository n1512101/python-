import numpy as np

t = np.arange(24).reshape(4,6)
# print(t)

t[:,0] = 0
# print(t)
# print(np.count_nonzero(t))

t = t.astype(float)
t[3,3] = np.nan
# print(t)
# print(t != t)
# print(np.count_nonzero(t!=t))

# print(np.isnan(t))
# print(np.count_nonzero(np.isnan(t)))

# print(np.sum(t))

t2 = np.arange(24).reshape(4,6)
# print(t2)
# print(np.sum(t2))
# print(t2.sum())
# print(np.sum(t2, axis=0))
# print(np.sum(t2, axis=1))